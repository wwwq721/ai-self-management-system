# Skill Format and Structure

本文件承载 `SKILL.md` 的格式、目录和资源细节。写入或修改 Skill 时，同时核对当前官方 [Agent Skills specification](https://agentskills.io/specification)；平台字段和环境事实以 [MACHINE.md](../../../MACHINE.md) 为准。

## Contents

- [Package anatomy](#package-anatomy)
- [Frontmatter](#frontmatter)
- [Body](#body)
- [Bundled resources](#bundled-resources)
- [References](#references)
- [Validation](#validation)

## Package anatomy

一个 Skill 是一个目录，必须有根目录 `SKILL.md`，其他文件按实际工作流选择：

```text
skill-name/
|-- SKILL.md       Required metadata and instructions
|-- scripts/       Optional executable helpers
|-- references/    Optional on-demand documentation
`-- assets/        Optional files used in generated output
```

目录名应与 Skill 名称一致，frontmatter 的 `name` 必须与父目录名完全一致。除上述约定目录外，规范允许按实际工作流添加其他文件或目录；不要为凑结构创建空目录、占位文件、README、安装指南、变更日志或重复的快速参考。

## Frontmatter

开放规范支持以下字段：

| 字段 | 要求与用途 |
|---|---|
| `name` | 必填；1-64 个字符，仅小写字母、数字和连字符，不以连字符开头或结尾，不使用连续连字符。 |
| `description` | 必填；非空且不超过 1024 个字符，说明 Skill 做什么以及何时使用，并包含帮助 Agent 路由的具体关键词。 |
| `license` | 可选；许可证名称或随包许可证文件的简短引用。 |
| `compatibility` | 可选；不超过 500 个字符，仅在存在具体环境要求时填写。 |
| `metadata` | 可选；开放规范定义为字符串键到字符串值的映射，用于保存额外元数据；支持该字段的平台可将治理字段放在这里。 |
| `allowed-tools` | 可选且实验性；开放规范使用空格分隔的预批准工具名，具体客户端可能不同。 |

平台可能扩展字段或改变解析方式。不要把某个平台的扩展当成开放规范；目标平台为 CodeBuddy、WorkBuddy、Claude Code 或 ZCode 时，先查 [MACHINE.md](../../../MACHINE.md) §4 及对应软件文件。不要把平台事实复制进通用 Skill。本治理系统的 `metadata.importance` 等 typed 字段属于本地扩展；需要开放规范兼容时，按目标平台核实其编码方式，不把本地类型假定为标准行为。

`read_when` 不是开放规范字段。只有目标平台明确支持时，才按平台规定放入 metadata；`description` 仍是主要触发来源。

## Body

frontmatter 后的 Markdown 正文没有额外格式限制，写 Agent 完成任务所需的目的、约束、判断标准、流程和引用入口。正文在 Skill 触发后加载，因此应保持聚焦；长流程、模式差异、模式化示例和技术细节按需放入 references。

正文应服务 Agent，不应要求用户执行 Skill 内部操作，例如输入某条命令、重启会话或手动加载文件。可以写 Agent 需要调用的脚本、检查的路径和验证条件。

## Bundled resources

- `scripts/`：重复编写或需要确定性、可重复验证的执行逻辑。脚本应自包含或说明依赖，并处理可预见的错误。
- `references/`：只有在 Skill 已触发且当前任务需要时才读取的文档、schema、政策、长例子、格式说明和实现细节。
- `assets/`：用于最终产出的模板、图片、字体、数据或其他静态资源，不作为默认指令加载。

每个资源都必须有明确调用场景。删除已有资源前，先检查调用者和用途。

## References

从 `SKILL.md` 使用相对 Skill 根目录的路径，例如在入口中写明 `references/schema.md`，并说明何时读取。

引用应直接指向实际存在的文件，保持从 `SKILL.md` 一层可达，避免通过 reference 串联深层级引用链。入口要说明何时读取 reference；不需要的 reference 不要默认全部加载。

## Validation

开放规范优先使用官方 `skills-ref validate` 验证；工作区提供的 `scripts/quick_validate.py` 用于补充本地 frontmatter、命名和描述字段等基本不变量。资源引用需另行检查；两者都不能代替对触发边界、用户范围、事实、引用可达性和实际行为的人工核查。
