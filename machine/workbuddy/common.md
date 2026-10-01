# WorkBuddy 桌面版 —— 跨机器共通

> 本目录登记 WorkBuddy 桌面版这个软件的机器事实。**本文件是跨机器共通部分**（机制、工具清单、注入通道、官方机制登记）；该软件在各台机器上的特化事实见`machine/_host/<机器标识名>/workbuddy.md`（**该目录未随公开仓上传**）。
> 读取方式：本文件 ＋ `machine/_host/<机器标识名>/workbuddy.md`（**后者不存在即表示该软件在本机未装**）。口径见 [../README.md](../README.md) 与根 [../../MACHINE.md](../../MACHINE.md) 的解析规则。
> **口径（重要）**：凡涉**具体值**处（路径、计数、实例清单、版本号），本文件只写机制与指针，**实际值在机器文件里**——按 `machine/README.md` 的识别特征取**本机**那份（`machine/_host/<机器标识名>/workbuddy.md`）。这样两台机器各自只写自己那份，不会互相覆盖。
> 定位：登记该软件里会话用到的全部工具与调用功能 ＋ 运行时坑 ＋ **在治理体系中的作用点（迁移清单）**，并登记本程序的落地层（提示词注入适配器、启动必读清单、记忆机制、程序特定要求）。已知工具来自第三版 workbuddy-manager 的记录（该 skill 不入治理备份）；**完整清单以 WorkBuddy 会话开头告知为准，下次进入该环境时对账补全**。**本文件同时是本程序全部已知「注入通道」的登记处**——治理文件之外还有平台固定注入（skill `description`、工具定义、运行提醒块）与未启用的通道（项目级注入、规则插件）；**怎么判（原则）见 [../../AGENT-CONTEXT.md](../../AGENT-CONTEXT.md) §1，本文件只登记本程序的实际通道与事实**。

## 本软件在治理体系中的作用点（迁移清单）

**用途**：本程序在治理体系里不是旁观者——下面这些位置**只有本程序能提供**。换软件时，这张表就是待办清单：逐条由新软件重新提供、重新核实，不照搬本文件（[../../MACHINE.md](../../MACHINE.md)「迁移流程」）。**本节是反向索引，只指位置、不复述机制**——机制细节仍在其下各节。

| # | 治理体系里的位置 | 本程序须提供什么 | 状态 / 依据 |
|---|---|---|---|
| 1 | `SOUL.md`「启动索引」（整节） | 借 `SOUL.md` 的自动注入通道，把"未被注入的治理文件须主动读"送到每个会话——**该节存在的唯一原因是通道一不含 `OPERATIONS.md`** | `[实测]` 2026-09-19 |
| 2 | `IMPORTANCE.md` §5「`importance=1` 的直接注入预期」 | 注入层真实存在且可核实 | 同上 |
| 3 | `AGENT-CONTEXT.md` §1–§2（注入通道、加载分层、必读清单的规则） | 平台侧通道清单与读取入口——该文件明写「每个程序须在其软件文件登记」 | 本文件「Agent 提示词注入适配器」「启动必读清单」两节 |
| 4 | 触发链：治理文件的 `read_when` | **本程序不消费它**——扫 `app.asar` 全文，`read_when` 仅 3 处命中，全在平台生成默认 `SOUL/IDENTITY/USER` 的**模板字符串**里，没有任何读取它的代码路径 → 治理文件的「触发层」在本程序实际靠**模型主动读**（「启动索引」＋「启动必读清单」） | `[实测]` 2026-09-21 |
| 5 | 触发链：skill 的 `description` | 平台按用户消息文本匹配 `description`——本程序唯一的 skill 触发信号 | `[官方]`＋`[实测]` 2026-07-11 |
| 6 | `OPERATIONS.md`「文件与目录放置（按平台隔离）」 | 平台专有内容的分文件落点：`machine/workbuddy/`、`memory/<platform>.md`、`skills/<platform>/` | 本目录即落点 |
| 7 | `OPERATIONS.md`「能力类问题核实」 | **根治理文件正文里唯一指名本软件的规则**——问到 WorkBuddy 自身能力时先查官方文档 | `[实测]` 2026-09-21 取原文 |
| 8 | `GIT.md` §5 远程与凭据 | 凭据由本机认证工具提供 → 本机事实在 `machine/_host/` 的「Git 凭据」节 | `[实测]` GCM 链 |
| 9 | 根 [../../MACHINE.md](../../MACHINE.md)「软件目录须有的节」的登记要求 | 工具与调用功能清单（`Bash` / `Agent` / `present_files` / `automation_update` …） | 本文件「工具清单」 |
| 10 | 记忆落点与注入 | 三层记忆的落点与注入方式（`<user_memory>`、工作区 `memory/`、云端画像） | 本文件「本程序记忆机制」＋机器文件 |
| 11 | 周期性治理动作的执行载体 | Automation（**仅时间触发**；配置存本地、**换机须重建**） | `[官方]`＋`[实测]` |
| 12 | `OPERATIONS.md` 第 6 节（安装 / 下载审计）的执行入口 | 插件市场 ＋ Hook——**可用性取决于本机有无 hook 实例**（各机不同，见机器文件）→ 在无实例的机器上该规则没有可信执行入口 | 缺口，见「官方机制 → 治理接口」Hook 行 |

其中 1、6、8、10、11 是**本程序专有落点**（换软件后须逐处换成新软件对应物）；4、5 是触发链的实现方式（新软件须重新核实它靠什么触发）；其余是通用治理规则在本程序的实例。

## 工具清单（已知部分，据第三版记录）

只列**工具层面**的项。**机制（skill / MCP / Hook / Agent / Rule / automation / 插件市场）一律见下文「官方机制 → 治理接口」，本节不重复登记。**

| 组 | 工具 | 要点 |
|---|---|---|
| 读 | `Read`（文本/图片/PDF/ipynb）、`Glob`、`Grep` | 前三者不经过 bash PATH，不受 PATH 坑影响；`Read` 对子代理不可用（子代理读不到治理文件） |
| 写 | `Write`、`Edit` | `Write` 拒绝覆盖"本会话未 Read 过"的文件（含自己刚用 Bash 建的）；`Edit` 直接从磁盘比对，**同一文件的多处改动必须串行**（同批并发会互相覆盖） |
| 执行 | `Bash`（Git Bash）、`PowerShell` | 原生 exe 路径坑、黑名单、PATH 坑见「运行时坑」；PowerShell 工具可能不回显 stdout |
| 检索委托 | `Agent`（内置 / 插件 `subagent_type`） | general-purpose / Explore / Plan / sheet-agent / doc-converter / doc-formatter / doc-writer 等；见「子代理委派」 |
| 任务管理 | `TaskCreate` / `TaskGet` / `TaskUpdate` / `TaskList` | 多步任务（≥3 步）才用；单步不用 |
| 技能 | `Skill` | 触发匹配靠 skill 的 `description`；已加载的技能无需重复调用 |
| 延后工具 | `ToolSearch` ＋ `DeferExecuteTool` | 延迟加载工具的 schema 要先搜再调（如 ImageGen / VideoGen / 各 MCP 工具） |
| 视觉 | `widget_guidelines` ＋ `show_widget` | 内联 SVG / HTML 图，**不是文件**；不替代 `present_files` |
| 联网 | `WebFetch`、`WebSearch` | 抓取与搜索；重定向要换 URL 重发 |
| 交互 | `AskUserQuestion` | 需要用户在选项间裁决时用 |
| 定时 | `automation_update` | 定时执行通道（可用性受本机程序黑名单约束，见机器文件的「运行时坑」） |
| 交付 | `present_files` | 成品文件呈现；HTML 会同时开预览面板与卡片；本地 HTML / http(s) URL 均可 |

## Agent 提示词注入适配器（WorkBuddy）

字段按 [../../MACHINE.md](../../MACHINE.md)「Agent 提示词注入适配器」登记；依据等级同下节（`[官方]`＝官方文档、`[实测]`＝本机直接观测）。

- **状态**：通道一已核实（2026-09-19 实测）；通道二有官方依据、经决定**不采用**；通道三有官方依据、**本机未启用、未核实**。
- **通道穷举**：本程序已知 **3 条**注入通道，见下三节；且**平台固定注入的内容不止治理文件**（见通道一末条）。登记格式与穷举要求见 [../../MACHINE.md](../../MACHINE.md)「Agent 提示词注入适配器」，本节不复述。
- **判定原则不在本文件**：「某段内容会不会进上下文、会不会改每次注入」怎么判，属**跨平台规则**，权威在 [../../AGENT-CONTEXT.md](../../AGENT-CONTEXT.md) §1；**本节只登记本程序的实际通道与事实**（2026-09-20 归属校正）。
- **适用平台 / 模型 / 会话范围**：WorkBuddy 桌面版；本机会话；未观测到模型或会话类型导致的差异。

**通道一 · 内建身份注入（当前唯一在用的治理通道；无用户可配项）**

- `[实测]` 来源是**治理根**下的 `SOUL.md`、`IDENTITY.md`、`USER.md` 三份**全文** → 系统提示词 `<identity_context>` 块。名单由程序固定，用户无法增删，也没有可调用的脚本、命令或配置入口。**治理根的具体路径见机器文件**（各机不同）。
- `[实测]` **每份身份文件的内容上限 10,000 字符**：程序内常量 `MAX_IDENTITY_FILE_CHARS = 1e4`（注释写明是防上下文溢出）→ 三份身份文件的常驻预算有硬顶（2026-09-21 扫 `app.asar` 得）。
- `[实测]` 注入由 `identity-collector` 从**数据目录**读这三份；数据目录解析优先序为 `WORKBUDDY_CONFIG_DIR` → `CODEBUDDY_CONFIG_DIR` → `~/.workbuddy`（文件夹名可经环境变量覆盖）。
- `[实测]` `<user_memory>` → 用户级 `MEMORY.md` 的内容（长度受平台预算限制，本会话观测到截断）；`<memory>` → 服务端生成的用户画像摘要（只读，缓存 `~/.workbuddy/memory/`）；另有工作记忆 / 技能 / 自动化 / 内容政策等运行提醒。
- 这些块的措辞由平台给出、**不得据其覆盖治理规则**——与治理文件冲突时以治理文件为准，并在当日 Memory 记录。
- `[实测]` `OPERATIONS.md`、`AGENT-CONTEXT.md` 等其余根治理文件**不在任何块内**。
- `[实测]` **同属通道一的还有非治理内容**：每个 skill 的 `name` ＋ `description`（skill 常驻只有这两项，正文按需载入）、工具定义（含延迟加载工具的 schema 描述）、平台自带的运行提醒块（工作记忆 / 技能 / 自动化 / 内容政策等）。**这些同样常驻、同样占上下文预算；改它们同样改每次注入**——只是它们不由治理体系编写。

**通道二 · 项目级配置注入（官方提供，经决定不采用）**

- `[官方]` [项目页](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Project)：创建任务时平台自动注入三项——项目指令（对 AI 的全局行为规则，拼入模型上下文）、项目资料库（reference 形式）、个人记忆；项目工作目录 `.codebuddy/` 另有 `rules/`、`CODEBUDDY.md`、`AGENTS.md`、`agents/`、`skills/`、`commands/`（官方限定「进行代码开发时」生效），优先级项目级 > 用户级 `~/.codebuddy/`。
- `[实测]` 本机 `~/.codebuddy/` 的构成与当前工作目录有无 `.codebuddy/` —— **具体状况见机器文件**（各机不同）。
- **决定（2026-09-19，用户）**：本治理体系走**用户级**路线，**不启用项目级注入**；`machine/` 仍是嵌入层的入口登记处。规则载体改走用户级规则插件（见下节 Rule 行）。

**通道三 · 规则插件 `alwaysApply`（官方提供，本机未启用、未核实）**

- `[官方]` 规则插件以 `*.mdc` ＋ frontmatter 随插件分发，`alwaysApply: true` 时**全文常驻**；`[实测]` 官方市场已有纯规则插件先例，但**本机尚未安装任何规则插件** → 该通道**未启用**，桌面版是否加载并注入其 `rules/` 也**未核实**（详表见「官方机制 → 治理接口」Rule 行）。
- **若启用须注意**：`alwaysApply` 是**全文常驻**，与 [../../AGENT-CONTEXT.md](../../AGENT-CONTEXT.md) §3 的上下文预算冲突 → 只宜承载薄门禁，不搬全文。

- **前置条件与调用方式**：通道一无需调用、每会话自动执行；通道二本体系不采用；通道三未启用。
- **验证方法与最近结果**：每会话开头检查 `<identity_context>` 块实际列出的文件与全文范围。
- **回退**：注入通道不含的治理文件一律走**强制首读**（启动或进入相关工作前主动读原文），读取层级见 [../../AGENT-CONTEXT.md](../../AGENT-CONTEXT.md) §2。等效常驻入口＝`SOUL.md` 的「启动索引」小节（只作指针与义务声明，不承载规则）——**它存在的唯一原因是通道一不含 `OPERATIONS.md`**；若后续以用户级规则插件承载门禁，该节应同步收窄。

## 启动必读清单（本程序）

只登记本程序实际会读的治理文件与所属层级；**读取规则的唯一权威是 [../../AGENT-CONTEXT.md](../../AGENT-CONTEXT.md) §2**，本节不复述、不另立。清单**非穷举**，成员以根 [../../README.md](../../README.md) 名单与实际文件为准。

| 层级 | 文件 | 本程序下的实际情形 |
|---|---|---|
| 常驻（平台注入） | `SOUL.md`、`IDENTITY.md`、`USER.md`（经 `<identity_context>`）；`MEMORY.md`（经 `<user_memory>`） | 自动注入，无需主动读；其余 `importance: 1` 文件（含 `OPERATIONS.md`）的规则核**未被注入**。**本表只登记治理文件**——非治理的常驻内容见「Agent 提示词注入适配器」通道一 |
| 按动作触发（强制首读） | `OPERATIONS.md`、`FREEDOM.md`、`IMPORTANCE.md` | 平台不注入 → **在需要它们的动作前**必须主动读原文：改任何内容前读 `OPERATIONS.md`；写或改规则 / 约束 / 判据 / 流程前读 `FREEDOM.md`；评估重要性、或做压缩 / 拆分 / 迁移前读 `IMPORTANCE.md` |
| 强制首读（触发后） | `AGENT-CONTEXT.md`、根 `MACHINE.md` 及 `machine/` 下当前机器文件 | 处理加载 / 注入 / 上下文，**或用到本机工具时先读——含委派子代理（`Agent` 工具）** |
| 按需（触发） | `machine/workbuddy/`「子代理成本与模型选择」节 | **要选 `model` 档 / 估积分 / 并行铺开时**才读；本目录其余部分按上一行的触发读 |
| 按需 | `GIT.md`、`README.md` | 按任务类型与各自登记的触发机制取用 |
| 触发 | 治理型 skill（`skills/` 下）、非当前机器的 `machine/` 下文件 | 触发条件满足时加载；非当前机器文件不读 |

## 本程序记忆机制（事实）

本程序自带三层记忆，路径与来源如下；**落点裁决不在这里**，见 [../../OPERATIONS.md](../../OPERATIONS.md)「记忆维护」。

| 层 | 落点 | 来源与写入方式 |
|---|---|---|
| 云端画像 | 服务端生成，注入为 `<memory>` 块（本地只读缓存 `~/.workbuddy/memory/`） | 服务端自历史会话隐式学习；本地不可写，本地写入会被覆盖 |
| 用户级（跨项目） | 治理根下的 `MEMORY.md`（**具体路径见机器文件**） | 本地文件，显式写入；平台把它当"用户级长期记忆"注入 |
| 工作区（项目） | 随当前工作区变（**本机当前值见本机那份机器文件**） | 每日日志 `YYYY-MM-DD.md`（只追加）＋ `MEMORY.md`（项目长期） |

**与治理根的关系（2026-09-19 决定）**：本程序原生落点就是用户级治理根。历史上治理根与桌面副本曾保持两份一致副本（桌面为版本库主稿，用户级为注入副本）；**2026-09-19 用户决定：只维护用户级，桌面那份冻结**——不再同步、不再作为修改落点，仅留作旧版本库历史。由此有两条必须记住的联动：

- 治理根 `MEMORY.md`（教训短记录暂存）经 `<user_memory>` 被**注入本程序每个会话**，实际处于常驻层——其长度与措辞须按 [../../AGENT-CONTEXT.md](../../AGENT-CONTEXT.md) §3 的上下文预算原则控制。**平台把该文件标为「Limit: 4,000 chars/session」，而文件实际体积**远**已超出该限额（具体值见机器文件）→ 截断是必然、不是偶发**（该限额属「每会话写入上限」还是「注入上限」，本机未实测区分）。推论：**细节不能靠 MEMORY 落地**，它只适合承载规则核心与索引。
- 平台注入的运行提醒与治理规则**分工**：提醒驱动的是程序原生落点；**跨项目与治理内容一律写治理根**。冲突时以治理文件为准。

## 本程序特定要求

- **治理根**：本程序读取与注入的治理文件都在治理根，**是唯一的维护对象**（2026-09-19 起）；桌面旧版本库主稿已冻结。**各机的治理根路径与目录构成见机器文件。**
- **skill 自定义字段**：放 `metadata` 下，平台差异见 [../../MACHINE.md](../../MACHINE.md)「平台差异速查」。
- **改 `SOUL.md` / `IDENTITY.md` / `USER.md` / `MEMORY.md` = 改每次注入**：前三份经 `<identity_context>`、`MEMORY.md` 经 `<user_memory>` 注入本程序每个会话（其余治理文件不注入；**但「注入」不止治理文件这一路**——skill 的 `description`、工具定义、平台自带的运行提醒块同样常驻，改它们同样改每次注入，另两条通道见上），改动直接改变常驻上下文，属高影响——按 [../../OPERATIONS.md](../../OPERATIONS.md)「治理文件修改流程」执行并做层级审计。
- **这三份身份文件平台自己也会写（启动时的字段迁移）**：平台内有两张表——字段迁移表 `FIELD_MIGRATIONS`（补字段）与整行替换表 `LINE_REPLACEMENTS`（换提示行），启动时由 `migrateIdentityTemplate(workbuddyDir, state.identityTemplateVersion)` 调用、`applyFieldAdditions` 执行：给 `USER.md` 补它缺的标准字段并插到指定位置（`- **Occupation:**` 插在 `- **Pronouns:**` **之前**），把 `IDENTITY.md` 的一句旧提示语整行换掉；写回走 `writeFileAtomic`（临时文件 ＋ rename）。`[实测]`（2026-09-21 / 09-23 扫 `app.asar`；2026-09-23 工作区 `USER.md` 实增该行，位置与 `beforeFields: ["pronouns"]` 吻合）⇒ `USER.md` / `IDENTITY.md` 里出现**你没写过的一行**属平台规范化写入，不是手滑、也不是「谁改了我的档案」。**边界**：只补缺失字段、只换**逐字命中**的提示行——`buildFieldMatcher([field, ...aliases])` 命中即跳过（别名也算已存在），已填字段值 / 自加字段 / `Notes` 多行 / `## Context` 段 / frontmatter 一概保留。**只跑一次**：`fromVersion >= 2` 即跳过，失败则不标记、下次启动重试 ⇒ **这行删掉后不会被自动补回**（`[推断]`：据代码分支与已置版本的语义，state 文件本身未验证；被重置则可能重跑）。`refreshBootstrapTemplate` 是同批第三种动作——仅 onboarding 未完成者，**整文覆盖** `BOOTSTRAP.md`。
- **记忆写入落点（本程序）**：项目局部日志 → **当前工作区**的 `.workbuddy\memory\YYYY-MM-DD.md`；跨项目与治理内容 → 治理根 `memory/` 与 `MEMORY.md`（**直接写这里**，不再经桌面副本）。分工权威见 [../../OPERATIONS.md](../../OPERATIONS.md)「记忆维护」的**落点裁决**。**本机的具体路径与治理根构成见本机那份机器文件。**
- **治理体系 Git 仓库位置**：治理根是否已是 git 仓库、remote 与分支，**属机器事实，见机器文件**（本机与另一台的状况不同）。
- **Git 凭据**：本机凭据管理器已能对 GitHub 远程仓库完成只读与推送认证 → Git 操作优先复用该凭据，不提取、不记录令牌内容；无 GitHub CLI 时仍可完成本地初始化与提交。**装在哪、配置链如何解析 → 见根 `machine/_host/<机器>.md` 的「Git 凭据」节，本节不写路径。**
- **automation**：用 `automation_update` 工具管理定时 / 重复任务。
- **运行时坑**：见下文「运行时坑」；本机专属项见机器文件。
- **交付**：成品文件用 `present_files` 呈现（HTML 会同时开预览面板）。
- **放置内容前先算注入成本（软件对自身的影响）**：判断依据是「**这段内容在需要它的那一刻，是否已经在上下文里**」，而不是「写在哪个文件」。
  - 已核实的**治理文件**注入＝`SOUL.md` / `IDENTITY.md` / `USER.md` 全文 ＋ `MEMORY.md`（有限额）；其余治理文件走强制首读或按需读。**但这不等于「注入只有这几个入口」**（2026-09-20 用户校正）。
  - **非治理内容同样常驻**：skill 的 `description`（常驻只有 name＋description）、工具定义、平台自带的运行提醒块——改这些**同样改每次注入**。
  - **注入通道不止一条**：项目级注入与规则插件的 `alwaysApply` 是另外两条，见「Agent 提示词注入适配器」与「官方机制 → 治理接口」的 Rule 行，**当前未启用或未核实**。
  - 故新增内容先问：**它是「必须常驻的规则核心」，还是「可按需读的细节」？**后者一律进按需文件，并**在已被强制首读的文件里留一行触发器**，否则等于没落地（依据 [../../AGENT-CONTEXT.md](../../AGENT-CONTEXT.md) §1/§3、[../../IMPORTANCE.md](../../IMPORTANCE.md) §4/§5）。
  - **本程序注入提醒中的治理内容（软件事实）**：本程序把「**工作区记忆的写入与维护规则**」作为会话开头的注入提醒（工作记忆／技能块）送到每次会话——① 实质工作完成后向工作区 `memory/YYYY-MM-DD.md` 追加（当日文件不存在先建）；② 长期事实写进工作区 `memory/MEMORY.md`；③ 日志满 30 天蒸馏进 `MEMORY.md` 再删旧文件。因此 [../../OPERATIONS.md](../../OPERATIONS.md)「记忆维护」**没有复述**它们。**登记规范见 [../../MACHINE.md](../../MACHINE.md)「因平台注入而略去的治理内容」**；本节只记"本程序注入了哪条"。⇢ 目标平台不注入等价规则时，把上述三条补写进 `OPERATIONS.md`「记忆维护」。

## 官方机制 → 治理接口

登记本平台官方机制与治理规则的挂接关系；字段定义（含**依据等级**）见 [../../MACHINE.md](../../MACHINE.md)「官方机制 → 治理接口（登记格式）」。**本平台没有的机制写「不适用」，不留空。**

官方口径（[官方] https://www.workbuddy.cn/docs/workbuddy/Plugins ）：WorkBuddy 把扩展机制统称**插件**，分五类——Skill / MCP / Hook / Agent / Rule。下表按此五类逐项登记，再列非插件的自动化与分发渠道。依据等级：`[官方]`＝官方文档（附 URL）；`[实测]`＝本机直接观测（文件、日志、记账文件）；`[推断]`＝由前两者推出、未经直接验证。**没有官方依据的落点不得写成官方规范。**

> **具体落点与实例清单属机器事实**——每格的 `[实测]` 值（路径、计数、装了哪些）见 `machine/_host/<机器标识名>/workbuddy.md`。本表只登记**机制与其能力边界**。

| 官方机制 | 官方定义文件 / 落点 | 触发入口 | 能力边界 | 能承接的治理规则 |
|---|---|---|---|---|
| Skill（技能插件） | `[官方]` 规范 https://open.workbuddy.cn/docs/skill —— `{skill-name}/SKILL.md` ＋ `references/`、`scripts/`、`templates/`；frontmatter 必填 description / description_zh / description_en / version / author，可选 name / allowed-tools / disable-model-invocation / user-invocable。`[实测]` 本机落点＝治理根 `skills/<name>/SKILL.md`（**目录数会变、不在此写死**——以根 `README.md` 名单和实际清点为准） | `[官方]` 用户消息文本匹配 `description` 自动调用，或对话中召唤；`disable-model-invocation: true` 仅手动触发，`user-invocable: false` 仅供模型内部调用 | `[官方]` 常驻只有 name＋description，正文按需载入；启用/关闭记在用户全局配置、**不改动技能原文件**，关闭≠卸载；**无「文件类型自动触发」** | 有触发条件的治理流程 → 治理型 skill（skill-creator、reflection-evolution、system-refactor）；其 `description` 未覆盖的触发场景＝该规则在本平台不存在 |
| MCP（MCP 插件；连接器＝「MCP＋Skill」或「CLI＋Skill」的打包分发，一个连接器只能选一种方案） | `[官方]` 连接器规范 https://open.workbuddy.cn/docs/connector —— `connector-meta.json`＋`mcp.json`＋`icon.svg`＋可选 `skills/`；CLI 方案改用 `cli.json`；管理页 https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Connector 。`[实测]` 本机 `mcp.json` 的 Server 清单、连接器实例目录、`connectors\skills\` 是否为空、市场元数据与信任记录 —— **具体值见机器文件** | `[官方]` 客户端左侧「连接器」→ 点 ＋ → 扫码或授权 → 平台自动挂载工具；自定义连接器按 MCP 配置 | `[官方]` 一个连接器只配一个 MCP Server；远程须 HTTPS（SSE／streamableHttp）；单次请求建议 30 秒内；**每个连接器独立授权、不主动定时抓取、不超出已有权限范围** | 外部数据来源按 `cite-sources` 标来源等级；可用性核查按 [../../OPERATIONS.md](../../OPERATIONS.md)「核查、覆盖度与可用项」穷举 |
| Hook（钩子插件） | `[官方]` 插件系统页「在特定时机自动执行操作」（同上 URL）。`[实测]` 本机是否装有 hook 实例、市场目录下有无 `local` 市场 —— **见机器文件**。市场包内确有若干 `hooks.json` 原型（`chainguard` 的 PreToolUse、`hookify` 的 PreToolUse/PostToolUse/Stop、`ralph-loop` 的 Stop、`plugin-finder` 的 UserPromptSubmit、`sheetagent` 的 SubagentStop、`tencent-docx` 的 SessionStart、`financial-analysis` 的 SessionStart），**但它们都在市场包内，是否随安装生效未核实** | `[官方]` 插件被加载后由工具调用事件触发。与 skill frontmatter 的 `hooks`（须 `context: fork`）是**两套机制**，勿混 | **若本机无任何 hook 实例** → Hook 在该机**不可作为任何治理规则的执行入口**，该机制等于**未配置**（各机状态见机器文件） | 设计意图＝承接「安装 / 下载审计」（OPERATIONS 第 6 节）与危险命令拦截；**无实例时实际仍靠模型自律**，见本节末尾缺口 |
| Agent（智能体插件；专家 / 专家团） | `[官方]` 专家规范 https://open.workbuddy.cn/docs/expert —— `my-expert/{.codebuddy-plugin/plugin.json, avatars/, agents/<name>.md, README.md}`，`plugin.json` 的 `expertType` 为 `agent` 或 `team`。`[实测]` 本机有无 `~/.workbuddy\experts` 目录、专家清单来自哪些市场包 —— **见机器文件** | `[官方]` 左侧「专家·技能·连接器」→ 专家市场 → 召唤（角色切换）；专家团由团长拆解、并行执行、整合交付。`[实测]` **不经 Agent 工具委派**（曾探针 `Task agent <name> is not available`） | `[官方]` 专家本身不主动获取系统权限，仅处理你主动提供的对话与上传文件；配备 Skill／MCP 时才在授权下间接访问；创建后名称不可改；专家团消耗为单专家数倍 | 领域任务的可选载体，**不构成依赖**——规则不能以「委派给某专家」为执行入口 |
| Rule（规则插件） | `[官方]` 插件系统页列为五类之一（作用＝「定义 WorkBuddy 的行为规范」）；规则文件规范 https://www.workbuddy.cn/docs/ide/User-guide/Rules 。规则以 `*.mdc` ＋ frontmatter（`description` / `globs`（官方 CLI 文档作 `paths`）/ `alwaysApply` / `enabled`）随插件分发。`[实测]` 官方市场已有**纯规则插件**先例 `codebuddy-plugins-official/plugins/security-rules/`；另有 20 余个市场插件包内含 `rules/`；**`rules/` 按约定自动发现，不在 `plugin.json` 里声明**（对照：`skills` / `commands` / `hooks` 需声明）。生效前提是该插件**已安装**；本机是否已装规则插件 —— **见机器文件** | `[官方]` 三种应用类型：**总是**（alwaysApply，全文常驻）／**智能体请求**（按 description 判断）／**手动**（`@my-rule`）；`globs`／`paths` 命中文件时条件触发；改规则后须**新开会话**才生效 | `[官方]` 是**约束**而非工作流；项目级 > 用户级同名优先。**待实测**：WorkBuddy 桌面版是否加载 `rules/` 并注入上下文。`[实测·平台侧]`（2026-09-21 扫 `app.asar`）程序内**确有** `parseRuleFile` 代码路径，按 `enabled` / `paths`→`globs` / `alwaysApply` 三元解析，并同时收集**用户级**与**项目级** `rules` 目录——**代码路径存在 ≠ 实际注入上下文**，注入与否仍未验证 | **拟作「通道三」**：把无条件门禁做成薄规则插件、走用户级插件系统（安装／启用／卸载由平台管理，取代「借 SOUL 通道」）；**不搬运 OPERATIONS 全文**——`alwaysApply` 是常驻，全文常驻与 `AGENT-CONTEXT.md` §3 的上下文预算冲突。可行性已具备，**未实施，待用户点头** |
| Automation（自动化；非插件） | `[官方]` https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Automation-Guide —— 配置项＝名称／提示词／工作空间／权限模式／模型与技能／定时规则／推送。`[实测]` 工具 `automation_update`；备份 `automation-backups\` | `[官方]` 到点由平台以当前登录身份自动发起 Agent 任务；`[实测]` 会话内亦可由 `automation_update` 直接建改 | `[官方]` **仅支持时间触发，不支持文件变更触发**；配置存**本地客户端、非云端**（换机不迁）；工作空间限定文件读写范围；受频率／最大时长／并发限制 | 周期性治理动作（lint 巡检、治理体检）的执行载体——**换机须在新机重建**，不得默认它随环境迁移 |
| 插件市场（分发渠道） | `[官方]` 插件系统页「添加插件市场」：插件页点 ＋ 输市场地址。`[实测]` 本机 `plugins\known_marketplaces.json` 的市场源清单、`installed_plugins.json` 的记账条数、`plugins\cache\<市场>\<插件>\<版本>` 落点 —— **见机器文件** | `[官方]` 插件管理页安装／卸载；内置源自动更新 | `[官方]` 安装即改变本地能力集；第三方市场与插件须自行审慎评估（官方只做安装前安全扫描） | 安装 / 下载一律走 [../../OPERATIONS.md](../../OPERATIONS.md) 第 6 节四步（含审计记录） |

**没有挂到任何入口的治理规则只是纸面规则**——这类缺口按 [../../OPERATIONS.md](../../OPERATIONS.md)「执行缝隙兜底」处理并记当日 Memory。当前已识别的缺口：OPERATIONS 第 6 节「安装 / 下载审计」——**在无 hook 实例的机器上完全没有执行入口**，全靠模型自律（见 Hook 行与机器文件）。

## 子代理委派（要点）

- **记得主动派**：本程序**没有模型侧自主委派**，`Agent` 工具只能由主 agent 显式调用，不会自动发生——复杂问题（多面、要并行取证、要独立复核）要自己想起来用；行为准则见 [../../SOUL.md](../../SOUL.md) 的 Core Truths，本节只记机制事实。
- **派什么类型、怎么交代**：`subagent_type` 的能力边界**以 `Agent` 工具定义为准**（各类型能碰什么写在那里）；平台自己已规定的要求（只读类型不派实现活、并行子任务写同一消息、子代理的汇报只算「它打算做什么」）也不复述。**唯一须自己记住**：子代理读不到任何治理文件、也看不到本对话——凡要它遵守的只能随 prompt 走（怎么写见下节末条）。
- **成本与模型选择** → 见下节「子代理成本与模型选择」（**未定稿**）。
- **不要再建 `subagent` skill**：同名 skill 曾因通篇描述 CodeBuddy Code CLI（落点、`/agents` 命令、模型别名、frontmatter 格式均与本程序不符）被删（2026-09-20）。**专家 ≠ 子代理**：专家是角色注入，不经 `Agent` 工具委派（机制见「官方机制 → 治理接口」Agent 行）。

## 子代理成本与模型选择（未定稿）

> **独立触发**：要选 `model` 档、估一次委派的积分、或准备并行铺开时读本节。**整节未设计完**——选型线是推断、消耗账没做实测，**勿当结论用**。

- **`Agent` 的 `model` 参数（2026-09-20 实测）**：能调不同模型；**名字无法识别则静默回落默认、不报错**（拼错＝没换，且不提示）。解析值未必等于显示名：`Kimi-K2.7-Code` → `kimi-k2.7`（后缀被丢）、`Kimi-K3` → `kimi-k3-1`、`Hy4 preview` → `hy4-preview`。**验证**：回问子代理实际运行的模型（它能自述），别凭传参假定已切换。
- **倍率以模型选择器为准**（会变，不抄成表）。2026-09-20 取值：0.00x＝`Hy4 preview` / `Hy3`（限时免费）；0.03x＝默认 `Deepseek-V4.1-Flash`；0.06x `GLM-5.3-Flash`；0.25x `MiniMax-M3`；0.52x `Kimi-K2.6`；0.57x `Kimi-K2.7-Code`；0.71x `GLM-5v-Turbo`；0.77x `Kimi-K2.8-Preview`；0.79x `GLM-5.3`；1.62x `Kimi-K3`。已下架或不存在的值（`GLM-4.7`、`sonnet`、随机名）实测静默回落默认。
- **一次委派的成本构成**：积分 ≈ 该模型倍率 × 子代理消耗的 token × 轮次；**并行 N 路＝整笔 ×N**；子代理的回传**整段进主上下文**、等于再计一次。护栏三条：① 并行分治一律用 0.00x 档；② 给 `max_turns` 设上界止损（**其行为未实测**）；③ prompt 里限定回传长度（只要结论与证据位置，不要原文）。
- **选型线（推断）**：批量机械活 / 并行每一路 → 0.00x 档；常规执行 → 不传 `model`；要独立判断或复核我的结论 → 0.7x 档；只能一次做对、或要它对撞我的结论 → `Kimi-K3`（1.62x，不用在能返工的活上）；**纯代码活 → `Kimi-K2.7-Code`；用户另有指定时依用户指定**（本用户 2026-09-28 明确：**不会写的代码交给 `GLM-5.3`（0.79x）的子 agent**）。**看图** `GLM-5v-Turbo` 与默认模型均实测能读准，读图不是 `5v` 独有。
- **交代任务：四项（控制组实测 2026-09-21）**：① 任务与产物落点——不给，它**自己挑路径**；② 边界（只读 / 可写、禁止做什么）——不设，就往那写；③ 回传格式＋长度上限——不给，自定格式并把源文件原文抄进产物；④ 可验证项（要求自述模型）——不问就不报。**这四项平台一条都不提供**，只能随 prompt 走。
- **模型名口径差异**：CodeBuddy Code 文档里的别名（`gpt-5.1-codex` / `gemini-3.0-flash` 等）与本程序不符，本机实际为国产模型；逐条详表见 `skills/workbuddy-manager/references/extensions-overview.md`（工具型 skill，未随公开仓上传）。
- **待办**：装 `workbuddy-token-usage` 才有按模型的真实消耗账，把选型从推断变成实测。

## Skill 触发机制（官方核查 2026-07-11）

**结论**：WorkBuddy/CodeBuddy 的 skill 触发信号是**用户输入文本匹配 `description`**，不是文件类型或上下文自动加载。

- 官方 `skill-dispatcher` 匹配逻辑三类信号：①关键词触发（用户消息出现特定词）②场景推断（对话历史）③手动指定（`@skill:`/`用XX技能`）。三类都以用户消息文本为前提。
- 开放标准 Progressive Disclosure 只规定"加载层级"（metadata 常驻、body 触发时载入、references 按需），不提供"文件自动触发"信号。
- 推论：用户上传/提及 PDF 却没说"提取"，pdf-text-extractor 浅匹配可能不触发；"填表→数据在PDF→用pdf skill"的跨步推理当前调度器不做。

**改进路径（按可行性）**：

- A. 改 skill 的 `description`，写明触发条件
- B. 在 SOUL.md / 项目约定写规则强制加载
- C. **历史兼容补充：Hooks `FileChanged`**（`watchPaths: ["*.pdf"]`）——部分平台版本提供此类事件入口；只有平台明确启用、非内置 skill 的信任设置和 `context: fork` 等条件满足，并经实测后才可使用，不能作为开放标准或跨平台的文件自动触发保证；插件级 hooks（`plugin.json` 声明 `hooks/hooks.json`）为另一套机制，见「官方机制 → 治理接口」Hook 行。**非内置 skill 另需 `allowUntrustedFrontmatterHooks: true`**——某个 skill 自身配没配、能否当自动链路，属机器事实，见机器文件
- D. Automation 定时扫文件夹（批量/周期，非实时）
- E. 手动 `@skill` / `/skills`

**跨平台对比**：所有采用 agentskills.io 开放标准的实现，SKILL.md 层面触发都是 description 语义匹配（LLM 推理，非关键词正则），**无一家原生支持"文件类型自动加载 skill"**——Claude Code（description 语义匹配；Hooks 可 hook 工具调用）、Codex CLI（`$skill-name` 显式 + description 隐式）、Gemini CLI（activate_skill + 用户确认）、GitHub Copilot（同开放标准）、Cursor（Skills 也是 description 匹配；但其 **Rules** 用 `globs` + `alwaysApply` 实现文件匹配自动加载——唯一明确的文件类型自动触发，属 Rules 而非 Skills）、Warp Oz（编排层支持 schedule/webhook/system event，非 skill 原生）、社区 workaround（Superpowers 在 CLAUDE.md 等写"任务前先检查 skills 目录"）。**但本平台自身的 Rule 机制支持 `paths` glob 条件触发**，可达成等效效果——差别在载体是 Rule（约束）而非 Skill（工作流）。

**自动反思/自我纠错机制（2026-07-11 查）**：没有专门的"auto-reflect"参数。用户纠正做法但未说"你错了"时自动反思，靠三种非参数机制兜底：① description 语义匹配（reflection skill 的 description 写"用户纠正/给出不同正确做法时触发"）；② system prompt / SOUL 规则；③ 平台特定 Hooks Stop 事件（Claude Code 有 Stop hook，CodeBuddy v2.97.0 有 Stop 类事件 + prompt 类型 hook）——只能作为历史兼容/补充路径。跨平台结论：Claude/Cursor/Codex/Gemini 均无"对话内自动反思"可配置参数；通用做法是 prompt 工程。

## 运行时坑（跨机器部分）

> 本机专属的坑（程序黑名单、PowerShell 不回显、Git Bash PATH 现状、safe-delete 机制与实测）见根 `machine/_host/<机器>.md` 的「运行时坑」节。

- **批量脚本必须限定文件清单，绝不 walk 整个治理根**：治理根同时是客户端数据目录，`workspace/sessions/<会话ID>/modify_backup/` 等路径**受权限规则保护**（写入会被拦并拒绝），且其中的副本本来也不该被改。遍历整个 `~/.workbuddy` 会撞上它们（2026-09-28 实测被拦一次，脚本中断）。正确做法＝**显式列出要改的文件**（例如「根目录已登记的治理 md ＋ `machine/` ＋ `skills/`」）；确实要遍历时也必须用白名单剪枝（跳过 `.git`、`.trash`、`workspace`、`sessions`、`node_modules`、`__pycache__`）。
- **原生工具链路径**：Bash（Git Bash）调用 Windows 原生程序（python3.exe / node.exe / 7z.exe）传文件路径必须用 `C:/...` 或 `C:\...`，禁止 msys 风格 `/c/...`——会被错拼成 `c:\c\`。凡路径交给原生 exe，先换风格。
- **防「参数被当路径转换」**：Git Bash 调原生 exe 时，形如 `/s` 的**开关参数**可能被 MSYS2 当路径改写，参数语义丢失。规避＝`export MSYS2_ARG_CONV_EXCL='*'`（或只列需豁免的参数名）或 `MSYS_NO_PATHCONV=1`。遇到"参数明明写了却不生效"先试这条。
- **Bash 通道禁调 `cmd.exe`**：`cmd /c <...>` **整条被平台拒绝**，报 `Invoking cmd.exe from Bash bypasses all command validation` ⇒ `cmd /c start` 这类启动 / 最小化窗口的写法走不通，Git Bash 自带的 `start` 同样无效。需要窗口动作时改用平台工具，或走 PowerShell。
- **工具选择门控（2026-09-22 立，用户同意）——检索类任务不进 Bash**：即将在 Bash 里写 `grep`/`rg`/`find`/`cat`/`head`/`ls`、且目的是检索内容或列文件 → 停，改用 Grep / Glob / Read / Edit。Bash 的正当用途：跑脚本、跑命令、git 操作、真正需要管道组合的执行类操作。
- **同一文件不要在同一批工具调用里并发编辑**：对同一个文件在同一批中发起多个编辑时，后一次写入会覆盖前一次的改动——工具仍回报成功，但前一处改动丢失。改同一文件的多个位置须**串行**执行（一次调用只改一处），且每次写入后读回或 grep 确认落盘。
- **`.ps1` 脚本的三条限制**：① **内联 `Add-Type` 被拦**，把代码**写进 `.ps1` 再执行可放行**；② `.ps1` **不要内嵌中文字面量**（UTF-8 无 BOM 保存会被按 ANSI 解码成乱码）⇒ 中文路径一律**经 `param` 传参**；③ 执行策略默认禁脚本，调用前先 `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force`。
- **PowerShell `Get-ChildItem -Exclude` 会静默滤空结果**：`Get-ChildItem -File <dir> -Exclude *.pyc | ForEach-Object { Copy-Item ... }` 一个文件都没复制、且不报错，目标目录最终为空。批量复制改用「先取全部文件，再用 `Where-Object` 按扩展名过滤」，复制后必须逐文件确认目标存在。
- **WinRT 异步在 PowerShell 里死锁 ⇒ 平台内置 OCR 走不通**：PowerShell 调 `Windows.Media.Ocr` 一类 WinRT 异步 API，在 STA 下 `Task.Wait(-1)` 报"发生一个或多个错误"，改用 `-MTA` 起子进程又被沙箱拦 ⇒ **平台内置 OCR 这条通道不可用**（OCR 实际走 `rapidocr-onnxruntime`，装在托管 venv，见机器文件的解释器节）。
- **写文件工具会自动创建缺失的父目录**：向不存在的目录下的路径写文件时，工具**静默建目录**并回报成功。写临时文件前先确认目标目录是否本应存在——曾因此在治理根凭空生成一个 `.trash`，与 `文件夹目录.md` 登记的"当前未创建"冲突。临时文件写进已存在的删除落点，别新造路径。
- **Write 拒绝覆盖「本会话未 Read 过」的文件**：报 `File has not been read yet: <path>. Read it first before writing to it.` ——**覆盖自己刚写过的文件也会撞上**。规避＝改用 **Edit**（直接从磁盘读现内容再比对 `old_string`，**不要求先 Read**），或先删再写。
- **临时脚本不要用标准库模块名命名**：把侦察脚本命名为 `_tmp/inspect.py`，会使**同目录其它脚本** `import inspect` 命中它而非标准库，随后报错——脚本自身目录会被置于 `sys.path` 首位，同名文件必被命中。临时脚本统一用 `_probe_*.py` 这类不与标准库撞名的前缀。
- **bash 里命令失败不会终止脚本**：`cd` 失败后脚本**继续在原当前目录执行**——曾因此在一处错误的目录建出 `.git` 仓库（事后已清掉）。规避：① 建目录、删文件改用 PowerShell 与 `[System.IO.Directory]` / `[System.IO.File]`；② 脚本里换目录一律写 `cd X || exit 1`；③ 破坏性命令（`git init`、删除、写文件）执行前先校验落点，例如 `git rev-parse --show-toplevel` 或 `pwd`。
- **经 shell 传文本会被静默改写**：① PowerShell 双引号展开 `$`，且变量名大小写不敏感——用双引号拼接含 shell 变量的文本时，`$T` 被当真变量展开，**整个文件内容被嵌进那一行**（体积涨到 3 倍）；② bash 反引号被当命令替换——含反引号的文本嵌进 `python -c "..."` 的双引号串时，反引号包裹的片段被当命令执行、内容被吞掉。**规避**：写入含特殊字符的文本先落成脚本文件；写完核对体积与关键串，体积异常增幅就是信号。
- **Python 读写文本时行尾会被静默改写**：`open(p, encoding="utf-8")` 默认是**通用换行模式**——读进来时 `\r\n` 已被换成 `\n`；再以 `newline=""` 写回，落盘就是**纯 LF**，整个文件的行尾被换掉而正文看不出异常（曾把一份 CRLF 文件转成 LF，体积异常时才察觉）。**规避**：① 只改内容、要保行尾 → **全程二进制**（`open(p,"rb")` → decode → 处理 → encode → `open(p,"wb")`）；② 必须用文本模式时显式 `newline=""`；③ 每次改完立刻对账：`count(b"\r\n")` 应等于 `count(b"\n")`。
- **批量替换脚本的锚点会命中"先出现的那一处"**：给替换脚本打补丁、想改"新值"里的片段时，`str.replace` 却改到了文档中**排在前面**的"旧值"槽位——该条替换的目标串从此失配，后续连带失败。**规避**：① 每个替换先断言命中数，≠期望就整批不写；② 同一片段可能在多个槽位出现时，别用 `str.replace`，改按行号／索引定位。
- **脚本报"成功"不等于落盘正确**：写入类脚本必须读回核验——计数对账、grep 关键串、比对行尾，都是判据（验证出口见 [../../OPERATIONS.md](../../OPERATIONS.md)「核查、覆盖度与可用项」）。

## 深度细节索引

数据布局（`~/.workbuddy/projects/` 等）、跨对话通信、扩展机制八面全景：见 `skills/workbuddy-manager/references/`——工具型 skill，归另一个私有仓，按需取文件。**注意数据布局细节可能与本机实测不符**，以机器文件登记的实测构成与根 [../../MACHINE.md](../../MACHINE.md) 的解析规则为准。
