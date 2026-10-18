# 方法规范与二级工具调研

**获取日期：2026-10-17。**本稿仅核对公开官方页面/原始摘要；没有登录、付费、账号访问、浏览器操作、产品功能接口调用或实际产品检索实验。

## 方法规范

### PRESS 2015
PubMed 原始摘要确认，PRESS 2015 用于系统综述、卫生技术评估等证据综合中的电子检索策略同行评审；共保留六个检查维度：**研究问题翻译；布尔与邻近运算符；主题词；文本词检索；拼写、语法与检索行号；限制条件与过滤器**。原摘要还说明，原第七项“将策略熟练翻译到其他数据库”被移除，交由检索者自行决定。[PubMed 原始摘要](https://pubmed.ncbi.nlm.nih.gov/27005575/?format=pubmed)

边界：本次读到的是 PubMed 官方摘要，出版社全文未打开；因此只确认上述维度，不声称已核对 PRESS 全部附件和实施细则。**工程借鉴：**P0 可把六维做成人工复核清单，记录问题翻译、运算符、主题词/文本词、语法行号、限制与过滤器；不能把“通过清单”写成召回率保证。

### PRISMA-S
PRISMA-S 是检索报告规范，不是检索器或召回率评测。官方页确认其 2021 年发布、含 **16 个报告条目**：[PRISMA-Search](https://www.prisma-statement.org/prisma-search)。原始表格逐项列出：数据库/平台、多库检索、研究注册库、在线或印刷资源、引文检索、联系作者/专家、其他方法；逐库逐源原样检索式；限制及理由、过滤器、复用既有策略、更新方法、最后检索日期；同行评审；各来源记录总数与去重软件/流程。[PRISMA-S Table 1](https://link.springer.com/article/10.1186/s13643-020-01542-z/tables/1)

**工程借鉴：**P0 的三类查询都应保存数据库/平台、原始字符串、时间、限制、记录数和去重信息，避免把“生成查询”误写成“完成可复现检索”。

### AHRQ 工具综述
待核对报告为《Systematic Review Search Strategy Development Tools: A Practical Guide for Expert Searchers》。给定入口 [NCBI Bookshelf NBK612666](https://www.ncbi.nlm.nih.gov/books/NBK612666/) 触发 reCAPTCHA，打印/阅读变体也未取得正文；未找到可读的 AHRQ 官方平行正文。因此“筛选 102 个工具、评估 21 个工具”及其 2025 年报告背景**均未核验**，只能保留线索，不能作为 P0 选型事实。

## 工具能力与借鉴

- **Yale MeSH Analyzer：**官方帮助页称，输入 PMID 后可从 PubMed 取元数据，生成按文章排列的 MeSH 分析网格；可查看 MeSH/副主题词、作者关键词、题名、摘要、期刊，最多 20 篇，支持 HTML 与 Excel，并有 PubMed 书签工具。[Yale Help](https://mesh.med.yale.edu/help) 本次未提交 PMID。**借鉴：**把“种子文献→候选主题词/作者词→来源 PMID/字段”做成证据层，候选词不直接等同最终检索词。
- **Litmaps：**官方帮助页称其依据引文网络推荐文章，并提供 Shared Citations & References（默认）、Common Authors、Similar Text 三种算法；后者基于题名和摘要的语义分析，不用引文/参考文献计算。[官方帮助](https://docs.litmaps.com/en/articles/9029858-search-algorithms-in-litmaps) **借鉴：**引文扩展与语义扩展必须分开记录，推荐结果不能替代可审计引文证据。
- **Connected Papers：**官方页只明确其是用于发现和探索相关论文的可视化工具。[官方页](https://www.connectedpapers.com/about) 本次未生成图，且未从公开入口核验图边定义。**边界：**相似论文图不等于直接引文图，也不等于完整 citing/cited-by 列表。**借鉴：**只能标为探索线索，再用可审计元数据确认关系。
- **2Dsearch：**官方页面称其用二维画布组合 Boolean blocks，支持错误提示/修正建议、面向 Google Scholar 和专业数据库、AI 查询建议，并可导出传统 Boolean 字符串。[官方页](https://www.2dsearch.com/researchers-and-students) 本次未启动应用或跨库实测。**借鉴：**二维结构适合 P0 查询 AST/可视化；“错误修正”不应写成已证明的召回率提升。
- **TERA：**名称、官方域名和原始页面均未确认，保留为未核验线索，不描述功能、不纳入 P0 依赖。

## 声明分类

- **官方声明：**上文产品能力来自相应官网/官方帮助页；PRESS 六维来自 PubMed 官方摘要；PRISMA-S 16 项来自原始论文表格。
- **实际测过：**仅公开网页读取与可读性检查；未提交 PMID、未创建 Litmap/Connected Papers 图、未运行 2Dsearch 查询。
- **工程建议：**记录 URL、日期、输入、输出、错误和证据等级；将 PRESS/PRISMA-S 用作人工审计与报告字段。

## 来源表

等级：A=一手/官方来源，B=可信二手，C=社区线索，U=未核验；等级不代表效果已实测。本会话没有可用 `web_search` 工具；替代搜索页仅用于定位，摘要未作原文证据。NCBI 验证码、PRESS 全文认证/Cloudflare、OSF 维护及 Yale 旧路径 404 均未绕过。

|ID|名称|URL|发布/更新|获取日|类型|等级|读取状态|
|---|---|---|---|---|---|---|---|
|S1|PRESS PubMed|https://pubmed.ncbi.nlm.nih.gov/27005575/?format=pubmed|2016-03摘要/2016-07刊|2026-10-17|官方摘要|A|可读；全文未开|
|S2|PRISMA-Search|https://www.prisma-statement.org/prisma-search|2021|2026-10-17|官方规范页|A|可读|
|S3|PRISMA-S表1|https://link.springer.com/article/10.1186/s13643-020-01542-z/tables/1|2021-01-26|2026-10-17|原始论文表格|A|可读，16项可核对|
|S4|Yale Analyzer Help|https://mesh.med.yale.edu/help|页面版本2026-05-07|2026-10-17|大学官方帮助|A|可读，未提交 PMID|
|S5|Litmaps算法|https://docs.litmaps.com/en/articles/9029858-search-algorithms-in-litmaps|2024-12-09|2026-10-17|官方帮助|A|可读，未登录|
|S6|Connected Papers|https://www.connectedpapers.com/about|—|2026-10-17|官方产品页|A|入口可读，算法未核验|
|S7|2Dsearch|https://www.2dsearch.com/researchers-and-students|—|2026-10-17|官方产品页|A|可读，未启动|
|S8|AHRQ/NBK612666|https://www.ncbi.nlm.nih.gov/books/NBK612666/|题名所称2025未核验|2026-10-17|政府书架入口|U|reCAPTCHA；102/21未核验|
|S9|TERA|未确认|—|2026-10-17|待定位线索|U|官方域名未确认|

## 应修改的夸大/不确定陈述

1. “PRESS 六维已核验”应改为“PubMed 摘要确认六维，附件细则待全文核对”；
2. “102 个筛选、21 个评估”在 AHRQ 正文可读前不得写成事实；
3. Connected Papers 的“引文图/直接引用关系”应改为“相似性探索图”；
4. Litmaps、Yale、2Dsearch 的效果不能写成已实测或已证明提升；
5. TERA 只能保留为未核验线索。
