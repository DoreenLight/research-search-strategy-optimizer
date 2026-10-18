# TypeSafe Jev Top-K 重排

## 目标

公开工作流别名：`jev@typesafe`。TypeSafe 官方 SDK/API 模型标识：`jev-latest`。在 OpenAlex/PubMed/Semantic Scholar 等确定性检索已经生成候选集后，用 Jev 对现有 shortlist 逐篇评分并重排，不扩展候选集，不替代人工相关性判断。

## 已实现

- `scripts/research_search/typesafe_reranker.py`
  - 使用 TypeSafe `Noul` 询问候选论文是否直接回答研究问题；
  - 支持 SDK typed response 的 `noul`；兼容 Score 概率形式；
  - 保存 score / noul、confidence、model、usage、error_type；
  - 无 `TYPESAFE_API_KEY` 时安全降级为原始顺序；
  - SDK 异常或无效答案时保留原始顺序并返回 `partial`；
  - `human_relevance_claim=false` 固定为 false。
- `scripts/research_search/typesafe_package.py`
  - 从已有 Research Search Package 读取指定策略的论文候选；
  - 输出 `rerank.json` 和 `manifest.json`；
  - 原检索包不修改；候选集合 hash 保留。
- CLI：

```bash
python3 scripts/research-search.py rerank-topk \
  artifacts/p0-live-20261018 \
  --strategy focused \
  --output artifacts/jev-rerank-plan
```

真实调用需显式：

```bash
export TYPESAFE_API_KEY='...'
python3 scripts/research-search.py rerank-topk \
  artifacts/p0-live-20261018 \
  --strategy focused \
  --top-k 20 \
  --use-typesafe \
  --output artifacts/jev-rerank-live
```

## 设计边界

- Jev 只能重排已经由词法/数据库检索找到的候选；它不能弥补初始召回不足。
- Jev 分数不是人工相关性标签，也不能直接计入 P@K 或 Recall@K 真值。
- 需要与原始顺序并列比较：原始 Top-K、Jev 重排 Top-K、人工确认 Top-K。
- 只有经过人工相关性审阅后，才可以评估 Jev 重排是否实际提高质量。
- 不把 TypeSafe cookbook 的演示数据和效果数字当作本项目结果。

## 依据

- TypeSafe HTTP API：<https://docs.typesafe.ai/api.md>
- Python SDK：<https://docs.typesafe.ai/sdk/python.md>
- Score：<https://docs.typesafe.ai/primitives/score.md>
- Re-ranking cookbook：<https://docs.typesafe.ai/cookbooks/rerank_typesafe.md>

## 当前测试

- reranker 单元测试：4 项
- package rerank 测试：3 项
- 当前环境未配置 `TYPESAFE_API_KEY`，所以仅验证安全降级和注入 judger 路径；没有实际请求 Jev。
