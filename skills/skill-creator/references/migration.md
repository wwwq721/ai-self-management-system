# Migration-Type Skill Creation

当新 Skill 从一个或多个已有 Skill 提取、合并或迁移而来时，使用本流程。目标是形成按能力组织的新入口，而不是把来源文件并排堆在一起。

## Before implementation

1. 读取每个源文件，包括没有脚本的纯文本 Skill；它们可能包含触发条件、流程、安全边界和应排除的职责。
2. 检查脚本内部耦合、导入关系、隐含路径和输出目录；移动目录可能使内部导入失效。
3. 根据耦合深度选择重写或薄包装：深耦合提取所需核心逻辑，浅耦合可连同少量依赖迁移。
4. 清除不适用于新 Skill 的源特定知识库、模板、目录和输出假设。

## Write the new Skill

5. 不复制源 Skill 的触发词；为新 Skill 写覆盖自身范围的 `description`，必要时声明边界以消除歧义。
6. 源 Skill 缺少的选择依据、比较资料或外部事实另行核实，不把单个源 Skill 的实现方式冒充通用决策规则。
7. 草稿中可以暂时引用源脚本；打包前必须改为新 Skill `scripts/` 中的本地脚本或明确存在的依赖。
8. **Dissolve, don't categorize**：把独有内容溶入已有能力结构，不按源 Skill、应用或网站各建一节。章节命名能力（如 Desktop Control、Browser Control），源特定细节放入对应能力的注记或 reference。

完成后按父 Skill 的验证流程检查每个源用例、触发边界、脚本耦合和资源引用；未验证的迁移不要打包。
