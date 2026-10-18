# P4 质量基准与人工审阅报告

这是离线汇总，不发起请求，也不自动宣告策略优势或产品化。live 为输入声明，未在本次评测中重新联网验证。
未知、不适用和未审阅均不按 0 或负例处理。synthetic 仅供工程验证，replay 只复用历史记录。

- 预计划 case 数：4；本次输入 case 数：4。
- 实际登记执行记录：0；live 成功记录：0。
- 输入记录中的新增 live 请求：0；本评测函数新增联网请求：0。
- 待人工审阅：0；K=20；比较锚点：A（同 mode）。

## 分模式执行账本

| 模式 | 登记 | 已执行 | 成功 | 失败 | partial | 未执行 | 新请求 |
|---|---:|---:|---:|---:|---:|---:|---:|
| live | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| replay | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| synthetic | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## 分 case、baseline、mode 比较

total_unique 仅来自成功组内 ID 并集；多库 reported_count 不相加。不同 mode 永不互作比较锚点。
一个组含失败、未执行或 partial 来源时，保留原记录，但整组不计质量或增量收益。

| Case / 类别 / split | Baseline / mode | 状态 | reported_count | total_unique | new_unique | K 内已知相关 | Recall@K | P@K | 成本 USD | 每新增确认相关成本 USD | 筛选分钟 |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| p4-mature-semg-joint-angle / mature / discovery | 无记录 | not_executed | — | — | — | — | — | — | — | — | — |
| p4-emerging-vision-language-action / emerging / discovery | 无记录 | not_executed | — | — | — | — | — | — | — | — | — |
| p4-interdisciplinary-urban-heat / interdisciplinary / discovery | 无记录 | not_executed | — | — | — | — | — | — | — | — | — |
| p4-medical-chest-radiograph-pneumonia / medical / discovery | 无记录 | not_executed | — | — | — | — | — | — | — | — | — |

## 来源与解释

| Case | Baseline / mode | 来源 | 状态 | 单来源 reported_count | 来源说明 |
|---|---|---|---|---:|---|

## 指标边界与审阅

- Recall 仅对显式独立、有来源说明的 test reference_set；discovery 或只给 ID 的集合不形成召回率。
- P@K 只在前 K 个去重结果全部有人工 relevant/irrelevant 标签且确有 K 个结果时计算；uncertain 不作负例。
- K 内已知相关是独立测试集命中，或人工已确认命中的下界；不是全部相关文献估计。模型标签从不进入质量指标。
- new_unique 相对同 mode 锚点与 existing_catalog_ids 的并集；缺少成功锚点则未知。A 对自身新增为 0。
- 每新增确认相关成本 = 候选组全部已知成本 / 人工确认新增相关数；不是候选减锚点的成本差。未知成本、无确认新增均为空。
- review-queue.jsonl 不含 baseline、mode 或模型判断；审阅员应在单独盲化材料中审阅，再由协调人回填标签。
- PRESS/PRISMA-S 是审查与报告指针，不是本实现获得合规认证。协议：docs/plans/p4-quality-protocol.md。
