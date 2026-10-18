# 来源与竞品索引

- 调研日期：2026-10-17
- 项目：Research Search Strategy Optimizer
- 说明：本页区分官方声明、原始研究、实际读取状态和工程推断。搜索结果摘要只用于定位，不单独作为事实证据。

## 结论摘要

1. **OpenAlex 适合作为 P0 的元数据检索底座，但不等于完整检索策略优化器。** 官方文档确认 Works 支持文本/关键词搜索、布尔关系、语义搜索和关键词字段；官方 `/text` 文档另列了文本标注端点及其限制。P0 先使用 Works 元数据检索，不调用 `/text`。
2. **litsearchr 证明了“从真实论文文本和关键词共现网络发现候选词”的方法可行。** 它是直接方法竞品，但主要解决半自动检索词选择和布尔式生成，不是本项目完整的对话式审计闭环。
3. **Elicit、ResearchRabbit、Scite 分别代表语义发现、引文/相似关系探索和引文语境/全文证据。** 它们提醒本项目不能只输出同义词列表，但本轮没有登录或付费产品实测。
4. **Agent Skills 规范要求 `SKILL.md` 位于与 `name` 相同的 kebab-case 目录中。** 因此本项目采用中文工作区根目录 + 英文技能包子目录。

## 来源表

| ID | 来源 | URL | 来源类型 | 等级 | 获取/更新信息 | 读取状态 | 项目用途 |
|---|---|---|---|---|---|---|---|
| OA-ABOUTNESS | OpenAlex Tag Aboutness | https://help.openalex.org/api/tag-aboutness/ | 官方 API 文档 | A | 页面标记更新 2026-10-07；获取 2026-10-17 | 已打开 | 记录 `/text`、topics、keywords、文本长度/频率/成本说明；P0 暂不调用 |
| OA-SEARCH | OpenAlex Search | https://help.openalex.org/api/searching/ | 官方 API 文档 | A | 页面标记更新 2026-10-03；获取 2026-10-17 | 已打开 | Works 搜索字段、关键词参与搜索、布尔查询、URL 长度和语义搜索 |
| LIT-REPO | litsearchr README | https://github.com/elizagrames/litsearchr | 官方开源仓库 | A | 获取 2026-10-17 | 已打开 | 关键词抽取、共现网络、概念组和布尔搜索的能力边界 |
| LIT-PAPER | Grames et al. 2019 | https://doi.org/10.1111/2041-210X.13268 | 原始研究论文 | A | 获取 2026-10-17 | 目标页被 Cloudflare challenge 拦截；只保留为待复核链接 | 方法原始论文入口；不得把未读正文数字写成已核验事实 |
| SCITE-DOCS | Scite API Documentation | https://docs.scite.ai/ | 官方 API 文档 | A | 获取 2026-10-17 | 已打开 | 检索、全文引文语境、Smart Citations、API/MCP 接入的官方声明 |
| ELICIT-WF | Elicit workflow guide | https://support.elicit.com/en/articles/14757543-getting-started-with-elicit-which-workflow-should-i-use | 官方帮助中心 | A | 页面更新 2026-09-30；获取 2026-10-17 | 已打开 | Research Agent、Report、Systematic Review 的工作流划分 |
| RR-HOME | ResearchRabbit Guides | https://learn.researchrabbit.ai/en/ | 官方帮助中心 | A | 获取 2026-10-17 | 已打开 | 官方帮助中心存在 Searching & discovery、Collections 等模块；未做产品内实测 |
| SKILL-SPEC | Agent Skills Specification | https://agentskills.io/specification | 官方开放规范 | A | 获取 2026-10-17 | 已打开 | `SKILL.md`、目录名、frontmatter、渐进披露和校验要求 |
| AHRQ | AHRQ/NCBI search strategy tools guide | https://www.ncbi.nlm.nih.gov/books/NBK612666/ | 机构指南入口 | A/B | 获取 2026-10-17 | 页面被 reCAPTCHA challenge 拦截；附件数字未核验 | 作为调研入口；具体筛选数字交由补充调研文件判定 |
| PRESS | PRESS 2015 | https://pubmed.ncbi.nlm.nih.gov/27005575/?format=pubmed | 原始方法摘要 | A | 获取 2026-10-17 | 摘要可读，出版社全文未打开；六维已确认 | 人工复核检索式，不等于召回率保证 |
| PRISMA-S | PRISMA-Search / Table 1 | https://www.prisma-statement.org/prisma-search | 官方规范页 + 原始表格 | A | 获取 2026-10-17 | 16 项可核对 | 记录数据库、检索式、限制、日期、数量和去重 |
| YALE-MESH | Yale MeSH Analyzer | https://mesh.med.yale.edu/help | 大学/图书馆工具 | A | 获取 2026-10-17 | 帮助页可读，未提交 PMID | 从种子论文反向分析主题词和作者词 |
| LITMAPS | Litmaps algorithms | https://docs.litmaps.com/en/articles/9029858-search-algorithms-in-litmaps | 官方帮助 | A | 获取 2026-10-17 | 算法说明可读，未登录/未实测 | 分开记录引文扩展与相似文本 |
| CONNECTED | Connected Papers | https://www.connectedpapers.com/about | 官方产品入口 | A | 获取 2026-10-17 | 入口可读，图边算法未核验 | 只能作为相似性探索线索 |
| 2DSEARCH | 2Dsearch researchers and students | https://www.2dsearch.com/researchers-and-students | 官方产品入口 | A | 获取 2026-10-17 | 页面可读，未启动应用 | 借鉴查询 AST/二维编排，不作效果结论 |
| TERA | TERA | 未确认 | 待定位线索 | U | 获取 2026-10-17 | 官方域名未确认 | 不纳入 P0 依赖 |
| METHODS | 方法规范与二级工具调研 | docs/research/methods-and-secondary-tools.md | 本项目调研记录 | A/B/U 分项 | 2026-10-17 | 已写入；每条有原始 URL 和未核验状态 | PRESS/PRISMA-S/辅助工具边界 |

## 关键能力核验

### OpenAlex

官方文档说明，Works 的 `search` 可以检索标题、摘要、全文和关键词；支持大写 `AND`、`OR`、`NOT`，并提供 `search.semantic`。长布尔式可能受到约 4 KB URL 限制，官方建议拆分请求后在客户端合并。该能力支持 P0 的查询适配和日志设计，但不能自动证明检索完整性。

官方 `/text` 文档说明，文本可被标注为 topics 和 keywords，结果可用于关键词过滤；该页还列出文本长度、请求频率和按请求计费信息。它是重要的后续能力，但 P0 不调用，避免将文本标注费用和元数据检索混为一谈。

### litsearchr

官方仓库将 litsearchr 描述为 R 包：从标题和摘要抽取候选关键词，结合作者/数据库标签，利用关键词共现网络识别重要术语，形成概念组并写出布尔检索式。它还提供去重和跨数据库组装能力。对本项目的借鉴是：把“真实文献反向发现术语”作为独立模块，而不是让 LLM 单独决定全部关键词。

本轮打开原始论文 DOI 时遇到 Cloudflare challenge，因此论文中的具体实验数字、时间节省和比较结论不写进本项目事实表。

### Scite

官方 API 文档把能力分成文献检索、Smart Citations、论文/作者数据和证据数据集，并说明可通过 REST API 或 MCP 接入。它的优势是引文上下文和支持/质疑/提及分类，不等于本项目 P0 要接入的通用元数据检索能力。未登录、未购买、未做接口调用，不能报告实际覆盖、质量或价格体验。

### Elicit

官方帮助文档将入口分为 Research Agent、Research Report 和 Systematic Review。文档说明 Agent 可在一个会话中从找论文到数据提取和综合；Systematic Review 强调检索、筛选、数据提取和 PRISMA 风格报告。借鉴点是把“探索”和“严格系统综述”区分成不同模式；本项目不把 Elicit 的官方功能描述当作本地实现或性能结论。

### ResearchRabbit

官方帮助中心显示其文档分为 Searching & discovery、Collections & Library management 等主题。它适合围绕种子文献进行发现和整理，但本轮没有验证推荐算法、论文数量、图谱覆盖或订阅能力。项目上只借鉴“种子论文/关系扩展是独立通道”，不把推荐列表当作可复现数据库检索。

## 对附件材料的纠偏

- 附件中 OpenAlex 关键词数量、价格和 2026 年更新内容必须以当前官方文档和具体运行记录为准；本索引不复述未逐项核验的数字。
- 附件中 Scite 的 2026 年功能发布时间未在本轮官方 API 文档中核验；本项目只引用当前官方能力页。
- Elicit 的功能合并日期可以由官方帮助文档支持，但其覆盖规模和性能数字不作为本地效果承诺。
- ResearchRabbit、Litmaps、Connected Papers 的论文规模、排序算法和推荐质量未做产品实测，保留为竞品线索而非本项目事实。
- AHRQ 报告的“102 个工具、21 个评估”等数字因入口被验证码拦截，暂不写成已核验事实。
- litsearchr 原始论文正文本轮未能读取；只使用官方仓库 README 和 DOI 入口，不使用搜索摘要中的实验数字。

## 使用规则

- 事实引用必须邻近 URL；来源等级和读取状态随记录保留。
- “官方声明”不等于“本项目已实现”。
- “搜索结果数量”不等于“相关论文数量”。
- 未登录或未执行的产品，只能做能力定位，不做效果、成本和覆盖承诺。
