# Progressive Disclosure

渐进披露用于控制上下文成本，不用于删除必要语义。按需下放后，定义、边界、权威关系、触发条件、必须动作和验证条件仍须可达。

## Loading layers

1. **Metadata**：`name` 和 `description` 用于发现和触发。
2. **Instructions**：Skill 触发后加载完整 `SKILL.md` 正文。
3. **Resources**：`scripts/`、`references/` 和 `assets/` 只在当前任务需要时引入或使用。

## What stays in `SKILL.md`

入口保留共同目的、触发与边界、核心决策、必要约束、停止条件、验证要求和 reference 路由。多个模式共享的选择标准留在入口，模式专属细节放入对应 reference。

## What moves to references

适合下放的内容包括：

- 只在特定模式或平台使用的字段、流程和故障排查；
- 长例子、schema、模板、API 说明和实现注记；
- 入口已声明选择条件后才需要的变体指南。

只有在父 Skill 已触发后才有意义的内容放 `references/`；能够独立触发、复用或承担决策入口的能力应成为独立 Skill。

## Split patterns

可采用以下形状，按实际路由选择：

```text
skill/
|-- SKILL.md                 Shared purpose and routing
`-- references/
    |-- format.md            Format-specific details
    `-- provider.md          Provider-specific details
```

没有真实路由差异时不要另加 router。reference 应聚焦、直接可达；较长的 reference 也应有目录，避免为了拆分而制造另一份大入口。

**目标不是压体量，是入口整洁、加载高效**——常驻只留必须每次生效的内容。**200 行 / 8,000 字留意、300 行 / 12,000 字必办**：到硬线必须动手，且比信号时更严格地拆或缩（两组数字按实测"字/行≈40"换算；**任一条越线即触发**——长行藏量是行数看不出来的）。

怎么做按内容定：能挪的挪进按需 reference（首选，信息不丢）、表述能压的压、冗余或别处已有落点的删；但**不得仅为压体量删掉必要语义**（判据见 [IMPORTANCE.md](../../../IMPORTANCE.md) 的影响测试）。本文件给的是可选方法，不是必须照做的步骤。
