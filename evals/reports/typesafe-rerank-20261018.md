# `jev@typesafe` Top-K 重排记录

- 日期：2026-10-18
- 状态：代码与离线测试完成；真实 Jev 请求未执行

## 配置

- 工作流别名：`jev@typesafe`
- TypeSafe 官方模型：`jev-latest`
- 输入：真实 P0 OpenAlex `focused` 检索包
- 候选数：14
- 原检索包不修改
- TypeSafe 请求数：0
- 原始候选集合变更：false
- 人工相关性声明：false

## 当前原因

当前 MCode 进程没有 `TYPESAFE_API_KEY`，所以 reranker 安全降级为原始 OpenAlex 顺序，并明确返回 `not_executed`。没有把模型未调用写成模型分数，也没有把原始排序当作人工相关性真值。

## 正式 live 运行条件

```bash
export TYPESAFE_API_KEY='...'
python3 scripts/research-search.py rerank-topk \
  artifacts/p0-live-20261018 \
  --strategy focused \
  --top-k 20 \
  --use-typesafe \
  --output artifacts/jev-rerank-live
```

正式比较需要同时保留：

- OpenAlex 原始顺序；
- Jev 重排顺序；
- 同一候选集上的人工相关性标签；
- Jev score / noul、confidence、usage、错误与服务状态。

Jev 的 typed 分数只是排序信号，不等于人工相关性、Recall、Precision 或论文质量。
