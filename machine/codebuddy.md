# CodeBuddy Code（CLI）工具清单与环境特化

> 提起来的时候：写给 CodeBuddy 的 skill、查其字段语义、在 CodeBuddy Code 环境干活时。定位：登记该软件的工具与调用功能＋字段细节。来源：官方文档 codebuddy.ai/docs/cli/skills（2026-08-22 联网核查）；（实测）＝本机直接操作。字段对照总表见 [../MACHINE.md](../MACHINE.md) §4，本文件只记表装不下的细节。**CLI 会话的工具清单（Bash/文件/子代理等）尚未采集——下次进入该环境时按 zcode.md 同格式补全对账。**

## frontmatter 字段语义（文档）

- 字段集 9 个，**全非必填**；省略 `name` 时用目录名。
- `allowed-tools` **逗号分隔**（开放规范为空格分隔）——写给 CodeBuddy 的 skill 用逗号。
- `disable-model-invocation: true`＝模型不能自动调，仅用户 `/skill名` 手动触发；`user-invocable: false`＝用户菜单隐藏，仅模型自动触发或被其他 skill 引用。
- `context: fork`＝在隔离子代理上下文运行；`agent`（如 Explore）、`model`、`hooks` 仅在 `context: fork` 下生效。

## 变量占位符（文档）

SKILL.md 正文支持运行时替换：`${CODEBUDDY_SKILL_DIR}`、`${CODEBUDDY_SESSION_ID}`、环境变量（可带默认值 `${ENV_VAR:-default}`）。

## 与 WorkBuddy 的关系

CodeBuddy Code（CLI/IDE）与 WorkBuddy 桌面版同族但不同产品——CLI 侧文档写的机制（文件型子代理、`/agents`、模型别名）在 WorkBuddy 桌面版有勘误，见 [workbuddy.md](workbuddy.md)；本文件记录的 frontmatter 字段语义两产品一致（skills 系统同源）。
