# P4：多领域质量基准与人工审阅协议

版本：0.1；日期：2026-10-18。范围仅限离线评测和人工审阅交接，不含新联网检索、密钥、付费、账号、浏览器、前端或服务化。

## 1. 结果边界与 case 索引

公开入口是 `research_search.benchmark.run_benchmark(manifest: dict, output_dir: pathlib.Path) -> dict`。它汇总调用者已持有的观察记录，不执行检索，也不把输入中的 `live` 声明当作本次重新验证的事实。今日已有接口记录若需纳入，必须由协调人从其实际产物逐项导入；此协议和四个 case 不补造这些运行。

| 分层 | 预设范围 fixture | 当前真值状态 |
|---|---|---|
| mature | [`p4-mature-semg-joint-angle.json`](../../evals/cases/p4-mature-semg-joint-angle.json) | 人工真值未提供 |
| emerging | [`p4-emerging-vision-language-action.json`](../../evals/cases/p4-emerging-vision-language-action.json) | 人工真值未提供 |
| interdisciplinary | [`p4-interdisciplinary-urban-heat.json`](../../evals/cases/p4-interdisciplinary-urban-heat.json) | 人工真值未提供 |
| medical | [`p4-medical-chest-radiograph-pneumonia.json`](../../evals/cases/p4-medical-chest-radiograph-pneumonia.json) | 人工真值未提供 |

这四个文件沿用现有 `research-case.schema.json`，包含完整研究范围、候选概念组、`independent_relevance_set: null` 和空 `judgments`。它们是**四类范围计划**，不是四次实际实验，也不是已经建立的独立测试集。分层是预设用途，不是对研究成熟度的量化结论。概念组必须经过人工审阅，不能把不同范围词仅因同组就视为经验证同义词。

A/B/C/D 是比较槽位，不是产品或质量等级。建议预注册：A=冻结基线，B=受控词法改进，C=独立发现通道，D=明确记录的融合策略；具体含义写入 `source_explanation`，不要在看完结果后更改 A。多个来源可属于同一槽位；同一 case、baseline、mode 的记录按来源汇成一组，组内输入顺序决定去重后排名。重复策略版本、重复历史试验不能塞在同一组，应单独建基准 manifest。

## 2. 公开 API 输入契约

输入是普通 JSON 可表达的 dict，不接收文件路径代替 dict。不扩展现有 Schema；以下是本模块自己的严格 0.1 契约。未知字段、错误类型、布尔冒充数字、负数、NaN/Infinity、非法枚举都报 `ValueError`，且校验失败前不创建输出。

### 顶层

| 字段 | 类型 / 默认 | 语义 |
|---|---|---|
| `cases` | 非空数组，必填 | 实际提交评测的 case；允许某个 case 的 runs 为空 |
| `schema_version` | 可选，只能 `"0.1"` | 接口版本 |
| `benchmark_id`, `notes` | 可选非空单行字符串 | 标识和说明 |
| `k` | 正整数，默认 20 | 对去重排名取前 K |
| `comparison_baseline_id` | A/B/C/D，默认 A | 只与同 case、同 mode 的成功锚点比较 |
| `planned_case_count`, `planned_run_count` | 非负整数或 null，可省略 | 预计划数，不回填成实际数 |
| `theoretical_search_space_size` | 非负整数或 null，可省略 | 理论搜索空间，不是运行次数 |
| `historical_run_count` | 非负整数或 null，可省略 | 历史运行数，不并入本批新增执行数 |
| `retained_configuration_count` | 非负整数或 null，可省略 | 已保留配置的外部登记，不自动等同成功数 |
| `training_seed_ids`, `test_reference_ids` | 可选、唯一非空字符串数组，默认 [] | 全局泄漏检查；仅给 ID 不形成真值 |

### 每个 case

| 字段 | 类型 / 要求 |
|---|---|
| `case_id` | 必填、全局唯一；1–128 字符，只含 ASCII 字母数字、点、下划线、连字符，首字符为字母或数字 |
| `domain_kind` | 必填：mature / emerging / interdisciplinary / medical |
| `split` | 必填：discovery / test |
| `reference_set` | 必填：唯一 ID 数组或 null；空数组不产生 Recall |
| `human_judgments` | 必填：`{paper_id: label}`，允许 `{}`，不接收 ID 数组 |
| `model_judgments` | 可选同形映射，默认 `{}`；独立保留，永不替代人工或参考集 |
| `runs` | 必填数组，允许 []，见下表 |
| `reference_set_independent` | 可选 boolean，默认 false；仅独立 test 参考集可置 true |
| `reference_set_source` | 独立声明为 true 时必填非空单行来源说明，记录参考集出处、冻结日期和人工确认路径 |
| `training_seed_ids`, `test_reference_ids`, `existing_catalog_ids` | 可选唯一 ID 数组，默认 []；最后一个表示开始比较前已经持有的目录 |
| `case_fixture` | 可选安全相对 POSIX 路径，仅留作来源定位，函数不打开它 |
| `notes` | 可选非空单行字符串 |

**人工最少分类：**`relevant`=相关；`irrelevant`=不相关；`pending`=待审/证据不足。为兼容现有 evaluator，`uncertain` 作为待审别名接受，计算时归一为 `uncertain`，原输入仍保留。缺失键也表示未审阅。模型映射使用相同枚举，但只作独立线索。没有人工标签时，模型即使给出全量“相关”也不能计算 P@K 或确认新增相关收益。

独立参考集须在策略迭代前由独立来源与人工筛选冻结，不能从本批候选结果自我构建。只有 `split=test`、`reference_set_independent=true`、存在 `reference_set_source` 才启用 Recall。仅给 `reference_set` 或 `test_reference_ids` 不足以声明独立，也不会自动生成人工判断。与独立参考集中 ID 相冲突的 `irrelevant`/待审人工标签会报错，应先仲裁。独立性声明无法由此函数证明，协调人必须保留外部证据。

**隔离检查：**全局及逐 case 的 `training_seed_ids`、discovery 的 reference_set 合并为训练侧；全局及逐 case 的 `test_reference_ids`、test 的 reference_set 合并为测试侧。两侧任一 ID 交叉即报错，包括跨 case 交叉。`test_reference_ids` 只用于泄漏审计，不会暗中扩充 reference_set。必须先做好跨库规范 ID 和别名去重；此 API 不能识别两个不同字符串实际上是同一篇论文，也不能检测未登记的训练使用。

### 每条来源 run

| 字段 | 类型 / 要求 |
|---|---|
| `baseline_id` | 必填：A/B/C/D |
| `status` | 必填：success / partial / failed / not_executed / planned |
| `mode` | 必填：live / replay / synthetic；planned 是 status，不是 mode |
| `paper_ids` | 必填非空字符串数组，数组本身可空；重复 ID 接受但不会增益 |
| `request_count` | 必填非负整数；只记本批新增请求，离线模式必须为 0 |
| `fetched_count` | 必填非负整数；实际取得的记录数，不是库端 total_count |
| `deduplicated_count` | 必填非负整数；必须等于本条 paper_ids 的唯一数，且不超过 fetched_count |
| `source_explanation` | 必填非空单行字符串；说明输入 provenance、运行/快照、基线定义、排序依据及必要限制 |
| `reported_count` | 可选非负整数或 null；原库 total_count，默认 null，不是跨库唯一文献数 |
| `estimated_cost_usd`, `screening_minutes` | 可选有限非负数字或 null，默认 null；未知不是免费或零时间 |
| `run_id`, `database`, `source_type`, `retrieved_at`, `query`, `error_type`, `error_message` | 可选非空单行字符串；run_id 若提供须在 case 内唯一；日期字符串仅留存，未进行日期解析 |
| `source_url` | 可选 HTTP(S) URL 或 null；不接受用户名/密码，不发起请求；不要输入 token 或签名参数 |
| `raw_path` | 可选安全相对 POSIX 路径或 null；不打开、不拼接、不复制原始文件 |
| `evidence_level` | 可选 A/B/C/U；来源级别不构成效果证明 |

`planned`/`not_executed` 的三个计数字段必须明确为 0，不能携带非零已发生成本或筛选时间。`live + success` 至少记录 1 次请求。`failed` 可保留实际请求、部分抓取和费用，方便审计，但不因此产生成功或收益。来源组包含不同状态时总状态为 partial；任何非全 success 组保留观察记录但不计算质量或增量。这里采取保守分母，不自动把部分成功提升为完整基准。

`raw_path`/`case_fixture` 不允许绝对路径、Windows 驱动器、反斜杠、空路径分段、`.`/`..` 或冒号。字段是定位说明，不表示原始文件已核验。API 不扫描密钥；调用方不得把密钥、个人敏感信息或完整私有 URL 写进任何输入。

## 3. 调用与四个输出

无需联网的最小计划调用（无论文、无真值、无实际执行）：

```python
from pathlib import Path
from research_search.benchmark import run_benchmark

manifest = {
    "schema_version": "0.1",
    "planned_case_count": 4,
    "planned_run_count": 16,
    "cases": [{
        "case_id": "p4-mature-semg-joint-angle",
        "domain_kind": "mature",
        "split": "discovery",
        "case_fixture": "evals/cases/p4-mature-semg-joint-angle.json",
        "reference_set": None,
        "human_judgments": {},
        "model_judgments": {},
        "runs": [],
    }],
}
report = run_benchmark(manifest, Path("artifacts/p4-plan-review-001"))
# actual_case_count == 1；actual_executed_case_count == 0；不是四次实验。
```

`output_dir` 必须为 `Path`，且是尚不存在的具体目录；已有空目录也拒绝覆盖。路径中 `..` 或已有符号链接组件会被拒绝。校验及序列化完成后才创建目录，固定文件名且以独占方式写入。I/O 中断可能留下不完整目录；没有完成的哈希清单不能当完整交付，重试应选新目录，不覆盖旧目录。没有网络访问、输入路径读取或 CLI 注册副作用。

| 输出 | 内容 |
|---|---|
| `benchmark.json` | 与返回 dict 相同；含原输入快照、规范输入 SHA-256、计划数/实际数、分 mode 账本、逐 case/来源组指标及 source_records |
| `benchmark.md` | 中文摘要、计划/执行区别、分模式账本、逐 case/baseline/mode 比较和单来源 reported_count |
| `review-queue.jsonl` | 所有观察 ID 的待人工审阅池，case 内去重；不含 baseline、mode、模型标签、策略或排序分值；可能为空文件 |
| `manifest.jsonsha256` | JSON 格式 SHA-256 清单，覆盖上面三个文件，`status=completed`；不自我哈希 |

输入哈希是 `json.dumps(input, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)` 的 UTF-8 SHA-256。输出哈希覆盖实际 UTF-8 字节（LF 换行），大小写十六进制为小写。输入不被修改。同一输入的重排对象键不改变输入哈希；数组次序会改变排名和哈希。清单仅检测内容一致性，不提供作者认证，也不证明输入是真的 live 记录。

## 4. 指标及计数纪律

1. **调用既有指标：**使用 `evaluate_retrieval` 计算去重后前 K 指标，使用 `compare_retrieval` 计算相对锚点新增，归因层级为策略版本而非单个词。若 helper 在“存在标签字典但 top-K 没有任何可判定人工标签”时返回 0，基准将该 `relevant_found` 恢复为 null，避免未知冒充测得的零。
2. **total/new unique：**`total_unique_count` 是全成功来源组的 ID 并集大小，不是原库 reported_count。候选 `new_unique_ids` 相对同 mode 成功锚点与 `existing_catalog_ids` 的并集计算；锚点对自身新增为 0。缺少锚点、非成功组、不同 mode 不产生可比新增值；输出 null 而不是假设 0。
3. **库端数量：**单来源 `reported_count` 原样保存；多来源组的单值为 null，并逐来源列在 `reported_counts_by_source`，不将多个库 total_count 相加称为唯一文献。跨来源 canonical ID 不同的重复仍需上游去重。
4. **K 内已知相关：**有独立 test 参考集时报告其命中数；否则只报告 top-K 人工已确认相关命中的下界。前 K 无可判定人工标签且无独立集时为 null。参考命中与人工确认在原指标中分别保留，不能称为“所有相关论文”。
5. **Recall@K：**仅 `独立 test reference_set 命中数 / 该集合大小`；无独立集合、discovery 或空集合为 null。这是参考集召回，不是对全部文献宇宙的完整召回证明。
6. **P@K：**去重后确有 K 个结果，且这 K 个全部有人类 relevant/irrelevant 才计算；缺失/待审不当负例。结果少于 K 时 P@K 为 null，即使全部已审；`precision_at_available` 另列。`judged_precision` 只是已审子集描述，不能代替 P@K。
7. **确认新增及费用：**仅人工 relevant 计入 `confirmed_new_relevant_count`。有新增却无可判定人工标签时为 null；部分审阅时可报告已确认下界，同时 `new_relevance_complete=false`、单列未审数量。`cost_per_incremental_confirmed_relevant_usd = 候选组总已知成本 / 人工确认新增相关数`，不是候选减锚点费用差。任何来源成本未知，或没有确认新增，结果为 null。筛选分钟只在全部来源已知时求和，需确认各来源计时没有重复覆盖。
8. **账本分层：**live/replay/synthetic 各自列登记、执行、成功、失败、partial、未执行与请求。只有 live 的 request_count 进入 `actual_live_request_count`；失败的真实请求仍计资源耗用。success/partial/failed 计已执行；planned/not_executed 不计。`actual_case_count` 是输入 case 数，`actual_executed_case_count` 才是实际有执行记录的 case 数。
9. **不能宣称真实优势：**synthetic 仅工程测试；replay 只有历史观察，不是本次新增实测。`real_advantage_eligible` 只是 live、同 mode 可比、有人类确认新增且所有新增已审的必要门槛，不是统计显著或因果优势认证。顶层 `real_advantage_demonstrated` 保持 false；须完成独立重复与人工审查再另行作结论。
10. **计划与变更分开：**理论搜索空间、历史运行、本批实际执行、保留配置分别保存。目标指标变化应由冻结的同 split、同 K、同标签集、同预算的前后版本比较；不得把词数、理论配置数或已有目录数量写成新增效果。

## 5. 最低人工审阅流程

### 5.1 预注册与隔离

- 协调人先冻结研究范围、纳入/排除标准、K、A/B/C/D 定义、预算、来源日期、排序合并规则和 canonical ID 规则；未指定条件保持 unspecified，不暗加语言、年份、人群或方法限制。
- 分开 discovery（词与策略开发）和 test（冻结后验收）。独立参考集来自另行保留的人工检索、专家整理或可追溯证据综述等，记录原始 URL/文档、日期、筛选人和纳排理由；不能从候选策略当轮输出选择“容易找回”的论文补真值。
- 策略修改后不得回看 test 论文调词；若泄漏，降为 discovery 并重新冻结未接触 test。函数只检查已声明 ID 交叉，不能替代流程隔离。

### 5.2 盲评与最少记录

- 至少汇集各策略 top-K 及全部拟主张的新增 ID；同一论文只给一个盲化材料编号、随机排列，不显示 baseline、策略文本、数据库排名、mode 或模型判断。队列是协调人输入，不是自动完成的随机化审阅包；协调人应离线打乱顺序并附合法取得的题名/摘要/必要全文及冻结范围。
- 每项最少记录：case/scope、规范 paper_id、审阅人匿名 ID、审阅轮次、`relevant/irrelevant/pending`、纳排理由或缺失信息、证据所在字段/页码、来源 URL/定位、来源级别、审阅日期及耗时。仅有论文 ID、数据库关键词或模型推荐不能当“人工相关”。缺摘要/全文不足时标 pending，不强行二分。
- `human_judgments` 只接收协调人已确认的最终标签；本 API 不存审阅者身份、理由、逐轮投票或仲裁历史。详细审阅表必须由现有工作流另行保留并在 source_explanation/reference_set_source 中定位，不新增此任务之外的 schema。
- 最低相关性判断：是否满足冻结的研究对象、输入和任务；有无实质研究证据；不满足哪一项或仍缺什么。方法分支未被明确设为纳入条件时，不能仅因不用某算法判不相关。医学方向另检查研究设计、模态、疾病及诊断定义是否符合范围，不据检索命中推断临床有效性。

### 5.3 双人复核、冲突与抽检

- 独立参考集、拟发布的全部 top-K 及用于确认新增收益的项目，至少两名审阅者独立完成；协调人封存首轮结果后再揭示分歧。低风险其余池可先单人筛查，但不得称为双人金标准。
- 两人一致 relevant/irrelevant 后才进入最终映射。任何分歧、证据缺失或不确定先保留 pending；第三人基于冻结标准仲裁，记录两份原始意见、最终理由和证据。不能以多数模型投票、baseline 身份或期望收益解冲突。
- 对其余单人筛查池做预先指定的分层随机抽检，覆盖四类 case、来源、相关/不相关及边界条目；抽检比例/样本量在开评前登记。观察到系统偏差后扩大到相应分层全量复核，并报告实际抽检数，不追认原计划为已完成。
- 报告已审覆盖率、pending 数、原始一致率与争议数。若计算一致性系数须说明样本与缺失处理；不能从空标签集生成系数。模型判断只能在人工结论封存后揭示，作为独立误差分析，不反写人工首轮标签。

### 5.4 来源等级与版本

沿用本仓库[来源索引](../research/source-index.md)的 A/B/C/U：A=官方/作者/原始论文或原始数据，B=可信机构二手，C=社区线索，U=未核验。每条证据保留 URL、发布日期/更新时间（未知则明确未知）、实际获取日、来源类型、等级、读取状态和局限。等级描述来源，不代表相关性、研究质量或效果已经验证；“有 DOI”不自动成为相关或高质量。

参考集、标签集、查询、来源快照和纳排标准发生变化时另建 manifest 与新输出目录，保留旧哈希；报告新增/改变/失效记录，不用更新后的真值回写旧实验。历史 replay 请求必须为 0；历史真实请求若需说明写来源说明，不能再次计为本批新增请求。

## 6. PRESS / PRISMA-S 逐项指针（不是认证）

以下来源继承仓库在 2026-10-17 的已读记录；本次未联网复核。PRESS 只据官方摘要确认六维，全文附件细则仍未核对。下表是本项目的人工留证建议，不声称逐条符合标准、通过认证或保证召回。

### PRESS 六项

原始摘要：McGowan 等，PRESS 2015，2016 年；官方 PubMed 摘要，A 级，仓库获取 2026-10-17，全文未开：[https://pubmed.ncbi.nlm.nih.gov/27005575/?format=pubmed](https://pubmed.ncbi.nlm.nih.gov/27005575/?format=pubmed)。

| 项 | 人工检查与留证位置 |
|---|---|
| 1 研究问题翻译 | 核对 scope 的对象/输入/任务/方法分支与 concept_groups；记录遗漏、额外限制及范围漂移 |
| 2 布尔与邻近运算符 | 保存逐库原始 query，检查 AND/OR/NOT、括号、邻近语法是否实际受支持；不支持则标明 |
| 3 主题词 | 医学等受控词表逐项核对来源、映射与扩展；没有核验时为待审，不拿主题词替代自由词 |
| 4 文本词 | 核对候选词、词形、拼写变体、宽窄/相关关系与实际论文证据；分开缺词与范围扩张 |
| 5 拼写、语法与行号 | 保存查询版本、分行/行号与库端错误；本地语法检查不写成库端已执行 |
| 6 限制与过滤器 | 保存显式日期/语言等限制与理由；无依据的临床/研究设计过滤器不得默认加入 |

### PRISMA-S 十六项

来源：2021 年官方规范页，A 级，仓库获取 2026-10-17：[https://www.prisma-statement.org/prisma-search](https://www.prisma-statement.org/prisma-search)；原始论文表 1，2021-01-26，A 级，同日获取记录：[https://link.springer.com/article/10.1186/s13643-020-01542-z/tables/1](https://link.springer.com/article/10.1186/s13643-020-01542-z/tables/1)。

| 项 | 本项目审阅/报告指针 |
|---|---|
| 1 数据库名称与平台 | source_records 的 database、source_type、source_url，另留平台版本或未知声明 |
| 2 多库检索 | 记录是否同时检索、所用平台、各库原始记录；本模块只做组内 ID 并集，不伪造跨库唯一总数 |
| 3 研究注册库 | 记录名称、方法、日期与结果；未检索明确“未执行”，不得用文献数据库代替 |
| 4 在线资源与浏览 | 记录资源及实际浏览方法；本次无浏览时标未执行 |
| 5 引文检索 | 记录种子、前向/后向、工具、轮数与真实来源；相似推荐不冒称引文关系 |
| 6 联系作者/专家 | 保存实际联系对象类别、日期与结果；没有联系不记成功 |
| 7 其他方法 | 单列手工检索等实际方法与状态；没有则明确不适用/未执行 |
| 8 完整检索策略 | 各来源原样 query、版本、字段、语法与运行定位；不得只给关键词摘要 |
| 9 限制与理由 | scope.constraints 与人工理由并列；不把系统默认截断当研究纳入标准 |
| 10 检索过滤器 | 记录过滤器文本、出处、版本及修改；未验证的过滤器不能称经验证 |
| 11 复用既有策略 | 记录原始策略引用、改写差异和采用理由；保留 discovery 来源不与 test 混合 |
| 12 更新检索 | 新旧 manifest、上次截止/本次执行日期、增删改失效记录与去重规则；不覆盖旧输出 |
| 13 检索日期 | 逐来源实际 retrieved_at/执行日期；报告生成日不代替最后检索日 |
| 14 同行评审 | 记录 PRESS 检查人、日期、问题、修改及未解决项；未做人工同行评审应直写未做 |
| 15 记录总数 | 各来源 reported_count、实际 fetched_count、失败/未执行、组内 unique 分开；没有总数用 null |
| 16 去重 | 记录软件/版本、canonical ID 与规则、冲突、来源链；本模块只按给定字符串去重，不承诺实体识别 |

## 7. 质量门槛与尚未验证的边界

工程门槛是公开 API 的离线测试和四个 fixture 的 `validate_case` 校验；它们不等于四领域实证验证。四域独立 test 真值、双人标注、真实预算/筛选分钟、公平排序与重复实验尚需实际材料。至少在相同资源预算和冻结标准下观察可复现的确认新增收益、审阅负担与不确定性后，才讨论界面或服务；本次不交付 Web UI，也不据 synthetic/replay 结果决定产品化。

未自动验证：独立参考集的真实独立性；live 声明和来源文件内容；不同字符串论文 ID 的实体等价；参考集是否覆盖研究宇宙；专家资质与盲评执行；耗时是否重复计费；网络、Key、实际 API 成本或临床效果。文件系统异常会原样暴露，输出不是带签名的可信执行证明。
