# P0 验收矩阵

本页定义完成标准，不是实际通过记录。实际结果见 `evals/reports/p0-evaluation.md`（生成后提供）。

| 编号 | 通过条件 | 检查方法 |
|---|---|---|
| A01 | 中文科研需求经宿主 Agent 明确拆为对象/输入/任务/方法/应用/开放限制 | 示例case及Skill有无对照；不声称Python自动理解任意主题 |
| A02 | 候选词、文本观察、作者词和机器标签来源分开 | evidence/source字段和出处片段自动检查 |
| A03 | 三类查询由角色而不是数组顺序构建，方法不进入探索检索 | 打乱顺序测试、无方法not_applicable、AST一致性 |
| A04 | DOI/OpenAlex/PMID合并可追溯，冲突保留 | 标识别名链、多轮合并、不同DOI冲突回归 |
| A05 | 失败/空结果/部分成功区分，凭证不入输出 | 429/403/超时/畸形JSON/反射密钥/摘要损坏测试 |
| A06 | 所有HTTP尝试纳入总请求预算，重试有界 | 注入transport/clock/sleep单元测试 |
| A07 | Scope/Keyword/Paper/Plan/Run/Evidence/Judgment等按Schema实际校验 | JSON Schema、跨文件ID和manifest哈希检查 |
| A08 | 完整检索包能在离线重放中重建稳定内容 | fixture/live_capture重放；不把重放计为新检索 |
| A09 | 至少一次实际OpenAlex Works响应保存，可追溯到论文及证据 | 小预算匿名联网检查；失败不伪装成功 |
| A10 | 效果评测不误把未标注当不相关，模型/人工判断分层 | partial labels、K大于样本、无真值集测试 |
| A11 | Skill格式与引用通过lint，自包含ZIP可运行 | 本地lint、ZIP目录/路径/缺失资源检查 |
| A12 | 至少一轮Skill有无对照且无重大回退 | 独立模型流程输出与逐条比较；非检索效果实验 |

## 本版边界

- 可交付P0工具不等于证明检索效果优于竞品。
- 没有人工金标准时，Recall/Precision优势仍未验证；单提示词对照仅评价工作流质量。
- 只有OpenAlex执行适配，PubMed/MeSH、Semantic Scholar、语义/引文独立通道及自动闭环为路线图阶段。
- 校验通过仅说明格式/来源链/程序行为与当前检查一致，不构成系统综述规范认证。
