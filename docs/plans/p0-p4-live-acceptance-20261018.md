# P0—P4 实际验收记录

日期：2026-10-18。Key 只通过命令环境传入，未写入源码、配置或交付包。

## P0

- 真实 OpenAlex：4 次成功请求（1 smoke + 3 三类策略），每策略 `per_page=5`。
- 三类数据库总命中：8,188 / 5,206 / 481。
- 每策略实际抓取 5 条；联合去重后 14 篇。
- P0 证据记录 2,245 条；候选词/统计短语 1,724 条。它们不是人工确认关键词或相关论文数。
- 真实包：`artifacts/p0/p0-live-20261018/`。
- 同一真实快照离线重放：0 新请求，内容哈希一致，验证通过。

## P1

- 真实两轮 OpenAlex 对照：6 次请求。
- 基线 A 与候选 B 的联合结果观察到 6 个新增 ID。
- 没有人工相关性标注，所以 `confirmed_gain=null`，候选版本停在 `pending_review`，active version 仍为基线。
- 真实会话：`artifacts/p1/p1-live-loop-20261018/`。
- 已实现：版本差异、候选词建议、独立发现遗漏候选、共享预算、语义漂移停止、回退与 manifest。

## P2

- PubMed ESearch/EFetch、MeSH/自由词分离、Semantic Scholar 搜索/推荐/引用/参考文献适配器完成。
- 计划态默认不联网；live 必须显式注入 transport/client。
- 融合保留 DOI/PMID/OpenAlex/S2/标题冲突和 discovery channel。
- P2 离线测试：42 项；本轮未执行 PubMed/Semantic Scholar live 请求。

## P3

- 从真实 P0 包生成 14 篇阅读卡片：`artifacts/p3/p3-reading-p0-20261018/`。
- `open_obsidian` 返回 `manual_import_required`；不扫描、不写 Vault、不启动 Obsidian。
- 不下载全文、不绕过付费墙；公开全文 URL 只有在输入记录明确给出公开断言时才进入获取队列。
- P3 专项测试：37 项。

## P4

- 四类 case fixture：mature / emerging / interdisciplinary / medical；均无人工真值。
- 真实 P0/P1 运行账本已导入：6 条 live runs，6 次历史请求，20 条待审论文。
- `Recall@K`、`P@K`、confirmed new relevant、cost per relevant 全部按契约保持未知。
- `real_advantage_demonstrated=false`。
- benchmark 产物：`artifacts/p4/p4-real-report-20261018/`。
- P4 定向测试：62 项；P2 provider 定向测试：42 项；P3 定向测试：37 项；P1 状态/安全/会话测试：27 项。

## `jev@typesafe` Top-K 重排

- 公开工作流别名：`jev@typesafe`；官方 SDK 模型标识：`jev-latest`。
- 已实现候选论文逐篇 Noul 评分、confidence、usage、错误记录和安全降级。
- 只重排已有 shortlist，不扩展候选集，不修改原始 Research Search Package。
- 当前环境未配置 `TYPESAFE_API_KEY`，真实 Jev 请求为 0；对真实 P0 focused shortlist（14 篇）执行 plan-only，状态为 `not_executed`，候选集未变化，`human_relevance_claim=false`。
- Jev 分数不作为人工相关性、Recall 或 Precision 真值；正式评估仍需人工标注。
- 依据：[TypeSafe API](https://docs.typesafe.ai/api.md)、[Python SDK](https://docs.typesafe.ai/sdk/python.md)、[Re-ranking cookbook](https://docs.typesafe.ai/cookbooks/rerank_typesafe.md)。

## 工程总检查

- 全套测试：最终复跑通过；当前测试函数总数按文件统计为 211 项，另包含参数化用例展开。
- Skill lint：通过。
- P3/P4 CLI 集成：通过。
- 自包含 ZIP：包含 Skill、P2/P3/P4 脚本、Schema、示例和 references。

## 未完成/未证明

- 无人工独立相关集，不能声称检索效果优于普通 LLM、litsearchr 或其他竞品。
- P2 真实多数据库覆盖未执行；P3 合法全文获取只完成交接，不完成下载；P4 只完成评测框架和真实账本导入。
- 不将数据库总命中、候选词数、抓取数量或新增 ID 写成相关论文数量。
