# ZCode 环境工具清单

> 提起来的时候：ZCode 会话里干活时。定位：**登记该软件给会话的全部工具与调用约束**——上下文开头环境区告知的内容以此为准落档。来源：（实测）＝本会话直接操作；（上下文）＝会话开头环境区告知。

## 环境常量（上下文）

- 平台 win32（Windows 10 19045 x64）；**Bash 工具用 Git Bash 执行**
- 会话有主工作区（持久 cwd）；权限模式由用户选定——被拒的调用＝用户拒绝，调整做法而非原样重试
- hooks 可能拦截工具调用，拦截输出视作用户反馈

## 工具清单（本会话快照，按用途分组）

| 组 | 工具 | 调用要点 |
|---|---|---|
| 文件 | Read / Write / Edit | 绝对路径；Read 默认 2000 行、可读图片；Edit 需先 Read、old_string 唯一匹配 |
| 执行 | Bash | Git Bash 语法；timeout 默认 120s、上限 600s；run_in_background 跨轮驻留、完成后回唤 |
| 委派 | Agent | subagent_type：general-purpose（全工具）/ Explore（只读搜索）；可后台运行；子代理带独立上下文 |
| 任务 | TaskOutput / TaskStop | 阻塞或非阻塞取后台任务输出 / 终止任务 |
| 通信 | SendMessage | 与本地子代理互发消息（按 agent_<uuid> 寻址）；纯文本输出对其他 agent 不可见 |
| 会话 | ReadSessionContext | 读 #sess_* 历史会话（relevant 聚焦 / handoff 接续） |
| 交互 | AskUserQuestion / EnterPlanMode / ExitPlanMode | 阻塞式决策提问 / 进出计划模式（需用户批准） |
| 待办 | TodoWrite / TodoRead | 会话任务清单，一次一条 in_progress |
| 技能 | Skill | 只可调列表内 skill；插件式双重命名 `插件名:skill名` |
| 网络 | WebFetch / WebSearch / mcp__web_reader__webReader | 抓取转 markdown（跨域重定向需手动跟进）/ 搜索（仅美区）/ 读网页 |
| 视觉 | mcp__4_5v_mcp__analyze_image | 仅远程 URL 图像分析 |
| 浏览器 | mcp__node_repl__js（＋js_add_node_module_dir / js_reset） | Browser Use 专用 Node 内核；**仅主代理可用，不得委派子代理**；每 call 独立内核 |
| 定时 | CronCreate / CronList / CronUpdate / CronDelete | 工作区级持久自动化；cron 按本地时区解释；相对延迟用 delayMinutes 不换算 |

## 本会话 skill 快照（上下文）

- 已装插件 skill：browser-use（control-browser、web-gui-tester）、document-skills（docx / pdf / pptx / xlsx）、skill-creator、zcode-guide（diagnosing-commands / hooks / mcp / plugins / skills、zcode-configuration-guide）
- 插件缓存位置：`C:\Users\纳\.zcode\cli\plugins\cache\zcode-plugins-official\<插件>\<版本>\skills\<名>\`（实测）
- skill 列表随插件安装动态变化——**每次会话以开头告知的列表为准**，本快照只作对账基线

## frontmatter

遵循 agentskills.io 开放规范，自定义字段放 `metadata`（实测：document-skills:pdf 为 name＋metadata＋description＋license 结构）；跨平台对照见 [../MACHINE.md](../MACHINE.md) §4。

## 到期核对

- 换会话 / 版本升级：工具表与 skill 快照对一遍上下文开头告知，差异更新本文件
- 重点核对：Agent 的 subagent_type 清单、插件缓存路径、MCP 工具增减
