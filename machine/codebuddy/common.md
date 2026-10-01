# CodeBuddy Code（CLI） —— 跨机器共通

> 本目录登记 CodeBuddy Code（CLI/IDE）这个软件的机器事实。**本文件是跨机器共通部分**（字段语义为文档事实，与机器无关）；各机器的特化事实见`machine/_host/<机器标识名>/codebuddy.md`（不存在即表示该软件在该机未装；**该目录未随公开仓上传**）。
> 来源：官方文档 codebuddy.ai/docs/cli/skills（2026-08-22 联网核查）。字段对照总表见 [../../MACHINE.md](../../MACHINE.md)「平台差异速查」，本文件只记表装不下的细节。

## frontmatter 字段语义（文档）

- 字段集 9 个，**全非必填**；省略 `name` 时用目录名。
- `allowed-tools` **逗号分隔**（开放规范为空格分隔）——写给 CodeBuddy 的 skill 用逗号。
- `disable-model-invocation: true` ＝模型不能自动调，仅用户 `/skill名` 手动触发；`user-invocable: false` ＝用户菜单隐藏，仅模型自动触发或被其他 skill 引用。
- `context: fork` ＝在隔离子代理上下文运行；`agent`（如 Explore）、`model`、`hooks` 仅在 `context: fork` 下生效。

## 变量占位符（文档）

SKILL.md 正文支持运行时替换：`${CODEBUDDY_SKILL_DIR}`、`${CODEBUDDY_SESSION_ID}`、环境变量（可带默认值 `${ENV_VAR:-default}`）。

## 与 WorkBuddy 的关系

CodeBuddy Code（CLI/IDE）与 WorkBuddy 桌面版同族但不同产品——CLI 侧文档写的机制（文件型子代理、`/agents`、模型别名）在 WorkBuddy 桌面版有勘误，见 `machine/workbuddy/`（跨机器共通与各机器文件的目录）；本文件记录的 frontmatter 字段语义两产品一致（skills 系统同源）。

## 已知缺口

- **CLI 会话的工具清单（Bash / 文件 / 子代理等）尚未采集**——下次进入该环境时按 [../zcode/common.md](../zcode/common.md) 同格式补全对账。
- 「Agent 提示词注入适配器」与「官方机制 → 治理接口」两节**尚未登记**（按根 [../../MACHINE.md](../../MACHINE.md)「迁移流程」第 2 条，提起该软件时先补）。
