# Research Search Strategy Optimizer

本项目把自然语言科研意图转换为有文献证据支撑、可执行、可追溯、可评估的检索策略。

## 当前阶段

- **P0**：Skill + Python 的基础能力：研究意图契约、OpenAlex 文献元数据检索、候选术语证据记录、三类检索策略、日志和离线评测。
- **已完成代码阶段**：P0 真实 OpenAlex 元数据检索；P1 版本化优化/预算/回退；P2 PubMed/MeSH 与 Semantic Scholar 适配器；P3 合法获取交接与阅读导出；P4 离线多领域评测框架。
- **仍未证明**：检索效果优于基线、完整召回、人工相关性收益、跨库实体等价、全文权限获取和产品化可行性。

## 项目边界

- `research-search-strategy-optimizer/`：符合 Agent Skills 规范的英文技能包入口。
- `docs/research/`：竞品、标准、官方接口和证据索引。
- `docs/plans/`：批准后的设计、完整路线图和 P0 实施计划。
- `schemas/`：模块间结构化数据契约。
- `scripts/research_search/`：确定性 Python 实现。
- `tests/`：离线单元测试和固定样本。
- `evals/`：基线、独立测试集、运行记录和评测报告。
- `assets/`：Research Search Package 输出模板。

## 当前事实边界

OpenAlex 官方文档已核实其 Works 搜索、布尔查询、语义搜索、关键词字段和 `/text` aboutness 接口说明；P0 暂不调用 `/text`，因为该接口文档列出单独的请求频率和按请求收费条件。具体日期、价格、配额和搜索结果数量必须以运行时的官方文档和实际运行记录为准。

竞品分析只记录官方声明、原始研究和实际测试三种不同状态。没有登录或付费产品实测时，不写成已验证的用户体验或性能结论。

## 本地运行

在项目根目录执行 `python3 -m pip install -e .` 后，可运行：

- `python3 -m research_search build-query evals/cases/semg-joint-angle.json`
- `python3 -m research_search evaluate <returned-ids.json> --fetched-count 10 --deduplicated-count 8`
- `python3 -m research_search search-openalex "surface electromyography joint angle" --per-page 1 --max-requests 1`
- `python3 scripts/research-search.py run evals/cases/semg-joint-angle.json --output artifacts/semg-package --candidate-limit 50`
- `python3 -m research_search validate-package artifacts/semg-package`
- `python3 scripts/research-search.py optimize evals/cases/p1-semg-live-loop.json --live --use-api-key --cache-dir .query-cache --max-requests 6 --output artifacts/p1-loop`
- `python3 scripts/research-search.py review-workbench artifacts/p1-loop/round-00 artifacts/p1-loop/round-01 --output artifacts/p1-review-workbench`
- `python3 scripts/research-search.py review-session artifacts/p1-loop --judgments artifacts/p1-review-workbench/judgments.jsonl --output artifacts/p1-loop-reviewed`
- `python3 scripts/research-search.py adopt-keywords evals/cases/semg-joint-angle.json artifacts/p1-loop/round-01/reviewed-keywords.json --group-id input --output artifacts/semg-input-reviewed.json`
- `python3 scripts/research-search.py provider-fusion artifacts/pubmed-result.json artifacts/semantic-scholar-result.json --output artifacts/provider-fusion`
- `python3 scripts/research-search.py provider-search pubmed "surface electromyography joint angle" --output artifacts/pubmed-plan.json`
- `python3 scripts/research-search.py provider-discover citation "DOI:10.3390/s23125404" --output artifacts/citation-plan.json`
- `python3 scripts/research-search.py acquisition-handoff artifacts/p0-live-20261018 --output artifacts/acquisition-queue.json`
- `python3 scripts/research-search.py reading-export artifacts/p0-live-20261018 --output artifacts/reading-export --metadata-format jsonl`
- `python3 scripts/research-search.py benchmark artifacts/p4-real-input-20261018.json --output artifacts/p4-report`
- `python3 scripts/research-search.py rerank-topk artifacts/p0-live-20261018 --strategy focused --output artifacts/jev-rerank-plan`（工作流别名：`jev@typesafe`；无 Key 时安全降级）
- `python3 scripts/research-search.py rerank-topk artifacts/p0-live-20261018 --strategy focused --output artifacts/jev-rerank-live --use-typesafe`

不安装项目时，可直接用 `python3 scripts/research-search.py ...`（仍需 Python 3.11+ 与 jsonschema）；Windows 使用 `py -3 scripts/research-search.py ...`。推荐把依赖安装到项目虚拟环境，而非修改系统 Python。

`run` 默认只生成方案，不访问网络。加 `--snapshots <bundle.json>` 为离线重放；加 `--live --per-page 10 --max-requests 3` 才执行联网检索。默认不使用账户密钥；主动指定 `--use-api-key` 后才读取 OPENALEX_API_KEY。未知费用为 null，匿名请求也受官方免费额度与限流约束。输出目录已存在会拒绝覆盖。执行包会同时写出 `raw-observations.jsonl`、限额排序的 `candidate-terms.json` 和只有明确审阅项的 `reviewed-keywords.json`；候选排序不等于语义批准。

`--cache-dir` 为显式启用的本地脱敏响应缓存；缓存命中不消耗网络请求预算，运行记录分别保存 `api_request_count`、`metadata_bytes` 和 `cache_hit_count`。`review-workbench` 生成完全离线的盲审页面与来源审计队列；`review-session` 使用导出的人工判断在原快照上重评，永不覆盖源会话或新增网络请求。

自包含发布 ZIP 将脚本、Schema 和示例放进同一个英文技能目录，可单独使用。源码的 Skill 入口与根目录脚本是单一来源；不自动注册全局技能或发布公网。

## 计划入口

- [已批准设计](docs/plans/2026-10-17-research-search-strategy-design.md)
- [完整路线图](docs/plans/roadmap.md)
- [P0 实施计划](docs/plans/p0-implementation-plan.md)
- [P1 闭环优化计划](docs/plans/p1-optimization-plan.md)
- [P2 多数据库计划](docs/plans/p2-provider-plan.md)
- [P3 阅读交接计划](docs/plans/p3-reading-handoff.md)
- [P4 质量协议](docs/plans/p4-quality-protocol.md)
- [P0—P4 实际验收记录](docs/plans/p0-p4-live-acceptance-20261018.md)
- [来源与竞品索引](docs/research/source-index.md)
- [研究资料索引页](docs/research/index.html)
