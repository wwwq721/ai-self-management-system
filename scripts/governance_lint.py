#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""治理文件只读巡检。

检查 frontmatter、Markdown 断链、锚点和 README 名单一致性。
machine/ 下的软件文件（由 MACHINE.md 管理、不入 README 名单）只参与断链与锚点检查。
README 是当前的名单制格式，因此脚本不要求职责、加载位置或引用表。
"""

import os
import re
import sys
import unicodedata
from urllib.parse import unquote


ROOT_FIELDS = ("title", "summary", "importance")
OPTIONAL_ROOT_FIELDS = ("platform", "created_at", "read_when")
# 跳过清单。
# 「文件夹目录.md」属裁定结果（2026-09-19 用户裁定）：它是工程 / 工作文件夹级的目录管理记录，
# 不算治理文件、不入 README 名单，故不参与名单一致性与 frontmatter 检查。
# （README.md 原在此列——视作非治理文件的仓库门面；2026-09-21 SYSTEM-MAP.md 改名为 README.md 后，
#   它即名单本身，故移出跳过清单、照常参与名单一致性与 frontmatter 检查。）
SKIP_NAMES = {"文件夹目录.md"}
SKIP_DIRS = {"references", "memory", "assets", "scripts", "node_modules"}
LINK_RE = re.compile(r"\[([^]\n]*)\]\(([^)\s]+)\)")
FENCE_RE = re.compile(r"```.*?```|~~~.*?~~~", re.S)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
GOVERNANCE_DESCRIPTION_RE = re.compile(
    r"治理(?:系统|文件|规则|架构)|\bgovernance\s+(?:system|file|rule|framework)\b",
    re.I,
)
EXPLICIT_GOVERNANCE_METADATA = {
    "governance": {"true", "yes", "1", "governance"},
    "governance_type": {"governance"},
    "kind": {"governance"},
    "type": {"governance"},
}


class Report:
    def __init__(self):
        self.items = []

    def add(self, level, check, path, message):
        self.items.append((level, check, path, message))

    def count(self, level):
        return sum(1 for item in self.items if item[0] == level)


def parse_frontmatter(text):
    if not text.startswith("---"):
        return None
    lines = text.splitlines()
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        return None

    top = {}
    metadata = {}
    current = None
    for raw in lines[1:end]:
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        match = re.match(r"^\s*([A-Za-z_][\w-]*)\s*:\s*(.*)$", raw)
        if not match:
            continue
        key, value = match.group(1), match.group(2).strip().strip('"').strip("'")
        indented = raw[:1] in (" ", "\t")
        if indented and current == "metadata":
            metadata[key] = value
        elif not indented:
            current = key
            top[key] = value
    return {"top": top, "metadata": metadata}


def importance(frontmatter):
    if not frontmatter:
        return None
    values = frontmatter["top"], frontmatter["metadata"]
    for fields in values:
        if "importance" in fields:
            try:
                return int(fields["importance"])
            except ValueError:
                return fields["importance"]
    return None


def read(path):
    with open(path, encoding="utf-8", errors="replace") as handle:
        return handle.read()


def collect(root):
    docs = []
    for name in sorted(os.listdir(root)):
        path = os.path.join(root, name)
        if os.path.isfile(path) and name.endswith(".md") and name not in SKIP_NAMES:
            docs.append(path)

    skills = []
    skills_root = os.path.join(root, "skills")
    if os.path.isdir(skills_root):
        for name in sorted(os.listdir(skills_root)):
            path = os.path.join(skills_root, name, "SKILL.md")
            if os.path.isfile(path):
                skills.append(path)

    # machine/ 下是软件环境文件，由 MACHINE.md 管理、不入 README 名单，
    # 故只纳入链接与锚点检查——不参与 frontmatter 与名单一致性检查。
    machine = []
    machine_root = os.path.join(root, "machine")
    if os.path.isdir(machine_root):
        for name in sorted(os.listdir(machine_root)):
            path = os.path.join(machine_root, name)
            if os.path.isfile(path) and name.endswith(".md") and name not in SKIP_NAMES:
                machine.append(path)
    return docs, skills, machine


def extract_links(text):
    cleaned = FENCE_RE.sub(lambda match: "\n" * match.group(0).count("\n"), text)
    links = []
    section = ""
    for line_number, line in enumerate(cleaned.splitlines(), 1):
        heading = re.match(r"^#{1,6}\s+(.+?)\s*$", line)
        if heading:
            section = heading.group(1)
        line_without_code = INLINE_CODE_RE.sub("", line)
        for match in LINK_RE.finditer(line_without_code):
            links.append((line_number, line.strip(), match.group(2), section))
    return links


def markdown_anchor_ids(text):
    """Return GitHub-style heading ids for local Markdown anchor checks."""
    cleaned = FENCE_RE.sub(lambda match: "\n" * match.group(0).count("\n"), text)
    counts = {}
    anchors = set()
    for line in cleaned.splitlines():
        heading = re.match(r"^#{1,6}\s+(.+?)\s*$", line)
        if not heading:
            continue
        title = re.sub(r"\s+#+\s*$", "", heading.group(1))
        slug = markdown_anchor_slug(title)
        if not slug:
            continue
        occurrence = counts.get(slug, 0)
        counts[slug] = occurrence + 1
        anchors.add(slug if occurrence == 0 else f"{slug}-{occurrence}")
    return anchors


def markdown_anchor_slug(title):
    """Approximate GitHub's generated anchor ids while preserving CJK text."""
    normalized = unicodedata.normalize("NFC", title).casefold()
    return "".join(
        "-" if char.isspace() else char
        for char in normalized
        if char.isspace() or char.isalnum() or char in "-_"
    )


def anchor_fragment(fragment):
    return unicodedata.normalize("NFC", unquote(fragment)).casefold()


def parse_system_map(path):
    if not os.path.isfile(path):
        return None, None
    root_names = set()
    skill_names = set()
    section = None
    for line in read(path).splitlines():
        heading = line.strip().lower()
        if heading.startswith("## 治理文件名单") or heading.startswith("## 1."):
            section = "root"
            continue
        if heading.startswith("## 治理型 skill 名单") or heading.startswith("## 2."):
            section = "skill"
            continue
        if not line.lstrip().startswith("-"):
            continue
        name = line.lstrip()[1:].strip().strip("`")
        name = re.sub(r"（.*?）|\(.*?\)$", "", name).strip().strip("`")
        if section == "root" and re.fullmatch(r"[A-Za-z0-9_.-]+\.md", name):
            root_names.add(name)
        elif section == "skill" and re.fullmatch(r"[A-Za-z0-9_.-]+", name):
            skill_names.add(name)
    return root_names, skill_names


def check_frontmatter(paths, report):
    frontmatters = {}
    importances = {}
    for path in paths:
        relative = os.path.relpath(path, os.path.dirname(os.path.dirname(path)))
        text = read(path)
        fm = parse_frontmatter(text)
        frontmatters[path] = fm
        if fm is None:
            report.add("ERROR", "frontmatter", relative, "frontmatter 缺失或无法解析")
            continue

        is_skill = os.path.basename(path) == "SKILL.md"
        required = ("name", "description") if is_skill else ROOT_FIELDS
        for field in required:
            if field not in fm["top"]:
                report.add("ERROR", "frontmatter", relative, f"缺少 {field}")

        value = importance(fm)
        if value is None:
            report.add("ERROR", "importance", relative, "缺少 importance")
        elif not isinstance(value, int) or not 1 <= value <= 10:
            report.add("ERROR", "importance", relative, f"importance 非法：{value!r}（应为 1~10）")
        else:
            importances[path] = value

        if not is_skill:
            missing = [field for field in OPTIONAL_ROOT_FIELDS if field not in fm["top"]]
            if missing:
                report.add("INFO", "frontmatter", relative, "缺少可选字段：" + ", ".join(missing))
        elif "importance" in fm["top"]:
            report.add("WARN", "frontmatter", relative, "skill 的自定义 importance 应放在 metadata 下")
    return frontmatters, importances


def check_links(paths, root, report):
    anchors_by_path = {}
    for path in paths:
        relative = os.path.relpath(path, root)
        for line_number, line, target, section in extract_links(read(path)):
            if re.match(r"^(?:https?|mailto):", target):
                continue
            target_path, separator, fragment = target.partition("#")
            target_path = unquote(target_path)
            resolved = (
                os.path.normpath(os.path.join(os.path.dirname(path), target_path))
                if target_path
                else path
            )
            if not os.path.exists(resolved):
                report.add("ERROR", "links", relative, f"L{line_number} 断链：{target}")
                continue
            if separator and fragment and resolved.lower().endswith(".md"):
                anchors = anchors_by_path.setdefault(resolved, markdown_anchor_ids(read(resolved)))
                if anchor_fragment(fragment) not in anchors:
                    report.add("ERROR", "anchors", relative,
                               f"L{line_number} 锚点不存在：{target}")
            if not target_path.lower().endswith(".md"):
                continue


def governance_skill_candidate(frontmatter):
    if not frontmatter:
        return None
    metadata = frontmatter["metadata"]
    for key, accepted_values in EXPLICIT_GOVERNANCE_METADATA.items():
        value = metadata.get(key)
        if value and value.casefold() in accepted_values:
            return f"metadata.{key}={value!r}"

    description = frontmatter["top"].get("description", "")
    if GOVERNANCE_DESCRIPTION_RE.search(description):
        return "description 明确声明治理范围"
    return None


def check_map(root, docs, skills, frontmatters, report):
    map_path = os.path.join(root, "README.md")
    mapped_roots, mapped_skills = parse_system_map(map_path)
    if mapped_roots is None:
        report.add("WARN", "map", "README.md", "名单不存在或无法解析")
        return

    actual_roots = {os.path.basename(path) for path in docs}
    missing = sorted(actual_roots - mapped_roots)
    stale = sorted(mapped_roots - actual_roots)
    for name in missing:
        report.add("WARN", "map", "README.md", f"根治理文件未登记：{name}")
    for name in stale:
        report.add("WARN", "map", "README.md", f"名单中的文件不存在：{name}")

    actual_skill_dirs = {os.path.basename(os.path.dirname(path)) for path in skills}
    for name in sorted(mapped_skills - actual_skill_dirs):
        report.add("WARN", "map", "README.md", f"名单中的 skill 不存在：{name}")
    for path in skills:
        name = os.path.basename(os.path.dirname(path))
        if name in mapped_skills:
            continue
        reason = governance_skill_candidate(frontmatters.get(path))
        if reason:
            report.add("WARN", "map", "README.md",
                       f"可能漏登记的治理型 skill：{name}（{reason}）")


def main():
    root = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if not os.path.isdir(root):
        print(f"目录不存在：{root}")
        return 2

    docs, skills, machine = collect(root)
    paths = docs + skills
    report = Report()
    frontmatters, _ = check_frontmatter(paths, report)
    check_links(paths + machine, root, report)
    check_map(root, docs, skills, frontmatters, report)

    print(f"治理巡检目录：{root}")
    for level in ("ERROR", "WARN", "INFO"):
        items = [item for item in report.items if item[0] == level]
        if not items:
            continue
        print(f"\n### {level}（{len(items)}）")
        for _, check, path, message in items:
            print(f"  [{check}] {path}: {message}")
    print("\n" + "=" * 72)
    print(f"ERROR {report.count('ERROR')} | WARN {report.count('WARN')} | INFO {report.count('INFO')}")
    print("检查范围：根目录治理文件、各 skill 的 SKILL.md、machine/ 下软件文件（仅链接与锚点）、Markdown 链接/锚点和 README 名单。")
    return 1 if report.count("ERROR") else 0


if __name__ == "__main__":
    sys.exit(main())
