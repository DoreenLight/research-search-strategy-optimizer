# 关键词知识网络：分阶段路线图

版本：0.1
日期：2026-10-19
对应设计：`docs/plans/keyword-knowledge-network-design.md`
当前基线：P1 闭环、P2 Provider/融合、P4 benchmark/intake 已有代码；2026-10-18 已记录 PubMed 真实成功联调与 Semantic Scholar HTTP 429；P4 独立真值和双人正式审阅尚未提供。

## 1. 总体目标

建立一个能够持续吸收论文关键词和多源术语、保留来源证据、形成候选关系、接受人工审阅、通过单变量实验验证、支持采用与回退的关键词知识网络。

## 2. 不可违反的路线规则

1. 原始观察、候选关系、已审阅关系、已采用关系分层保存。
2. 候选词/候选边不能自动进入正式查询。
3. 每一轮最多改变一个 concept group 或一个 discovery channel。
4. test split、独立 reference set 和封存人工标签不能反向用于扩词。
5. 历史请求、本批新增请求、理论搜索空间、实际执行次数和保留配置分开记录。
6. `pending`、失败、未知成本和未执行不能写成 0 或成功。
7. 推荐、citation、reference、keyword search 必须保留不同 channel。
8. 任何真实联网都必须显式、预算化、可取消、带失败账本。
9. P3 全文获取、付费访问、Vault 写入不属于本路线图。
10. 没有独立真值和完整人工标签时，不宣称 Recall@K、P@K 或策略优势。

## 3. 里程碑总览

| 里程碑 | 名称 | 目标 | 主要交付 | 完成门槛 |
|---|---|---|---|---|
| K0 | 规则冻结 | 固定网络边界和术语关系 | 本设计、字段枚举、审阅协议 | 关系类型和证据等级经确认；无隐式采用 |
| K1 | 只读网络构建 | 从已有 package 生成稳定节点/边 | `keyword_network.py`、nodes/edges/observations | 已实现；旧 P0/P1 包兼容；实际 sEMG 样例 5.8MB、4,692 observations、2,362 nodes、5,415 bounded edges；无网络请求 |
| K2 | 前沿排序 | 从候选边选择人工审阅队列 | `candidate-frontier.json`、评分说明 | 排序只改变顺序，不改变语义状态 |
| K3 | 网络审阅 | 复用工作台完成节点/边审阅 | edge review 页面、review events | 两人/单人状态、冲突、pending 可保留 |
| K4 | 显式采用 | 把 approved edge 生成新 case | `adopt-edge` 或扩展 `adopt-keywords` | 只改一个组；源 case 不覆盖；有 rollback target |
| K5 | 单变量实验 | 把采用边接入 P1 版本循环 | experiment/network link | 请求、论文、人工新增和成本可追溯 |
| K6 | P2 反馈 | 将多源和 discovery 结果反馈到网络 | Provider channel/source records | channel 分离；失败不当成功；融合冲突保留 |
| K7 | P4 冻结 | 四领域 discovery/test 和双审 | benchmark manifests、review outputs | 外部 reference set 和两份人工材料齐全 |
| K8 | 正式评测 | 计算 Recall@K/P@K/成本指标 | benchmark reports | 同 K、同 split、同预算、完整人工标签 |

## 4. K0：规则冻结

### 工作

- 确认节点类型：concept、lexical_form、controlled_term、paper、source_record、query_version、provider_channel。
- 确认边类型：observed_in、database_assigned、cooccurs_with、variant_of、equivalent_to、broader_than、narrower_than、related_task、alternative_method、application_of、retrieved_by、discovered_by、tested_in。
- 确认状态：observed、candidate、pending_review、approved、rejected、adopted、retired、conflicted。
- 确认来源等级：A/B/C/U；来源等级不等于相关性或研究质量。
- 冻结 P4 test 不得被网络扩展回看。

### 输出

- `keyword-knowledge-network-design.md`
- 关系类型和状态表
- 审阅字段和审阅者输入约定

### 停止条件

若无法区分 `equivalent_to` 与 `related_task` / `broader_than`，不进入 K1，先回到范围和关系定义。

## 5. K1：只读网络构建

### 工作

输入现有 Research Search Package：

- `02-keywords.json`
- `raw-observations.jsonl`
- `07-evidence.jsonl`
- `04-papers.jsonl`
- `05-search-runs.jsonl`
- `11-provider-results.jsonl`
- `12-provider-fusion.json`

生成：

```text
nodes.jsonl
edges.jsonl
observations.jsonl
source-index.jsonl
network.json
manifest.json
```

### 实现建议

- 观察 ID：由 scope、paper、field、normalized term、excerpt 的稳定 hash 生成；
- 节点 ID：由 scope、node_type、normalized label 生成；
- `observed_in` 边：每个 observation 到 paper/field；
- `database_assigned`：数据库关键词/MeSH 与 source record；
- `cooccurs_with`：只在同一 paper/字段内生成，保存 document frequency；默认最多 50,000 条、单节点最多 25 条、document frequency 至少 2；完整观察仍保留，边是可审阅候选前沿而不是完整笛卡尔积；
- 关系边初始均为 `candidate` 或 `observed`，不能生成 approved equivalent；
- P2 discovery channel 单独写 `discovered_by`，不能写成 `retrieved_by`。

### 验收

- 相同输入重复构建，节点/边 ID、排序和 hash 一致；
- 字段片段可在论文记录中定位；
- 未知 provider/失败 run 有明确状态；
- `candidate_count` 与 `reviewed_count` 分开；
- 无网络请求；
- 输出目录拒绝覆盖。

## 6. K2：候选前沿排序

### 工作

候选前沿排序输入：

- source diversity；
- paper diversity；
- field type；
- document frequency；
- omission signal；
- relation type；
- review cost；
- semantic drift risk。

输出：

```json
{
  "frontier_version": "frontier-0001",
  "selection_limit": 30,
  "selection_rule": "...",
  "terms": [],
  "edges": [],
  "deferred_count": 0
}
```

### 验收

- 排序不自动修改边状态；
- `equivalent_to` 候选不能因为高频自动变成 approved；
- broader/related/application 默认要求 branch；
- 前沿大小和人工分钟预算可单独报告。

## 7. K3：网络审阅

### 工作

扩展当前本地工作台：

- `paper review`：判断论文是否相关；
- `term review`：判断词形是否有用；
- `edge review`：判断关系类型；
- `evidence review`：查看字段片段和来源等级。

默认隐藏：

- baseline/candidate 名称；
- 预期新增收益；
- 模型分数；
- 该边是否来自 test；
- 策略排序。

### 审阅结果

- 一致 approved/rejected；
- 冲突 `conflicted`；
- 缺失证据 `pending_review`；
- 不自动仲裁；
- 保留 reviewer 原始事件。

### 验收

- 两个 reviewer 不互相覆盖；
- 导入只接受当前 scope、queue fingerprint 和 paper/edge pool；
- 任何证据缺失都不能变成 irrelevant；
- 导出结果可供 K4 使用。

## 8. K4：显式采用

### 工作

提供：

```bash
python3 scripts/research-search.py adopt-keywords \
  <case.json> <reviewed-keywords.json> \
  --group-id input \
  --output <new-case.json>
```

后续扩展：

```bash
python3 scripts/research-search.py adopt-edge \
  <case.json> <network.json> \
  --edge-id edge-0001 \
  --output <new-case.json>
```

### 采用记录

```json
{
  "adoption_id": "adopt-0001",
  "parent_case_id": "case-1",
  "parent_version": "v0",
  "changed_group": "input",
  "adopted_edge_ids": ["edge-0001"],
  "reason": "...",
  "evidence_ids": ["ev-1"],
  "rollback_target": "v0",
  "status": "candidate"
}
```

### 验收

- source case 永不覆盖；
- 只改一个 concept group；
- approved 关系必须有外部证据；
- adopted 不是 retained；
- 必须进入 K5 测试或保持候选状态。

## 9. K5：单变量实验

### 工作

复用现有 `optimization_session.py`：

- parent version = 当前 active；
- candidate version = 显式采用后的 case；
- `changed_groups` 必须只有一个；
- provider/channel、query、filters 和 cost 分开记录；
- 结果连接到 `tested_in` 边；
- 人工确认相关后才计算 `confirmed_new_relevant_count`。

### 验收

- 未审阅新增 → `pending_review`；
- 丢失已确认相关 → rollback；
- 成本预算已启用但未知 → pending；
- 无正向确认新增 → 不 retain；
- semantic drift → rollback；
- P4 test 论文不进入词扩展。

## 10. K6：P2 多源反馈

当前已验证事实：PubMed 一次小预算真实联调成功（2 请求、reported 271、fetched 5）；Semantic Scholar 同主题一次请求返回 HTTP 429，失败已保留，不能解释为空结果或覆盖未存在。

### 工作

每次 Provider 结果都生成：

```text
provider
query_type/channel
status
historical_request_count
new_network_request_count
reported_count
fetched_count
deduplicated_count
source_level
error_type
```

网络反馈：

- PubMed MeSH 与 free text 分开；
- Semantic Scholar keyword/recommendation/citation/reference 分开；
- 失败来源进入 coverage/error ledger；
- DOI/PMID/OpenAlex/S2 ID 冲突保留；
- 只有人工确认后，才把新术语连接到已确认边。

### 当前事实

- PubMed 已完成一次真实小预算成功联调：2 请求、reported 271、fetched 5；
- Semantic Scholar 同主题一次请求返回 HTTP 429；
- 这两条记录已经保存为真实审计产物；
- 失败不代表无论文；本轮不反复重试。

## 11. K7：P4 冻结与双审

### 工作

四个预设领域：

- mature：sEMG / joint angle；
- emerging：vision-language-action；
- interdisciplinary：urban heat / health risk；
- medical：chest radiograph / pneumonia。

每个领域建立：

```text
discovery case
test case
independent reference_set
reference_set_source
reviewer-a.jsonl
reviewer-b.jsonl
```

当前 `p4-four-domain-plan-20261018` 只有 plan-only case，不能称 test set。

### 双审门槛

- 两名 reviewer 独立判断；
- 同意 relevant/irrelevant 才能成为最终标签；
- 冲突或 pending 不自动仲裁；
- P4 intake 只生成 benchmark manifest；
- Recall@K/P@K 交给现有 `run_benchmark`；
- 没有真实材料时所有效果指标保持 null。

## 12. K8：正式评测

### Recall@K

只在：

```text
split=test
reference_set_independent=true
reference_set_source 非空
```

时启用。分母是独立 reference set 大小，不是领域全部论文。

### P@K

只在：

```text
去重后至少 K 条结果
前 K 每条都有 human relevant/irrelevant
```

时启用。pending/缺失标签不能当负例。

### 新增相关收益

```text
candidate_strategy 新增 ID 中人工确认 relevant 的数量
```

未完全审阅时为 null 或下界，不写成 0。

### 成本效率

```text
candidate total known cost / confirmed incremental relevant count
```

任何成本未知或确认新增为 0 时为 null。

## 13. 依赖关系与推荐执行顺序

```text
K0 规则冻结
  ↓
K1 只读网络构建
  ↓
K2 前沿排序 ──→ K3 网络审阅
                      ↓
                  K4 显式采用
                      ↓
                  K5 P1 单变量实验
                      ↓
K6 P2 多源反馈 ────────┘
  ↓
K7 P4 discovery/test 冻结
  ↓
K8 正式 Recall@K/P@K
```

推荐顺序：

1. 先完成 K1/K2/K3，确保网络可解释、可审；
2. 再做 K4/K5，不要直接把图算法接入实时检索；
3. P2 结果作为 evidence/source/channel 输入，不自动成为 approved edge；
4. 先冻结 P4 test，再扩展网络；
5. 最后用 P4 计算正式指标。

## 14. 每轮交付模板

每个里程碑都必须交付：

```text
目标
本轮不做什么
输入 manifest/hash
理论搜索空间
历史运行数
本批实际请求数
实际成功/失败/partial 数
候选节点/边数
人工审阅数
pending/conflict 数
保留/回退决定
新增相关数（unknown/null/confirmed）
成本与筛选分钟
输出目录
验证命令
未验证边界
```

## 15. 完成定义

关键词知识网络路线图只有在以下条件都满足后才可称为第一版完成：

- 观察节点和证据可追溯；
- 候选边与 approved/adopted 分离；
- 工作台可以审阅边和证据；
- 显式采用只改一个变量组；
- 单变量实验连接到 P1 retain/rollback；
- P2 source/channel/失败账本可回溯；
- P4 有冻结 test reference set 和双审材料；
- 正式 Recall@K/P@K 由 benchmark 计算；
- 全部未知/失败/pending 没有被转成 0 或成功；
- 所有输出可用 manifest/hash 复核；
- 没有因网络中心性、词数或模型分数直接宣称检索优势。
