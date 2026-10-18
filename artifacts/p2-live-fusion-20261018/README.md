# P2 联调结果离线融合

输入：`../p2-live-20261018/pubmed-result.json` 与 `../p2-live-20261018/semantic-scholar-result.json`。

- fusion 模式：`offline_fusion`
- 本次新增网络请求：0
- 输入历史 Provider 请求数：3（PubMed 2 + Semantic Scholar 1）
- PubMed 成功结果与 Semantic Scholar HTTP 429 失败记录均保留。
- 失败来源不被当作空成功来源，也不进入正式 P4 效果结论。

输出文件：`fusion.json`、`papers.jsonl`、`source-records.jsonl`、`conflicts.jsonl`、`manifest.json`。
