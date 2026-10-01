---
title: "README.md - 治理体系门面与名单"
summary: "治理体系的对外门面与内部名单——门面段：这是什么、设计要点、仓库结构、怎么用到自己身上；名单段：体系目的、成员判据、根治理文件与治理型 skill 名单。了解这套体系或判断某个文件是不是治理文件时看这里；新建 / 删除成员时同步更新。"
importance: 3
platform: common
created_at: 2026-08-23
read_when:
  - 第一次接触这套治理体系、想知道它是什么时
  - 判断某文件是否治理文件、该按哪套规则管时
---

# README.md - 治理体系门面与名单

> 本文件是这个治理体系的**对外门面**，也是**内部名单的唯一权威**：门面段说明它是什么、为什么这么设计；名单段登记目的、判据与成员。它仍然只登记、不定义——规则在各文件自身。

## 这是什么

一套写给 AI 的治理体系：用一组 Markdown 文件，把 AI 的行为约束、操作门禁、记忆维护、版本控制边界固定下来，让每次会话的 AI 都按同一套规则办事，而不是每次都靠临场判断。

单次会话的 AI 不缺能力，缺的是**跨会话的稳定约束**——同一件事今天这么做、明天那样做，而没有任何地方记得"应该怎么做"；也没有地方记得"上次为什么做错"。这套文件解决的就是这两件事：把判断沉淀成规则与教训，让它们下次还能用上。

## 体系总览（第一次接触先看这里）

- **为什么存在**：单次会话的 AI 不缺能力，缺的是**跨会话的稳定约束**——同一件事的做法无处沉淀、上次的教训无处记取。这套文件把判断固化成规则与教训，让它们下次仍能生效（体系目的详见下节）。
- **分三层，按加载成本放置**：① **常驻注入层**——平台每个会话自动注入的少数核心（如 `SOUL.md`），只放必须每次生效的；② **强制首读层**——启动或进入相关工作前必读的权威文件；③ **按需层**——由任务类型与实际决策需要引入的文件与 skill。层级细则见 `AGENT-CONTEXT.md` §2。
- **有哪些成员**：根治理文件（名单见下文「治理文件名单」）＋ 治理型 skill 三个（`skill-creator`／`reflection-evolution`／`system-refactor`，见下文名单）。
- **拿到一个新任务怎么读**：先靠常驻层兜底（入口是 `SOUL.md` 的「启动索引」）→ 按动作触发读 `OPERATIONS.md`（创建/修改/删除前）、`FREEDOM.md`（写规则前）、`IMPORTANCE.md`（压缩/拆分/迁移前）→ 需要外部能力时再加载对应 skill；各文件的触发条件写在自身 frontmatter 的 `read_when`。

## 治理体系目的

整个治理体系的目的是更好地管理 AI 的各个“手脚”，包括 MCP、Markdown 等文件与能力接口，并提升 AI 的思考能力。

## 设计要点（为什么这么做）

- **规则与内容都带目的与原因**：写约束时写明它要防的是什么 → `FREEDOM.md`
- **分层，按加载成本放置**：常驻注入层只放必须每次生效的，其余走强制首读或按需读 → `AGENT-CONTEXT.md` §2
- **删的代价不对称，宁加不删**：压缩、拆分或迁移前先做内容影响测试 → `IMPORTANCE.md`
- **规则先行**：先立规则再改文件；改治理文件的动作本身也守该文件的规则 → `OPERATIONS.md`
- **每个「必须」都要有执行载体**：能落到脚本 / checklist / skill 的就落到机制上，不把"应该有人检查"当成已生效 → `OPERATIONS.md`
- **默认私有，对外走派生仓**：工作仓要个人档案的**版本历史与备份**，对外展示又不能带私密内容——两个目的合不到一个仓里，故拆成「私有工作仓 ＋ 派生公开快照仓」；派生仓剥掉那三份个人文件与 `machine/_host/`，推送前先过私密性审核 → `GIT.md`

## 仓库结构

```text
.
├── README.md              本文件：对外门面 + 名单
├── SOUL.md                人格原则
├── OPERATIONS.md          操作规范：创建/修改/删除、门禁、规则先行
├── GIT.md                 版本控制规范与仓库边界
├── FREEDOM.md             规则力度与写作检查
├── IMPORTANCE.md          重要性分级（PSU + CRR）
├── MACHINE.md             机器事实的登记规范与读取入口（具体机器值在 machine/ 下）
├── AGENT-CONTEXT.md       上下文稳定原则
├── FUTURE.md              对未来版本的预言
├── 文件夹目录.md           本工程工作文件夹的目录记录
├── USER.md                用户档案（私有内容：私有仓保留，公开仓不含）
├── MEMORY.md              教训暂存（同上）
├── IDENTITY.md            AI 身份事实（同上）
├── examples/              上述三份的样例模板（公开仓以这些代替真值）
├── machine/               机器事实（_host/<机器标识名>/ 每机一夹 ＋ <软件>/common.md；索引见 machine/README.md）
├── skills/                全部 skill 都放这里，由两个仓按白名单分开跟踪：治理型 3 个（下文名单）随本仓；其余归嵌套的独立私有仓（remote `wwwq721/skill`，见 `GIT.md` §1）
└── scripts/
    └── governance_lint.py 机械巡检：frontmatter、断链、锚点、名单一致性
```

`USER.md`、`MEMORY.md`、`IDENTITY.md` 是**私有内容**：它们被平台按固定路径注入每个会话，私有仓保留它们以获得版本历史与备份；从工作仓派生的公开仓不含这三份，改以 `examples/` 下的样例模板代替（边界见 GIT.md §1）。

## 怎么用到自己身上

1. 把这套文件放到你所用程序的治理根（本机为 `%USERPROFILE%\.workbuddy\`）。
2. 自建三份个人文件 `USER.md`、`MEMORY.md`、`IDENTITY.md`：把 `examples/` 下的 `.example.md` 复制过去再填真值。**公开仓不含这三份**——你若是在公开克隆里用，别把填好的真值提交进去；私有仓则可以随仓保存。
3. 按 MACHINE.md 的做法重采本机机器事实——换环境后旧值一律不沿用。
4. 装上 `skills/` 下的治理型 skill。
5. 跑一次 `python scripts/governance_lint.py` 做机械巡检。
6. 按 GIT.md 把仓库管起来；要公开就按 GIT.md §2「推送前私密性审核」先审一遍。

## 判据

约束 AI 行为或体系运作的内容（规范、流程、元规则、事实档案）为治理文件；其余 skill 归「**其他**」——外挂式领域工具与约束产出类规范，不承载体系运作职能，只走 skill-creator 流程。

## 治理文件名单（根目录）

各文件的定位在其开头 frontmatter 的 summary，此处不重复，仅列名单（标「公开仓不含」的三份属私有内容，公开仓以 `examples/` 的样例代替）：

- SOUL.md
- OPERATIONS.md
- GIT.md
- FREEDOM.md
- IMPORTANCE.md
- MEMORY.md（公开仓不含：个人教训暂存，示例见 examples/MEMORY.example.md）
- IDENTITY.md（公开仓不含：AI 身份事实，示例见 examples/IDENTITY.example.md）
- USER.md（公开仓不含：用户档案，示例见 examples/USER.example.md）
- MACHINE.md
- AGENT-CONTEXT.md
- FUTURE.md
- README.md（本名单）

> machine/ 下的机器事实文件**及其索引**（含 `machine/README.md`）由 MACHINE.md 管理，**一律**不列入本治理文件名单。

## 治理型 skill 名单

定位见各自 SKILL.md 的 description，此处不重复，仅列名单：

- skill-creator
- reflection-evolution
- system-refactor

（requested_by: 用户, source: 整合操作 2026-08-23）
