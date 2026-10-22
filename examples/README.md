# Examples

本目录收录**少量**经过挑选的运行输出，用来展示各个阶段产物长什么样、Schema 校验能否通过。
完整的历史证据档案（P0—P4 全部运行记录、关键词网络、离线缓存等）体量大且包含抓取原文线索，
只保留在本地 `artifacts/`，不随仓库发布。

| 目录 | 阶段 | 说明 |
| --- | --- | --- |
| [`p0-semg-search-package/`](p0-semg-search-package/) | P0 | 一份完整的 Research Search Package（01—10 号文件 + replay bundle），可用 `validate-package` 校验 |
| [`p2-provider-fusion/`](p2-provider-fusion/) | P2 | PubMed 成功结果与 Semantic Scholar 429 失败记录的离线融合产物，展示“失败来源不进正式结论”的记账方式 |
| [`p4-benchmark-report/`](p4-benchmark-report/) | P4 | 离线评测报告：`benchmark.json` / `benchmark.md` / 复核队列 / SHA-256 清单 |

## 校验示例

```bash
# P0 执行包结构校验（离线，不联网）
python3 -m research_search validate-package examples/p0-semg-search-package

# 不安装项目时
python3 scripts/research-search.py validate-package examples/p0-semg-search-package
```

## 注意事项

- 示例是**历史快照**，其中的论文 ID、计数与时间戳都来自当时那次运行，不是当前数据库状态。
- 示例不构成“检索效果优于基线”“完整召回”“跨库实体等价”的证据。
- 重新生成同类产物会把结果写入本地 `artifacts/`（已被 `.gitignore` 忽略）。
