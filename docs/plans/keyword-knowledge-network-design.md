# 关键词知识网络：完整设计方案

版本：0.1
日期：2026-10-19
状态：设计方案；本文件不代表知识网络已经完成真实验证

## 1. 目标与核心判断

### 1.1 目标

把每次论文检索中出现的关键词、术语变体、受控词、任务表达、方法表达、应用表达和跨来源关系，沉淀成一个**可追溯、可审阅、可版本化、可回退、可用于下一轮检索的关键词知识网络**。

它解决的不是“把关键词收集得越多越好”，而是回答：

- 这个词在哪篇论文、哪个字段、哪个数据库记录中出现？
- 它是作者/数据库提供的词，还是标题/摘要中观察到的短语？
- 它与当前研究概念是什么关系？这个关系由谁、依据什么确认？
- 它曾经被哪一版查询测试过，带来多少返回、去重后论文和人工确认新增？
- 它是否只在某一来源或某一方法分支中出现，是否可能造成语义漂移？
- 下一轮是否应该把它作为检索词、独立分支、发现线索，还是只留在知识网络中？

### 1.2 核心判断

这个思路可行，但必须把“知识网络”定义成**证据网络 + 候选关系网络**，而不是自动生成的同义词表。

关键词之间的共现、相似、嵌套或来自同一篇论文，只能形成观察或候选边，不能自动证明：

- 两个词是同义词；
- 一个词可以替代另一个词；
- 一篇论文与研究问题相关；
- 一条边应进入正式检索式；
- 某个来源的结果代表整个研究领域。

因此，网络需要至少分为三层：

```text
原始观察层 raw observations
        ↓
候选关系层 candidate graph
        ↓  人工/宿主 Agent 明确审阅
已确认知识层 reviewed knowledge graph
        ↓  显式采用、单变量测试
检索策略版本与实验记录
```

默认只允许前两层产生“待审线索”，只有第三层的已确认边和明确采用动作，才允许进入新的正式查询版本。

## 2. 非目标

本方案当前不做：

- 自动把图上的高频词直接加入查询；
- 用语言模型相似度替代论文字段证据和人工判断；
- 把关键词网络当成完整领域知识图谱；
- 从候选策略输出反向制造独立 test reference set；
- 把推荐论文当作引文关系；
- 自动下载全文、绕过付费墙或写入 Vault；
- 用网络中心性、词频或模型分数宣称检索优势；
- 在没有人工真值时计算正式 Recall@K / P@K；
- 把历史运行、理论搜索空间和本批新增实验混成一个数字。

## 3. 现有代码能力与新增模块边界

当前项目已经具备：

- P0 OpenAlex 论文元数据、字段级证据和三类查询计划；
- P1 版本、回退、预算、人工审阅和候选词三层输出；
- P2 PubMed / Semantic Scholar Provider、推荐/引文/参考文献通道和融合冲突记录；已完成一次 PubMed 小预算真实联调，Semantic Scholar 同主题请求返回 HTTP 429，失败已留存；
- P4 离线 benchmark、独立 reference set 契约和双人审阅 intake；
- 本地离线审阅工作台、缓存和 `provider-plan` 主流程入口。

关键词知识网络应作为新的深模块，外部接口尽量小：

```python
build_keyword_network(package_paths, *, prior_network=None) -> KeywordNetwork
propose_network_frontier(network, *, budget, scope_id) -> FrontierProposal
record_network_review(network, review_records) -> KeywordNetwork
export_network(network, output_dir) -> dict
```

### 3.1 接口不变量

- 所有输入包先经过现有 `validate_package`；
- 输入包只读，不覆盖历史包；
- 观察、候选、已审阅和已采用记录必须可追溯到 evidence/paper/run；
- `propose_network_frontier` 只输出候选动作，不直接执行检索；
- 只有显式的 `adopt`/`test` 动作才会改变下一版 query case；
- 网络构建不新增网络请求；Provider 执行仍由独立的 `provider-plan`/`run_package` 预算管理；
- 输出目录拒绝覆盖，并有自己的 manifest/hash。

## 4. 领域模型

### 4.1 节点类型

| 节点类型 | 说明 | 是否可直接进入查询 |
|---|---|---:|
| `scope` | 冻结的研究范围、对象、输入、任务和未指定条件 | 否 |
| `concept` | 研究者/宿主 Agent 定义的概念，例如 `surface electromyography` | 只有已审阅并显式采用时 |
| `lexical_form` | 具体词形、缩写、拼写变体或短语，例如 `sEMG` | 只有已审阅关系确认后 |
| `observation` | 从论文字段或数据库字段原样观察到的短语 | 否 |
| `controlled_term` | MeSH 等受控词或数据库控制字段 | 只有对应数据库规则审阅后 |
| `paper` | 论文记录，带 DOI/PMID/OpenAlex/S2 ID 和来源链 | 否 |
| `source_record` | 某个 Provider/数据库对论文的原始记录 | 否 |
| `query_version` | 一次冻结的查询策略版本 | 否；它是实验对象 |
| `provider_channel` | OpenAlex、PubMed free text、PubMed MeSH、S2 keyword、citation、reference、recommendation 等 | 否 |
| `review_event` | 人工/Agent 对节点或边的审阅事件 | 否 |
| `experiment` | 对某个 query version 的实际执行和指标 | 否 |
| `cluster` | 仅用于导航的术语簇或主题簇 | 否 |

### 4.2 边类型

| 边类型 | 示例 | 证据要求 | 默认状态 |
|---|---|---|---|
| `observed_in` | 词形 → 论文字段 | 字段、原文片段、paper_id、run_id | `observed` |
| `database_assigned` | 数据库词 → source record | Provider 字段和来源等级 | `observed` |
| `cooccurs_with` | `joint angle` ↔ `sEMG` | 同文档/同字段统计 | `candidate` |
| `variant_of` | `sEMG` → `surface electromyography` | 论文证据 + 人工确认 | `candidate` |
| `equivalent_to` | 两个词可互换 | 明确人工/Agent 审阅；最好有多来源证据 | `pending_review` |
| `broader_than` | `joint kinematics` → `joint angle` | 概念层级理由 | `pending_review` |
| `narrower_than` | `knee angle` → `joint angle` | 范围和纳入边界 | `pending_review` |
| `related_task` | `recognition` ↔ `estimation` | 任务差异说明 | `pending_review` |
| `alternative_method` | `Transformer` ↔ `TCN-LSTM` | 方法角色和可比条件 | `pending_review` |
| `application_of` | `rehabilitation robotics` → `joint-angle estimation` | 应用上下文 | `pending_review` |
| `retrieved_by` | 论文 → query/provider channel | query_version、run_id、channel | `observed` |
| `discovered_by` | 论文 → recommendation/citation/reference | seed、channel、Provider 记录 | `observed` |
| `tested_in` | 词/边 → experiment | query_version、请求数、结果集合 | `observed` |
| `supports` | evidence → edge/concept | 原文片段和定位 | `observed` |
| `contradicts` | evidence → proposed edge | 反例或冲突来源 | `reviewed` |

### 4.3 边状态

边状态不能只用一个布尔值，建议使用：

```text
observed       只表示字段中实际出现
candidate       可作为审阅/测试候选
pending_review  已进入审阅但证据或判断不足
approved        人工/Agent 明确确认关系
rejected        明确拒绝该关系
adopted         已进入某个新 query case；不是永久真理
retired         曾采用但后来被回退/废弃
conflicted      不同审阅者或来源结论冲突
```

`adopted` 必须绑定到 `case_id` / `query_version`，不能表示跨项目、永久有效。

## 5. 数据层设计

### 5.1 推荐输出目录

```text
keyword-network-<case>-<date>/
├── network.json
├── nodes.jsonl
├── edges.jsonl
├── observations.jsonl
├── candidate-frontier.json
├── review-events.jsonl
├── adoption-events.jsonl
├── network-experiments.jsonl
├── source-index.jsonl
├── README.md
└── manifest.json
```

### 5.2 原始观察 `observations.jsonl`

```json
{
  "observation_id": "obs-000001",
  "term": "surface EMG",
  "normalized_term": "surface emg",
  "source_field": "title",
  "paper_id": "https://openalex.org/W...",
  "source_record_id": "openalex:...",
  "run_id": "run-plan-...",
  "query_version": "round-01",
  "excerpt": "Surface EMG based continuous estimation...",
  "evidence_level": "A",
  "observed_at": "2026-10-18T...",
  "status": "observed"
}
```

规则：

- 原文片段必须能在指定字段中定位；
- `normalized_term` 只做格式规范化，不做语义归并；
- 单词、数字、摘要碎片可以保留在原始层，但不一定进入候选前沿；
- 不删除低质量观察，避免以后无法追溯为什么产生候选。

### 5.3 节点 `nodes.jsonl`

```json
{
  "node_id": "lex-surface-emg",
  "node_type": "lexical_form",
  "label": "surface EMG",
  "normalized_label": "surface emg",
  "scope_ids": ["scope-semg"],
  "observation_ids": ["obs-000001", "obs-000023"],
  "paper_ids": ["https://openalex.org/W..."],
  "document_frequency": 4,
  "source_field_count": 2,
  "provider_count": 1,
  "evidence_status": "observed",
  "review_status": "pending",
  "adopted_cases": [],
  "created_from": "package-artifact",
  "schema_version": "0.1"
}
```

### 5.4 边 `edges.jsonl`

```json
{
  "edge_id": "edge-000001",
  "subject": "lex-surface-emg",
  "predicate": "equivalent_to",
  "object": "concept-surface-electromyography",
  "scope_id": "scope-semg",
  "status": "pending_review",
  "confidence": null,
  "evidence_ids": ["ev-0001", "ev-0009"],
  "supporting_paper_ids": ["https://openalex.org/W..."],
  "review_event_ids": [],
  "query_test_ids": [],
  "source_count": 2,
  "created_at": "2026-10-19T...",
  "updated_at": "2026-10-19T..."
}
```

`confidence` 只允许表示证据/审阅状态的结构化摘要，不能被解释为模型对相关性的概率。若需要数值，必须同时保存计算方法、数据集、分母和是否人工封存。

### 5.5 审阅事件

```json
{
  "review_event_id": "review-000001",
  "target_type": "edge",
  "target_id": "edge-000001",
  "reviewer_id": "reviewer-a",
  "label": "approved",
  "relationship": "equivalent_to",
  "rationale": "两个词在目标论文和多个数据库记录中作为同一输入模态变体使用。",
  "evidence_locator": "title/abstract/database keyword",
  "judged_at": "2026-10-19T...",
  "review_round": "discovery-review-01",
  "source_level": "A",
  "adjudication_status": "not_needed"
}
```

对于正式 test 资产，继续使用 P4 的双人规则：

- 两名审阅者一致 decisive 才能成为 `approved`；
- 冲突、缺失、pending 不自动仲裁；
- 模型建议只能作为独立线索；
- 采用事件与原始审阅事件分开保存。

## 6. 网络构建流程

### 6.1 阶段 A：采集与归一化

输入：Research Search Package、ProviderResult、P2 FusionResult。

处理：

1. 读取 `04-papers.jsonl`、`07-evidence.jsonl`、`02-keywords.json`、`raw-observations.jsonl`；
2. 读取 Provider 的 MeSH、作者关键词、来源字段和 channel；
3. 生成稳定 `observation_id`；
4. 规范大小写、空格、连字符、Unicode 形式；
5. 保留原词与标准化词两列；
6. 按 DOI/PMID/OpenAlex/S2 ID 建立 paper/source record 关联；
7. 把推荐、citation、reference 放在独立 discovery channel。

不得在此阶段生成 `equivalent_to`。

### 6.2 阶段 B：候选边生成

候选边可以来自：

- 同一论文标题/摘要/关键词字段中的共现；
- 同一数据库受控词与自由词映射；
- 多篇论文中稳定出现的词形变体；
- P2 citation/reference/recommendation 发现的论文及其新增术语；
- P1 识别出的独立通道漏检论文；
- 显式人工输入的候选关系。

候选边生成必须说明 `generation_reason`，并按以下优先级排序：

1. 多来源、多个独立论文支持；
2. 来自标题、作者关键词、数据库受控字段；
3. 同一概念组的稳定共现；
4. 单篇摘要短语；
5. 只有模型提出、没有论文证据。

排序只是筛选人工工作量，不能改变边状态。

### 6.3 阶段 C：前沿选择

每轮只选择一个变量组或一个 discovery channel：

```text
Round 0：冻结基线 concept graph
Round 1：测试一个 lexical variant edge
Round 2：测试一个 broader/narrower edge
Round 3：测试一个 task-related edge
Round 4：测试一个 alternative_method edge
Round 5：测试一个独立 discovery channel
```

一轮禁止同时改变：

- 多个 concept group；
- query 词法、任务词、方法词和日期过滤器；
- 数据库与排序策略；
- Provider channel 和检索词；
- 人工标签规则和 test reference set。

### 6.4 阶段 D：人工审阅与采用

审阅页面展示：

- 研究范围的中性条件；
- 论文标题、作者、年份、摘要、必要标识；
- 原始数据库关键词；
- 词/边的 evidence excerpt 和定位；
- 不展示策略身份、候选收益、模型判断和当前比较槽位。

审阅后产生：

```text
candidate edge → approved / rejected / pending / conflicted
```

只有显式 `adopt-keywords` 或未来等价的 `adopt-edge` 动作，才会生成新的 case/query version。采用必须记录：

- parent case/version；
- adopted edge IDs；
- changed concept group；
- rationale；
- evidence IDs；
- expected risk；
- rollback target。

### 6.5 阶段 E：单变量检索实验

实验结果必须连接回网络：

```text
edge/query version
  → provider/channel
  → request log
  → returned/fetched/deduplicated IDs
  → new IDs
  → human labels
  → confirmed new relevant IDs
  → retain/rollback/pending
```

没有人工标签时：

- `new_ids` 可以记录；
- `confirmed_new_relevant_ids` 使用 `null` 表示尚未完成/未知，使用 `[]` 表示已完成审阅但确认新增为零；
- `new_relevance_complete` 必须明确标记是否完成全量审阅；
- 不把新增 ID 数称为新增相关论文；
- 不改变 active version。

## 7. 网络探索策略

### 7.1 不做“全图遍历”，做受约束前沿搜索

关键词网络会快速膨胀，建议维护三种集合：

```text
active frontier      当前最值得人工审阅/测试的边
held-out frontier    已发现但暂不进入本轮的边
retired frontier     被拒绝、回退或证明低收益的边
```

每次前沿选择使用可解释的优先级分数，但只用于排序：

```text
priority =
  evidence_strength
  × source_diversity
  × paper_diversity
  × omission_signal
  × task_relevance_hint
  ÷ review_cost
  ÷ semantic_drift_risk
```

建议分数拆开保存，不只存一个总分。

### 7.2 四类搜索动作

| 动作 | 目的 | 默认结果 |
|---|---|---|
| `expand_variant` | 测试拼写、缩写、词形变体 | 独立检索式，不自动合并 |
| `expand_scope` | 探索上位/下位概念 | 单独 branch，不并入主查询 |
| `expand_task` | 发现近邻任务 | `related_task` 候选 |
| `expand_discovery` | 从推荐/引文/参考文献找漏检 | 独立来源记录 |

`expand_scope`、`expand_task` 和 `expand_discovery` 默认不能作为 `equivalent_to` 使用。

### 7.3 停止条件

当满足任一条件时暂停网络扩展，转人工或 P4：

- 连续两轮没有人工确认新增相关论文；
- 新边大部分只有单篇摘要支持；
- 候选前沿超过人工预算；
- 语义漂移超过阈值；
- 新来源增加论文数量但不增加独立概念/相关证据；
- P@K 下降或丢失已有确认相关论文；
- P2 Provider 失败率/429/成本超过预算；
- 进入 test split 后不允许再用结果反向扩词。

## 8. 评价体系

### 8.1 网络本身的结构指标

这些指标只描述网络结构，不代表检索效果：

- `observed_term_count`：原始观察词数；
- `candidate_node_count`：候选节点数；
- `reviewed_edge_count`：已审阅边数；
- `approved_edge_count`：确认边数；
- `conflict_edge_count`：冲突边数；
- `source_diversity`：支持节点/边的独立来源数量；
- `paper_diversity`：支持节点/边的独立论文数量；
- `orphan_node_count`：只有一个未核验来源的节点数；
- `retired_edge_count`：回退/拒绝边数；
- `frontier_size`：当前待审前沿规模。

### 8.2 检索效果指标

继续使用现有 `evaluate_retrieval` / `benchmark.run_benchmark`：

- `Recall@K`：只在独立 test reference set 存在时计算；
- `P@K`：前 K 全部有人类 decisive 标签且确有 K 个结果时计算；
- `judged_precision`：仅描述已审子集，不冒充 P@K；
- `confirmed_new_relevant_count`：只计人工确认 relevant 的新增；
- `cost_per_incremental_confirmed_relevant_usd`：候选组全部已知成本 / 确认新增相关数；
- `screening_minutes`：所有来源已知时才求和。

### 8.3 网络驱动的附加指标

| 指标 | 定义 | 使用边界 |
|---|---|---|
| `edge_test_yield` | 经该边测试并人工确认的新增相关数 | 不是单词因果收益，归因到 edge/query version |
| `frontier_review_burden` | 每轮需人工查看的候选节点/边数 | 反映可维护性，不是效果指标 |
| `concept_coverage_gain` | 新增且确认属于冻结概念范围的节点/边数 | 需要人工标签和固定 reference |
| `semantic_drift_rate` | 候选结果中偏离冻结范围的比例 | 需要人工定义分母，不能由模型自报；第一版默认阈值 0.6，达到阈值即停止并回退 |
| `cross_provider_complementarity` | 一来源未发现、另一来源发现且人工确认相关的数量 | 只在来源和 channel 独立时使用 |
| `graph_stability` | 相同输入/快照重建后的节点/边 ID 一致性 | 用于工程复现，不等同研究稳定性 |

## 9. 防止知识网络污染

### 9.1 证据隔离

每条边至少保留：

```text
source_type
source_url
retrieved_at
source_level A/B/C/U（每条证据一个等级；多来源时拆成多条 evidence，不写复合值）
evidence_status
paper_ids
run_ids
query_version
review_event_ids
```

没有原始证据的模型生成词只能是 `unverified_candidate`，不能进入 approved graph。

### 9.2 Discovery/Test 隔离

- discovery 发现的词可进入候选前沿；
- test 论文、test reference set 和 test 人工标签不能用于扩词；
- 一旦 test 泄漏，当前 case 降级为 discovery，重新冻结 test；
- 变更 reference set、标签集或纳入标准时建立新 manifest，不回写旧实验。

### 9.3 同义词误合并控制

以下情况不能自动合并：

- 同标题但 DOI/PMID 冲突；
- DOI 相同但标题和作者明显冲突；
- 一个词是上位概念，另一个词是具体应用；
- 一个词是方法，一个词是任务；
- 一个词只在 recommendation 中出现；
- 只有 embedding 相似，没有来源字段证据。

### 9.4 时间与版本控制

网络是有时间的：

- 节点和边带 `created_at` / `updated_at`；
- 每次生成保存输入 package manifest hash；
- 每个 adopted edge 绑定 case/version；
- 不能用新来源的定义修改旧历史边而不留事件；
- 旧边只能 `retired`，不能删除。

## 10. 分阶段落地后的文件与模块

### 第一批：只读网络构建

新增建议：

```text
scripts/research_search/keyword_network.py
scripts/research_search/network_scoring.py
schemas/keyword-network-node.schema.json
schemas/keyword-network-edge.schema.json
schemas/keyword-observation.schema.json
tests/test_keyword_network.py
```

第一批只读已有 package，不执行网络，不改变 query。

### 第二批：前沿和审阅接入

- 将现有 `review_workbench.py` 扩展为 edge review 模式；
- `reviewed-keywords.json` 与 `edges.jsonl` 双向链接；
- 增加 `candidate-frontier.json`；
- 不把节点中心性直接显示成预期收益；
- 导入审阅结果时保留 reviewer 原始意见和 conflict/pending。

### 第三批：显式采用与单变量实验

公开接口：

```python
adopt_edge(case: dict, network: dict, *, edge_id: str, output_path: Path) -> dict
record_network_experiment(network_path: Path, experiment: dict, output_dir: Path) -> dict
```

`adopt_edge` 输入必须是 `status=approved` 的边，输出一个新 case，不覆盖源 case；输出至少包含 `parent_case_id`、`parent_version`、`changed_group`、`adopted_edge_ids`、`evidence_ids`、`rollback_target`。若边无法映射到唯一 concept group，拒绝采用。

`record_network_experiment` 接收 query_version、provider/channel、request count、paper IDs、human labels、cost 和 screening minutes，输出 `tested_in` 边及 retain/rollback/pending 决定；不执行网络。

- `adopt-keywords` 扩展为 `adopt-edge`；
- 自动生成新 case 的 concept group 版本；
- 强制 parent version、changed group、evidence IDs、rollback target；
- 复用现有 `optimization_session.py` 做 retain/rollback/pending。

### 第四批：P2 多源和 discovery 反馈

- 将 ProviderResult 的 channel、MeSH、推荐、citation、reference 接入观察层；
- 统一跨源 paper/source record；
- 失败来源仍进入覆盖账本；
- 不把推荐关系写成 citation edge。

### 第五批：P4 冻结评测

- 对四个领域分别冻结 discovery/test；
- 从网络中导出 test 期间禁止修改的 query versions；
- 由两名审阅者独立标注；
- 通过 `prepare_p4_review` 生成 benchmark manifest；
- 最后由 `run_benchmark` 计算正式指标。

## 11. 第一版完成定义

关键词知识网络第一版只有满足以下条件才算完成：

- 同一 package 重建得到稳定 node/edge IDs；
- 每个观察节点能追溯到论文字段、来源和 run；
- candidate 与 reviewed/adopted 状态严格分开；
- 至少支持 `observed_in`、`cooccurs_with`、`equivalent_to`、`broader_than`、`narrower_than`、`related_task`、`alternative_method`、`retrieved_by`、`discovered_by`；
- 不会把候选词自动写入 query case；
- 显式采用后只改变一个 concept group；
- 能通过现有 review workbench 审阅节点/边；
- 能把 edge test 连接到 request、paper、human judgment、retain/rollback；
- 失败 Provider 和未知指标不被静默当作零；
- 全部输出有 manifest/hash；
- 没有独立真值时，报告明确写 `not_proven_complete`，不宣称完整召回或策略优势。

## 12. 结论

这个思路值得做，但真正有价值的不是“建立一个很大的关键词图”，而是建立一个**能解释每个词为什么存在、能被人审、能被单变量测试、能被回退的检索知识网络**。

最小正确闭环是：

```text
论文字段观察
  → 证据节点
  → 候选关系边
  → 人工审阅
  → 显式采用
  → 单变量检索
  → 人工确认新增
  → 保留/回退
  → 网络版本化
```

只要坚持这条链，关键词网络会从“词表”升级为真正有研究价值的检索基础设施；如果跳过审阅和版本边界，它很快会退化成高频噪声和自我强化的伪知识图谱。
