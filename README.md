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

## 治理体系目的

整个治理体系的目的是更好地管理 AI 的各个“手脚”，包括 MCP、Markdown 等文件与能力接口，并提升 AI 的思考能力。

## 设计要点（为什么这么做）

- **规则与内容都带目的与原因**：写约束时写出它要防的是什么；将来要改这条，靠的就是这个原因，而不是重新猜一遍。
- **分层，按加载成本放置**：常驻注入层（被平台注入每个会话的那几份）只放必须每次生效的，其余走强制首读或按需读——常驻层多一行，每个会话都要付。
- **删的代价不对称，宁加不删**：被删的定义性内容往往只在出事时才被想起；压缩前先做内容影响测试。
- **规则先行**：先立规则、再改文件；改治理文件的动作本身也要守该文件的规则。
- **每个「必须」都要有执行载体**：能被脚本、checklist 或 skill 检查的，就落到机制上，不把"应该有人检查"当成已生效。
- **默认私有，对外走派生仓**：工作仓默认私有，个人档案随仓保存（才有版本历史与备份）；对外展示用从工作仓派生的公开仓——它剥掉那三份个人文件、只按用户指令更新，推送前先过私密性审核。

## 仓库结构

```text
.
├── README.md              本文件：对外门面 + 名单
├── SOUL.md                人格原则
├── OPERATIONS.md          操作规范：创建/修改/删除、门禁、规则先行
├── GIT.md                 版本控制规范与仓库边界
├── FREEDOM.md             规则力度与写作检查
├── IMPORTANCE.md          重要性分级（PSU + CRR）
├── MACHINE.md             机器、平台与软件事实的总入口
├── AGENT-CONTEXT.md       上下文稳定原则
├── FILE-AUDIT-RECORDS.md  文件读取审计规范
├── FUTURE.md              尚未成型的治理概念
├── 文件夹目录.md           本工程工作文件夹的目录记录
├── USER.md                用户档案（私有内容：私有仓保留，公开仓不含）
├── MEMORY.md              教训暂存（同上）
├── IDENTITY.md            AI 身份事实（同上）
├── examples/              上述三份的样例模板（公开仓以这些代替真值）
├── machine/               各平台与软件的机器事实
├── skills/                治理型 skill（工具型 skill 归另一个私有仓）
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

约束 AI 行为或体系运作的内容（规范、流程、元规则、事实档案）为治理文件；提供外部任务能力的是工具型 skill，不承载治理职能，只走 skill-creator 流程。

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
- FILE-AUDIT-RECORDS.md
- FUTURE.md
- README.md（本名单）

> machine/ 下的软件环境文件由 MACHINE.md 管理，不列入本治理文件名单。

## 治理型 skill 名单

定位见各自 SKILL.md 的 description，此处不重复，仅列名单：

- skill-creator
- reflection-evolution
- system-refactor

（requested_by: 用户, source: 整合操作 2026-08-23）
