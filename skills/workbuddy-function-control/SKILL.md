---
name: workbuddy-function-control
description: 管理 WorkBuddy 功能控制：识别 skill 触发域冲突、处理能力真空、维护功能开关与路由边界。当需要判断多个 WorkBuddy skill 的触发范围或功能归属，或调整相关开关时使用；单个 skill 的创建、正文编辑和验证使用 skill-creator。
metadata:
  importance: 2
  platform: workbuddy
  created_at: 2026-08-19
  requested_by: WorkBuddy
  source: user-created
---

# WorkBuddy 功能控制

## 引用文件

- [../../OPERATIONS.md](../../OPERATIONS.md)：全量检查、操作门禁、停止条件和改动记录。
- [../skill-creator/SKILL.md](../skill-creator/SKILL.md)：skill description、相似 skill、同类边界和验证规则；修改 skill 时按其流程执行。
- [../../README.md](../../README.md)：治理文件与工具型 skill 的分类判据。
- [../../MACHINE.md](../../MACHINE.md)：目标平台字段和平台差异的核对入口。
- [../../machine/workbuddy.md](../../machine/workbuddy.md)：WorkBuddy 当前触发机制及可用功能事实。

## 范围与边界

本 skill 只处理 WorkBuddy 的功能组织与控制：判断触发域是否冲突、能力是否存在真空、功能归属如何仲裁，以及平台支持的功能开关如何核对。它不定义通用操作规范，不把所有 skill 视为治理文件，也不承担单个 skill 的创建或正文维护。

治理文件与工具型 skill 的分类按 `README.md` 判定；skill 的触发和加载行为按目标平台的实际机制核实，不从本 skill 推导跨平台结论。

## 触发域冲突仲裁

当一个具体请求可能命中多个同类 skill 时：

1. 先穷举当前任务实际可用的项目级、用户级和平台来源 skill，再开始比较，不凭记忆判断“没有”或“只有一个”。
2. 将具体请求分别与各 `description` 的用途、使用时机和关键词进行语义对照，并检查其中是否有排除性边界；仅关键词相似不单独构成冲突。
3. 同一具体请求同时命中两个或更多同类 skill，且没有一方边界语言可以排除另一方时，认定为触发域冲突。
4. 按以下顺序裁决：具体领域 skill 优先于通用 skill；明确写出适用边界者优先；对当前请求约束更具体者优先。
5. 仍然无法区分时停止代选，向用户说明候选 skill、冲突点和影响，请用户决定归属。

裁决后发现 description 仍会误触发时，只提出最小边界修正；实际编辑按 `skill-creator` 的 BP #1、BP #6 和 BP #6a 执行，不在本 skill 中复制其写作规则。

## 能力真空仲裁

完成上述全量检查后，若没有现有 skill 的 description 认领该能力，标记为“能力真空”，并按以下顺序处理：

- 优先判断是否应收窄或扩展一个相近现有 skill，遵循 `OPERATIONS.md` 的“优先改现有”原则。
- 只有在职责边界清楚、不会造成触发混淆时，才提出新建 skill；新建及其验证由 `skill-creator` 处理。
- 将候选归属、复用现有 skill 的理由或新建建议报告给用户，由用户确认，不擅自制造新的入口。

## 功能开关

需要调整 `disable`、`disable-model-invocation` 或其他平台支持的 skill 扩展字段时：

1. 先从 `MACHINE.md` 及 `machine/workbuddy.md` 核对目标平台是否支持该字段及其语义，不把其他平台的字段行为当作 WorkBuddy 事实。
2. 明确开关影响的是模型自动调用、用户可见性还是 skill 是否启用，避免用一个开关同时表达不同意图。
3. 只改为解决当前功能控制问题所需的最小范围，并遵守 `OPERATIONS.md` 与 `skill-creator` 的修改、验证和记录流程。

## 输出要求

完成一次控制判断时，至少说明：实际检查的 skill 来源、命中的候选、冲突或真空的判定、最终归属或待用户裁决项，以及涉及的边界或开关影响。
