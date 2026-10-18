# 独立离线评测

## 正常最终答案

**范围。** 表面肌电为输入，人体关节角度预测/估计为任务，Transformer 是方法兴趣；具体关节、实时性、康复场景、人群、日期和语言均保持开放，不擅自收窄。

**英文词表。** 下列词均来自模型生成，证据等级 U，外部来源尚无、检索测试未执行。
- 输入变体候选：`surface electromyography`、`surface EMG`、`sEMG`、`surface electromyogram`；可暂作同一输入组，但同义关系仍待核验。
- 对象：核心为 `joint angle`；`joint kinematics`、`joint position` 是较宽或相关概念，单独扩展，不冒充同义词。
- 任务：`prediction`、`estimation`、`regression`，作为相关任务分别测试。
- 方法：`Transformer`、`transformer-based`；相关分支为 `self-attention`、`temporal transformer`、`time-series transformer`，不直接等同。

**OpenAlex 分层计划。** 先建逻辑，再转为 `works` 的独立 `search` 请求；以下仅为待核验模板，不是已验证 API 语法或运行结果。
- 宽范围，INPUT AND OBJECT：`surface electromyography joint angle`；另测输入变体和 `joint kinematics` 分支，不加方法词。
- 任务聚焦，增加 TASK：`surface EMG joint angle estimation`；将任务词分别换成 `prediction`、`regression`，保留独立版本。
- 方法限定，再加 METHOD：`surface EMG joint angle prediction Transformer`；另测 `transformer-based`，相关注意力方法另列分支。

不要把独立变体拼成未经验证的括号/OR 表达式。当前无 API Key，不假定匿名访问一定可用；以后联网前核对官方接口、认证与配额，本次不申请密钥或发请求。

**怎么确认词有用。** 先人工确认一批相关论文，记录可靠标识符作为参考集；保留候选来源字段、原句与检索日期。词在标题/摘要出现只证明出现，不证明同义、相关或检索增益；机器标签不当作作者关键词。固定比较预算，每次只改一个词组，保存各版原始响应，分别记录返回、抓取、去重规模，并人工标注相关、不相关或不确定。比较新增相关记录、参考集覆盖及噪声后再取舍；未判断不算负例，参考集覆盖不叫全局召回。当前没有人工确认集及完整判断，精度、召回与优劣结论均不可得。

## 简短实际过程

已读技能及三份 references，采用 plan-only，按开放范围、分层查询、证据与效果分离的规则完成模型推演。实际未执行联网，也没有论文、引用、命中或效果数字可报告。技能的脚本执行、完整数据包及哈希校验对本次单文件离线评测属于多余步骤，与授权边界不符，已跳过，不能称为检索实测或包验证通过。

## 所读文件与未执行工作

所读均位于 `research-search-strategy-optimizer/`：`SKILL.md`、`references/execution.md`、`references/evidence-rules.md`、`references/output-contract.md`。

未执行：联网/OpenAlex 请求、脚本、安装、论文核验、人工标注、指标计算、数据包导出及校验；未读 `baseline.md` 或主线开发代码。Token 计数：未知。
