# Research Search Package

案例：semg-baseline；状态：live_complete。

## 研究边界

- 描述：基于表面肌电预测人体关节角度，想了解 Transformer 和其他方法的研究情况。
- 对象：['人体关节角度']
- 输入：['表面肌电']；任务：['关节角度估计或预测']
- 方法：['Transformer（方法分支，不限制探索检索）']
- 应用：未指定（P0 记录应用上下文，不自动作为过滤条件）
- 约束：{}；未指定：['具体关节', '实时性', '预测时间跨度', '发表日期', '人群']
- 概念分组由宿主 Agent 提供；不做自动语义解析、等价归并或相关性推断。系统检索准备不等于系统综述完成。

## 执行与证据

- 实际新增网络 attempts：3；实际请求策略：3；回放策略：0。
- 去重后论文：14；失败策略：0。数据库总量、抓取量与逐策略去重量分别记录。
- 数据 origin：live_capture。A 级仅表示 API 字段来源可追溯，不证明论文结论、相关性或术语等价。
- 独立相关集只用于参考命中/召回；仅有人类完整标注时才能计算相应 precision。未标注文献不是负例；模型标注单列。
- 原词片段保留大小写与连续文字，可在 Evidence.locator 指向的 Paper 字段定位；共现不代表语义等价。

## 候选审阅（最多 20 条）

标题/摘要的统计 n-gram 不是语义术语。全部候选保持 unclassified、adopted=false；发现词不自动加入查询。

| 候选词（待审） | 来源 | 文档频率 |
|---|---|---:|
| surface electromyography | openalex_keyword | 14 |
| joint | paper_metadata | 12 |
| surface | paper_metadata | 12 |
| electromyography | paper_metadata | 11 |
| surface electromyography | paper_metadata | 11 |
| angles | paper_metadata | 10 |
| joint angles | paper_metadata | 10 |
| signals | paper_metadata | 10 |
| angle | paper_metadata | 9 |
| joint angle | paper_metadata | 9 |
| semg | paper_metadata | 9 |
| model | paper_metadata | 7 |
| prediction | paper_metadata | 7 |
| based | paper_metadata | 6 |
| joint angles | openalex_keyword | 6 |
| muscle | paper_metadata | 6 |
| semg signals | paper_metadata | 6 |
| continuous | paper_metadata | 5 |
| during | paper_metadata | 5 |
| error | paper_metadata | 5 |

## 文件索引

01 研究范围；02 候选词数组；03 三类查询计划数组；04 论文 JSONL；05 逐策略运行 JSONL；06 评测；07 字段证据 JSONL；08 文档频率与共现边；09 去重记录；10 人工/模型标注 JSONL。

`raw/` 保存各已执行/回放策略的原始响应（无响应时为 null）；`input-case.json` 保存输入；`replay-bundle.json`（若有可回放响应）记录捕获来源与时间；`manifest.json` 记录全部文件 SHA-256、内容摘要与完成状态。
