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

接近 500 行是检查拆分的信号，不是为了达标而删除定义性或验证性内容。压缩前使用 [IMPORTANCE.md](../../../IMPORTANCE.md) 的影响测试；能改变理解、决策、执行、适用边界或验证结果的内容保留语义，可改写或迁移。
