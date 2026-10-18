# P2 真实小预算联调记录

日期：2026-10-18；主题：surface electromyography joint angle；limit=5。

## 实际结果

- PubMed：`success`；2 次请求（ESearch + EFetch）；reported_count=271；fetched_count=5。
- Semantic Scholar：`failed`；1 次请求；error_type=`http_error`；HTTP 429；fetched_count=0。
- 本批真实 Provider 请求数：3。
- 未执行全文获取、P3 Vault 写入或付费访问。
- Semantic Scholar 失败不是空结果，也不代表该来源没有论文。

## 文件

- `pubmed-result.json`：脱敏 ProviderResult，含 PubMed 论文元数据与原始来源字段。
- `pubmed-request.json`：请求模式、query、filters、limit、计数和 query_hash。
- `semantic-scholar-result.json`：结构化失败 ProviderResult。
- `semantic-scholar-request.json`：失败请求账本。
- `manifest.json`：本目录文件 SHA-256。

这些是一次真实小预算联调记录，不是 P4 独立测试集、真值集或检索优势证明。
