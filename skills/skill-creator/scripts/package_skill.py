#!/usr/bin/env python3
"""
Skill Packager - Creates a distributable .skill file of a skill folder

Usage:
    python utils/package_skill.py <path/to/skill-folder> [output-directory]

Example:
    python utils/package_skill.py skills/public/my-skill
    python utils/package_skill.py skills/public/my-skill ./dist
"""

import sys
import zipfile
from fnmatch import fnmatch
from pathlib import Path
from quick_validate import validate_skill


# 打包时恒定排除项：私人信息 / 运行时产物，无论如何都不进分发包。
# 与 .packageignore 叠加生效（后者放各 skill 自己的排除项，如登录态备份区）。
ALWAYS_EXCLUDE = (".git", "__pycache__", ".packageignore")


def load_packageignore(skill_path: Path):
    """读 skill 根下的 .packageignore：gitignore 风格的 glob，一行一条，# 开头为注释。

    用途是把凭据与私人信息剔除出可分发包——打包默认 rglob 全收，没有它就等于
    把明文 token 一起打进 .skill。
    """
    f = skill_path / ".packageignore"
    if not f.is_file():
        return []
    pats = []
    for line in f.read_text("utf-8").splitlines():
        s = line.strip()
        if s and not s.startswith("#"):
            pats.append(s.rstrip("/"))
    return pats


def is_excluded(rel_parts, rel_posix: str, patterns) -> bool:
    """按路径各段与整条相对路径匹配排除规则；目录规则对其下所有文件生效。"""
    for pat in list(ALWAYS_EXCLUDE) + list(patterns):
        pat = pat.rstrip("/")
        if any(fnmatch(seg, pat) for seg in rel_parts):
            return True
        if fnmatch(rel_posix, pat) or fnmatch(rel_posix, pat + "/*"):
            return True
    return False


def package_skill(skill_path, output_dir=None):
    """
    Package a skill folder into a .skill file.

    Args:
        skill_path: Path to the skill folder
        output_dir: Optional output directory for the .skill file (defaults to current directory)

    Returns:
        Path to the created .skill file, or None if error
    """
    skill_path = Path(skill_path).resolve()

    # Validate skill folder exists
    if not skill_path.exists():
        print(f"❌ Error: Skill folder not found: {skill_path}")
        return None

    if not skill_path.is_dir():
        print(f"❌ Error: Path is not a directory: {skill_path}")
        return None

    # Validate SKILL.md exists
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        print(f"❌ Error: SKILL.md not found in {skill_path}")
        return None

    # Run validation before packaging
    print("🔍 Validating skill...")
    valid, message = validate_skill(skill_path)
    if not valid:
        print(f"❌ Validation failed: {message}")
        print("   Please fix the validation errors before packaging.")
        return None
    print(f"✅ {message}\n")

    # Determine output location
    skill_name = skill_path.name
    if output_dir:
        output_path = Path(output_dir).resolve()
        output_path.mkdir(parents=True, exist_ok=True)
    else:
        output_path = Path.cwd()

    skill_filename = output_path / f"{skill_name}.skill"

    ignore = load_packageignore(skill_path)
    if ignore:
        print(f"🔒 排除私人信息（.packageignore）：{', '.join(ignore)}")

    # Create the .skill file (zip format)
    try:
        skipped = []
        with zipfile.ZipFile(skill_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Walk through the skill directory
            for file_path in skill_path.rglob('*'):
                if file_path.is_file():
                    rel = file_path.relative_to(skill_path)
                    if is_excluded(rel.parts, rel.as_posix(), ignore):
                        skipped.append(rel.as_posix())
                        continue
                    # Calculate the relative path within the zip
                    arcname = file_path.relative_to(skill_path.parent)
                    zipf.write(file_path, arcname)
                    print(f"  Added: {arcname}")
        if skipped:
            print(f"\n🔒 已跳过 {len(skipped)} 个含私人信息/运行时的文件：")
            for s in skipped[:20]:
                print(f"   - {s}")
            if len(skipped) > 20:
                print(f"   … 其余 {len(skipped) - 20} 个")

        print(f"\n✅ Successfully packaged skill to: {skill_filename}")
        return skill_filename

    except Exception as e:
        print(f"❌ Error creating .skill file: {e}")
        return None


def main():
    if len(sys.argv) < 2:
        print("Usage: python utils/package_skill.py <path/to/skill-folder> [output-directory]")
        print("\nExample:")
        print("  python utils/package_skill.py skills/public/my-skill")
        print("  python utils/package_skill.py skills/public/my-skill ./dist")
        sys.exit(1)

    skill_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None

    print(f"📦 Packaging skill: {skill_path}")
    if output_dir:
        print(f"   Output directory: {output_dir}")
    print()

    result = package_skill(skill_path, output_dir)

    if result:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
