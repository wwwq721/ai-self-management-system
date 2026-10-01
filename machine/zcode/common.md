# ZCode —— 跨机器共通

> 本目录登记 ZCode 这个软件的机器事实。**本文件是跨机器共通部分**（软件机制、工具清单）；该软件在各台机器上的特化事实见`machine/_host/<机器标识名>/zcode.md`（**该目录未随公开仓上传**）。
> 读取方式：本文件 ＋ `machine/_host/<机器标识名>/zcode.md`（后者不存在即表示该软件在本机未装）。口径见 [../README.md](../README.md) 与根 [../../MACHINE.md](../../MACHINE.md) 的解析规则。

## 工具清单（会话快照，软件级）

| 组 | 工具 | 调用要点 |
|---|---|---|
| 文件 | Read / Write / Edit | 绝对路径；Read 默认 2000 行、可读图片；Edit 需先 Read、old_string 唯一匹配 |
| 执行 | Bash | Git Bash 语法；timeout 默认 120s、上限 600s；run_in_background 跨轮驻留、完成后回唤 |
| 委派 | Agent | subagent_type：general-purpose（全工具）/ Explore（只读搜索）；可后台运行；子代理带独立上下文 |
| 任务 | TaskOutput / TaskStop | 阻塞或非阻塞取后台任务输出 / 终止任务 |
| 通信 | SendMessage | 与本地子代理互发消息（按 agent_&lt;uuid&gt; 寻址）；纯文本输出对其他 agent 不可见 |
| 会话 | ReadSessionContext | 读 #sess_* 历史会话（relevant 聚焦 / handoff 接续） |
| 交互 | AskUserQuestion / EnterPlanMode / ExitPlanMode | 阻塞式决策提问 / 进出计划模式（需用户批准） |
| 待办 | TodoWrite / TodoRead | 会话任务清单，一次一条 in_progress |
| 技能 | Skill | 只可调列表内 skill；插件式双重命名 `插件名:skill名` |
| 网络 | WebFetch / WebSearch / mcp__web_reader__webReader | 抓取转 markdown（跨域重定向需手动跟进）/ 搜索（仅美区）/ 读网页 |
| 视觉 | mcp__4_5v_mcp__analyze_image | 仅远程 URL 图像分析 |
| 浏览器 | mcp__node_repl__js（＋js_add_node_module_dir / js_reset） | Browser Use 专用 Node 内核；**仅主代理可用，不得委派子代理**；每 call 独立内核 |
| 定时 | CronCreate / CronList / CronUpdate / CronDelete | 工作区级持久自动化；cron 按本地时区解释；相对延迟用 delayMinutes 不换算 |

- 工具清单是快照，**以每次会话开头告知为准对账**。
- 已装插件 skill（软件级观察）：browser-use（control-browser、web-gui-tester）、document-skills（docx / pdf / pptx / xlsx）、skill-creator、zcode-guide（diagnosing-commands / hooks / mcp / plugins / skills、zcode-configuration-guide）。**该清单随插件安装动态变化，以会话开头告知为准。**

## frontmatter

遵循 agentskills.io 开放规范，自定义字段放 `metadata`（实测：document-skills:pdf 为 name＋metadata＋description＋license 结构）；跨平台对照见 [../../MACHINE.md](../../MACHINE.md)「平台差异速查」。

## 到期核对

- 换会话 / 版本升级：工具表与 skill 快照对一遍上下文开头告知，差异更新**本文件**（软件级）或本机文件（机器级）。
- 重点核对：Agent 的 subagent_type 清单、插件缓存路径（机器级，见本机文件）、MCP 工具增减。
