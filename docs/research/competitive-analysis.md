# 竞品分析与 P0 选型决策

日期：2026-10-17。方法：优先官方文档、官方仓库、原始方法摘要；本轮没有购买订阅、登录竞品或测其真实召回率。数据库搜索调用属于本项目接口检查，不等于竞品效果对照。

## 结论

**采用 Agent Skill + Python 确定性脚本 + OpenAlex Works，不复制 SaaS 平台，不把关键词数量作为价值。** P0 的核心产物是可追溯检索包；真正的差异化假设是：在同等请求和筛选成本下，通过证据和审计减少错误归并、未知限制和伪指标。这个假设仍需独立人工标注集验证。

## 同类能力比较

| 工具/类别 | 已读取来源能支持的能力 | 借鉴与复用 | 本项目不作的推断 |
|---|---|---|---|
| litsearchr（直接方法竞品） | 标题/摘要抽取，结合作者及数据库词，关键词共现网络，概念分组和布尔搜索 | 借鉴文本反向发现、共现统计、已知文献检查思路；P0原创Python实现，不复制上游R源码 | 不声称我们的统计方法等同litsearchr算法，不复述未读论文的效果数字 |
| OpenAlex（底座） | Works词法/布尔检索、标签、主题；语义端点和/text在文档中存在 | P0只调用Works；保留原始响应，标签与文本词分开 | 文档存在不等于本版实现；搜索排名不等于相关性真值 |
| Scite（证据发现） | 元数据与全文引文语句搜索、Smart Citations、REST/MCP | 借鉴句级证据与引用语境的可审计性 | 未核验2026年5月布尔生成上线日期，不承诺其效果、费用或全库访问 |
| Elicit（语义/研究流程） | Research Agent、Report、Systematic Review三类工作流；官方说明2026-09-30整合旧工具 | 区分探索与严格综述准备；输出应能迭代而非一次聊天 | 不把产品宣传准确率写成本地能力，不与其付费流程做未发生的性能比较 |
| ResearchRabbit（关系探索） | 官方指南入口包含搜索发现、文献合集、工作流等栏目 | 把种子/关系探索列为独立未来通道 | 未实测算法/收录范围；不称推荐列表为完整检索 |
| Yale MeSH Analyzer（专科术语） | PMID元数据的MeSH网格、作者词、标题摘要查看 | P2采用受控词+自由词双轨，保留字段来源 | P0没有医学数据库接入，不称数据库标签为MeSH |
| Litmaps（多通道探索） | Shared Citations & References、Common Authors、Similar Text；后者不使用引文计算 | 将引文、共同作者、语义通道分别记录 | 不混称所有边为引用关系 |
| Connected Papers | 官方说明是相关论文可视化探索 | 输出探索线索再用源元数据核验 | 未核验图边定义，不当作直接引文图 |
| 2Dsearch（表达式编排） | 二维Boolean blocks、错误提示、AI建议、导出 | 概念组AST先于字符串；人工审查结构 | 不把本地结构检查当远端数据库语法或召回率验证 |
| TERA | 本次官方身份尚未确认 | 仅线索，不接入 | 不根据名称推断功能 |

主要来源：[litsearchr README](https://raw.githubusercontent.com/elizagrames/litsearchr/main/README.md)、[OpenAlex Search](https://help.openalex.org/api/searching/)、[Scite Introduction](https://docs.scite.ai/introduction.md)、[Elicit 官方流程](https://support.elicit.com/en/articles/14757543-getting-started-with-elicit-which-workflow-should-i-use)、[ResearchRabbit 指南](https://learn.researchrabbit.ai/en/)。辅助工具和标准的逐项原始URL见[补充调研](methods-and-secondary-tools.md)。

## 四项实施决策

1. **复用索引，不自建搜索引擎。** OpenAlex返回机器标签，不能冒充作者关键词、专业术语真值或人工相关性判断。P0以原文片段和字段为证据，只自动完成可确定的计数与清洗。
2. **AST先行，限制语法子集。** 概念组内OR、组间AND；方法仅作用于方法分支。P0拒绝未经支持的运算符或限制，不静默丢失语义。复杂近邻、NOT、截断、跨库转换后续再独立验证。
3. **Skill处理语义，脚本处理事实。** 中文意图、同义关系及术语维度由宿主Agent显式给出；Python不假装能凭规则自动理解任意科研方向。提取短语先处于unclassified，不自动塞进正式查询。
4. **可审计优先于全自动。** 同时保存计划、执行、结果、失败、原始快照、证据、标注和哈希。支持离线重放，但重放不计为新网络实验。

## 接口及成本边界

[OpenAlex认证文档](https://help.openalex.org/api/authentication.md)说明基础匿名调用可用，免费Key提高额度；游标翻页超过首个页面需要Key。P0默认匿名、小页数和总HTTP尝试上限；不从环境自动消费账户额度。用户主动启用Key时才读取环境变量。

[Aboutness文档](https://help.openalex.org/api/tag-aboutness/)另列/text的文本长度、速率和按次成本。因此P0不调用/text，也不调用search.semantic/rerank。Works本身也受预算和规则约束，不能以“不调用/text”推导“所有搜索无限免费”。价格和额度不硬编码成长期事实。

搜索索引和当前官方[Keywords文本页](https://help.openalex.org/data/keywords.md)可能呈现不同版本的数量与算法说明；本项目不依赖词表规模或模型名称，仅保存记录实际返回的ID、字段和时间。

## 原附件纠错台账

| 原说法 | 本轮证据状态 | 执行处置 |
|---|---|---|
| AHRQ 2025筛选102个、评估21个 | NCBI入口遇验证码，未核验正文 | 保留线索，不用于定量论证 |
| litsearchr论文具体节省时间/召回效果 | 仓库可读，出版社正文被拦截 | 只采用方法定位，不挪用实验数字 |
| OpenAlex关键词约190万 | 当前文本页有类似声明，索引存在版本差异 | 无需作为P0验收；以实际记录为准 |
| Scite 2026-05布尔生成 | 原博客本轮403，当前API页只支持现有检索能力说明 | 上线日期待核验 |
| Elicit旧流程合并 | 官方帮助说明2026-09-30 | 可报告官方流程变化，不推断质量提升 |
| 相似图=引文图 | 没有该等价证据 | 语义与引用关系分开 |
| 自动停止=完整覆盖 | 工程规则不能证明穷尽 | P1仅报告停止原因，保留覆盖限制 |

## 尚缺的效果证据

四类主题（成熟、新兴、交叉、医学）与A/B/C/D对照是计划，不是本轮已做实验。当前可以完成的是工程、接口和单提示词流程比较；真实Precision/Recall提升需额外收集独立人工标注集。没有它时，不以候选数量或单个示例替代性能证据。
