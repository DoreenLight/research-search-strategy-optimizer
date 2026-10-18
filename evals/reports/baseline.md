# 基线回答

## 正常最终答案

你可以先把词拆成三组，再组合检索；这一步是在定义**理论搜索空间**，不是在报告论文结果，也不是在进行模型实验。

**信号词**：`surface electromyography`、`surface EMG`、`sEMG`、`myoelectric signal`、`EMG signal`、`electromyographic signal`。其中 `myoelectric` 可能带来控制类研究，适合作为扩展词而不是唯一主词。

**任务与目标词**：`joint angle`、`joint angle estimation`、`joint angle prediction`、`joint kinematics`、`limb kinematics`、`angular position`、`kinematic decoding`、`continuous kinematics`、`motion estimation`。`kinematics` 和 `motion` 的范围比关节角更宽，可能包含轨迹、速度或姿态，需要后续人工判定，不要直接当作等价词。

**方法词**：`Transformer`、`transformer network`、`attention mechanism`、`self-attention`、`temporal attention`、`time-series Transformer`、`sequence modeling`、`encoder`、`long-range temporal dependency`。`attention` 和 `encoder` 可能检出非 Transformer 方法，因此应作为扩展检索词单独观察。

### OpenAlex 检索方案

**宽范围方案**：先用信号词与任务词组合，例如：`surface electromyography joint angle`；再把信号词替换为 `sEMG`、`myoelectric signal`，把任务词替换为 `joint kinematics`、`kinematic decoding`。目的在于覆盖不同命名，不预设具体关节、实时系统或康复场景。

**任务聚焦方案**：围绕角度预测/估计，分别检索：`surface EMG joint angle estimation`、`surface EMG joint angle prediction`、`surface electromyography angular position`、`sEMG continuous kinematics`。把 `estimation`、`prediction`、`decoding` 分开跑，避免一个词的偏好掩盖另一类表述。

**方法限定方案**：在任务词后加入方法词，分别检索：`surface EMG joint angle Transformer`、`surface electromyography joint kinematics self-attention`、`sEMG angle prediction temporal attention`、`myoelectric kinematic decoding time-series Transformer`。这些查询只表达方法约束，不表示已经确认有相关论文。OpenAlex 的 `search` 解析可能与布尔语法存在差异，稳妥做法是把短语组合拆成多次独立查询，并记录原始查询文本、日期、排序和筛选条件；不要把未实际请求的返回内容写成结果。

### 如何确认词是否有用

建立一个查询日志，区分：理论候选词、实际执行过的查询、人工检查过的记录和最终保留词。对每个词观察标题、摘要和关键词是否真正涉及表面肌电、人体运动学和角度任务；同时记录同义词带来的重复、明显无关主题和新增表达。若一个词只增加噪声，保留它作为线索并标注限制，不要悄悄删掉。待有人工确认的论文后，可从高相关记录中回溯作者使用的术语，再补充下一轮查询。当前没有人工确认论文，因此不能声称任何词已经有效，也不能给出命中量、相关率、排序成绩或模型效果。检索评估与后续实验要分开：搜索空间、历史检索记录、实际新增检索、保留词及目标指标变化不能混写。

## 简短实际过程

本次仅检查了指定报告路径是否已有文件；未读取 `with-skill.md` 或项目技能文件，未联网、未调用 OpenAlex、未安装依赖，也未再委派任务。随后按要求生成本文件；其中所有检索方案均为未执行的建议，不是实测结果。

## 未执行工作

- 未执行任何 OpenAlex 请求，未验证返回内容、论文或词的实际覆盖情况。
- 未进行人工论文确认、去重、相关性标注或检索效果比较。
- 未进行模型训练、参数搜索、实时性测试、关节场景选择或康复场景分析。
- 未使用 API Key；未制造论文、引用、成绩或数字。
- 工具 token 计数：未知。
