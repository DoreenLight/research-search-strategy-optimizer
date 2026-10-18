# P2 多数据库与独立发现通道

状态：Provider API、离线融合导出、主 `run_package` 可选 provider-plan/provider-results 接入已完成；2026-10-18 已完成一次 PubMed 小预算真实联调，Semantic Scholar 同主题请求返回 HTTP 429，失败已保留为结构化审计记录。

## 已实现

- `research_search.providers` 统一 Provider / SearchRequest / ProviderResult 契约。
- PubMed ESearch/EFetch XML 与 JSON/ESummary 离线解析：PMID、标题、摘要、作者、期刊、MeSH、作者关键词分开；可生成日期、语言、MeSH 查询计划。
- Semantic Scholar Search、recommendations、citations、references 计划与可注入执行接口；推荐/引用/参考文献保留独立 `channel`、`seed_ids` 和关系说明。
- 多源融合：DOI、PMID、OpenAlex、S2 ID、标题指纹冲突审计；不把来源总数相加成唯一论文数。
- 计划态默认不联网；live 必须注入 transport/client，未在本轮自动使用 Key 或网络。

## 限制

- MeSH 和作者关键词不能互相替代。
- 语义推荐不是直接引文边；未执行的接口不能写成已验证覆盖。
- P2 适配器已通过可选 `provider-plan` / `provider-results` 接入主 `run_package`；默认仍离线，主包保留独立 Provider 计数和失败状态；CLI 仍支持独立 `provider-fusion` 审计导出。
- 跨库实体等价仍依赖显式 DOI/PMID/OpenAlex/S2 ID，标题相似冲突保留人工审计。
