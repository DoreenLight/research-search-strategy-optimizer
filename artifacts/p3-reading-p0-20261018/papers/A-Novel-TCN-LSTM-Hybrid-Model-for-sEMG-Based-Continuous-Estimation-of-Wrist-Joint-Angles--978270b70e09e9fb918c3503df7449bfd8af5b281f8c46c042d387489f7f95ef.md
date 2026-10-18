---
{
  "authors": [
    "Jiale Du",
    "Zunyi Liu",
    "Wenyuan Dong",
    "Weifeng Zhang",
    "Zhonghua Miao"
  ],
  "case_id": "semg-joint-angle",
  "doi": "https://doi.org/10.3390/s24175631",
  "human_judgments": [],
  "innovation_points": "",
  "model_judgments": [],
  "model_promoted_to_human": false,
  "paper_id": "https://openalex.org/W4402054497",
  "pmid": "39275542",
  "publication_year": 2024,
  "reading_status": "\u5f85\u786e\u8ba4",
  "reading_status_options": [
    "\u5f85\u786e\u8ba4",
    "\u5f85\u8bfb",
    "\u5df2\u8bfb"
  ],
  "relevance_status": "\u5f85\u4eba\u5de5\u786e\u8ba4",
  "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
  "schema_version": "p3-reading-export-0.1",
  "source_run_ids": [
    "run-plan-e7a1ff1c355c"
  ],
  "source_title": "Sensors",
  "source_url": "https://openalex.org/W4402054497",
  "title": "A Novel TCN-LSTM Hybrid Model for sEMG-Based Continuous Estimation of Wrist Joint Angles",
  "translation": ""
}
---

# 阅读任务

状态默认为 **待确认**；可人工改为 **待读** / **已读**。模型相关性不代表人工确认。

## 标题
```
A Novel TCN-LSTM Hybrid Model for sEMG-Based Continuous Estimation of Wrist Joint Angles
```

## 作者
```
[
  "Jiale Du",
  "Zunyi Liu",
  "Wenyuan Dong",
  "Weifeng Zhang",
  "Zhonghua Miao"
]
```

## 年份 / DOI / PMID
```
{
  "doi": "https://doi.org/10.3390/s24175631",
  "pmid": "39275542",
  "publication_year": 2024
}
```

## 摘要
```
Surface electromyography (sEMG) offers a novel method in human–machine interactions (HMIs) since it is a distinct physiological electrical signal that conceals human movement intention and muscle information. Unfortunately, the nonlinear and non-smooth features of sEMG signals often make joint angle estimation difficult. This paper proposes a joint angle prediction model for the continuous estimation of wrist motion angle changes based on sEMG signals. The proposed model combines a temporal convolutional network (TCN) with a long short-term memory (LSTM) network, where the TCN can sense local information and mine the deeper information of the sEMG signals, while LSTM, with its excellent temporal memory capability, can make up for the lack of the ability of the TCN to capture the long-term dependence of the sEMG signals, resulting in a better prediction. We validated the proposed method in the publicly available Ninapro DB1 dataset by selecting the first eight subjects and picking three types of wrist-dependent movements: wrist flexion (WF), wrist ulnar deviation (WUD), and wrist extension and closed hand (WECH). Finally, the proposed TCN-LSTM model was compared with the TCN and LSTM models. The proposed TCN-LSTM outperformed the TCN and LSTM models in terms of the root mean square error (RMSE) and average coefficient of determination (R2). The TCN-LSTM model achieved an average RMSE of 0.064, representing a 41% reduction compared to the TCN model and a 52% reduction compared to the LSTM model. The TCN-LSTM also achieved an average R2 of 0.93, indicating an 11% improvement over the TCN model and an 18% improvement over the LSTM model.
```

## 来源
```
{
  "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
  "source_title": "Sensors",
  "source_url": "https://openalex.org/W4402054497"
}
```

## 检索 / 运行 ID
```
{
  "case_id": "semg-joint-angle",
  "plan_ids": [
    "plan-e7a1ff1c355c"
  ],
  "source_run_ids": [
    "run-plan-e7a1ff1c355c"
  ]
}
```

## 相关性状态
```
{
  "human_judgments": [],
  "model_judgments": [],
  "model_promoted_to_human": false,
  "relevance_status": "\u5f85\u4eba\u5de5\u786e\u8ba4"
}
```

## 关键词（保留来源，不自动采用）
```
[
  {
    "adopted": false,
    "canonical_term": "ability",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00029",
      "evidence-00030"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4284878820",
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "ability",
    "term_id": "term-00026"
  },
  {
    "adopted": false,
    "canonical_term": "angle",
    "category": "unclassified",
    "document_frequency": 9,
    "evidence_ids": [
      "evidence-00095",
      "evidence-00096",
      "evidence-00097",
      "evidence-00098",
      "evidence-00099",
      "evidence-00100",
      "evidence-00101",
      "evidence-00102",
      "evidence-00103",
      "evidence-00104",
      "evidence-00105"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W1918406696",
      "https://openalex.org/W2091022037",
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4284878820",
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402054497",
      "https://openalex.org/W4402270704",
      "https://openalex.org/W4407450426",
      "https://openalex.org/W4416190202"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "angle",
    "term_id": "term-00080"
  },
  {
    "adopted": false,
    "canonical_term": "angle changes",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00109",
      "evidence-00110"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W2091022037",
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "angle changes",
    "term_id": "term-00084"
  },
  {
    "adopted": false,
    "canonical_term": "angle changes based",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00111"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "angle changes based",
    "term_id": "term-00085"
  },
  {
    "adopted": false,
    "canonical_term": "angle estimation",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00113",
      "evidence-00114"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "angle estimation",
    "term_id": "term-00087"
  },
  {
    "adopted": false,
    "canonical_term": "angle estimation difficult",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00115"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "angle estimation difficult",
    "term_id": "term-00088"
  },
  {
    "adopted": false,
    "canonical_term": "angle prediction",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00121",
      "evidence-00122"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497",
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "angle prediction",
    "term_id": "term-00094"
  },
  {
    "adopted": false,
    "canonical_term": "angle prediction model",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00123",
      "evidence-00124"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497",
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "angle prediction model",
    "term_id": "term-00095"
  },
  {
    "adopted": false,
    "canonical_term": "angles",
    "category": "unclassified",
    "document_frequency": 10,
    "evidence_ids": [
      "evidence-00129",
      "evidence-00130",
      "evidence-00131",
      "evidence-00132",
      "evidence-00133",
      "evidence-00134",
      "evidence-00135",
      "evidence-00136",
      "evidence-00137",
      "evidence-00138",
      "evidence-00139",
      "evidence-00140",
      "evidence-00141",
      "evidence-00142"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W1918406696",
      "https://openalex.org/W2072588720",
      "https://openalex.org/W3013651137",
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4284878820",
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402054497",
      "https://openalex.org/W4402270704",
      "https://openalex.org/W4407450426",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "angles",
    "term_id": "term-00100"
  },
  {
    "adopted": false,
    "canonical_term": "available",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00176"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "available",
    "term_id": "term-00130"
  },
  {
    "adopted": false,
    "canonical_term": "available ninapro",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00177"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "available ninapro",
    "term_id": "term-00131"
  },
  {
    "adopted": false,
    "canonical_term": "available ninapro db1",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00178"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "available ninapro db1",
    "term_id": "term-00132"
  },
  {
    "adopted": false,
    "canonical_term": "based",
    "category": "unclassified",
    "document_frequency": 6,
    "evidence_ids": [
      "evidence-00180",
      "evidence-00181",
      "evidence-00182",
      "evidence-00183",
      "evidence-00184",
      "evidence-00185",
      "evidence-00186"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3013651137",
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4284878820",
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402054497",
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "based",
    "term_id": "term-00134"
  },
  {
    "adopted": false,
    "canonical_term": "based on semg",
    "category": "unclassified",
    "document_frequency": 3,
    "evidence_ids": [
      "evidence-00187",
      "evidence-00188",
      "evidence-00189"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402054497",
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "based on semg",
    "term_id": "term-00135"
  },
  {
    "adopted": false,
    "canonical_term": "better",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00197",
      "evidence-00198"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3013651137",
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "better",
    "term_id": "term-00140"
  },
  {
    "adopted": false,
    "canonical_term": "better prediction",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00200"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "better prediction",
    "term_id": "term-00142"
  },
  {
    "adopted": false,
    "canonical_term": "can",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00234",
      "evidence-00235"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "can",
    "term_id": "term-00171"
  },
  {
    "adopted": false,
    "canonical_term": "can make",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00236"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "can make",
    "term_id": "term-00172"
  },
  {
    "adopted": false,
    "canonical_term": "can make up",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00237"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "can make up",
    "term_id": "term-00173"
  },
  {
    "adopted": false,
    "canonical_term": "can sense",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00240"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "can sense",
    "term_id": "term-00176"
  },
  {
    "adopted": false,
    "canonical_term": "can sense local",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00241"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "can sense local",
    "term_id": "term-00177"
  },
  {
    "adopted": false,
    "canonical_term": "capability",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00242"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "capability",
    "term_id": "term-00178"
  },
  {
    "adopted": false,
    "canonical_term": "capture",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00245"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "capture",
    "term_id": "term-00181"
  },
  {
    "adopted": false,
    "canonical_term": "capture the long-term",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00246"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "capture the long-term",
    "term_id": "term-00182"
  },
  {
    "adopted": false,
    "canonical_term": "changes",
    "category": "unclassified",
    "document_frequency": 3,
    "evidence_ids": [
      "evidence-00261",
      "evidence-00262",
      "evidence-00263"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W1918406696",
      "https://openalex.org/W2091022037",
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "changes",
    "term_id": "term-00197"
  },
  {
    "adopted": false,
    "canonical_term": "changes based",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00264"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "changes based",
    "term_id": "term-00198"
  },
  {
    "adopted": false,
    "canonical_term": "combines",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00295",
      "evidence-00296"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "combines",
    "term_id": "term-00227"
  },
  {
    "adopted": false,
    "canonical_term": "combines a temporal",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00297"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "combines a temporal",
    "term_id": "term-00228"
  },
  {
    "adopted": false,
    "canonical_term": "conceals",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00313"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "conceals",
    "term_id": "term-00241"
  },
  {
    "adopted": false,
    "canonical_term": "conceals human",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00314"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "conceals human",
    "term_id": "term-00242"
  },
  {
    "adopted": false,
    "canonical_term": "conceals human movement",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00315"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "conceals human movement",
    "term_id": "term-00243"
  },
  {
    "adopted": false,
    "canonical_term": "continuous",
    "category": "unclassified",
    "document_frequency": 5,
    "evidence_ids": [
      "evidence-00326",
      "evidence-00327",
      "evidence-00328",
      "evidence-00329",
      "evidence-00330",
      "evidence-00331",
      "evidence-00332"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W2072588720",
      "https://openalex.org/W3013651137",
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4402054497",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "continuous",
    "term_id": "term-00254"
  },
  {
    "adopted": false,
    "canonical_term": "continuous estimation",
    "category": "unclassified",
    "document_frequency": 3,
    "evidence_ids": [
      "evidence-00333",
      "evidence-00334",
      "evidence-00335",
      "evidence-00336"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W2072588720",
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "continuous estimation",
    "term_id": "term-00255"
  },
  {
    "adopted": false,
    "canonical_term": "convolutional",
    "category": "unclassified",
    "document_frequency": 3,
    "evidence_ids": [
      "evidence-00361",
      "evidence-00362",
      "evidence-00363",
      "evidence-00364"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402054497",
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "convolutional",
    "term_id": "term-00276"
  },
  {
    "adopted": false,
    "canonical_term": "convolutional network",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00365"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "convolutional network",
    "term_id": "term-00277"
  },
  {
    "adopted": false,
    "canonical_term": "dataset",
    "category": "unclassified",
    "document_frequency": 3,
    "evidence_ids": [
      "evidence-00401",
      "evidence-00402",
      "evidence-00403"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497",
      "https://openalex.org/W4402270704",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "dataset",
    "term_id": "term-00305"
  },
  {
    "adopted": false,
    "canonical_term": "dataset by selecting",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00404"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "dataset by selecting",
    "term_id": "term-00306"
  },
  {
    "adopted": false,
    "canonical_term": "db1",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00406"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "db1",
    "term_id": "term-00308"
  },
  {
    "adopted": false,
    "canonical_term": "db1 dataset",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00407"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "db1 dataset",
    "term_id": "term-00309"
  },
  {
    "adopted": false,
    "canonical_term": "deeper",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00415"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "deeper",
    "term_id": "term-00317"
  },
  {
    "adopted": false,
    "canonical_term": "deeper information",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00416"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "deeper information",
    "term_id": "term-00318"
  },
  {
    "adopted": false,
    "canonical_term": "dependence",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00425"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "dependence",
    "term_id": "term-00326"
  },
  {
    "adopted": false,
    "canonical_term": "deviation",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00439"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "deviation",
    "term_id": "term-00339"
  },
  {
    "adopted": false,
    "canonical_term": "difficult",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00449",
      "evidence-00450"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "difficult",
    "term_id": "term-00348"
  },
  {
    "adopted": false,
    "canonical_term": "distinct",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00461"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "distinct",
    "term_id": "term-00359"
  },
  {
    "adopted": false,
    "canonical_term": "distinct physiological",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00462"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "distinct physiological",
    "term_id": "term-00360"
  },
  {
    "adopted": false,
    "canonical_term": "distinct physiological electrical",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00463"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "distinct physiological electrical",
    "term_id": "term-00361"
  },
  {
    "adopted": false,
    "canonical_term": "eight",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00517"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "eight",
    "term_id": "term-00407"
  },
  {
    "adopted": false,
    "canonical_term": "eight subjects",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00518"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "eight subjects",
    "term_id": "term-00408"
  },
  {
    "adopted": false,
    "canonical_term": "electrical",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00526",
      "evidence-00527",
      "evidence-00528"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4284878820",
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "electrical",
    "term_id": "term-00415"
  },
  {
    "adopted": false,
    "canonical_term": "electrical signal",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00529"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "electrical signal",
    "term_id": "term-00416"
  },
  {
    "adopted": false,
    "canonical_term": "electromyography",
    "category": "unclassified",
    "document_frequency": 11,
    "evidence_ids": [
      "evidence-00545",
      "evidence-00546",
      "evidence-00547",
      "evidence-00548",
      "evidence-00549",
      "evidence-00550",
      "evidence-00551",
      "evidence-00552",
      "evidence-00553",
      "evidence-00554",
      "evidence-00555",
      "evidence-00556",
      "evidence-00557",
      "evidence-00558"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W1918406696",
      "https://openalex.org/W2086303648",
      "https://openalex.org/W3013651137",
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4284878820",
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402054497",
      "https://openalex.org/W4402270704",
      "https://openalex.org/W4407450426",
      "https://openalex.org/W4416190202",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "electromyography",
    "term_id": "term-00430"
  },
  {
    "adopted": false,
    "canonical_term": "estimation",
    "category": "unclassified",
    "document_frequency": 4,
    "evidence_ids": [
      "evidence-00623",
      "evidence-00624",
      "evidence-00625",
      "evidence-00626",
      "evidence-00627",
      "evidence-00628"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W2072588720",
      "https://openalex.org/W3013651137",
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "estimation",
    "term_id": "term-00486"
  },
  {
    "adopted": false,
    "canonical_term": "estimation difficult",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00630"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "estimation difficult",
    "term_id": "term-00488"
  },
  {
    "adopted": false,
    "canonical_term": "estimation of wrist",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00633",
      "evidence-00634"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "estimation of wrist",
    "term_id": "term-00490"
  },
  {
    "adopted": false,
    "canonical_term": "excellent",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00640"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "excellent",
    "term_id": "term-00496"
  },
  {
    "adopted": false,
    "canonical_term": "excellent temporal",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00641"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "excellent temporal",
    "term_id": "term-00497"
  },
  {
    "adopted": false,
    "canonical_term": "excellent temporal memory",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00642"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "excellent temporal memory",
    "term_id": "term-00498"
  },
  {
    "adopted": false,
    "canonical_term": "features",
    "category": "unclassified",
    "document_frequency": 4,
    "evidence_ids": [
      "evidence-00699",
      "evidence-00700",
      "evidence-00701",
      "evidence-00702"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4284878820",
      "https://openalex.org/W4402054497",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "features",
    "term_id": "term-00548"
  },
  {
    "adopted": false,
    "canonical_term": "features of semg",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00706"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "features of semg",
    "term_id": "term-00552"
  },
  {
    "adopted": false,
    "canonical_term": "first",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00724",
      "evidence-00725"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "first",
    "term_id": "term-00567"
  },
  {
    "adopted": false,
    "canonical_term": "first eight",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00728"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "first eight",
    "term_id": "term-00570"
  },
  {
    "adopted": false,
    "canonical_term": "first eight subjects",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00729"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "first eight subjects",
    "term_id": "term-00571"
  },
  {
    "adopted": false,
    "canonical_term": "flexion",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00737",
      "evidence-00738"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W1918406696",
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "flexion",
    "term_id": "term-00579"
  },
  {
    "adopted": false,
    "canonical_term": "hmis",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00846"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "hmis",
    "term_id": "term-00669"
  },
  {
    "adopted": false,
    "canonical_term": "human",
    "category": "unclassified",
    "document_frequency": 4,
    "evidence_ids": [
      "evidence-00854",
      "evidence-00855",
      "evidence-00856",
      "evidence-00857",
      "evidence-00858"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W2072588720",
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402054497",
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "human",
    "term_id": "term-00676"
  },
  {
    "adopted": false,
    "canonical_term": "human movement",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00867"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "human movement",
    "term_id": "term-00683"
  },
  {
    "adopted": false,
    "canonical_term": "human movement intention",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00868"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "human movement intention",
    "term_id": "term-00684"
  },
  {
    "adopted": false,
    "canonical_term": "human-machine interaction",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00874",
      "evidence-00875"
    ],
    "evidence_status": "database_assigned",
    "paper_ids": [
      "https://openalex.org/W4402054497",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "term": "human-machine interaction",
    "term_id": "term-00690"
  },
  {
    "adopted": false,
    "canonical_term": "hybrid",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00880",
      "evidence-00881"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "hybrid",
    "term_id": "term-00695"
  },
  {
    "adopted": false,
    "canonical_term": "hybrid model",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00882",
      "evidence-00883"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "hybrid model",
    "term_id": "term-00696"
  },
  {
    "adopted": false,
    "canonical_term": "information",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00913",
      "evidence-00914"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4284878820",
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "information",
    "term_id": "term-00724"
  },
  {
    "adopted": false,
    "canonical_term": "information and mine",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00915"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "information and mine",
    "term_id": "term-00725"
  },
  {
    "adopted": false,
    "canonical_term": "intention",
    "category": "unclassified",
    "document_frequency": 3,
    "evidence_ids": [
      "evidence-00934",
      "evidence-00935",
      "evidence-00936"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3013651137",
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "intention",
    "term_id": "term-00742"
  },
  {
    "adopted": false,
    "canonical_term": "intention and muscle",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00937"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "intention and muscle",
    "term_id": "term-00743"
  },
  {
    "adopted": false,
    "canonical_term": "interactions",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00945"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "interactions",
    "term_id": "term-00750"
  },
  {
    "adopted": false,
    "canonical_term": "its",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00969",
      "evidence-00970"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497",
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "its",
    "term_id": "term-00773"
  },
  {
    "adopted": false,
    "canonical_term": "its excellent",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00972"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "its excellent",
    "term_id": "term-00775"
  },
  {
    "adopted": false,
    "canonical_term": "its excellent temporal",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00973"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "its excellent temporal",
    "term_id": "term-00776"
  },
  {
    "adopted": false,
    "canonical_term": "joint",
    "category": "unclassified",
    "document_frequency": 12,
    "evidence_ids": [
      "evidence-00975",
      "evidence-00976",
      "evidence-00977",
      "evidence-00978",
      "evidence-00979",
      "evidence-00980",
      "evidence-00981",
      "evidence-00982",
      "evidence-00983",
      "evidence-00984",
      "evidence-00985",
      "evidence-00986",
      "evidence-00987",
      "evidence-00988",
      "evidence-00989",
      "evidence-00990",
      "evidence-00991",
      "evidence-00992",
      "evidence-00993",
      "evidence-00994",
      "evidence-00995",
      "evidence-00996"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W1918406696",
      "https://openalex.org/W2072588720",
      "https://openalex.org/W2091022037",
      "https://openalex.org/W3013651137",
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4284878820",
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402054497",
      "https://openalex.org/W4402270704",
      "https://openalex.org/W4407450426",
      "https://openalex.org/W4416190202",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "joint",
    "term_id": "term-00778"
  },
  {
    "adopted": false,
    "canonical_term": "joint angle",
    "category": "unclassified",
    "document_frequency": 9,
    "evidence_ids": [
      "evidence-00997",
      "evidence-00998",
      "evidence-00999",
      "evidence-01000",
      "evidence-01001",
      "evidence-01002",
      "evidence-01003",
      "evidence-01004",
      "evidence-01005",
      "evidence-01006",
      "evidence-01007"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W1918406696",
      "https://openalex.org/W2091022037",
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4284878820",
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402054497",
      "https://openalex.org/W4402270704",
      "https://openalex.org/W4407450426",
      "https://openalex.org/W4416190202"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "joint angle",
    "term_id": "term-00779"
  },
  {
    "adopted": false,
    "canonical_term": "joint angle estimation",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01013",
      "evidence-01014"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "joint angle estimation",
    "term_id": "term-00784"
  },
  {
    "adopted": false,
    "canonical_term": "joint angle prediction",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01017",
      "evidence-01018"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497",
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "joint angle prediction",
    "term_id": "term-00786"
  },
  {
    "adopted": false,
    "canonical_term": "joint angles",
    "category": "unclassified",
    "document_frequency": 10,
    "evidence_ids": [
      "evidence-01026",
      "evidence-01027",
      "evidence-01028",
      "evidence-01029",
      "evidence-01030",
      "evidence-01031",
      "evidence-01032",
      "evidence-01033",
      "evidence-01034",
      "evidence-01035",
      "evidence-01036",
      "evidence-01037",
      "evidence-01038",
      "evidence-01039"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W1918406696",
      "https://openalex.org/W2072588720",
      "https://openalex.org/W3013651137",
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4284878820",
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402054497",
      "https://openalex.org/W4402270704",
      "https://openalex.org/W4407450426",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "joint angles",
    "term_id": "term-00789"
  },
  {
    "adopted": false,
    "canonical_term": "lack",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01091"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "lack",
    "term_id": "term-00824"
  },
  {
    "adopted": false,
    "canonical_term": "local",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01119"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "local",
    "term_id": "term-00846"
  },
  {
    "adopted": false,
    "canonical_term": "local information",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01120"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "local information",
    "term_id": "term-00847"
  },
  {
    "adopted": false,
    "canonical_term": "long",
    "category": "unclassified",
    "document_frequency": 3,
    "evidence_ids": [
      "evidence-01126",
      "evidence-01127",
      "evidence-01128"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497",
      "https://openalex.org/W4402270704",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "long",
    "term_id": "term-00853"
  },
  {
    "adopted": false,
    "canonical_term": "long short-term",
    "category": "unclassified",
    "document_frequency": 3,
    "evidence_ids": [
      "evidence-01129",
      "evidence-01130",
      "evidence-01131"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497",
      "https://openalex.org/W4402270704",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "long short-term",
    "term_id": "term-00854"
  },
  {
    "adopted": false,
    "canonical_term": "long short-term memory",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01132"
    ],
    "evidence_status": "database_assigned",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "term": "long short-term memory",
    "term_id": "term-00855"
  },
  {
    "adopted": false,
    "canonical_term": "long short-term memory",
    "category": "unclassified",
    "document_frequency": 3,
    "evidence_ids": [
      "evidence-01133",
      "evidence-01134",
      "evidence-01135"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497",
      "https://openalex.org/W4402270704",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "long short-term memory",
    "term_id": "term-00856"
  },
  {
    "adopted": false,
    "canonical_term": "long-term",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01138"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "long-term",
    "term_id": "term-00859"
  },
  {
    "adopted": false,
    "canonical_term": "long-term dependence",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01139"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "long-term dependence",
    "term_id": "term-00860"
  },
  {
    "adopted": false,
    "canonical_term": "lstm",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01161",
      "evidence-01162"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497",
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "lstm",
    "term_id": "term-00881"
  },
  {
    "adopted": false,
    "canonical_term": "machine",
    "category": "unclassified",
    "document_frequency": 3,
    "evidence_ids": [
      "evidence-01166",
      "evidence-01167",
      "evidence-01168"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3013651137",
      "https://openalex.org/W4402054497",
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "machine",
    "term_id": "term-00885"
  },
  {
    "adopted": false,
    "canonical_term": "machine interactions",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01169"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "machine interactions",
    "term_id": "term-00886"
  },
  {
    "adopted": false,
    "canonical_term": "make",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01172"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "make",
    "term_id": "term-00889"
  },
  {
    "adopted": false,
    "canonical_term": "make joint",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01173"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "make joint",
    "term_id": "term-00890"
  },
  {
    "adopted": false,
    "canonical_term": "make joint angle",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01174"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "make joint angle",
    "term_id": "term-00891"
  },
  {
    "adopted": false,
    "canonical_term": "make up",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01175"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "make up",
    "term_id": "term-00892"
  },
  {
    "adopted": false,
    "canonical_term": "memory",
    "category": "unclassified",
    "document_frequency": 4,
    "evidence_ids": [
      "evidence-01221",
      "evidence-01222",
      "evidence-01223",
      "evidence-01224"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497",
      "https://openalex.org/W4402270704",
      "https://openalex.org/W4407450426",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "memory",
    "term_id": "term-00927"
  },
  {
    "adopted": false,
    "canonical_term": "memory capability",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01225"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "memory capability",
    "term_id": "term-00928"
  },
  {
    "adopted": false,
    "canonical_term": "mine",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01232"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "mine",
    "term_id": "term-00935"
  },
  {
    "adopted": false,
    "canonical_term": "mine the deeper",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01233"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "mine the deeper",
    "term_id": "term-00936"
  },
  {
    "adopted": false,
    "canonical_term": "model",
    "category": "unclassified",
    "document_frequency": 7,
    "evidence_ids": [
      "evidence-01241",
      "evidence-01242",
      "evidence-01243",
      "evidence-01244",
      "evidence-01245",
      "evidence-01246",
      "evidence-01247",
      "evidence-01248",
      "evidence-01249",
      "evidence-01250"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3013651137",
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402054497",
      "https://openalex.org/W4402270704",
      "https://openalex.org/W4407450426",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "model",
    "term_id": "term-00944"
  },
  {
    "adopted": false,
    "canonical_term": "model combines",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01259",
      "evidence-01260"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "model combines",
    "term_id": "term-00953"
  },
  {
    "adopted": false,
    "canonical_term": "model for semg-based",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01261"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "model for semg-based",
    "term_id": "term-00954"
  },
  {
    "adopted": false,
    "canonical_term": "motion",
    "category": "unclassified",
    "document_frequency": 5,
    "evidence_ids": [
      "evidence-01293",
      "evidence-01294",
      "evidence-01295",
      "evidence-01296",
      "evidence-01297"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4284878820",
      "https://openalex.org/W4402054497",
      "https://openalex.org/W4407450426",
      "https://openalex.org/W4416190202"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "motion",
    "term_id": "term-00981"
  },
  {
    "adopted": false,
    "canonical_term": "motion angle",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01299"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "motion angle",
    "term_id": "term-00983"
  },
  {
    "adopted": false,
    "canonical_term": "motion angle changes",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01300"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "motion angle changes",
    "term_id": "term-00984"
  },
  {
    "adopted": false,
    "canonical_term": "movement",
    "category": "unclassified",
    "document_frequency": 5,
    "evidence_ids": [
      "evidence-01313",
      "evidence-01314",
      "evidence-01315",
      "evidence-01316",
      "evidence-01317"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W2091022037",
      "https://openalex.org/W3013651137",
      "https://openalex.org/W4284878820",
      "https://openalex.org/W4402054497",
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "movement",
    "term_id": "term-00997"
  },
  {
    "adopted": false,
    "canonical_term": "movement intention",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01318",
      "evidence-01319"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3013651137",
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "movement intention",
    "term_id": "term-00998"
  },
  {
    "adopted": false,
    "canonical_term": "movements",
    "category": "unclassified",
    "document_frequency": 3,
    "evidence_ids": [
      "evidence-01323",
      "evidence-01324",
      "evidence-01325"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4284878820",
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "movements",
    "term_id": "term-01002"
  },
  {
    "adopted": false,
    "canonical_term": "muscle",
    "category": "unclassified",
    "document_frequency": 6,
    "evidence_ids": [
      "evidence-01333",
      "evidence-01334",
      "evidence-01335",
      "evidence-01336",
      "evidence-01337",
      "evidence-01338",
      "evidence-01339"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W1918406696",
      "https://openalex.org/W2091022037",
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4284878820",
      "https://openalex.org/W4402054497",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "muscle",
    "term_id": "term-01010"
  },
  {
    "adopted": false,
    "canonical_term": "muscle information",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01348"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "muscle information",
    "term_id": "term-01019"
  },
  {
    "adopted": false,
    "canonical_term": "network",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01361",
      "evidence-01362"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W2072588720",
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "network",
    "term_id": "term-01031"
  },
  {
    "adopted": false,
    "canonical_term": "ninapro",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01384",
      "evidence-01385"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "ninapro",
    "term_id": "term-01050"
  },
  {
    "adopted": false,
    "canonical_term": "ninapro db1",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01386"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "ninapro db1",
    "term_id": "term-01051"
  },
  {
    "adopted": false,
    "canonical_term": "ninapro db1 dataset",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01387"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "ninapro db1 dataset",
    "term_id": "term-01052"
  },
  {
    "adopted": false,
    "canonical_term": "non-smooth",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01396"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "non-smooth",
    "term_id": "term-01061"
  },
  {
    "adopted": false,
    "canonical_term": "non-smooth features",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01397"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "non-smooth features",
    "term_id": "term-01062"
  },
  {
    "adopted": false,
    "canonical_term": "nonlinear",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01398"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "nonlinear",
    "term_id": "term-01063"
  },
  {
    "adopted": false,
    "canonical_term": "nonlinear and non-smooth",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01399"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "nonlinear and non-smooth",
    "term_id": "term-01064"
  },
  {
    "adopted": false,
    "canonical_term": "novel",
    "category": "unclassified",
    "document_frequency": 3,
    "evidence_ids": [
      "evidence-01408",
      "evidence-01409",
      "evidence-01410",
      "evidence-01411"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W2086303648",
      "https://openalex.org/W4402054497",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "novel",
    "term_id": "term-01073"
  },
  {
    "adopted": false,
    "canonical_term": "novel tcn-lstm",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01416"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "novel tcn-lstm",
    "term_id": "term-01078"
  },
  {
    "adopted": false,
    "canonical_term": "novel tcn-lstm hybrid",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01417"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "novel tcn-lstm hybrid",
    "term_id": "term-01079"
  },
  {
    "adopted": false,
    "canonical_term": "offers",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01431"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "offers",
    "term_id": "term-01093"
  },
  {
    "adopted": false,
    "canonical_term": "offers a novel",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01432"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "offers a novel",
    "term_id": "term-01094"
  },
  {
    "adopted": false,
    "canonical_term": "often",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01433",
      "evidence-01434"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497",
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "often",
    "term_id": "term-01095"
  },
  {
    "adopted": false,
    "canonical_term": "often make",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01435"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "often make",
    "term_id": "term-01096"
  },
  {
    "adopted": false,
    "canonical_term": "often make joint",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01436"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "often make joint",
    "term_id": "term-01097"
  },
  {
    "adopted": false,
    "canonical_term": "paper",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01458"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "paper",
    "term_id": "term-01119"
  },
  {
    "adopted": false,
    "canonical_term": "paper proposes",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01459"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "paper proposes",
    "term_id": "term-01120"
  },
  {
    "adopted": false,
    "canonical_term": "physiological",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01502"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "physiological",
    "term_id": "term-01154"
  },
  {
    "adopted": false,
    "canonical_term": "physiological electrical",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01503"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "physiological electrical",
    "term_id": "term-01155"
  },
  {
    "adopted": false,
    "canonical_term": "physiological electrical signal",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01504"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "physiological electrical signal",
    "term_id": "term-01156"
  },
  {
    "adopted": false,
    "canonical_term": "picking",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01505"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "picking",
    "term_id": "term-01157"
  },
  {
    "adopted": false,
    "canonical_term": "picking three",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01506"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "picking three",
    "term_id": "term-01158"
  },
  {
    "adopted": false,
    "canonical_term": "picking three types",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01507"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "picking three types",
    "term_id": "term-01159"
  },
  {
    "adopted": false,
    "canonical_term": "prediction",
    "category": "unclassified",
    "document_frequency": 7,
    "evidence_ids": [
      "evidence-01545",
      "evidence-01546",
      "evidence-01547",
      "evidence-01548",
      "evidence-01549",
      "evidence-01550",
      "evidence-01551",
      "evidence-01552",
      "evidence-01553",
      "evidence-01554"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3013651137",
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402054497",
      "https://openalex.org/W4402270704",
      "https://openalex.org/W4407450426",
      "https://openalex.org/W4416190202",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "prediction",
    "term_id": "term-01194"
  },
  {
    "adopted": false,
    "canonical_term": "prediction model",
    "category": "unclassified",
    "document_frequency": 3,
    "evidence_ids": [
      "evidence-01559",
      "evidence-01560",
      "evidence-01561"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3013651137",
      "https://openalex.org/W4402054497",
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "prediction model",
    "term_id": "term-01198"
  },
  {
    "adopted": false,
    "canonical_term": "proposed",
    "category": "unclassified",
    "document_frequency": 4,
    "evidence_ids": [
      "evidence-01588",
      "evidence-01589",
      "evidence-01590",
      "evidence-01591"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3013651137",
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4284878820",
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "proposed",
    "term_id": "term-01224"
  },
  {
    "adopted": false,
    "canonical_term": "proposed model",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01593",
      "evidence-01594"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "proposed model",
    "term_id": "term-01226"
  },
  {
    "adopted": false,
    "canonical_term": "proposed model combines",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01595"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "proposed model combines",
    "term_id": "term-01227"
  },
  {
    "adopted": false,
    "canonical_term": "proposes",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01597",
      "evidence-01598"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "proposes",
    "term_id": "term-01229"
  },
  {
    "adopted": false,
    "canonical_term": "proposes a joint",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01599"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "proposes a joint",
    "term_id": "term-01230"
  },
  {
    "adopted": false,
    "canonical_term": "publicly",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01611",
      "evidence-01612"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497",
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "publicly",
    "term_id": "term-01241"
  },
  {
    "adopted": false,
    "canonical_term": "publicly available",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01615"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "publicly available",
    "term_id": "term-01244"
  },
  {
    "adopted": false,
    "canonical_term": "publicly available ninapro",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01616"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "publicly available ninapro",
    "term_id": "term-01245"
  },
  {
    "adopted": false,
    "canonical_term": "resulting",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01718"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "resulting",
    "term_id": "term-01335"
  },
  {
    "adopted": false,
    "canonical_term": "selecting",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01761"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "selecting",
    "term_id": "term-01369"
  },
  {
    "adopted": false,
    "canonical_term": "selecting the first",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01762"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "selecting the first",
    "term_id": "term-01370"
  },
  {
    "adopted": false,
    "canonical_term": "semg",
    "category": "unclassified",
    "document_frequency": 9,
    "evidence_ids": [
      "evidence-01763",
      "evidence-01764",
      "evidence-01765",
      "evidence-01766",
      "evidence-01767",
      "evidence-01768",
      "evidence-01769",
      "evidence-01770",
      "evidence-01771",
      "evidence-01772",
      "evidence-01773",
      "evidence-01774"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W1918406696",
      "https://openalex.org/W3013651137",
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4284878820",
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402054497",
      "https://openalex.org/W4402270704",
      "https://openalex.org/W4407450426",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "semg",
    "term_id": "term-01371"
  },
  {
    "adopted": false,
    "canonical_term": "semg signals",
    "category": "unclassified",
    "document_frequency": 6,
    "evidence_ids": [
      "evidence-01790",
      "evidence-01791",
      "evidence-01792",
      "evidence-01793",
      "evidence-01794",
      "evidence-01795"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3013651137",
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402054497",
      "https://openalex.org/W4402270704",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "semg signals",
    "term_id": "term-01386"
  },
  {
    "adopted": false,
    "canonical_term": "semg signals often",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01796"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "semg signals often",
    "term_id": "term-01387"
  },
  {
    "adopted": false,
    "canonical_term": "semg-based",
    "category": "unclassified",
    "document_frequency": 3,
    "evidence_ids": [
      "evidence-01797",
      "evidence-01798",
      "evidence-01799"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W2072588720",
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "semg-based",
    "term_id": "term-01388"
  },
  {
    "adopted": false,
    "canonical_term": "semg-based continuous",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01800",
      "evidence-01801"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W2072588720",
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "semg-based continuous",
    "term_id": "term-01389"
  },
  {
    "adopted": false,
    "canonical_term": "semg-based continuous estimation",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01802",
      "evidence-01803"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W2072588720",
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "semg-based continuous estimation",
    "term_id": "term-01390"
  },
  {
    "adopted": false,
    "canonical_term": "sense",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01808"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "sense",
    "term_id": "term-01395"
  },
  {
    "adopted": false,
    "canonical_term": "sense local",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01809"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "sense local",
    "term_id": "term-01396"
  },
  {
    "adopted": false,
    "canonical_term": "sense local information",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01810"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "sense local information",
    "term_id": "term-01397"
  },
  {
    "adopted": false,
    "canonical_term": "short-term",
    "category": "unclassified",
    "document_frequency": 4,
    "evidence_ids": [
      "evidence-01815",
      "evidence-01816",
      "evidence-01817",
      "evidence-01818"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497",
      "https://openalex.org/W4402270704",
      "https://openalex.org/W4407450426",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "short-term",
    "term_id": "term-01401"
  },
  {
    "adopted": false,
    "canonical_term": "short-term memory",
    "category": "unclassified",
    "document_frequency": 4,
    "evidence_ids": [
      "evidence-01819",
      "evidence-01820",
      "evidence-01821",
      "evidence-01822"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497",
      "https://openalex.org/W4402270704",
      "https://openalex.org/W4407450426",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "short-term memory",
    "term_id": "term-01402"
  },
  {
    "adopted": false,
    "canonical_term": "signal",
    "category": "unclassified",
    "document_frequency": 4,
    "evidence_ids": [
      "evidence-01827",
      "evidence-01828",
      "evidence-01829",
      "evidence-01830"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W2091022037",
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402054497",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "signal",
    "term_id": "term-01405"
  },
  {
    "adopted": false,
    "canonical_term": "signal that conceals",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01832"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "signal that conceals",
    "term_id": "term-01407"
  },
  {
    "adopted": false,
    "canonical_term": "signals",
    "category": "unclassified",
    "document_frequency": 10,
    "evidence_ids": [
      "evidence-01834",
      "evidence-01835",
      "evidence-01836",
      "evidence-01837",
      "evidence-01838",
      "evidence-01839",
      "evidence-01840",
      "evidence-01841",
      "evidence-01842",
      "evidence-01843",
      "evidence-01844",
      "evidence-01845"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W2076757040",
      "https://openalex.org/W2086303648",
      "https://openalex.org/W2091022037",
      "https://openalex.org/W3013651137",
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402054497",
      "https://openalex.org/W4402270704",
      "https://openalex.org/W4416190202",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "signals",
    "term_id": "term-01409"
  },
  {
    "adopted": false,
    "canonical_term": "signals often",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01852"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "signals often",
    "term_id": "term-01416"
  },
  {
    "adopted": false,
    "canonical_term": "signals often make",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01853"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "signals often make",
    "term_id": "term-01417"
  },
  {
    "adopted": false,
    "canonical_term": "since",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01872"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "since",
    "term_id": "term-01431"
  },
  {
    "adopted": false,
    "canonical_term": "subjects",
    "category": "unclassified",
    "document_frequency": 5,
    "evidence_ids": [
      "evidence-01927",
      "evidence-01928",
      "evidence-01929",
      "evidence-01930",
      "evidence-01931"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4284878820",
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402054497",
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "subjects",
    "term_id": "term-01476"
  },
  {
    "adopted": false,
    "canonical_term": "subjects and picking",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01932"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "subjects and picking",
    "term_id": "term-01477"
  },
  {
    "adopted": false,
    "canonical_term": "surface",
    "category": "unclassified",
    "document_frequency": 12,
    "evidence_ids": [
      "evidence-01946",
      "evidence-01947",
      "evidence-01948",
      "evidence-01949",
      "evidence-01950",
      "evidence-01951",
      "evidence-01952",
      "evidence-01953",
      "evidence-01954",
      "evidence-01955",
      "evidence-01956",
      "evidence-01957",
      "evidence-01958",
      "evidence-01959",
      "evidence-01960",
      "evidence-01961"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W1918406696",
      "https://openalex.org/W2086303648",
      "https://openalex.org/W2091022037",
      "https://openalex.org/W3013651137",
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4284878820",
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402054497",
      "https://openalex.org/W4402270704",
      "https://openalex.org/W4407450426",
      "https://openalex.org/W4416190202",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "surface",
    "term_id": "term-01491"
  },
  {
    "adopted": false,
    "canonical_term": "surface electromyography",
    "category": "unclassified",
    "document_frequency": 14,
    "evidence_ids": [
      "evidence-01964",
      "evidence-01965",
      "evidence-01966",
      "evidence-01967",
      "evidence-01968",
      "evidence-01969",
      "evidence-01970",
      "evidence-01971",
      "evidence-01972",
      "evidence-01973",
      "evidence-01974",
      "evidence-01975",
      "evidence-01976",
      "evidence-01977"
    ],
    "evidence_status": "database_assigned",
    "paper_ids": [
      "https://openalex.org/W1918406696",
      "https://openalex.org/W2072588720",
      "https://openalex.org/W2076757040",
      "https://openalex.org/W2086303648",
      "https://openalex.org/W2091022037",
      "https://openalex.org/W3013651137",
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4284878820",
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402054497",
      "https://openalex.org/W4402270704",
      "https://openalex.org/W4407450426",
      "https://openalex.org/W4416190202",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "term": "surface electromyography",
    "term_id": "term-01494"
  },
  {
    "adopted": false,
    "canonical_term": "surface electromyography",
    "category": "unclassified",
    "document_frequency": 11,
    "evidence_ids": [
      "evidence-01978",
      "evidence-01979",
      "evidence-01980",
      "evidence-01981",
      "evidence-01982",
      "evidence-01983",
      "evidence-01984",
      "evidence-01985",
      "evidence-01986",
      "evidence-01987",
      "evidence-01988",
      "evidence-01989",
      "evidence-01990",
      "evidence-01991"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W1918406696",
      "https://openalex.org/W2086303648",
      "https://openalex.org/W3013651137",
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4284878820",
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402054497",
      "https://openalex.org/W4402270704",
      "https://openalex.org/W4407450426",
      "https://openalex.org/W4416190202",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "surface electromyography",
    "term_id": "term-01495"
  },
  {
    "adopted": false,
    "canonical_term": "tcn",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02010"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "tcn",
    "term_id": "term-01513"
  },
  {
    "adopted": false,
    "canonical_term": "tcn can",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02011"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "tcn can",
    "term_id": "term-01514"
  },
  {
    "adopted": false,
    "canonical_term": "tcn can sense",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02012"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "tcn can sense",
    "term_id": "term-01515"
  },
  {
    "adopted": false,
    "canonical_term": "tcn to capture",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02013"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "tcn to capture",
    "term_id": "term-01516"
  },
  {
    "adopted": false,
    "canonical_term": "tcn-lstm",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02014"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "tcn-lstm",
    "term_id": "term-01517"
  },
  {
    "adopted": false,
    "canonical_term": "tcn-lstm hybrid",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02015"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "tcn-lstm hybrid",
    "term_id": "term-01518"
  },
  {
    "adopted": false,
    "canonical_term": "tcn-lstm hybrid model",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02016"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "tcn-lstm hybrid model",
    "term_id": "term-01519"
  },
  {
    "adopted": false,
    "canonical_term": "temporal",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-02018",
      "evidence-02019"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "temporal",
    "term_id": "term-01521"
  },
  {
    "adopted": false,
    "canonical_term": "temporal convolutional",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02020"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "temporal convolutional",
    "term_id": "term-01522"
  },
  {
    "adopted": false,
    "canonical_term": "temporal convolutional network",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02021"
    ],
    "evidence_status": "database_assigned",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "term": "temporal convolutional network",
    "term_id": "term-01523"
  },
  {
    "adopted": false,
    "canonical_term": "temporal convolutional network",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02022"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "temporal convolutional network",
    "term_id": "term-01524"
  },
  {
    "adopted": false,
    "canonical_term": "temporal memory",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02023"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "temporal memory",
    "term_id": "term-01525"
  },
  {
    "adopted": false,
    "canonical_term": "temporal memory capability",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02024"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "temporal memory capability",
    "term_id": "term-01526"
  },
  {
    "adopted": false,
    "canonical_term": "three",
    "category": "unclassified",
    "document_frequency": 3,
    "evidence_ids": [
      "evidence-02049",
      "evidence-02050",
      "evidence-02051"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4402054497",
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "three",
    "term_id": "term-01548"
  },
  {
    "adopted": false,
    "canonical_term": "three types",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02057"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "three types",
    "term_id": "term-01554"
  },
  {
    "adopted": false,
    "canonical_term": "types",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02121"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "types",
    "term_id": "term-01606"
  },
  {
    "adopted": false,
    "canonical_term": "types of wrist-dependent",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02122"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "types of wrist-dependent",
    "term_id": "term-01607"
  },
  {
    "adopted": false,
    "canonical_term": "ulnar",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02123"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "ulnar",
    "term_id": "term-01608"
  },
  {
    "adopted": false,
    "canonical_term": "ulnar deviation",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02124"
    ],
    "evidence_status": "database_assigned",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "term": "ulnar deviation",
    "term_id": "term-01609"
  },
  {
    "adopted": false,
    "canonical_term": "ulnar deviation",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02125"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "ulnar deviation",
    "term_id": "term-01610"
  },
  {
    "adopted": false,
    "canonical_term": "unfortunately",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02128"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "unfortunately",
    "term_id": "term-01613"
  },
  {
    "adopted": false,
    "canonical_term": "up",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02141"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "up",
    "term_id": "term-01626"
  },
  {
    "adopted": false,
    "canonical_term": "validated",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02158"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "validated",
    "term_id": "term-01639"
  },
  {
    "adopted": false,
    "canonical_term": "validated the proposed",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02159"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "validated the proposed",
    "term_id": "term-01640"
  },
  {
    "adopted": false,
    "canonical_term": "wf",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02197"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "wf",
    "term_id": "term-01676"
  },
  {
    "adopted": false,
    "canonical_term": "where",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02202"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "where",
    "term_id": "term-01680"
  },
  {
    "adopted": false,
    "canonical_term": "where the tcn",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02203"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "where the tcn",
    "term_id": "term-01681"
  },
  {
    "adopted": false,
    "canonical_term": "while",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02216"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "while",
    "term_id": "term-01691"
  },
  {
    "adopted": false,
    "canonical_term": "while lstm",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02217"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "while lstm",
    "term_id": "term-01692"
  },
  {
    "adopted": false,
    "canonical_term": "wrist",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02231",
      "evidence-02232"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "wrist",
    "term_id": "term-01705"
  },
  {
    "adopted": false,
    "canonical_term": "wrist flexion",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02233"
    ],
    "evidence_status": "database_assigned",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "term": "wrist flexion",
    "term_id": "term-01706"
  },
  {
    "adopted": false,
    "canonical_term": "wrist flexion",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02234"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "wrist flexion",
    "term_id": "term-01707"
  },
  {
    "adopted": false,
    "canonical_term": "wrist joint",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02235"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "wrist joint",
    "term_id": "term-01708"
  },
  {
    "adopted": false,
    "canonical_term": "wrist joint angles",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02236"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "wrist joint angles",
    "term_id": "term-01709"
  },
  {
    "adopted": false,
    "canonical_term": "wrist motion",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02238"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "wrist motion",
    "term_id": "term-01711"
  },
  {
    "adopted": false,
    "canonical_term": "wrist motion angle",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02239"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "wrist motion angle",
    "term_id": "term-01712"
  },
  {
    "adopted": false,
    "canonical_term": "wrist ulnar",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02240"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "wrist ulnar",
    "term_id": "term-01713"
  },
  {
    "adopted": false,
    "canonical_term": "wrist-dependent",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02241"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "wrist-dependent",
    "term_id": "term-01714"
  },
  {
    "adopted": false,
    "canonical_term": "wrist-dependent movements",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02242"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402054497"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "wrist-dependent movements",
    "term_id": "term-01715"
  }
]
```

## 证据与引用 URL
```
[
  {
    "evidence_id": "evidence-00030",
    "evidence_level": "A",
    "excerpt": "ability",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00102",
    "evidence_level": "A",
    "excerpt": "angle",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00110",
    "evidence_level": "A",
    "excerpt": "angle changes",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00111",
    "evidence_level": "A",
    "excerpt": "angle changes based",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00114",
    "evidence_level": "A",
    "excerpt": "angle estimation",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00115",
    "evidence_level": "A",
    "excerpt": "angle estimation difficult",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00121",
    "evidence_level": "A",
    "excerpt": "angle prediction",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00123",
    "evidence_level": "A",
    "excerpt": "angle prediction model",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00137",
    "evidence_level": "A",
    "excerpt": "Angles",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00176",
    "evidence_level": "A",
    "excerpt": "available",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00177",
    "evidence_level": "A",
    "excerpt": "available Ninapro",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00178",
    "evidence_level": "A",
    "excerpt": "available Ninapro DB1",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00185",
    "evidence_level": "A",
    "excerpt": "based",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00188",
    "evidence_level": "A",
    "excerpt": "based on sEMG",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00198",
    "evidence_level": "A",
    "excerpt": "better",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00200",
    "evidence_level": "A",
    "excerpt": "better prediction",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00235",
    "evidence_level": "A",
    "excerpt": "can",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00236",
    "evidence_level": "A",
    "excerpt": "can make",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00237",
    "evidence_level": "A",
    "excerpt": "can make up",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00240",
    "evidence_level": "A",
    "excerpt": "can sense",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00241",
    "evidence_level": "A",
    "excerpt": "can sense local",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00242",
    "evidence_level": "A",
    "excerpt": "capability",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00245",
    "evidence_level": "A",
    "excerpt": "capture",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00246",
    "evidence_level": "A",
    "excerpt": "capture the long-term",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00263",
    "evidence_level": "A",
    "excerpt": "changes",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00264",
    "evidence_level": "A",
    "excerpt": "changes based",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00296",
    "evidence_level": "A",
    "excerpt": "combines",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00297",
    "evidence_level": "A",
    "excerpt": "combines a temporal",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00313",
    "evidence_level": "A",
    "excerpt": "conceals",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00314",
    "evidence_level": "A",
    "excerpt": "conceals human",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00315",
    "evidence_level": "A",
    "excerpt": "conceals human movement",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00330",
    "evidence_level": "A",
    "excerpt": "continuous",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00331",
    "evidence_level": "A",
    "excerpt": "Continuous",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00335",
    "evidence_level": "A",
    "excerpt": "continuous estimation",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00336",
    "evidence_level": "A",
    "excerpt": "Continuous Estimation",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00363",
    "evidence_level": "A",
    "excerpt": "convolutional",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00365",
    "evidence_level": "A",
    "excerpt": "convolutional network",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00401",
    "evidence_level": "A",
    "excerpt": "dataset",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00404",
    "evidence_level": "A",
    "excerpt": "dataset by selecting",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00406",
    "evidence_level": "A",
    "excerpt": "DB1",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00407",
    "evidence_level": "A",
    "excerpt": "DB1 dataset",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00415",
    "evidence_level": "A",
    "excerpt": "deeper",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00416",
    "evidence_level": "A",
    "excerpt": "deeper information",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00425",
    "evidence_level": "A",
    "excerpt": "dependence",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00439",
    "evidence_level": "A",
    "excerpt": "deviation",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00450",
    "evidence_level": "A",
    "excerpt": "difficult",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00461",
    "evidence_level": "A",
    "excerpt": "distinct",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00462",
    "evidence_level": "A",
    "excerpt": "distinct physiological",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00463",
    "evidence_level": "A",
    "excerpt": "distinct physiological electrical",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00517",
    "evidence_level": "A",
    "excerpt": "eight",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00518",
    "evidence_level": "A",
    "excerpt": "eight subjects",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00528",
    "evidence_level": "A",
    "excerpt": "electrical",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00529",
    "evidence_level": "A",
    "excerpt": "electrical signal",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00554",
    "evidence_level": "A",
    "excerpt": "electromyography",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00627",
    "evidence_level": "A",
    "excerpt": "estimation",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00628",
    "evidence_level": "A",
    "excerpt": "Estimation",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00630",
    "evidence_level": "A",
    "excerpt": "estimation difficult",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00633",
    "evidence_level": "A",
    "excerpt": "estimation of wrist",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00634",
    "evidence_level": "A",
    "excerpt": "Estimation of Wrist",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00640",
    "evidence_level": "A",
    "excerpt": "excellent",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00641",
    "evidence_level": "A",
    "excerpt": "excellent temporal",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00642",
    "evidence_level": "A",
    "excerpt": "excellent temporal memory",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00701",
    "evidence_level": "A",
    "excerpt": "features",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00706",
    "evidence_level": "A",
    "excerpt": "features of sEMG",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00725",
    "evidence_level": "A",
    "excerpt": "first",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00728",
    "evidence_level": "A",
    "excerpt": "first eight",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00729",
    "evidence_level": "A",
    "excerpt": "first eight subjects",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00738",
    "evidence_level": "A",
    "excerpt": "flexion",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00846",
    "evidence_level": "A",
    "excerpt": "HMIs",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00857",
    "evidence_level": "A",
    "excerpt": "human",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00867",
    "evidence_level": "A",
    "excerpt": "human movement",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00868",
    "evidence_level": "A",
    "excerpt": "human movement intention",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00874",
    "evidence_level": "A",
    "excerpt": "human-machine interaction",
    "locator": "database_keywords",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00880",
    "evidence_level": "A",
    "excerpt": "Hybrid",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00882",
    "evidence_level": "A",
    "excerpt": "Hybrid Model",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00914",
    "evidence_level": "A",
    "excerpt": "information",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00915",
    "evidence_level": "A",
    "excerpt": "information and mine",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00936",
    "evidence_level": "A",
    "excerpt": "intention",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00937",
    "evidence_level": "A",
    "excerpt": "intention and muscle",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00945",
    "evidence_level": "A",
    "excerpt": "interactions",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00969",
    "evidence_level": "A",
    "excerpt": "its",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00972",
    "evidence_level": "A",
    "excerpt": "its excellent",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00973",
    "evidence_level": "A",
    "excerpt": "its excellent temporal",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00988",
    "evidence_level": "A",
    "excerpt": "joint",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00989",
    "evidence_level": "A",
    "excerpt": "Joint",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01004",
    "evidence_level": "A",
    "excerpt": "joint angle",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01014",
    "evidence_level": "A",
    "excerpt": "joint angle estimation",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01017",
    "evidence_level": "A",
    "excerpt": "joint angle prediction",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01034",
    "evidence_level": "A",
    "excerpt": "Joint Angles",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01091",
    "evidence_level": "A",
    "excerpt": "lack",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01119",
    "evidence_level": "A",
    "excerpt": "local",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01120",
    "evidence_level": "A",
    "excerpt": "local information",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01126",
    "evidence_level": "A",
    "excerpt": "long",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01129",
    "evidence_level": "A",
    "excerpt": "long short-term",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01132",
    "evidence_level": "A",
    "excerpt": "long short-term memory",
    "locator": "database_keywords",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01133",
    "evidence_level": "A",
    "excerpt": "long short-term memory",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01138",
    "evidence_level": "A",
    "excerpt": "long-term",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01139",
    "evidence_level": "A",
    "excerpt": "long-term dependence",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01161",
    "evidence_level": "A",
    "excerpt": "LSTM",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01167",
    "evidence_level": "A",
    "excerpt": "machine",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01169",
    "evidence_level": "A",
    "excerpt": "machine interactions",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01172",
    "evidence_level": "A",
    "excerpt": "make",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01173",
    "evidence_level": "A",
    "excerpt": "make joint",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01174",
    "evidence_level": "A",
    "excerpt": "make joint angle",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01175",
    "evidence_level": "A",
    "excerpt": "make up",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01221",
    "evidence_level": "A",
    "excerpt": "memory",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01225",
    "evidence_level": "A",
    "excerpt": "memory capability",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01232",
    "evidence_level": "A",
    "excerpt": "mine",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01233",
    "evidence_level": "A",
    "excerpt": "mine the deeper",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01246",
    "evidence_level": "A",
    "excerpt": "model",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01247",
    "evidence_level": "A",
    "excerpt": "Model",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01260",
    "evidence_level": "A",
    "excerpt": "model combines",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01261",
    "evidence_level": "A",
    "excerpt": "Model for sEMG-Based",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01295",
    "evidence_level": "A",
    "excerpt": "motion",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01299",
    "evidence_level": "A",
    "excerpt": "motion angle",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01300",
    "evidence_level": "A",
    "excerpt": "motion angle changes",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01316",
    "evidence_level": "A",
    "excerpt": "movement",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01319",
    "evidence_level": "A",
    "excerpt": "movement intention",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01325",
    "evidence_level": "A",
    "excerpt": "movements",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01338",
    "evidence_level": "A",
    "excerpt": "muscle",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01348",
    "evidence_level": "A",
    "excerpt": "muscle information",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01362",
    "evidence_level": "A",
    "excerpt": "network",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01384",
    "evidence_level": "A",
    "excerpt": "Ninapro",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01386",
    "evidence_level": "A",
    "excerpt": "Ninapro DB1",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01387",
    "evidence_level": "A",
    "excerpt": "Ninapro DB1 dataset",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01396",
    "evidence_level": "A",
    "excerpt": "non-smooth",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01397",
    "evidence_level": "A",
    "excerpt": "non-smooth features",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01398",
    "evidence_level": "A",
    "excerpt": "nonlinear",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01399",
    "evidence_level": "A",
    "excerpt": "nonlinear and non-smooth",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01409",
    "evidence_level": "A",
    "excerpt": "novel",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01410",
    "evidence_level": "A",
    "excerpt": "Novel",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01416",
    "evidence_level": "A",
    "excerpt": "Novel TCN-LSTM",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01417",
    "evidence_level": "A",
    "excerpt": "Novel TCN-LSTM Hybrid",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01431",
    "evidence_level": "A",
    "excerpt": "offers",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01432",
    "evidence_level": "A",
    "excerpt": "offers a novel",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01433",
    "evidence_level": "A",
    "excerpt": "often",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01435",
    "evidence_level": "A",
    "excerpt": "often make",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01436",
    "evidence_level": "A",
    "excerpt": "often make joint",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01458",
    "evidence_level": "A",
    "excerpt": "paper",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01459",
    "evidence_level": "A",
    "excerpt": "paper proposes",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01502",
    "evidence_level": "A",
    "excerpt": "physiological",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01503",
    "evidence_level": "A",
    "excerpt": "physiological electrical",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01504",
    "evidence_level": "A",
    "excerpt": "physiological electrical signal",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01505",
    "evidence_level": "A",
    "excerpt": "picking",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01506",
    "evidence_level": "A",
    "excerpt": "picking three",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01507",
    "evidence_level": "A",
    "excerpt": "picking three types",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01548",
    "evidence_level": "A",
    "excerpt": "prediction",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01560",
    "evidence_level": "A",
    "excerpt": "prediction model",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01591",
    "evidence_level": "A",
    "excerpt": "proposed",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01594",
    "evidence_level": "A",
    "excerpt": "proposed model",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01595",
    "evidence_level": "A",
    "excerpt": "proposed model combines",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01597",
    "evidence_level": "A",
    "excerpt": "proposes",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01599",
    "evidence_level": "A",
    "excerpt": "proposes a joint",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01611",
    "evidence_level": "A",
    "excerpt": "publicly",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01615",
    "evidence_level": "A",
    "excerpt": "publicly available",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01616",
    "evidence_level": "A",
    "excerpt": "publicly available Ninapro",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01718",
    "evidence_level": "A",
    "excerpt": "resulting",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01761",
    "evidence_level": "A",
    "excerpt": "selecting",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01762",
    "evidence_level": "A",
    "excerpt": "selecting the first",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01768",
    "evidence_level": "A",
    "excerpt": "sEMG",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01793",
    "evidence_level": "A",
    "excerpt": "sEMG signals",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01796",
    "evidence_level": "A",
    "excerpt": "sEMG signals often",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01799",
    "evidence_level": "A",
    "excerpt": "sEMG-Based",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01801",
    "evidence_level": "A",
    "excerpt": "sEMG-Based Continuous",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01803",
    "evidence_level": "A",
    "excerpt": "sEMG-Based Continuous Estimation",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01808",
    "evidence_level": "A",
    "excerpt": "sense",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01809",
    "evidence_level": "A",
    "excerpt": "sense local",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01810",
    "evidence_level": "A",
    "excerpt": "sense local information",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01815",
    "evidence_level": "A",
    "excerpt": "short-term",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01819",
    "evidence_level": "A",
    "excerpt": "short-term memory",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01829",
    "evidence_level": "A",
    "excerpt": "signal",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01832",
    "evidence_level": "A",
    "excerpt": "signal that conceals",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01840",
    "evidence_level": "A",
    "excerpt": "signals",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01852",
    "evidence_level": "A",
    "excerpt": "signals often",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01853",
    "evidence_level": "A",
    "excerpt": "signals often make",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01872",
    "evidence_level": "A",
    "excerpt": "since",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01930",
    "evidence_level": "A",
    "excerpt": "subjects",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01932",
    "evidence_level": "A",
    "excerpt": "subjects and picking",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01957",
    "evidence_level": "A",
    "excerpt": "Surface",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01973",
    "evidence_level": "A",
    "excerpt": "surface electromyography",
    "locator": "database_keywords",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01987",
    "evidence_level": "A",
    "excerpt": "Surface electromyography",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02010",
    "evidence_level": "A",
    "excerpt": "TCN",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02011",
    "evidence_level": "A",
    "excerpt": "TCN can",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02012",
    "evidence_level": "A",
    "excerpt": "TCN can sense",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02013",
    "evidence_level": "A",
    "excerpt": "TCN to capture",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02014",
    "evidence_level": "A",
    "excerpt": "TCN-LSTM",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02015",
    "evidence_level": "A",
    "excerpt": "TCN-LSTM Hybrid",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02016",
    "evidence_level": "A",
    "excerpt": "TCN-LSTM Hybrid Model",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02018",
    "evidence_level": "A",
    "excerpt": "temporal",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02020",
    "evidence_level": "A",
    "excerpt": "temporal convolutional",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02021",
    "evidence_level": "A",
    "excerpt": "temporal convolutional network",
    "locator": "database_keywords",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02022",
    "evidence_level": "A",
    "excerpt": "temporal convolutional network",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02023",
    "evidence_level": "A",
    "excerpt": "temporal memory",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02024",
    "evidence_level": "A",
    "excerpt": "temporal memory capability",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02050",
    "evidence_level": "A",
    "excerpt": "three",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02057",
    "evidence_level": "A",
    "excerpt": "three types",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02121",
    "evidence_level": "A",
    "excerpt": "types",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02122",
    "evidence_level": "A",
    "excerpt": "types of wrist-dependent",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02123",
    "evidence_level": "A",
    "excerpt": "ulnar",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02124",
    "evidence_level": "A",
    "excerpt": "ulnar deviation",
    "locator": "database_keywords",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02125",
    "evidence_level": "A",
    "excerpt": "ulnar deviation",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02128",
    "evidence_level": "A",
    "excerpt": "Unfortunately",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02141",
    "evidence_level": "A",
    "excerpt": "up",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02158",
    "evidence_level": "A",
    "excerpt": "validated",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02159",
    "evidence_level": "A",
    "excerpt": "validated the proposed",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02197",
    "evidence_level": "A",
    "excerpt": "WF",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02202",
    "evidence_level": "A",
    "excerpt": "where",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02203",
    "evidence_level": "A",
    "excerpt": "where the TCN",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02216",
    "evidence_level": "A",
    "excerpt": "while",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02217",
    "evidence_level": "A",
    "excerpt": "while LSTM",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02231",
    "evidence_level": "A",
    "excerpt": "wrist",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02232",
    "evidence_level": "A",
    "excerpt": "Wrist",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02233",
    "evidence_level": "A",
    "excerpt": "wrist flexion",
    "locator": "database_keywords",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02234",
    "evidence_level": "A",
    "excerpt": "wrist flexion",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02235",
    "evidence_level": "A",
    "excerpt": "Wrist Joint",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02236",
    "evidence_level": "A",
    "excerpt": "Wrist Joint Angles",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02238",
    "evidence_level": "A",
    "excerpt": "wrist motion",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02239",
    "evidence_level": "A",
    "excerpt": "wrist motion angle",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02240",
    "evidence_level": "A",
    "excerpt": "wrist ulnar",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02241",
    "evidence_level": "A",
    "excerpt": "wrist-dependent",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02242",
    "evidence_level": "A",
    "excerpt": "wrist-dependent movements",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402054497",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402054497",
    "supports": "Field observation only; not semantic equivalence or relevance."
  }
]
```

## 译文
未分析，留空供人工填写。

## 创新点
未分析，留空供人工填写。

## 用户笔记
