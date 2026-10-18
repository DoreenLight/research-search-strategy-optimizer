# `jev@typesafe` 全流程优化方案

## 核心修正

Jev 不再只是 Top-K 重排序器，而是作为科研检索策略优化闭环中的**辅助判断层**。代码仍由确定性流程控制，Jev 只返回 typed judgment / probability，不能自动把候选词、论文或版本标记为真实正确。

## Jev 介入的五个位置

### 1. 候选术语筛选

输入：

- 原始观察词；
- 论文标题/摘要中的连续片段；
- OpenAlex 数据库标签；
- 当前研究范围和概念角色。

Jev 判断：

- 是否直接描述研究对象、输入模态、任务或方法；
- 是否是上位概念、相邻任务、替代方法或应用场景；
- 是否存在明显语义漂移。

输出：

```text
term
relationship_probability
candidate_status
confidence
source_paper_ids
```

规则：

- Jev 结果是候选排序信号，不是人工批准；
- `equivalent` 仍需要人工或 Agent 审阅；
- broader / related / application 不自动进入正式 OR 组；
- 未知或低置信度候选进入 review queue。

### 2. 论文相关性判断

输入：

- 完整研究问题；
- 论文标题、摘要、数据库关键词；
- 当前查询版本和概念组。

Jev 使用 Noul 判断：

> 该论文是否直接研究当前研究对象、输入模态和任务？

输出：

```text
paper_id
jev_relevance_score
confidence
model
usage
query_version
```

规则：

- 只用于排序和人工审阅优先级；
- 不写入 `human_judgments`；
- 不直接计算 Precision/Recall；
- 不覆盖用户已经写入的人工判断。

### 3. 漏检候选确认

独立语义或引文通道发现论文后，Jev 判断：

- 是否直接落在当前研究范围内；
- 是否只是相邻领域；
- 是否值得提取新术语。

只有同时满足以下条件，才生成高优先级人工审阅任务：

```text
独立通道发现
+ Jev 直接相关概率达到配置阈值
+ 有标题/摘要证据
+ 不属于已知检索结果
```

即使满足，也仍然是：

```text
candidate_for_review
```

而不是：

```text
confirmed_relevant
```

### 4. 版本保留与回退建议

Jev 可提供候选版本之间的辅助比较：

- 新增论文直接相关比例的模型估计；
- 原有确认相关论文是否可能丢失；
- 查询变化是否引入语义漂移；
- 候选版本与研究范围的契合度。

代码决策仍必须遵守：

- 人工确认相关论文不能丢失；
- 新增论文没有完整人工标签时，状态为 `pending_review`；
- Jev 只能建议 `retain_candidate` 或 `rollback_candidate`；
- 正式 active version 只能由人工/Agent 审阅规则保留。

### 5. 人工审阅排序与 P4 分析

Jev 可以把人工队列排序为：

```text
高相关概率 + 高不确定性
```

优先人工查看：

- Jev 分数高但 confidence 低；
- 不同策略分数差异大；
- 模型与人工历史判断不一致；
- 独立通道发现但词法通道未覆盖的论文。

P4 中保留：

- `human_label`；
- `model_label`；
- `jev_score`；
- `jev_confidence`；
- `reviewer_decision`。

模型信号仅做独立误差分析，不能替代人工真值。

## 运行模式

### plan-only

- 不调用 TypeSafe；
- 输出 Jev 计划与问题模板；
- `status=not_executed`；
- 原排序不变。

### replay

- 读取已保存的 Jev typed response；
- 不新增请求；
- 复现排序和人工队列；
- 原始 response 保存并哈希。

### live

需要显式：

```bash
export TYPESAFE_API_KEY='...'
```

并添加：

```bash
--use-typesafe
```

官方模型：`jev-latest`；工作流别名：`jev@typesafe`。

## 成本与预算

每个论文候选通常对应一个 Jev typed judgment。系统必须记录：

```text
jev_request_count
input_tokens
output_tokens
estimated_cost_usd
failed_request_count
low_confidence_count
```

如果服务返回没有费用信息，`estimated_cost_usd=null`，不能记为 0。

## 本轮已实现

- `typesafe_reranker.py`：候选论文 typed score/noul、confidence、安全降级；
- `typesafe_package.py`：对现有 Research Search Package 应用 Jev 排序；
- CLI：`rerank-topk`；
- `references/typesafe-rerank.md`；
- 7 项 Jev 离线测试；
- 真实 P0 shortlist plan-only 验证：14 个候选保持不变、0 次 TypeSafe 请求。

## 本轮尚未执行

- 真实 Jev live API 请求；当前环境没有 `TYPESAFE_API_KEY`；
- Jev 候选术语筛选 live；
- Jev 漏检判断 live；
- Jev 辅助 P1 active version 决策 live；
- Jev 与人工标签的真实校准评估。
