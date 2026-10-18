# P2 多数据库与独立发现通道

状态：代码与离线测试已完成；真实 PubMed/Semantic Scholar 请求未在本轮执行。

## 已实现

- `research_search.providers` 统一 Provider / SearchRequest / ProviderResult 契约。
- PubMed ESearch/EFetch XML 与 JSON/ESummary 离线解析：PMID、标题、摘要、作者、期刊、MeSH、作者关键词分开；可生成日期、语言、MeSH 查询计划。
- Semantic Scholar Search、recommendations、citations、references 计划与可注入执行接口；推荐/引用/参考文献保留独立 `channel`、`seed_ids` 和关系说明。
- 多源融合：DOI、PMID、OpenAlex、S2 ID、标题指纹冲突审计；不把来源总数相加成唯一论文数。
- 计划态默认不联网；live 必须注入 transport/client，未在本轮自动使用 Key 或网络。

## 限制

- MeSH 和作者关键词不能互相替代。
- 语义推荐不是直接引文边；未执行的接口不能写成已验证覆盖。
- P2 适配器尚未接入主 `run_package`，当前通过独立 Provider API、CLI 计划命令和离线 `provider-fusion` 审计导出使用。
- 跨库实体等价仍依赖显式 DOI/PMID/OpenAlex/S2 ID，标题相似冲突保留人工审计。
