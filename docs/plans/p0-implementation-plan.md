# P0 实施计划

- 状态：设计已批准，按阶段执行
- 目标：完成一个可运行、可审计、可离线测试的科研检索策略生成 Skill
- 原则：先测试数据契约和确定性函数，再接真实网络；每步都有可检查出口

## 1. 骨架与契约

创建：

- `research-search-strategy-optimizer/SKILL.md`
- `research-search-strategy-optimizer/references/`
- `assets/`（源码模板；发布 ZIP 内打包为技能 assets）
- `schemas/`
- `scripts/research_search/`
- `tests/fixtures/`
- `evals/cases/`、`evals/reports/`

为 ResearchScope、Keyword、Paper、SearchPlan、SearchRun、Judgment 建 JSON Schema。每个 Schema 使用 `schema_version`，并明确必填、可空和枚举值。

完成条件：无空目录；所有计划新增目录都有至少一个当前需要的文件；字段可描述 P0 结果而不依赖 P1。

## 2. 先写离线测试

覆盖：

1. 术语标准化仅处理确定性文本变换，不进行未经授权的语义合并。
2. 论文按 OpenAlex ID、DOI、PMID 和标题指纹去重，冲突保留审计信息。
3. 三类策略输出概念树和查询字符串；未指定方法不强行加入探索策略。
4. 指标计算区分返回数量、获取数量、去重数量、已标记相关数量。
5. 错误响应转换为结构化失败记录，不抛失上下文。
6. 查询长度、空组和非法布尔关系得到可读错误。

完成条件：测试先失败，然后在实现后通过；每个关键失败模式至少有一个固定样本。

## 3. Python 实现

建议模块边界：

- `models.py`：轻量数据类和枚举。
- `keyword_extractor.py`：标题/摘要/作者关键词/数据库标签的确定性提取。
- `keyword_normalizer.py`：大小写、空白、标点、缩写保留规则。
- `paper_deduplicator.py`：稳定标识、标题指纹和冲突记录。
- `query_builder.py`：数据库无关逻辑与 OpenAlex 查询适配。
- `search_evaluator.py`：离线指标和运行差异。
- `openalex_client.py`：超时、重试、预算、日志和响应归档。
- `cli.py`：最小的 fixture/JSON 输入输出入口。

依赖原则：优先标准库；只有真实实现需要时才确认第三方依赖，并在项目 manifest 中固定版本范围。

完成条件：所有模块有公开函数说明、异常可诊断、不会输出凭证；离线测试通过。

## 4. Skill 入口

`SKILL.md` 只写：

- 触发范围：研究关键词、检索式、学术文献发现、研究方向探索等。
- 输入收集：研究描述、明确限制、目标模式、可用来源、成本边界。
- 流程：解析→候选→证据→术语关系→策略→执行→评测→输出。
- 证据和状态约束。
- 失败降级。
- 输出契约。

详细字段和数据库事实放 references，不把主文件写成 API 手册。

完成条件：Skill 文件符合 Agent Skills 规范，正文低于 500 行，所有相对引用可解析。

## 5. 真实 OpenAlex 检查

使用小预算、单一研究问题和明确的 `per-page`：

1. 一次普通 Works 搜索。
2. 一次有布尔关系的 Works 搜索。
3. 一次列表/过滤或单实体查询，视官方文档和运行条件决定。
4. 记录 HTTP 状态、请求参数（去除凭证）、响应摘要、返回数量、实际保存数量和失败原因。

P0 不调用 `/text` aboutness 端点；其官方文档中列出的速率与收费条件单独记入能力矩阵，不算 P0 已使用能力。

完成条件：真实运行记录可复现或明确说明无法复现；任何失败不被隐藏。

## 6. Research Search Package 输出

至少生成：

- `01-research-scope.json`
- `02-keywords.json`
- `03-search-strategies.json`
- `04-papers.jsonl`
- `05-search-runs.jsonl`
- `06-evaluation.json`
- `07-evidence.jsonl`、`08-cooccurrence.json`、`09-deduplication.json`、`10-judgments.jsonl`
- `input-case.json`、实际返回的 `raw/*.json`
- `README.md`、`report.md`、`manifest.json`

必要时同时生成面向人的 Markdown 报告，但结构化文件是事实源。

完成条件：每个论文、术语、查询和运行均能通过 ID 互相定位；来源、日期、状态和限制齐全。

## 7. 评测与收尾

执行并分别报告：

- `pytest` 或项目选定的测试命令：工程正确性。
- Skill lint：入口格式。
- 真实接口 smoke test：只报告实际请求。
- 有 Skill／无 Skill 的一个真实提示词对照：质量差异由人工检查，不能夸大。
- 如没有独立标注集，只生成探索性指标，不生成优越性结论。

收尾检查：

- 交付路径存在且内容为本轮创建/修改版本。
- 无凭证、临时文件、空目录、重复技能入口。
- 路线图的未来阶段没有被写成已完成。
- README、Skill、Schema、代码和测试的边界互相一致。
