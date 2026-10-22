# P1 闭环优化实现

状态：核心模块已实现并通过 27 项 P1 状态/安全/会话测试；真实 P1 OpenAlex 两轮、6 请求已执行，因无人工相关性标签停在 pending_review，active_version 保持基线。

真实产物：`artifacts/p1/p1-live-loop-20261018/`。候选版本相对基线观察到 6 个新增 ID；确认新增相关数为未知，因此未自动保留候选版本。

## 已实现

- `iteration_optimizer.py`
  - 两个策略版本的去重差异；
  - 人工相关、模型相关、未标注和冲突分开；
  - broader / narrower / related_task / alternative_method / application 作为待审候选；
  - `analyze_omissions()` 仅对独立发现通道找到且人工确认相关的论文做漏检候选提取；
  - 预算、语义漂移、低收益和人工审阅停止原因。
- `optimization_session.py`
  - baseline / candidate / retain / rollback / pending_review / execution_failed / plan_only 状态；
  - current_version 与 active_version 分开；
  - live client 共享 session request budget；
  - snapshots 重放不增加网络请求；
  - scope drift、未审阅变更、未分支的 broader 变更拒绝；
  - history、summary、active-case、manifest 输出。
- CLI：`scripts/research-search.py optimize <config.json> --output <dir>`。

## 保留规则

候选版本只有在以下条件满足时才可 `retain`：

1. 版本已由 Agent/人工明确审阅；
2. 变化关系已标记；
3. 不是未经分支的 broader/related/application 扩展；
4. 新增记录有完整人工相关性判断；
5. 没有丢失当前已确认相关的论文；
6. 请求仍在 session budget 内。

否则状态为 `pending_review`、`rollback_to_previous` 或 `execution_failed`，不会自动改写 active case。

## 不承诺

- 没有人工真值集时，新增论文只叫 `new_ids`，不能叫新增相关论文。
- 停止条件不代表完整覆盖；所有停止输出都带 `coverage_claim=not_proven_complete`。
- P1 仍只使用 P0 已支持的 OpenAlex 通道；PubMed、Semantic Scholar、引文通道属于 P2。
