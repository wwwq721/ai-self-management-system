---
name: skill-creator
description: 创建、修改和打包 Agent Skills：理解用例、规划资源、初始化、编写、验证和发布。当用户要新建或修改 skill，或对任一 skill 做实质性正文、结构或资源编辑时使用。
license: Complete terms in LICENSE.txt
metadata:
  importance: 3
  platform: common
  created_at: 2026-07-04
  source: marketplace
---

# Skill Creator

## Referenced Files

- [文件夹目录.md](文件夹目录.md)：记录本 Skill 工作文件夹的标准目录结构；创建、修改或删除目录、文件、脚本或资源前读取，结构变更后同步维护。
- [references/skill-format.md](references/skill-format.md)：编辑 frontmatter、目录结构、资源或文件引用时读取。
- [references/progressive-disclosure.md](references/progressive-disclosure.md)：拆分、压缩或设计按需加载时读取。
- [references/migration.md](references/migration.md)：从已有多个 skill 提取、合并或迁移时读取。
- [references/workflows.md](references/workflows.md)：需要多步流程或条件分支时读取。
- [references/output-patterns.md](references/output-patterns.md)：需要固定输出格式、模板或示例时读取。
- [scripts/init_skill.py](scripts/init_skill.py)：新建 skill 时运行。
- [scripts/quick_validate.py](scripts/quick_validate.py)：交付或打包前验证 skill 目录。
- [scripts/package_skill.py](scripts/package_skill.py)：需要生成可分发 `.skill` 包时运行。打包默认全收目录内所有文件；skill 根下可放 `.packageignore`（gitignore 风格 glob）排除凭据与私人信息，另有 `.git` / `__pycache__` / `.packageignore` 恒定排除，被跳过的文件会打印出来。
- [LICENSE.txt](LICENSE.txt)：需要确认许可证条款时读取。
- [../../OPERATIONS.md](../../OPERATIONS.md)：任何创建、修改或删除前读取，遵守操作门禁、范围和记录要求。
- [../../FREEDOM.md](../../FREEDOM.md)：决定规则具体程度、压缩方式或是否写死步骤时读取。
- [../../IMPORTANCE.md](../../IMPORTANCE.md)：压缩、拆分或迁移内容时读取内容保留判断。
- [../../MACHINE.md](../../MACHINE.md)：目标平台、字段、工具或本机路径事实影响任务时读取。

## Table of Contents

- [About Skills](#about-skills)
- [Core Principles](#core-principles)
- [Preflight](#preflight必走步骤不是参考目录)
- [Workflow](#workflow)
- [1. Understand](#1-understand)
- [2. Plan](#2-plan)
- [3. Initialize](#3-initialize)
- [4. Edit](#4-edit)
- [5. Validate](#5-validate)
- [6. Package](#6-package)
- [7. Iterate](#7-iterate)

## About Skills

Skill 是模块化、自包含的能力包，用专门知识、工作流、工具集成、领域规则或随附资源扩展 Agent。它把重复或不易凭通用能力稳定完成的工作变成可复用的 Agent 指引。

每个 Skill 至少包含根目录的 `SKILL.md`；可按实际需要包含 `scripts/`、`references/` 和 `assets/`。`SKILL.md` 的正文是给 Agent 的工作指引，不是教用户操作的手册。完整格式和目录说明见 [references/skill-format.md](references/skill-format.md)。

## Core Principles

- **假定 Agent 已具备通用能力**：只加入会改变判断、提高执行质量或保护真实不变量的内容。
- **保留用户意图、范围和授权**：Skill 支持任务，不替用户扩大产品、范围、权限或外部动作；失败重试和外部变更要有与风险相称的停止条件。
- **分开判断重要性与自由度**：重要性决定注意力、核查和验证深度；自由度决定规则是否写死、允许多少判断。高重要不自动意味着低自由，只有错误代价高且步骤机械固定时才收紧。
- **渐进披露**：入口保留共同目的、必要约束和路由条件；条件性细节、长例子、格式和实现说明放入按需 reference，且只在当前任务需要时读取。
- **压缩保留语义**：删除或迁移前，检查是否会改变定义、理解、决策、执行、适用边界或验证结果；会改变就保留语义，可改写或迁移，不得仅因篇幅长、非直接执行或低频而删除。

### Skill Writing Rules

以下规则保留原有 BP 编号，便于其他治理文件定位：

1. **BP #1，description**：写清 Skill 做什么、何时使用和可识别关键词；遵守官方 1~1024 字符限制，聚焦用户意图，只加入防止误路由所需的边界。
2. **BP #2，结构**：按任务复杂度选择结构；多模式、条件性或长细节使用 reference，不为形式增加章节。
3. **BP #3，单一权威**：已有 Skill、规则或安全/验证流程由其他文件负责时，引用它，不复制内容。
4. **BP #4，例子**：只有例子能消除实际歧义时才加入；保持短小，必要时声明非穷举，不让例子冒充范围或定义。
5. **BP #5，frontmatter**：按 [references/skill-format.md](references/skill-format.md) 与当前 [MACHINE.md](../../MACHINE.md) 核对目标平台；确认 `name` 与父目录完全一致、开放规范的 `metadata` 遵守字符串键值映射要求；不要凭记忆决定字段，也不要把平台事实硬编码进通用 Skill。
6. **BP #6，相似 Skill**：创建或修改前，检查当前平台可用的用户级和项目级 Skill 目录；有重叠时优先更新或合并既有能力，而不是制造重复入口。目录与发现方式按机器事实核实，不硬编码平台路径。
7. **BP #6a，同类路由**：同一功能类使用共同分类词，触发域保持不重叠；只有选择确实有歧义时才设置路由 Skill。
8. **BP #7，入口长度**：优先让 `SKILL.md` 保持精简；接近 500 行且拆分能改善上下文使用时，按 [references/progressive-disclosure.md](references/progressive-disclosure.md) 拆分。500 行是信号，不是为了达标而删除必要语义的硬目标。
9. **BP #8，reference 或独立 Skill**：只在父 Skill 触发后有用的内容放 `references/`；可独立触发、复用或作为决策入口的能力才建独立 Skill。按能力整合，不按来源文件分类。
10. **BP #9，导航**：入口先列出实际存在的引用文件及读取时机；正文超过约 100 行或结构超过 5 节时添加目录。
11. **BP #10，read_when**：它不是开放规范的顶层字段；只有目标平台支持时才放在平台规定的 metadata 位置。主要触发机制始终是 `description`。
12. **BP #11，官方依据**：写入或修改前核对当前官方 Agent Skills 规范；平台差异按 [MACHINE.md](../../MACHINE.md) 核实，不以本地已安装版本或旧稿作为权威。
13. **BP #12，Agent 受众**：保留 Agent 为了判断、执行、路由和验证所需的内容，不写要求用户输入命令、重启会话或执行其他操作的说明。
14. **BP #13，内容取舍**：逐句问它是否帮助 Agent 做判断、动作或验证；定义、边界、权威关系、路由条件和验证条件即使不直接执行动作，也可能是必需语义，须按影响测试保留。
15. **BP #14，自检**：每次修改后检查事实、无关内容、用户指令残留、内部矛盾、引用可达性和必要语义是否仍在。

## Preflight（必走步骤，不是参考目录）

下列为动手前的必走步骤；**未走完不得进入第 4 步 Edit**。

修改任一 Skill 前：

1. 完整读取目标 `SKILL.md`；读取 [OPERATIONS.md](../../OPERATIONS.md)；读取当前官方 [Agent Skills specification](https://agentskills.io/specification)。目标平台或环境事实会影响字段、工具或路径时，再读取 [MACHINE.md](../../MACHINE.md) 及对应软件事实文件。
   同时读取目标 Skill 工作文件夹根目录的 `文件夹目录.md`；尚无此文件时，先按本文件的格式创建并填写，再继续操作。
2. 搜索当前平台可用的相似 Skill，确认这是新建、更新、合并、拆分还是仅修正文案；检查将要移除的 reference、脚本或资源是否仍有调用者。**逐条回答一个必答项：拟加或拟改的职责，是否已有 skill 承担？** 有重合就走更新或合并，不新建重复入口（判据见 BP #6、#6a）；答案要写出来，不只在心里过一遍。
3. 明确用户要求的结果、范围和授权。缺少的信息只有在确实影响方案时才询问，不用默认结构替代用户意图。

## Workflow

按任务需要依次执行以下流程；已有 Skill 跳过初始化，使用场景已经清楚时可跳过重复的例子收集。

### 1. Understand

从真实请求、既有产物和失败案例中确定 Skill 的目标、输入、输出、触发条件和边界。用最少的具体例子验证这些判断；例子只是测试样本，不是穷举范围。

### 2. Plan

从用例推导可复用的 `scripts/`、`references/` 和 `assets/`。只有重复编写、技术细节、稳定模板或确定性执行确实受益时才添加资源；不要创建占位文件或“以后可能有用”的文档。

需要从已有 Skill 形成新 Skill 时，先读 [references/migration.md](references/migration.md)，再确定是合并既有能力、薄包装还是重写。

方案落定前自检一句：本次要加的能力，是否已有 skill 承担（对照 Preflight 第 2 步的必答项）？有 → 改为更新那个 skill，不新建叠床架屋的入口。

### 3. Initialize

仅新建 Skill 时运行 `scripts/init_skill.py <skill-name> --path <output-directory>`，并只申请实际需要的资源目录。已有 Skill 不要重复初始化；初始化后替换或删除不需要的示例和占位内容，并在 Skill 根目录创建按统一格式填写的 `文件夹目录.md`。

### 4. Edit

先实现确定性脚本、模板和其他资源，再编写 `SKILL.md` 的 frontmatter 与正文。正文使用指令/不定式表达，保留必要约束、判断标准和引用入口；条件性细节按需下放，避免同一规则在多个文件重复。

涉及 Skill 工作文件夹内文件、目录、脚本或资源的新建、移动、改名、删除或结构变更时，先读取该根目录的 `文件夹目录.md`，完成后同步更新；待删除文件按既有操作门禁处理，落点见根 [文件夹目录.md](../../文件夹目录.md) 与 [OPERATIONS.md](../../OPERATIONS.md) 第 5 节。

编辑 frontmatter 或目录结构时读取 [references/skill-format.md](references/skill-format.md)，平台差异读取 [MACHINE.md](../../MACHINE.md)。压缩、拆分、迁移或删除前执行内容影响测试，并在修改后逐项核对定义、边界、权威关系、路由条件和验证条件仍可找到。

迁移型创建在打包前必须把对源 Skill 的脚本依赖替换为新 Skill 内的本地脚本或明确的可用依赖。

### 5. Validate

优先使用官方 `skills-ref validate` 验证开放规范；当前环境没有该工具时运行：

```bash
scripts/quick_validate.py <path/to/skill-folder>
```

**解释器**：该脚本需要 PyYAML。某个解释器报 `ModuleNotFoundError: No module named 'yaml'` 时，**不说明环境装了没装**——先换本机的隔离 venv 解释器重跑，再考虑替代验证；不要用单点探测结果推及整机环境。本机解释器清单与 venv 路径由当前平台的机器事实文件持有（见 [../../MACHINE.md](../../MACHINE.md) 及 `machine/` 下当前软件文件），本 skill 不硬编码路径。

验证 frontmatter、`name` 与父目录一致性、命名、描述触发边界、引用和资源是否存在、是否残留占位内容、是否违反用户范围或产生内部矛盾。新增或修改脚本必须实际运行；需要行为验证时，使用原始用例或可观察不变量，不只匹配标题或文案。
验证 `文件夹目录.md` 中记录的当前结构与实际目录一致，并确认其中没有机器绝对路径。

### 6. Package

验证通过且确实需要分发时运行：

```bash
scripts/package_skill.py <path/to/skill-folder> [output-directory]
```

打包脚本会先验证，验证失败时先修复再重试，不交付未验证的包。

### 7. Iterate

用真实任务观察 Skill 的触发、执行和输出质量；根据可复现的失败或效率问题做窄修正。单个例子不能直接升级为普遍规则，除非它揭示了可复用的不变量或流程。
