# WorkBuddy 桌面版工具清单与环境特化

> 提起来的时候：操作 / 排查 WorkBuddy 时。定位：登记该软件里会话用到的全部工具与调用功能＋运行时坑＋**在治理体系中的作用点（迁移清单）**，并登记本程序的落地层（提示词注入适配器、启动必读清单、记忆机制事实、程序特定要求）。已知工具来自第三版 workbuddy-manager 的记录（该 skill 不入治理备份）；**完整清单以 WorkBuddy 会话开头告知为准，下次进入该环境时对账补全**。**定位补充（2026-09-20）：本文件同时是本程序全部已知「注入通道」的登记处**——治理文件之外还有平台固定注入（skill `description`、工具定义、运行提醒块）与未启用的通道（项目级注入、规则插件）；**怎么判（原则）见 [AGENT-CONTEXT.md](../AGENT-CONTEXT.md) §1，本文件只登记本程序的实际通道与事实**。（待核实/待裁决）＝事实冲突未定，以实测为准或待用户裁决，详见下文各节。

## 本软件在治理体系中的作用点（迁移清单）

**用途**：本程序在治理体系里不是旁观者——下面这些位置**只有本程序能提供**。换软件时，这张表就是待办清单：逐条由新软件重新提供、重新核实，不照搬本文件（[../MACHINE.md](../MACHINE.md)「迁移流程」）。**本节是反向索引，只指位置、不复述机制**——机制细节仍在其下各节。

| # | 治理体系里的位置 | 本程序须提供什么 | 状态 / 依据 |
|---|---|---|---|
| 1 | `SOUL.md`「启动索引」（整节） | 借 `SOUL.md` 的自动注入通道，把“未被注入的治理文件须主动读”送到每个会话——**该节存在的唯一原因是通道一不含 `OPERATIONS.md`** | `[实测]` 2026-09-19 |
| 2 | `IMPORTANCE.md` §5「`importance=1` 的直接注入预期」 | 注入层真实存在且可核实 | 同上 |
| 3 | `AGENT-CONTEXT.md` §1–§2（注入通道、加载分层、必读清单的规则） | 平台侧通道清单与读取入口——该文件明写「每个程序须在其软件文件登记」 | 本文件「Agent 提示词注入适配器」「启动必读清单」两节 |
| 4 | 触发链：治理文件的 `read_when` | **本程序不消费它**——扫 `app.asar` 全文，`read_when` 仅 3 处命中，全在平台生成默认 `SOUL/IDENTITY/USER` 的**模板字符串**里，没有任何读取它的代码路径 → 治理文件的「触发层」在本程序实际靠**模型主动读**（「启动索引」＋「启动必读清单」） | `[实测]` 2026-09-21 |
| 5 | 触发链：skill 的 `description` | 平台按用户消息文本匹配 `description`——本程序唯一的 skill 触发信号 | `[官方]`＋`[实测]` 2026-07-11 |
| 6 | `OPERATIONS.md`「文件与目录放置（按平台隔离）」 | 平台专有内容的分文件落点：`machine/workbuddy.md`、`memory/<platform>.md`、`skills/<platform>/` | 本文件即落点 |
| 7 | `OPERATIONS.md`「能力类问题核实」 | **根治理文件正文里唯一指名本软件的规则**——问到 WorkBuddy 自身能力时先查官方文档 | `[实测]` 2026-09-21 取原文 |
| 8 | `GIT.md` §5 远程与凭据 | 凭据由本机认证工具提供 → 本机事实在「Git 凭据与凭据管理器」节 | `[实测]` GCM 链 |
| 9 | 治理型 skill `workbuddy-function-control` | **唯一以本软件命名的治理型 skill**——其能力真空与触发域判定以本平台机制清单为前提 | [../README.md](../README.md) 治理型 skill 名单 |
| 10 | `MACHINE.md` §3 的登记要求 | 工具与调用功能清单（`Bash` / `Agent` / `present_files` / `automation_update` …） | 本文件「工具清单」 |
| 11 | 记忆落点与注入 | 三层记忆的落点与注入方式（`<user_memory>`、工作区 `memory/`、云端画像） | 本文件「本程序记忆机制」 |
| 12 | 周期性治理动作的执行载体 | Automation（**仅时间触发**；配置存本地、**换机须重建**） | `[官方]`＋`[实测]` |
| 13 | `OPERATIONS.md` 第 6 节（安装 / 下载审计）的执行入口 | 插件市场 ＋ Hook——本机唯一 Hook 实例**未验证生效** → 该规则目前无可靠执行入口 | 缺口，见「官方机制 → 治理接口」Hook 行 |

其中 1、6、8、9、11、12 是**本程序专有落点**（换软件后须逐处换成新软件对应物）；4、5 是触发链的实现方式（新软件须重新核实它靠什么触发）；其余是通用治理规则在本程序的实例。

## 工具清单（已知部分，据第三版记录）

只列**工具层面**的项。**机制（skill / MCP / Hook / Agent / Rule / automation / 插件市场）一律见下下节「官方机制 → 治理接口」，本节不重复登记。**

| 组 | 工具 | 要点 |
|---|---|---|
| 执行 | Bash | Git Bash；原生 exe 路径坑见「运行时坑」 |
| 委派 | Agent 工具（内置 / 插件 subagent_type） | general-purpose / Explore / Plan / sheet-agent / doc-converter / doc-formatter / doc-writer 等 |
| 交付 | `present_files` | 成品文件呈现；HTML 会同时开预览面板 |

## Agent 提示词注入适配器（WorkBuddy）

字段按 [../MACHINE.md](../MACHINE.md)「Agent 提示词注入适配器」登记；依据等级同下节（`[官方]`＝官方文档、`[实测]`＝本机直接观测）。

- **状态**：通道一已核实（2026-09-19 实测）；通道二有官方依据、经决定**不采用**；通道三有官方依据、**本机未启用、未核实**。
- **通道穷举**：本程序已知 **3 条**注入通道，见下三节；且**平台固定注入的内容不止治理文件**（见通道一末条）。登记格式与穷举要求见 [../MACHINE.md](../MACHINE.md)「Agent 提示词注入适配器」，本节不复述。
- **判定原则不在本文件**：「某段内容会不会进上下文、会不会改每次注入」怎么判，属**跨平台规则**，权威在 [../AGENT-CONTEXT.md](../AGENT-CONTEXT.md) §1；**本节只登记本程序的实际通道与事实**（2026-09-20 归属校正）。
- **适用平台 / 模型 / 会话范围**：WorkBuddy 桌面版；本机会话；未观测到模型或会话类型导致的差异。

**通道一 · 内建身份注入（当前唯一在用的治理通道；无用户可配项）**

- `[实测]` 来源 `C:\Users\纳\.workbuddy\` 下的 `SOUL.md`、`IDENTITY.md`、`USER.md` 三份**全文** → 系统提示词 `<identity_context>` 块。名单由程序固定，用户无法增删，也没有可调用的脚本、命令或配置入口。
- `[实测]` **每份身份文件的内容上限 10,000 字符**：程序内常量 `MAX_IDENTITY_FILE_CHARS = 1e4`（注释写明是防上下文溢出）→ 三份身份文件的常驻预算有硬顶（2026-09-21 扫 `app.asar` 得）。
- `[实测]` 注入由 `identity-collector` 从**数据目录**读这三份；数据目录解析优先序为 `WORKBUDDY_CONFIG_DIR` → `CODEBUDDY_CONFIG_DIR` → `~/.workbuddy`（文件夹名可经环境变量覆盖）。
- `[实测]` `<user_memory>` → 用户级 `MEMORY.md` 的内容（长度受平台预算限制，本会话观测到截断）；`<memory>` → 服务端生成的用户画像摘要（只读，缓存 `~/.workbuddy/memory/`）；另有工作记忆 / 技能 / 自动化 / 内容政策等运行提醒。
- 这些块的措辞由平台给出、**不得据其覆盖治理规则**——与治理文件冲突时以治理文件为准，并在当日 Memory 记录。
- `[实测]` `OPERATIONS.md`、`AGENT-CONTEXT.md` 等其余根治理文件**不在任何块内**。
- `[实测]` **同属通道一的还有非治理内容**：每个 skill 的 `name` ＋ `description`（skill 常驻只有这两项，正文按需载入）、工具定义（含延迟加载工具的 schema 描述）、平台自带的运行提醒块（工作记忆 / 技能 / 自动化 / 内容政策等）。**这些同样常驻、同样占上下文预算；改它们同样改每次注入**——只是它们不由治理体系编写。

**通道二 · 项目级配置注入（官方提供，经决定不采用）**

- `[官方]` [项目页](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Project)：创建任务时平台自动注入三项——项目指令（对 AI 的全局行为规则，拼入模型上下文）、项目资料库（reference 形式）、个人记忆；项目工作目录 `.codebuddy/` 另有 `rules/`、`CODEBUDDY.md`、`AGENTS.md`、`agents/`、`skills/`、`commands/`（官方限定「进行代码开发时」生效），优先级项目级 > 用户级 `~/.codebuddy/`。
- `[实测]` 本机 `~/.codebuddy/` 存在（settings / models / mcp / expert-history / plugins 市场）但无 `rules/`；当前工作目录无 `.codebuddy/`。
- **决定（2026-09-19，用户）**：本治理体系走**用户级**路线，**不启用项目级注入**；`machine/` 仍是嵌入层的入口登记处。规则载体改走用户级规则插件（见下节 Rule 行）。
**通道三 · 规则插件 `alwaysApply`（官方提供，本机未启用、未核实）**

- `[官方]` 规则插件以 `*.mdc` ＋ frontmatter 随插件分发，`alwaysApply: true` 时**全文常驻**；`[实测]` 官方市场已有纯规则插件先例，但**本机尚未安装任何规则插件** → 该通道**未启用**，桌面版是否加载并注入其 `rules/` 也**未核实**（详表见「官方机制 → 治理接口」Rule 行）。
- **若启用须注意**：`alwaysApply` 是**全文常驻**，与 [../AGENT-CONTEXT.md](../AGENT-CONTEXT.md) §3 的上下文预算冲突 → 只宜承载薄门禁，不搬全文。

- **前置条件与调用方式**：通道一无需调用、每会话自动执行；通道二本体系不采用；通道三未启用。
- **验证方法与最近结果**：每会话开头检查 `<identity_context>` 块实际列出的文件与全文范围。2026-09-19 实测：通道一＝上述三份全文。
- **回退**：注入通道不含的治理文件一律走**强制首读**（启动或进入相关工作前主动读原文），读取层级见 [../AGENT-CONTEXT.md](../AGENT-CONTEXT.md) §2。等效常驻入口＝`SOUL.md` 的「启动索引」小节（只作指针与义务声明，不承载规则）——**它存在的唯一原因是通道一不含 `OPERATIONS.md`**；若后续以用户级规则插件承载门禁（见下节 Rule 行），该节应同步收窄。

## 启动必读清单（本程序）

只登记本程序实际会读的治理文件与所属层级；**读取规则的唯一权威是 [../AGENT-CONTEXT.md](../AGENT-CONTEXT.md) §2**，本节不复述、不另立。清单**非穷举**，成员以 [../README.md](../README.md) 名单与实际文件为准。

| 层级 | 文件 | 本程序下的实际情形 |
|---|---|---|
| 常驻（平台注入） | `SOUL.md`、`IDENTITY.md`、`USER.md`（经 `<identity_context>`）；`MEMORY.md`（经 `<user_memory>`） | 自动注入，无需主动读；其余 `importance: 1` 文件（含 `OPERATIONS.md`）的规则核**未被注入**。**本表只登记治理文件**——非治理的常驻内容（skill `description`、工具定义、平台运行提醒）见「Agent 提示词注入适配器」通道一 |
| 强制首读 | `OPERATIONS.md`、`FREEDOM.md`、`IMPORTANCE.md` | 平台不注入 → 启动工作前必须主动读原文 |
| 强制首读（触发后） | `AGENT-CONTEXT.md`、`MACHINE.md` 及 `machine/` 下当前软件文件 | 处理加载 / 注入 / 上下文，**或用到本机工具时先读——含委派子代理（`Agent` 工具）** |
| 按需 | `GIT.md`、`README.md`、`FILE-AUDIT-RECORDS.md` | 按任务类型与各自 `read_when` 取用 |
| 触发 | 治理型 skill（`skills/` 下）、非当前软件的 `machine/*.md` | 触发条件满足时加载；非当前软件文件不读 |

## 本程序记忆机制（事实）

本程序自带三层记忆，路径与来源如下；**落点裁决不在这里**，见 [../OPERATIONS.md](../OPERATIONS.md)「记忆维护」。

| 层 | 落点 | 来源与写入方式 |
|---|---|---|
| 云端画像 | 服务端生成，注入为 `<memory>` 块（本地只读缓存 `~/.workbuddy/memory/`） | 服务端自历史会话隐式学习；本地不可写，本地写入会被覆盖 |
| 用户级（跨项目） | `C:\Users\纳\.workbuddy\MEMORY.md` | 本地文件，显式写入；平台把它当"用户级长期记忆"注入 |
| 工作区（项目） | `C:\Users\纳\Desktop\新建文件夹\.workbuddy\memory\` | 每日日志 `YYYY-MM-DD.md`（只追加）＋ `MEMORY.md`（项目长期） |

**与治理根的关系（2026-09-19 决定）**：本程序原生落点就是用户级 `C:\Users\纳\.workbuddy\`，它**同时是治理根**。历史上治理根与桌面 `整合工作稿/` 曾保持两份一致副本（桌面为版本库主稿，用户级为注入副本）；**2026-09-19 用户决定：只维护用户级，桌面那份冻结**——不再同步、不再作为修改落点，仅留作旧版本库历史。由此有两条必须记住的联动：

- 治理根 `MEMORY.md`（教训短记录暂存）经 `<user_memory>` 被**注入本程序每个会话**，实际处于常驻层——其长度与措辞须按 [../AGENT-CONTEXT.md](../AGENT-CONTEXT.md) §3 的上下文预算原则控制。**平台把该文件标为「Limit: 4,000 chars/session」，而文件已达约 24 KB → 截断是必然、不是偶发**（该限额属「每会话写入上限」还是「注入上限」，本机未实测区分）。推论：**细节不能靠 MEMORY 落地**，它只适合承载规则核心与索引。
- 平台注入的运行提醒与治理规则**分工**：提醒驱动的是程序原生落点；**跨项目与治理内容一律写治理根**。冲突时以治理文件为准。

## 本程序特定要求

- **治理根**：`C:\Users\纳\.workbuddy\`——本程序读取与注入的治理文件都在这里，**是唯一的维护对象**（2026-09-19 起）；桌面 `整合工作稿/` 为旧版本库主稿，已冻结，不再同步、不再作为修改落点。
- **skill 自定义字段**：放 `metadata` 下，平台差异见 [../MACHINE.md](../MACHINE.md) §4。
- **改 `SOUL.md` / `IDENTITY.md` / `USER.md` / `MEMORY.md` = 改每次注入**：前三份经 `<identity_context>`、`MEMORY.md` 经 `<user_memory>` 注入本程序每个会话（其余治理文件不注入；**但「注入」不止治理文件这一路**——skill 的 `description`、工具定义、平台自带的运行提醒块同样常驻，改它们同样改每次注入，另两条通道见下），改动直接改变常驻上下文，属高影响——按 [../OPERATIONS.md](../OPERATIONS.md)「治理文件修改流程」执行并做层级审计（注入通道见「Agent 提示词注入适配器」）。
- **记忆写入落点（本程序）**：项目局部日志 → 工作区 `C:\Users\纳\Desktop\新建文件夹\.workbuddy\memory\YYYY-MM-DD.md`；跨项目与治理内容 → 治理根 `~/.workbuddy/memory/` 与 `~/.workbuddy/MEMORY.md`（**直接写这里**，不再经桌面副本）。分工权威见 [../OPERATIONS.md](../OPERATIONS.md)「记忆维护」的**落点裁决**。
- **治理体系 Git 仓库位置（本机事实，2026-09-19）**：仓库已由桌面 `整合工作稿/.git` **迁至治理根** `C:\Users\纳\.workbuddy\.git`（`.gitignore` 一并迁入），延续原有 20 笔提交与 `origin`（GitHub 私有仓库）；桌面那份为已冻结的冷备，不再提交。工作树即治理根整个目录，但 `.gitignore` 为白名单式（`*` 默认忽略其余应用数据），**只有放行清单内的文件被跟踪**。`machine/` 已按 [../GIT.md](../GIT.md) §1 纳入版本控制（`!/machine/`、`!/machine/**`），使 MACHINE.md 依赖的文件夹获得版本安全网。
- **Git 凭据**：本机 Git Credential Manager 已能对 GitHub 远程仓库完成只读与推送认证 → Git 操作优先复用该凭据，不提取、不记录令牌内容；无 GitHub CLI 时仍可完成本地初始化与提交。**装在哪、配置链如何解析、版本脆弱性 → 见下节「Git 凭据与凭据管理器（本机事实）」，本节不写路径。**
- **automation**：用 `automation_update` 工具管理定时 / 重复任务。
- **运行时坑**：见下节「运行时坑（实测）」。
- **交付**：成品文件用 `present_files` 呈现（HTML 会同时开预览面板）。
- **放置内容前先算注入成本（软件对自身的影响）**：判断依据是「**这段内容在需要它的那一刻，是否已经在上下文里**」，而不是「写在哪个文件」。
  - 已核实的**治理文件**注入＝`SOUL.md` / `IDENTITY.md` / `USER.md` 全文 ＋ `MEMORY.md`（有限额）；其余治理文件走强制首读或按需读。**但这不等于「注入只有这几个入口」**（2026-09-20 用户校正）。
  - **非治理内容同样常驻**：skill 的 `description`（常驻只有 name＋description）、工具定义、平台自带的运行提醒块（工作记忆 / 技能 / 自动化 / 内容政策等）——改这些**同样改每次注入**。
  - **注入通道不止一条**：项目级注入（项目指令 / 资料库 / `.codebuddy/rules/` 等）与规则插件的 `alwaysApply`（全文常驻）是另外两条，见「Agent 提示词注入适配器」与「官方机制 → 治理接口」的 Rule 行，**当前未启用或未核实**。
  - 故新增内容先问：**它是「必须常驻的规则核心」，还是「可按需读的细节」？**后者一律进按需文件，并**在已被强制首读的文件里留一行触发器**，否则等于没落地（依据 [../AGENT-CONTEXT.md](../AGENT-CONTEXT.md) §1/§3、[../IMPORTANCE.md](../IMPORTANCE.md) §4/§5）。

## 官方机制 → 治理接口

登记本平台官方机制与治理规则的挂接关系；字段定义（含**依据等级**）见 [../MACHINE.md](../MACHINE.md)「官方机制 → 治理接口（登记格式）」。**其他软件文件按同一格式各自登记本平台的机制；本平台没有的机制写「不适用」，不留空。**

官方口径（[官方] https://www.workbuddy.cn/docs/workbuddy/Plugins ）：WorkBuddy 把扩展机制统称**插件**，分五类——Skill / MCP / Hook / Agent / Rule。下表按此五类逐项登记，再列非插件的自动化与分发渠道。依据等级：`[官方]`＝官方文档（附 URL）；`[实测]`＝本机直接观测（文件、日志、记账文件）；`[推断]`＝由前两者推出、未经直接验证。**没有官方依据的落点不得写成官方规范。**

| 官方机制 | 官方定义文件 / 落点 | 触发入口 | 能力边界 | 能承接的治理规则 |
|---|---|---|---|---|
| Skill（技能插件） | `[官方]` 规范 https://open.workbuddy.cn/docs/skill —— `{skill-name}/SKILL.md` ＋ `references/`、`scripts/`、`templates/`；frontmatter 必填 description / description_zh / description_en / version / author，可选 name / allowed-tools / disable-model-invocation / user-invocable。`[实测]` 本机落点 `C:\Users\纳\.workbuddy\skills\<name>\SKILL.md`（23 个目录，2026-09-19 实测） | `[官方]` 用户消息文本匹配 `description` 自动调用，或对话中召唤；`disable-model-invocation: true` 仅手动触发，`user-invocable: false` 仅供模型内部调用 | `[官方]` 常驻只有 name＋description，正文按需载入；启用/关闭记在用户全局配置、**不改动技能原文件**，关闭≠卸载；**无「文件类型自动触发」** | 有触发条件的治理流程 → 治理型 skill（skill-creator、reflection-evolution、system-refactor、workbuddy-function-control）；其 `description` 未覆盖的触发场景＝该规则在本平台不存在 |
| MCP（MCP 插件；连接器＝「MCP＋Skill」或「CLI＋Skill」的打包分发，一个连接器只能选一种方案） | `[官方]` 连接器规范 https://open.workbuddy.cn/docs/connector —— `connector-meta.json`＋`mcp.json`＋`icon.svg`＋可选 `skills/`；CLI 方案改用 `cli.json`；管理页 https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Connector 。`[实测]` 本机 `C:\Users\纳\.workbuddy\mcp.json`（2 个 Server：playwright、lighthouse-ops）；连接器实例 `connectors\<id>\{mcp.json, connector-states.json}`；连接器自带 skill 在 `connectors\skills\connector-*`；市场缓存 `connectors-marketplace\`；信任记录 `mcp-approvals.json` | `[官方]` 客户端左侧「连接器」→ 点 ＋ → 扫码或授权 → 平台自动挂载工具；自定义连接器按 MCP 配置 | `[官方]` 一个连接器只配一个 MCP Server；远程须 HTTPS（SSE／streamableHttp）；单次请求建议 30 秒内；**每个连接器独立授权、不主动定时抓取、不超出已有权限范围** | 外部数据来源按 `cite-sources` 标来源等级；可用性核查按 [../OPERATIONS.md](../OPERATIONS.md)「核查、覆盖度与可用项」穷举 |
| Hook（钩子插件） | `[官方]` 插件系统页「在特定时机自动执行操作」（同上 URL）。`[实测]` 本机实例 `plugins\cache\local\tool-guardian\1.0.0\`：`.codebuddy-plugin\plugin.json` 以 `"hooks": "hooks/hooks.json"` 声明，hooks.json 定义 PreToolUse（matcher `Bash` → `guard-tool.sh`，`GUARD_MODE=block`）与 PostToolUse（matcher `Bash` → `audit-install.sh`） | `[官方]` 插件被加载后由工具调用事件触发。与 skill frontmatter 的 `hooks`（须 `context: fork`）是**两套机制**，勿混 | **本机可用性未验证**：该实例日志只有 2026-07-06 两条，早于它 2026-08-10 的安装时间，自安装以来零触发记录 → 不得作为某条治理规则的唯一执行入口 | 设计意图＝承接「安装 / 下载审计」（OPERATIONS 第 6 节）与危险命令拦截；**当前实际仍靠模型自律**，见本节末尾缺口 |
| Agent（智能体插件；专家 / 专家团） | `[官方]` 专家规范 https://open.workbuddy.cn/docs/expert —— `my-expert/{.codebuddy-plugin/plugin.json, avatars/, agents/<name>.md, README.md}`，`plugin.json` 的 `expertType` 为 `agent` 或 `team`。`[实测]` 本机自建 `experts\custom\<id>\`；市场安装包在 `plugins\cache\experts\<name>\<ver>\` | `[官方]` 左侧「专家·技能·连接器」→ 专家市场 → 召唤（角色切换）；专家团由团长拆解、并行执行、整合交付。`[实测]` **不经 Agent 工具委派**（2026-08-20 探针 `Task agent <name> is not available`） | `[官方]` 专家本身不主动获取系统权限，仅处理你主动提供的对话与上传文件；配备 Skill／MCP 时才在授权下间接访问；创建后名称不可改；专家团消耗为单专家数倍 | 领域任务的可选载体，**不构成依赖**——规则不能以「委派给某专家」为执行入口 |
| Rule（规则插件） | `[官方]` 插件系统页列为五类之一（作用＝「定义 WorkBuddy 的行为规范」）；规则文件规范 https://www.workbuddy.cn/docs/ide/User-guide/Rules 。规则以 `*.mdc` ＋ frontmatter（`description` / `globs`（官方 CLI 文档作 `paths`）/ `alwaysApply` / `enabled`）随插件分发。`[实测]` 官方市场已有**纯规则插件**先例 `codebuddy-plugins-official/plugins/security-rules/`（`.codebuddy-plugin/plugin.json` ＋ `rules/security_rules_v5.mdc`，`globs: **/*` ＋ `alwaysApply: true`），另有 20 余个市场插件包内含 `rules/`；**`rules/` 按约定自动发现，不在 `plugin.json` 里声明**（对照：`skills` / `commands` / `hooks` 需声明）。生效前提是该插件**已安装**（`installed_plugins.json` 记账）；本机尚未安装任何规则插件 | `[官方]` 三种应用类型：**总是**（alwaysApply，全文常驻）／**智能体请求**（按 description 判断）／**手动**（`@my-rule`）；`globs`／`paths` 命中文件时条件触发；改规则后须**新开会话**才生效 | `[官方]` 是**约束**而非工作流；项目级 > 用户级同名优先。**待实测**：WorkBuddy 桌面版是否加载 `rules/` 并注入上下文。`[实测]`（2026-09-21 扫 `app.asar`）程序内**确有** `parseRuleFile` 代码路径，按 `enabled` / `paths`→`globs` / `alwaysApply` 三元解析，并同时收集**用户级**与**项目级** `rules` 目录——**代码路径存在 ≠ 实际注入上下文**，注入与否仍未验证 | **拟作「通道三」**：把无条件门禁做成薄规则插件、走用户级插件系统（安装／启用／卸载由平台管理，取代「借 SOUL 通道」）；**不搬运 OPERATIONS 全文**——`alwaysApply` 是常驻，全文常驻与 `AGENT-CONTEXT.md` §3 的上下文预算冲突。可行性已具备，**未实施，待用户点头** |
| Automation（自动化；非插件） | `[官方]` https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Automation-Guide —— 配置项＝名称／提示词／工作空间／权限模式／模型与技能／定时规则／推送。`[实测]` 工具 `automation_update`；备份 `automation-backups\` | `[官方]` 到点由平台以当前登录身份自动发起 Agent 任务；`[实测]` 会话内亦可由 `automation_update` 直接建改 | `[官方]` **仅支持时间触发，不支持文件变更触发**；配置存**本地客户端、非云端**（换机不迁）；工作空间限定文件读写范围；受频率／最大时长／并发限制 | 周期性治理动作（lint 巡检、治理体检）的执行载体——**换机须在新机重建**，不得默认它随环境迁移 |
| 插件市场（分发渠道） | `[官方]` 插件系统页「添加插件市场」：插件页点 ＋ 输市场地址。`[实测]` `plugins\known_marketplaces.json` 现 6 源——内置 `workbuddy-builtin`／`cb_teams_marketplace`／`codebuddy-plugins-official`（zip 自动更新），本地目录 `local`／`experts`／`my-experts`；安装记账 `plugins\installed_plugins.json`，落点 `plugins\cache\<市场>\<插件>\<版本>` | `[官方]` 插件管理页安装／卸载；内置源自动更新 | `[官方]` 安装即改变本地能力集；第三方市场与插件须自行审慎评估（官方只做安装前安全扫描） | 安装 / 下载一律走 [../OPERATIONS.md](../OPERATIONS.md) 第 6 节四步（含审计记录） |

**没有挂到任何入口的治理规则只是纸面规则**——这类缺口按 [../OPERATIONS.md](../OPERATIONS.md)「执行缝隙兜底」处理并记当日 Memory。当前已识别的缺口：OPERATIONS 第 6 节「安装 / 下载审计」在本机有 Hook 插件实例试图承接，但未验证生效（见 Hook 行）。

## Python 解释器与隔离环境（本机事实）

登记本机可用的解释器与各自的依赖状态。**「跑脚本该用哪个解释器」的单一权威在本节**——其他 skill 与文档只引用本节，不各自硬编码路径。

| 解释器 | 路径 | 依赖状态（2026-09-20 实测） |
|---|---|---|
| **托管 venv —— 跑脚本首选** | `C:\Users\纳\.workbuddy\binaries\python\envs\default\Scripts\python.exe` | Python 3.13.14；已装 PyYAML 6.0.2、ruamel.yaml 0.19.1、python-docx 1.2.0、PyMuPDF(fitz) 1.28.0、Pillow 12.3.0、rapidocr（新包名） |
| 托管 base | `C:\Users\纳\.workbuddy\binaries\python\versions\3.13.12\python.exe` | 目录名写 3.13.12、实报 3.13.14；**无 PyYAML**、无上述第三方库，只有标准库 |
| 系统（fallback） | `C:\Users\纳\AppData\Local\Microsoft\WindowsApps\python{,3,w}.exe` | Python 3.14.6；**无 PyYAML** |

规则：

- **跑需要第三方库的脚本 → 用 venv 的解释器**。venv 由托管 base 建成，是它的超集；venv 不存在时退回 base，最后才退回 PATH 上的 python。
- **安装依赖只装进 `binaries\python\envs\` 下的隔离环境**，不装 base、不装系统 Python（平台包隔离要求＋[../OPERATIONS.md](../OPERATIONS.md) 第 6 节四步流程）。
- **不要拿单个解释器的探测结果推及整机环境**。某个解释器报 `ModuleNotFoundError` 只说明它自己没有这个包，不说明"环境没装"。陈述"缺少某依赖"前先穷举本节全部解释器（必要时再扫全盘包目录与 pip 缓存），且只用穷举口径（"我在这 N 处都试过，都没有"），不用全称句。
- **Bash PATH 损坏（见下节）→ 只能写绝对路径调用解释器**，所以"默认用哪个"完全取决于文档里写的是哪条路径。这正是必须把解释器选择收在本节一处的理由；零散硬编码会各自传播同一个默认值。

**反面记录（教训）**：2026-09-03 / 09-04 / 09-05 / 09-19 / 09-20 五篇 Memory 里都出现过"本机 / 环境没装 PyYAML"的结论，实际是拿托管 base 解释器单点探测的结果外推；09-19 的安装审计其实已核实 venv 里早有 6.0.2，次日仍被复述。教训见用户级 `MEMORY.md`（本机文件，未随公开仓上传）T22。

## Git 凭据与凭据管理器（本机事实）

登记本机 git 取凭据的机制与落点。**「GCM 装在哪、helper 怎么配」的单一权威在本节**——其他 skill 与文档只引用本节，不各自硬编码路径（与上节解释器的处理相同；依据 [../MACHINE.md](../MACHINE.md)「迁移流程」第 3 条：治理内容出现硬编码机器信息即违规）。

| 项 | 值（2026-09-20 实测） |
|---|---|
| ① PortableGit 自带 | `C:\Users\纳\.workbuddy\binaries\PortableGit\versions\1.2.0\mingw64\bin\git-credential-manager.exe`（132,920 B），版本 **2.9.0** |
| ② 系统 Git 自带 | `C:\Program Files\Git\mingw64\bin\git-credential-manager.exe`（133,192 B），版本 **2.7.3** |
| helper 名 `manager` 解析到 | **②**（`git credential-manager --version` → 2.7.3；`GIT_TRACE` 显示 `run_command: git credential-manager get`） |
| 令牌落点 | **Windows 凭据管理器**，条目 `LegacyGeneric:target=git:https://github.com`；`~/.git-credentials` 不存在 → **无任何明文令牌文件** |
| 两份 GCM 的关系 | 读的是**同一个** Windows 凭据条目，实测取到的 username / password 完全一致 → 对取令牌而言可互换 |

**配置链（三层叠加，最后一层清链）**：

1. 系统级 `C:\Program Files\Git\etc\gitconfig` → `credential.helper = manager`
2. PortableGit `versions\1.2.0\etc\gitconfig` → `credential.helper = helper-selector`（Git for Windows 首次运行引导器，**即「每次要凭据就弹选默认框」的根源**；该 PortableGit 内确有 `git-credential-helper-selector.exe`）
3. 用户级 `C:\Users\纳\.gitconfig` → `credential.helper =`（**空值，清掉前面整条累积链**）＋ `credential.helper = manager`

→ 叠加后链上只剩 `manager` 一项：直读 Windows 凭据管理器，非交互、无弹窗。**用户级那行空值不能删**，删了就退回 selector 弹窗。

**版本脆弱性（必须留意）**：`binaries\PortableGit\current` **不存在**（该目录下只有 `versions\` 与 `versions\1.2.0\`，均为 reparse 目录）→ PortableGit 下**没有**与版本无关的入口；任何写死 `versions/1.2.0/…` 的路径都会在 PortableGit 升级后立即指向不存在的 exe。**故一律用 helper 名 `manager` 引用，不写版本化绝对路径。**

**取令牌（不提取、不记录内容）**：`printf "protocol=https\nhost=github.com\n" | GIT_TERMINAL_PROMPT=0 GCM_INTERACTIVE=never git -c credential.helper= -c credential.helper=manager credential fill`；管道与推送的完整写法见 `skills/git-workflow` §5（该 skill 未随公开仓上传）。GCM 自带 `get`/`store`/`erase`/`configure`/`diagnose`/`github list|login|logout`，排障可用 `git-credential-manager diagnose`。

## 运行时坑（实测）

- **原生工具链路径**：Bash（Git Bash）调用 Windows 原生程序（python3.exe / node.exe / 7z.exe）传文件路径必须用 `C:/...` 或 `C:\...`，禁止 msys 风格 `/c/...`——会被错拼成 `c:\c\`。凡路径交给原生 exe，先换风格。
- **Git Bash PATH 损坏（2026-09-19 实测）**：`ls` / `dirname` / `head` 等内建命令均 command not found → 本机优先用 PowerShell 与专用文件工具（Glob / Read / Grep），不依赖 Bash 内建命令。
- **同一文件不要在同一批工具调用里并发编辑（2026-09-19 实测）**：对同一个文件在同一批中发起多个编辑时，后一次写入会覆盖前一次的改动——工具仍回报成功，但前一处改动丢失。改同一文件的多个位置须**串行**执行（一次调用只改一处），且每次写入后读回或 grep 确认落盘。
- **PowerShell 工具可能不回显 stdout（exit 0 却无输出）**：需要看命令结果时，先把结论 `Set-Content` 写入临时文件再 Read，不要依赖 stdout。
- **PowerShell `Get-ChildItem -Exclude` 会静默滤空结果（2026-09-19 实测）**：`Get-ChildItem -File <dir> -Exclude *.pyc | ForEach-Object { Copy-Item ... }` 一个文件都没复制、且不报错，目标目录最终为空。批量复制改用「先取全部文件，再用 `Where-Object` 按扩展名过滤」，复制后必须逐文件确认目标存在（不能只看命令退出码）。

- **删除被平台 safe-delete 接管：实际进回收站，却会误报失败（2026-09-19 实测）**
  - **机制**：`settings.json` 的 `sandbox.safeDeleteRuntimeEnabled`（本机 `true`；同节还有 `deleteProtection`、`safeDeleteBulkThreshold`、`versionControl`）经 `buildSafeDeleteEnv()` 注入 `CODEBUDDY_SAFE_DELETE_*` 环境变量，由**随程序发布的 shim** 执行：bash 侧 `cli\vendor\shim\safe-bin\{rm,rmdir,unlink}` ＋ `safe-delete-common.sh`、Node 侧 `node-safe-delete-shim.cjs`、Python 侧 `sitecustomize.py`。删除一律送 **OS 回收站**（i18n：`safeDelete.target.windows = "回收站"`）；**唯一例外**＝ OS 临时目录（`%TEMP%` 等）下的路径，走真删、不回收。
  - **平台无自定义落点**：**没有**「把删除移到指定 trash 目录」的配置项。`GENIE_TRASH_DIR` 只指定 `genie-trash` 二进制所在目录，不改变落点。要改落点只能改上述 shim 文件本身（属程序文件，随版本更新会被覆盖，且 asar 头里带 integrity 哈希）。
  - **实测（四位置逐一删除 ＋ 回读回收站 `$I` 记录）**：工作区内、`~/.workbuddy`、`~/Documents` 的删除**全部回报** `[safe-delete][SAFE_DELETE_FAIL_CLOSED] {"reason":"trash-failed", …, "Some operations were aborted"}`，但**文件实际已删除**，并能在 `C:\$Recycle.Bin\S-1-5-21-…-1001\` 找到对应 `$I` 记录（含原始路径）→ 结论是**「删成功、报失败」的误报**；只有 `%TEMP%` 下不报错。根因是 Windows trash crate 的 `IFileOperation::GetAnyOperationsAborted` 误报（shim 注释已记载），bash 侧有「以文件系统事实为准」的兜底，**PowerShell / Node 这条路径没有**。
  - **后果（要紧）**：该错误是**终止性错误**（`RuntimeException`），未被捕获时会**让整个脚本静默中止、不产出任何输出**（exit 1、无 stdout）——本会话两次「脚本跑到一半无声结束」即此故，曾误判为「工作区内删除正常、只有工作区外失败」。
  - **可用手段（2026-09-19 实测，按推荐序）**：① **移动代替删除**——`Move-Item` / `Rename-Item` **完全不触发 shim**（工作文件夹内、跨目录、从 `~/.workbuddy` 到工作文件夹，全部无报错、目标到位）→ 工作文件夹内的删除一律先移到 `.trash/`；② **要进系统回收站且不想看到报错 → 用 Python**：`os.remove()` / `shutil.rmtree()` **零报错**，且文件**确实进了回收站**（`$I` 记录已逐条核对）；从 PowerShell 工具里调 python 一样有效（shim 的 `CODEBUDDY_SAFE_DELETE_ENABLED` / `PYTHONPATH` / `GENIE_TRASH_DIR` 照样注入）——**这是目前唯一「报干净、又真进回收站」的命令**；③ 必须真删的（OS 临时目录、构建产物）用 `[System.IO.File]::Delete()` / `[System.IO.Directory]::Delete($p,$true)`（.NET 直删、**不可恢复**）；④ 不得已用了 `Remove-Item` 时**必须包 `try/catch`**，并在删后用 `Test-Path` 复核事实（文件已消失＝成功，忽略该报错）；⑤ 不用 `Remove-Item` 做「验证性删除」。
  - **PowerShell 侧走不通的替代路径（本工具安全策略拦，不是机器限制）**：`Add-Type`（连带 `[Microsoft.VisualBasic.FileIO.FileSystem]::DeleteFile(..., SendToRecycleBin)`——正是平台 bash 兜底所用的同一 API）、`[System.Reflection.Assembly]::Load*`、`New-Object -ComObject`（Explorer 的 `InvokeVerb('delete')`）全部被拦。`genie-trash` 二进制直调**没有用**：实测 `resources\vendor\genie-trash\win32-x64.exe` 同样是 `exit=1` ＋ 同一误报（文件照样进回收站）——**说明缺陷在原生程序内部，不在 shim**。
  - **不要用「关掉 `safeDeleteRuntimeEnabled`」来消错**：那等于让删除退回真删、失去回收站兜底（推断，未实测），用不可恢复换掉一条报错，不划算。该误报是平台侧 Windows 缺陷（shim 注释已记载、bash 有兜底而 PowerShell/Node 无），可选路径是反馈官方。
  - **可用作审计**：回收站 `$I` 记录（路径位于 `C:\$Recycle.Bin\<SID>\$I*`，头部 24 字节后为 UTF-16LE 原始路径）可反查某次删除的真实落点与时间——核对「删除去了哪」时用它，不靠命令输出。

- **写文件工具会自动创建缺失的父目录（2026-09-19 实测）**：向不存在的目录下的路径写文件时，工具**静默建目录**并回报成功。写临时文件前先确认目标目录是否本应存在——曾因此在治理根凭空生成一个 `.trash`，与 `文件夹目录.md` 登记的「当前未创建」冲突。临时文件写进已存在的删除落点，别新造路径。

- **bash shim 缺 `mkdir` / `ls` / `dirname` / `grep` / `head` / `cut`，且命令失败不会终止脚本（2026-09-19 实测，已致事故）**：本环境 bash 下这批命令 command not found，而 `cd` 失败后脚本**继续在原当前目录执行**——一次「`mkdir -p $T` 后 `cd $T` 再跑 `git init`」的实验因此**在工作区根目录 `Desktop\新建文件夹` 建出了一个 `.git` 仓库并写入测试文件**（事后已清掉，`整合工作稿` 仓库未受影响）。规避：① 建目录、删文件改用 PowerShell 与 `[System.IO.Directory]` / `[System.IO.File]`；② 脚本里换目录一律写 `cd X || exit 1`；③ 破坏性命令（`git init`、删除、写文件）执行前先校验落点，例如 `git rev-parse --show-toplevel` 或 `pwd`，确认在预期目录再动手。

- **经 shell 传文本会被静默改写（2026-09-19 / 2026-09-21 各一例，均已致事故；通则见 [../OPERATIONS.md](../OPERATIONS.md)「改动前告知、范围与停止」）**：
  - **PowerShell 双引号展开 `$`，且变量名大小写不敏感**：用双引号字符串拼接含 shell 变量（如 `$T`）的文本时，`$T` 被当成 PowerShell 的 `$t` 展开——**整个文件内容被嵌进那一行**，文件体积涨到 3 倍、内容重复三份。
  - **bash 反引号被当命令替换**：把含反引号的文本直接嵌进 `python -c "..."` 的双引号串时，反引号包裹的片段被当成命令执行、内容被吞掉（写当日 Memory 时实际发生，已当场改为脚本文件重写修复）。
  - **规避（两例同）**：写入含特殊字符的文本先落成脚本文件；写完核对体积与关键串，体积异常增幅就是信号。
  - **2026-09-21 修改记号**：本条原为「PowerShell 专用」单条；通则已升入 OPERATIONS，此处只留本程序实例与证据。

- **Git 推送链路与 `refs/remotes`（2026-09-21 实测）**：本会话环境注入本地代理（`HTTP(S)_PROXY=http://127.0.0.1:<端口>`，本次为 60355，端口随会话变）。习惯性的 `no_proxy=github.com` 直连**可能**失败（`Connection was reset` / 443 超时），而改走代理**也可能**失败（`CONNECT tunnel failed, response 502`）——**两个方向都要试**，本轮即直连失败后一次重试成功。另：本仓 `git fetch` 会报 `* [new branch] main -> origin/main`，但 `refs/remotes/origin/main` **不落地**（`refs/remotes` 为空、无 `packed-refs`），故 `status -sb` 与 `branch -vv` 恒显示 `[gone]`——**推送不受影响**。核对是否真推上去，用 `git ls-remote origin refs/heads/main` 与 `git rev-parse HEAD` 比对，**不要相信 `[gone]`**。

## 子代理委派（已核实 2026-09-20）

- **怎么委派**：本程序经**函数列表里的 `Agent` 工具**显式委派；`subagent_type` 可取 `general-purpose` / `Explore` / `Plan` / `sheet-agent` / `doc-converter` / `doc-formatter` / `doc-writer` 等（**以工具定义为准**，本节不逐一复述）。实测可委派并取回完整结果。**未观测到模型侧自主委派**——实际用法是主 agent 显式调用。
- **平台自己已规定的子代理要求（随委派方的系统提示词常驻，本节不复述）**：只读类型（`Explore` / `Plan`）不得派实现类任务；探索类任务优先用 `Explore`（平台给的理由是省上下文）；并行子任务写在同一消息里；子代理的汇报只算「它打算做什么」（须核实际变更）；简报要给足背景与目的（它看不到本对话）。**2026-09-21 实测：这些只到委派方，子代理侧看不到任何一条**——两个探针（`general-purpose` / `Explore`）均报告未被注入治理文件、也没有「写清任务目的」「不要删内容」这类要求；后者落在下文骨架 ② 边界里，须按任务写。**本节只补平台未展开的部分**：类型→工具的完整边界、积分倍率、选型判据、回传上限。
- **类型 → 能力边界**（2026-09-20 依工具定义整理）：

  | `subagent_type` | 能碰什么 | 碰不了什么 |
  |---|---|---|
  | `general-purpose` | 全部工具：读 / 写 / 改文件、跑命令、联网、任务管理 | — |
  | `Explore` | 只读 + 检索：Read / Glob / Grep / 命令行 / 联网检索 | **不能改文件**（无 Edit / Write） |
  | `Plan` | 只读，产出实施方案；可建团队 | **不能改文件** |
  | `sheet-agent` | 表格读写、公式、分析（MCP 表格工具） | 不碰非表格任务 |
  | `doc-converter` / `doc-formatter` / `doc-writer` | 文档流水线三段（转换 / 美化 / 创作） | 各只管其中一段 |
  | `statusline-setup` | 改状态行配置（有 Read / Write / Edit） | **无命令行、无检索** |

  → 派 `Explore` / `Plan` 去改文件、派 `sheet-agent` 去读 PDF，都是白花积分的典型。

- **一次委派的成本构成（补「经济」这一半）**：**积分 ≈ 该模型倍率 × 子代理消耗的 token × 轮次**（倍率见上表）；**并行 N 路＝整笔 ×N**；子代理的回传**整段进主上下文**，等于再计一次。三条护栏：① **并行分治一律用 0.00x 档**（N 路分治最容易被倍率放大）；② 给 `max_turns` 设上界作止损——其**行为未实测**，只记「可作止损」；③ prompt 里**限定回传长度**（只要结论与证据位置，不要原文）。
- **委派前三问**：① **类型**选对了吗（对照上表）？② **模型档**按「需要多少智力 × 错了要返多少工」选了吗（默认取最省）？③ **并行数 × 倍率**算过吗、**回传长度**限了吗？
- **子代理 prompt 骨架（四项必带）**：子代理**读不到任何治理文件**（它只带平台给的小提示 ＋ 本条 prompt），所以下列四项只能随 prompt 走：① **任务与产物落点**（做什么、结果放哪——不给路径它会自己猜）；② **边界**（只读还是可写、禁止做什么）；③ **回传格式 ＋ 长度上限**；④ **可验证项**（需要时要求它自述实际运行的模型，用于确认路由生效）。

  **四项均已实测（2026-09-21 控制组：只给任务目标，四项全不给）**：不给落点 → 它**自己挑路径**，把产物写进了用户工作目录（`Desktop\新建文件夹\`，该处我没提过）；不设边界 → 就往那个目录写；不给格式与长度 → 它自定格式，并把源文件原文抄进产物；不要求自述模型 → 不问就不报（本次未报）。四项**平台一条都不提供**——平台只规定「简报要给足背景与目的」「只读类型不得派实现类任务」「并行子任务写在同一消息里」。

  **归属与判据**：这四项平台都不定义，故归本文件。**“要不要写某项”按 [../OPERATIONS.md](../OPERATIONS.md)「规则先行原则」第 3 步核管辖归属**——平台或治理文件已定义的即不重复写（如“简报要给足背景与目的”已在平台要求里，就不进骨架）；实测只作“槽位确有必要”的佐证，不作重复性判据。

- **`Agent` 的 `model` 参数（2026-09-20 实测）**：**能调不同模型**——参数真实生效并做名称解析；**无法识别的值静默回落到默认模型、不报错**（名字拼错等于没换，且不会提示）。解析结果未必等于显示名：`Kimi-K2.7-Code` → `kimi-k2.7`（后缀被丢）、`Kimi-K3` → `kimi-k3-1`、`Hy4 preview` → `hy4-preview`。**验证手段**：子代理能自述自己实际运行的模型（模型名写在其上下文中，自述来源标注为「上下文里明确写出的」）——**回问一句即可确认，不要凭传参假定已切换**。
- **可用模型与积分消耗倍率（2026-09-20 取自模型选择器）**：倍率是**每 token 的积分开销倍率**，不是质量分。

  | 选择器显示名 | 积分倍率 | 传入 `model` 实测解析为 |
  |---|---|---|
  | Hy4 preview | **0.00x**（限时免费） | `hy4-preview` ✓ |
  | Hy3 | **0.00x**（限时免费） | `hy3` ✓ |
  | Deepseek-V4.1-Flash | 0.03x（独家优惠） | 默认模型（不传 `model` 即此） |
  | GLM-5.3-Flash | 0.06x | `glm-5.3-flash` ✓ |
  | MiniMax-M3 | 0.25x | `MiniMax-M3` ✓ |
  | Kimi-K2.6 | 0.52x | `Kimi-K2.6` ✓ |
  | Kimi-K2.7-Code | 0.57x | `kimi-k2.7`（显示名后缀被丢） |
  | GLM-5v-Turbo | 0.71x | `GLM-5v-Turbo` ✓ |
  | Kimi-K2.8-Preview | 0.77x | `Kimi-K2.8-Preview` ✓ |
  | GLM-5.3 | 0.79x | `glm-5.3` ✓ |
  | GLM-5.2 / GLM-5.1 | 0.79x（5.2 夜间折扣） | 未实测 |
  | Kimi-K3 | 1.62x | `kimi-k3-1` ✓ |

  （已下架或不存在者静默回落默认：`GLM-4.7`、`sonnet`、随机名实测均回落。）

- **看图**：`GLM-5v-Turbo` 与**默认模型**均实测能准确读出截图内容——读图不是 `5v` 独有；底层是模型多模态还是平台预处理**未核实**。
- **选哪个模型（按积分消耗优先）**：判据是「这活需要多少智力」×「错了要返工多少」，**默认取最省的那一档**。
  - **批量机械活**（全量通读、清点、机械改写、跑验证脚本、并行分治的每一路）→ **0.00x 免费档**（`Hy4 preview` / `Hy3`），不够用再上 `GLM-5.3-Flash`（0.06x）。**并行铺开时尤其要用免费档**——N 路分治会乘 N 倍开销。
  - **常规执行** → 不传 `model`（默认 `Deepseek-V4.1-Flash`，0.03x）。
  - **需要独立判断、复核、挑战我的结论** → 0.7x 档（`GLM-5.3` / `Kimi-K2.8-Preview`）。
  - **只能一次做对、或要它对撞我的结论** → `Kimi-K3`（1.62x），**不用在能返工的活上**。
  - **纯代码活** → `Kimi-K2.7-Code`（0.57x）。
  - 以上用途线由**名称族＋消耗倍率＋通用认知**推出，**不是实测的能力对比**；要在具体任务上比过一轮再回来改。
- **子代理定义的真实落点**：**插件包内** `plugins/marketplaces/*/plugins/*/agents/*.md`（本机 669 个；分布如 codebuddy-plugins-official 117+41+15+12+11+11+8、seo-expert 33、ai-hedge-fund 21、trading-agent 12、a-share-analysis 7）。`~/.codebuddy/agents/` 与 `.codebuddy/agents/` **本程序不加载**（前者实测为空目录）。
- **本程序不设 `subagent` skill，也不需要**：委派机制（本节）与委派判据（[../OPERATIONS.md](../OPERATIONS.md)「委派与分工」）已各有归属。曾有同名 skill 因通篇描述 **CodeBuddy Code CLI**（落点、`/agents` 命令、模型别名、frontmatter 格式均与本程序不符）而被删除（2026-09-20）。**不要再建同名载体。**
- **专家机制**：expert-manager 自建专家＝角色注入（当前 AI 切换人格），**不经 Agent 工具委派**——机制、落点与探针依据见「官方机制 → 治理接口」Agent 行，本节不复述。
- **CodeBuddy Code 文档 vs 本程序实际（2026-09-20 登记）**：文档所称子代理目录 `~/.codebuddy/agents/`、`.codebuddy/agents/` 本程序不加载（走 `plugins/marketplaces/*/plugins` + `expert_id`）；文档里的模型别名 `gpt-5.1-codex` / `gemini-3.0-flash` / `gemini-3.1-pro` 在本程序实际为国产模型（`hy3` / `deepseek-v4-flash` / Kimi / GLM / MiniMax 等，**当前清单与积分倍率见上表**）；文档 `/agents` 命令对应专家中心（专家 / 专家团）；环境变量为 `WORKBUDDY_*` / `CODEBUDDY_SESSION_ID`；专家包结构为 `plugin.json` + `agents/*.md`。逐条详表见 `skills/workbuddy-manager/references/extensions-overview.md`（未随公开仓上传）。

## Skill 触发机制（官方核查 2026-07-11）

**结论**：WorkBuddy/CodeBuddy 的 skill 触发信号是**用户输入文本匹配 `description`**，不是文件类型或上下文自动加载。
- 官方 `skill-dispatcher` 匹配逻辑三类信号：①关键词触发（用户消息出现特定词）②场景推断（对话历史）③手动指定（`@skill:`/`用XX技能`）。三类都以用户消息文本为前提。
- 开放标准 Progressive Disclosure 只规定"加载层级"（metadata 常驻、body 触发时载入、references 按需），不提供"文件自动触发"信号。
- 推论：用户上传/提及 PDF 却没说"提取"，pdf-text-extractor 浅匹配可能不触发；"填表→数据在PDF→用pdf skill"的跨步推理当前调度器不做。

**改进路径（按可行性）**：
- A. 改 skill 的 `description`，写明触发条件
- B. 在 SOUL.md/项目约定写规则强制加载
- C. **历史兼容补充：Hooks `FileChanged`**（`watchPaths: ["*.pdf"]`）——部分平台版本提供此类事件入口；只有平台明确启用、非内置 skill 的信任设置和 `context: fork` 等条件满足，并经实测后才可使用，不能作为开放标准或跨平台的文件自动触发保证；插件级 hooks（`plugin.json` 声明 `hooks/hooks.json`）为另一套机制，见「官方机制 → 治理接口」Hook 行。它与插件级 hooks 是两套机制：本机 `reflection-evolution` 的顶层 `hooks` 未配 `context: fork`，当前不能当自动链路，配置暂保留供兼容；非内置 skill 另需 `allowUntrustedFrontmatterHooks: true`
- D. Automation 定时扫文件夹（批量/周期，非实时）
- E. 手动 `@skill` / `/skills`

**跨平台对比**：所有采用 agentskills.io 开放标准的实现，SKILL.md 层面触发都是 description 语义匹配（LLM 推理，非关键词正则），**无一家原生支持"文件类型自动加载 skill"**。
- Claude Code：description 语义匹配；Hooks（PreToolUse/PostToolUse/Stop）可 hook 工具调用
- Codex CLI：`$skill-name` 显式 + description 隐式
- Gemini CLI：activate_skill（任务匹配 description）+ 用户确认
- GitHub Copilot：同开放标准
- Cursor：**Skills** 也是 description 匹配；但其 **Rules**（.mdc）用 `globs` + `Apply to Specific Files`/`alwaysApply` 实现"文件匹配自动加载"——唯一明确的文件类型自动触发，但属 Rules（约束）而非 Skills（工作流）
- Warp Oz：编排层支持 schedule/webhook/system event 触发 skill，非 skill 原生
- 社区 workaround（Superpowers）：在 CLAUDE.md/AGENTS.md/GEMINI.md 写"任务前先检查 skills 目录匹配上下文"
- 推论：用户要的"遇到 PDF 自动用 pdf skill"在 skill 层面确非原生能力；**但本平台自身的 Rule 机制支持 `paths` glob 条件触发**（`[官方]` https://www.workbuddy.cn/docs/ide/User-guide/Rules ），可达成等效效果——差别在载体是 Rule（约束）而非 Skill（工作流）。Cursor 用 Rules globs 属同型实现

**自动反思/自我纠错机制（2026-07-11 查）**：没有专门的"auto-reflect"参数。用户纠正做法但未说"你错了"时自动反思，靠三种非参数机制兜底：
- ① description 语义匹配：reflection skill 的 description 写"用户纠正/给出不同正确做法时触发"
- ② system prompt/SOUL 规则：写"用户给出不同做法时必反思"
- ③ 平台特定 Hooks Stop 事件：Claude Code 有 Stop hook，CodeBuddy v2.97.0 有 Stop 类事件 + prompt 类型 hook；只能作为历史兼容/补充路径，不能替代 Agent 自主判断和实测核验
- 跨平台结论：Claude/Cursor/Codex/Gemini 均无"对话内自动反思"可配置参数；通用做法是 prompt 工程

## 深度细节索引

数据布局（`~/.workbuddy/projects/` 等）、跨对话通信、扩展机制八面全景：见第三版 `skills/workbuddy-manager/references/`——不入治理备份、也未随公开仓上传，按需取文件。
