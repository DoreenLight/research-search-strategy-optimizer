# P4 benchmark report (示例)

由 `pull` 自本地 P4 评测运行输出，用于展示 `benchmark` 报告的结构。

```bash
python3 scripts/research-search.py benchmark <benchmark-manifest.json> --output artifacts/p4/p4-report
```

## 文件

| 文件 | 内容 |
| --- | --- |
| `benchmark.json` | 结构化指标：召回、精确率、judgment 覆盖率与明示的“未证明”边界 |
| `benchmark.md` | 同一份指标的人读版本 |
| `review-queue.jsonl` | 待人工复核条目 |
| `manifest.sha256.json` | 覆盖上面三个文件的 SHA-256 清单（不自我哈希） |

## 边界

示例中的数据来自特定日期的运行快照，不代表检索效果优于基线的结论；未判定条目不能被当作负例。
