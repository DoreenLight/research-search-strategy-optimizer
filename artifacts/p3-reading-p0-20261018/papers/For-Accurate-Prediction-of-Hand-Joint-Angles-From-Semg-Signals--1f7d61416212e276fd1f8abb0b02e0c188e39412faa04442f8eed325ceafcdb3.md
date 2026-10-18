---
{
  "authors": [
    "Anita Sadat Sadati Rostami",
    "Alireza Nazari",
    "Mohammad Reza Nayeri"
  ],
  "case_id": "semg-joint-angle",
  "doi": "https://doi.org/10.1109/icbme68496.2025.11392281",
  "human_judgments": [],
  "innovation_points": "",
  "model_judgments": [],
  "model_promoted_to_human": false,
  "paper_id": "https://openalex.org/W7133186646",
  "pmid": null,
  "publication_year": 2025,
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
  "source_title": "National and International Iranian Conference on Biomedical Engineering (ICBME)",
  "source_url": "https://openalex.org/W7133186646",
  "title": "For Accurate Prediction of Hand Joint Angles From Semg Signals",
  "translation": ""
}
---

# 阅读任务

状态默认为 **待确认**；可人工改为 **待读** / **已读**。模型相关性不代表人工确认。

## 标题
```
For Accurate Prediction of Hand Joint Angles From Semg Signals
```

## 作者
```
[
  "Anita Sadat Sadati Rostami",
  "Alireza Nazari",
  "Mohammad Reza Nayeri"
]
```

## 年份 / DOI / PMID
```
{
  "doi": "https://doi.org/10.1109/icbme68496.2025.11392281",
  "pmid": null,
  "publication_year": 2025
}
```

## 摘要
```
Surface electromyography (sEMG) signals offer a non-invasive pathway for advancing human-machine interfaces, yet predicting continuous hand joint angles is challenging due to signal variability and complexity. This study proposes a novel hybrid model integrating bidirectional long short-term memory (BiLSTM) and Transformer architectures to accurately predict 10 degrees of freedom (DOF) in hand joints-metacarpophalangeal (MCP) and proximal interphalangeal (PIP)-using the NinaPro DB8 dataset. The model captures temporal muscle dynamics through BiLSTM and models long-range dependencies with a Transformer encoder, enhanced by residual connections for training stability. To enhance efficiency, a comprehensive preprocessing pipeline extracts time-domain features, applies dimensionality reduction, and employs standardization to optimize performance. A custom regularized loss function mitigates overfitting, ensuring robust predictions. The model achieves a mean absolute error of 8.2° across all 10 joints, with 6.8° for metacarpophalangeal joints and 9.7° for proximal interphalangeal joints, outperforming prior benchmarks focused on fewer aggregated joint angles. This approach enables precise, naturalistic hand pose reconstruction for prosthetic control, offering scalability and personalization for rehabilitation applications.
```

## 来源
```
{
  "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
  "source_title": "National and International Iranian Conference on Biomedical Engineering (ICBME)",
  "source_url": "https://openalex.org/W7133186646"
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
    "canonical_term": "10",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00006",
      "evidence-00007"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "10",
    "term_id": "term-00005"
  },
  {
    "adopted": false,
    "canonical_term": "10 degrees",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00008"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "10 degrees",
    "term_id": "term-00006"
  },
  {
    "adopted": false,
    "canonical_term": "8",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00026"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "8",
    "term_id": "term-00023"
  },
  {
    "adopted": false,
    "canonical_term": "absolute",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00031",
      "evidence-00032"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "absolute",
    "term_id": "term-00027"
  },
  {
    "adopted": false,
    "canonical_term": "absolute error",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00033",
      "evidence-00034"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "absolute error",
    "term_id": "term-00028"
  },
  {
    "adopted": false,
    "canonical_term": "accurate",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00042",
      "evidence-00043"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4284878820",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "accurate",
    "term_id": "term-00033"
  },
  {
    "adopted": false,
    "canonical_term": "accurate prediction",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00045"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "accurate prediction",
    "term_id": "term-00035"
  },
  {
    "adopted": false,
    "canonical_term": "accurately",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00046",
      "evidence-00047"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "accurately",
    "term_id": "term-00036"
  },
  {
    "adopted": false,
    "canonical_term": "accurately predict",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00048"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "accurately predict",
    "term_id": "term-00037"
  },
  {
    "adopted": false,
    "canonical_term": "accurately predict 10",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00049"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "accurately predict 10",
    "term_id": "term-00038"
  },
  {
    "adopted": false,
    "canonical_term": "achieves",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00050"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "achieves",
    "term_id": "term-00039"
  },
  {
    "adopted": false,
    "canonical_term": "achieves a mean",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00051"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "achieves a mean",
    "term_id": "term-00040"
  },
  {
    "adopted": false,
    "canonical_term": "advancing",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00070"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "advancing",
    "term_id": "term-00059"
  },
  {
    "adopted": false,
    "canonical_term": "advancing human-machine",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00071"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "advancing human-machine",
    "term_id": "term-00060"
  },
  {
    "adopted": false,
    "canonical_term": "advancing human-machine interfaces",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00072"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "advancing human-machine interfaces",
    "term_id": "term-00061"
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
    "canonical_term": "angles from semg",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00150"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "angles from semg",
    "term_id": "term-00105"
  },
  {
    "adopted": false,
    "canonical_term": "angles is challenging",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00151"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "angles is challenging",
    "term_id": "term-00106"
  },
  {
    "adopted": false,
    "canonical_term": "applies",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00165"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "applies",
    "term_id": "term-00120"
  },
  {
    "adopted": false,
    "canonical_term": "applies dimensionality",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00166"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "applies dimensionality",
    "term_id": "term-00121"
  },
  {
    "adopted": false,
    "canonical_term": "applies dimensionality reduction",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00167"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "applies dimensionality reduction",
    "term_id": "term-00122"
  },
  {
    "adopted": false,
    "canonical_term": "architectures",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00168"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "architectures",
    "term_id": "term-00123"
  },
  {
    "adopted": false,
    "canonical_term": "architectures to accurately",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00169"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "architectures to accurately",
    "term_id": "term-00124"
  },
  {
    "adopted": false,
    "canonical_term": "bidirectional",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00212",
      "evidence-00213"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "bidirectional",
    "term_id": "term-00152"
  },
  {
    "adopted": false,
    "canonical_term": "bidirectional long",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00214",
      "evidence-00215"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "bidirectional long",
    "term_id": "term-00153"
  },
  {
    "adopted": false,
    "canonical_term": "bidirectional long short-term",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00216",
      "evidence-00217"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "bidirectional long short-term",
    "term_id": "term-00154"
  },
  {
    "adopted": false,
    "canonical_term": "bilstm",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00220"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "bilstm",
    "term_id": "term-00157"
  },
  {
    "adopted": false,
    "canonical_term": "bilstm and models",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00221"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "bilstm and models",
    "term_id": "term-00158"
  },
  {
    "adopted": false,
    "canonical_term": "captures",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00247"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "captures",
    "term_id": "term-00183"
  },
  {
    "adopted": false,
    "canonical_term": "captures temporal",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00248"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "captures temporal",
    "term_id": "term-00184"
  },
  {
    "adopted": false,
    "canonical_term": "captures temporal muscle",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00249"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "captures temporal muscle",
    "term_id": "term-00185"
  },
  {
    "adopted": false,
    "canonical_term": "challenging",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00257"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "challenging",
    "term_id": "term-00193"
  },
  {
    "adopted": false,
    "canonical_term": "challenging due",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00258"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "challenging due",
    "term_id": "term-00194"
  },
  {
    "adopted": false,
    "canonical_term": "complexity",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00307"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "complexity",
    "term_id": "term-00236"
  },
  {
    "adopted": false,
    "canonical_term": "comprehensive",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00308",
      "evidence-00309"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3121018641",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "comprehensive",
    "term_id": "term-00237"
  },
  {
    "adopted": false,
    "canonical_term": "comprehensive preprocessing",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00311"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "comprehensive preprocessing",
    "term_id": "term-00239"
  },
  {
    "adopted": false,
    "canonical_term": "comprehensive preprocessing pipeline",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00312"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "comprehensive preprocessing pipeline",
    "term_id": "term-00240"
  },
  {
    "adopted": false,
    "canonical_term": "connections",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00320"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "connections",
    "term_id": "term-00248"
  },
  {
    "adopted": false,
    "canonical_term": "connections for training",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00321"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "connections for training",
    "term_id": "term-00249"
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
    "canonical_term": "continuous hand",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00337"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "continuous hand",
    "term_id": "term-00256"
  },
  {
    "adopted": false,
    "canonical_term": "continuous hand joint",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00338"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "continuous hand joint",
    "term_id": "term-00257"
  },
  {
    "adopted": false,
    "canonical_term": "custom",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00395"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "custom",
    "term_id": "term-00299"
  },
  {
    "adopted": false,
    "canonical_term": "custom regularized",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00396"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "custom regularized",
    "term_id": "term-00300"
  },
  {
    "adopted": false,
    "canonical_term": "custom regularized loss",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00397"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "custom regularized loss",
    "term_id": "term-00301"
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
    "canonical_term": "db8",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00408"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "db8",
    "term_id": "term-00310"
  },
  {
    "adopted": false,
    "canonical_term": "db8 dataset",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00409"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "db8 dataset",
    "term_id": "term-00311"
  },
  {
    "adopted": false,
    "canonical_term": "degrees",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00417"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "degrees",
    "term_id": "term-00319"
  },
  {
    "adopted": false,
    "canonical_term": "degrees of freedom",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00418"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "degrees of freedom",
    "term_id": "term-00320"
  },
  {
    "adopted": false,
    "canonical_term": "dependencies",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00426"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "dependencies",
    "term_id": "term-00327"
  },
  {
    "adopted": false,
    "canonical_term": "dimensionality",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00452"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "dimensionality",
    "term_id": "term-00350"
  },
  {
    "adopted": false,
    "canonical_term": "dimensionality reduction",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00453"
    ],
    "evidence_status": "database_assigned",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "term": "dimensionality reduction",
    "term_id": "term-00351"
  },
  {
    "adopted": false,
    "canonical_term": "dimensionality reduction",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00454"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "dimensionality reduction",
    "term_id": "term-00352"
  },
  {
    "adopted": false,
    "canonical_term": "dof",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00467"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "dof",
    "term_id": "term-00365"
  },
  {
    "adopted": false,
    "canonical_term": "due",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00470"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "due",
    "term_id": "term-00368"
  },
  {
    "adopted": false,
    "canonical_term": "due to signal",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00471"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "due to signal",
    "term_id": "term-00369"
  },
  {
    "adopted": false,
    "canonical_term": "dynamics",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00499",
      "evidence-00500"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3121018641",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "dynamics",
    "term_id": "term-00392"
  },
  {
    "adopted": false,
    "canonical_term": "dynamics through",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00501"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "dynamics through",
    "term_id": "term-00393"
  },
  {
    "adopted": false,
    "canonical_term": "dynamics through bilstm",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00502"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "dynamics through bilstm",
    "term_id": "term-00394"
  },
  {
    "adopted": false,
    "canonical_term": "efficiency",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00516"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "efficiency",
    "term_id": "term-00406"
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
    "canonical_term": "employs",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00584"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "employs",
    "term_id": "term-00454"
  },
  {
    "adopted": false,
    "canonical_term": "employs standardization",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00585"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "employs standardization",
    "term_id": "term-00455"
  },
  {
    "adopted": false,
    "canonical_term": "encoder",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00586"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "encoder",
    "term_id": "term-00456"
  },
  {
    "adopted": false,
    "canonical_term": "enhance",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00592"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "enhance",
    "term_id": "term-00461"
  },
  {
    "adopted": false,
    "canonical_term": "enhance efficiency",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00593"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "enhance efficiency",
    "term_id": "term-00462"
  },
  {
    "adopted": false,
    "canonical_term": "enhanced",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00594"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "enhanced",
    "term_id": "term-00463"
  },
  {
    "adopted": false,
    "canonical_term": "enhanced by residual",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00595"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "enhanced by residual",
    "term_id": "term-00464"
  },
  {
    "adopted": false,
    "canonical_term": "ensuring",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00596"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "ensuring",
    "term_id": "term-00465"
  },
  {
    "adopted": false,
    "canonical_term": "ensuring robust",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00597"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "ensuring robust",
    "term_id": "term-00466"
  },
  {
    "adopted": false,
    "canonical_term": "ensuring robust predictions",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00598"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "ensuring robust predictions",
    "term_id": "term-00467"
  },
  {
    "adopted": false,
    "canonical_term": "error",
    "category": "unclassified",
    "document_frequency": 5,
    "evidence_ids": [
      "evidence-00603",
      "evidence-00604",
      "evidence-00605",
      "evidence-00606",
      "evidence-00607"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402270704",
      "https://openalex.org/W4407450426",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "error",
    "term_id": "term-00472"
  },
  {
    "adopted": false,
    "canonical_term": "extracts",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00680"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "extracts",
    "term_id": "term-00531"
  },
  {
    "adopted": false,
    "canonical_term": "extracts time-domain",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00681"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "extracts time-domain",
    "term_id": "term-00532"
  },
  {
    "adopted": false,
    "canonical_term": "extracts time-domain features",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00682"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "extracts time-domain features",
    "term_id": "term-00533"
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
    "canonical_term": "freedom",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00755"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "freedom",
    "term_id": "term-00596"
  },
  {
    "adopted": false,
    "canonical_term": "function",
    "category": "unclassified",
    "document_frequency": 3,
    "evidence_ids": [
      "evidence-00758",
      "evidence-00759",
      "evidence-00760"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3013651137",
      "https://openalex.org/W4284878820",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "function",
    "term_id": "term-00599"
  },
  {
    "adopted": false,
    "canonical_term": "function mitigates",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00762"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "function mitigates",
    "term_id": "term-00601"
  },
  {
    "adopted": false,
    "canonical_term": "function mitigates overfitting",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00763"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "function mitigates overfitting",
    "term_id": "term-00602"
  },
  {
    "adopted": false,
    "canonical_term": "hand",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00791",
      "evidence-00792"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "hand",
    "term_id": "term-00625"
  },
  {
    "adopted": false,
    "canonical_term": "hand joint",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00793",
      "evidence-00794"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "hand joint",
    "term_id": "term-00626"
  },
  {
    "adopted": false,
    "canonical_term": "hand joint angles",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00795",
      "evidence-00796"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "hand joint angles",
    "term_id": "term-00627"
  },
  {
    "adopted": false,
    "canonical_term": "hand joints-metacarpophalangeal",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00797"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "hand joints-metacarpophalangeal",
    "term_id": "term-00628"
  },
  {
    "adopted": false,
    "canonical_term": "human-machine",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00873"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "human-machine",
    "term_id": "term-00689"
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
    "canonical_term": "human-machine interfaces",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00876"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "human-machine interfaces",
    "term_id": "term-00691"
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
    "canonical_term": "hybrid model integrating",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00884"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "hybrid model integrating",
    "term_id": "term-00697"
  },
  {
    "adopted": false,
    "canonical_term": "integrating",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00927"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "integrating",
    "term_id": "term-00735"
  },
  {
    "adopted": false,
    "canonical_term": "integrating bidirectional",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00928"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "integrating bidirectional",
    "term_id": "term-00736"
  },
  {
    "adopted": false,
    "canonical_term": "integrating bidirectional long",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00929"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "integrating bidirectional long",
    "term_id": "term-00737"
  },
  {
    "adopted": false,
    "canonical_term": "interfaces",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00946"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "interfaces",
    "term_id": "term-00751"
  },
  {
    "adopted": false,
    "canonical_term": "interphalangeal",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00947"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "interphalangeal",
    "term_id": "term-00752"
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
    "canonical_term": "joints-metacarpophalangeal",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01058"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "joints-metacarpophalangeal",
    "term_id": "term-00802"
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
    "canonical_term": "long-range",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01136"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "long-range",
    "term_id": "term-00857"
  },
  {
    "adopted": false,
    "canonical_term": "long-range dependencies",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01137"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "long-range dependencies",
    "term_id": "term-00858"
  },
  {
    "adopted": false,
    "canonical_term": "loss",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01142"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "loss",
    "term_id": "term-00863"
  },
  {
    "adopted": false,
    "canonical_term": "loss function",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01143"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "loss function",
    "term_id": "term-00864"
  },
  {
    "adopted": false,
    "canonical_term": "loss function mitigates",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01144"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "loss function mitigates",
    "term_id": "term-00865"
  },
  {
    "adopted": false,
    "canonical_term": "mcp",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01194"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "mcp",
    "term_id": "term-00909"
  },
  {
    "adopted": false,
    "canonical_term": "mean",
    "category": "unclassified",
    "document_frequency": 5,
    "evidence_ids": [
      "evidence-01195",
      "evidence-01196",
      "evidence-01197",
      "evidence-01198",
      "evidence-01199"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402270704",
      "https://openalex.org/W4407450426",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "mean",
    "term_id": "term-00910"
  },
  {
    "adopted": false,
    "canonical_term": "mean absolute",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01200",
      "evidence-01201"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "mean absolute",
    "term_id": "term-00911"
  },
  {
    "adopted": false,
    "canonical_term": "mean absolute error",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01202",
      "evidence-01203"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "mean absolute error",
    "term_id": "term-00912"
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
    "canonical_term": "metacarpophalangeal joint",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01229"
    ],
    "evidence_status": "database_assigned",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "term": "metacarpophalangeal joint",
    "term_id": "term-00932"
  },
  {
    "adopted": false,
    "canonical_term": "mitigates",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01234"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "mitigates",
    "term_id": "term-00937"
  },
  {
    "adopted": false,
    "canonical_term": "mitigates overfitting",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01235"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "mitigates overfitting",
    "term_id": "term-00938"
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
    "canonical_term": "model achieves",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01251"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "model achieves",
    "term_id": "term-00945"
  },
  {
    "adopted": false,
    "canonical_term": "model captures",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01257"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "model captures",
    "term_id": "term-00951"
  },
  {
    "adopted": false,
    "canonical_term": "model captures temporal",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01258"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "model captures temporal",
    "term_id": "term-00952"
  },
  {
    "adopted": false,
    "canonical_term": "model integrating",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01262"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "model integrating",
    "term_id": "term-00955"
  },
  {
    "adopted": false,
    "canonical_term": "model integrating bidirectional",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01263"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "model integrating bidirectional",
    "term_id": "term-00956"
  },
  {
    "adopted": false,
    "canonical_term": "models",
    "category": "unclassified",
    "document_frequency": 3,
    "evidence_ids": [
      "evidence-01275",
      "evidence-01276",
      "evidence-01277"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704",
      "https://openalex.org/W4407450426",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "models",
    "term_id": "term-00968"
  },
  {
    "adopted": false,
    "canonical_term": "models long-range",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01278"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "models long-range",
    "term_id": "term-00969"
  },
  {
    "adopted": false,
    "canonical_term": "models long-range dependencies",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01279"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "models long-range dependencies",
    "term_id": "term-00970"
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
    "canonical_term": "muscle dynamics",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01345"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "muscle dynamics",
    "term_id": "term-01016"
  },
  {
    "adopted": false,
    "canonical_term": "muscle dynamics through",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01346"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "muscle dynamics through",
    "term_id": "term-01017"
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
    "canonical_term": "ninapro db8",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01388"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "ninapro db8",
    "term_id": "term-01053"
  },
  {
    "adopted": false,
    "canonical_term": "ninapro db8 dataset",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01389"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "ninapro db8 dataset",
    "term_id": "term-01054"
  },
  {
    "adopted": false,
    "canonical_term": "non-invasive",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01394"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "non-invasive",
    "term_id": "term-01059"
  },
  {
    "adopted": false,
    "canonical_term": "non-invasive pathway",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01395"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "non-invasive pathway",
    "term_id": "term-01060"
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
    "canonical_term": "novel hybrid",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01412"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "novel hybrid",
    "term_id": "term-01074"
  },
  {
    "adopted": false,
    "canonical_term": "novel hybrid model",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01413"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "novel hybrid model",
    "term_id": "term-01075"
  },
  {
    "adopted": false,
    "canonical_term": "offer",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01429"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "offer",
    "term_id": "term-01091"
  },
  {
    "adopted": false,
    "canonical_term": "offer a non-invasive",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01430"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "offer a non-invasive",
    "term_id": "term-01092"
  },
  {
    "adopted": false,
    "canonical_term": "optimize",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01438"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "optimize",
    "term_id": "term-01099"
  },
  {
    "adopted": false,
    "canonical_term": "optimize performance",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01439"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "optimize performance",
    "term_id": "term-01100"
  },
  {
    "adopted": false,
    "canonical_term": "overfitting",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01445"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "overfitting",
    "term_id": "term-01106"
  },
  {
    "adopted": false,
    "canonical_term": "overfitting regularization",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01446"
    ],
    "evidence_status": "database_assigned",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "term": "overfitting regularization",
    "term_id": "term-01107"
  },
  {
    "adopted": false,
    "canonical_term": "pathway",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01465"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "pathway",
    "term_id": "term-01126"
  },
  {
    "adopted": false,
    "canonical_term": "pathway for advancing",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01466"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "pathway for advancing",
    "term_id": "term-01127"
  },
  {
    "adopted": false,
    "canonical_term": "performance",
    "category": "unclassified",
    "document_frequency": 5,
    "evidence_ids": [
      "evidence-01486",
      "evidence-01487",
      "evidence-01488",
      "evidence-01489",
      "evidence-01490"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3013651137",
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402270704",
      "https://openalex.org/W4407450426",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "performance",
    "term_id": "term-01142"
  },
  {
    "adopted": false,
    "canonical_term": "pip",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01508"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "pip",
    "term_id": "term-01160"
  },
  {
    "adopted": false,
    "canonical_term": "pipeline",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01509"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "pipeline",
    "term_id": "term-01161"
  },
  {
    "adopted": false,
    "canonical_term": "pipeline extracts",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01510"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "pipeline extracts",
    "term_id": "term-01162"
  },
  {
    "adopted": false,
    "canonical_term": "pipeline extracts time-domain",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01511"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "pipeline extracts time-domain",
    "term_id": "term-01163"
  },
  {
    "adopted": false,
    "canonical_term": "predict",
    "category": "unclassified",
    "document_frequency": 3,
    "evidence_ids": [
      "evidence-01526",
      "evidence-01527",
      "evidence-01528"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402270704",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "predict",
    "term_id": "term-01178"
  },
  {
    "adopted": false,
    "canonical_term": "predict 10",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01529"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "predict 10",
    "term_id": "term-01179"
  },
  {
    "adopted": false,
    "canonical_term": "predict 10 degrees",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01530"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "predict 10 degrees",
    "term_id": "term-01180"
  },
  {
    "adopted": false,
    "canonical_term": "predicting",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01542"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "predicting",
    "term_id": "term-01191"
  },
  {
    "adopted": false,
    "canonical_term": "predicting continuous",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01543"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "predicting continuous",
    "term_id": "term-01192"
  },
  {
    "adopted": false,
    "canonical_term": "predicting continuous hand",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01544"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "predicting continuous hand",
    "term_id": "term-01193"
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
    "canonical_term": "prediction of hand",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01564"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "prediction of hand",
    "term_id": "term-01201"
  },
  {
    "adopted": false,
    "canonical_term": "predictions",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01569"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "predictions",
    "term_id": "term-01206"
  },
  {
    "adopted": false,
    "canonical_term": "preprocessing",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01572"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "preprocessing",
    "term_id": "term-01209"
  },
  {
    "adopted": false,
    "canonical_term": "preprocessing pipeline",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01573"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "preprocessing pipeline",
    "term_id": "term-01210"
  },
  {
    "adopted": false,
    "canonical_term": "preprocessing pipeline extracts",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01574"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "preprocessing pipeline extracts",
    "term_id": "term-01211"
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
    "canonical_term": "proposes a novel",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01600"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "proposes a novel",
    "term_id": "term-01231"
  },
  {
    "adopted": false,
    "canonical_term": "prosthetic control",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01601"
    ],
    "evidence_status": "database_assigned",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "term": "prosthetic control",
    "term_id": "term-01232"
  },
  {
    "adopted": false,
    "canonical_term": "proximal",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01605",
      "evidence-01606"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W1918406696",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "proximal",
    "term_id": "term-01236"
  },
  {
    "adopted": false,
    "canonical_term": "proximal interphalangeal",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01607"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "proximal interphalangeal",
    "term_id": "term-01237"
  },
  {
    "adopted": false,
    "canonical_term": "proximal interphalangeal joint",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01608"
    ],
    "evidence_status": "database_assigned",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "term": "proximal interphalangeal joint",
    "term_id": "term-01238"
  },
  {
    "adopted": false,
    "canonical_term": "reduction",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01670"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "reduction",
    "term_id": "term-01291"
  },
  {
    "adopted": false,
    "canonical_term": "regularized",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01677"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "regularized",
    "term_id": "term-01298"
  },
  {
    "adopted": false,
    "canonical_term": "regularized loss",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01678"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "regularized loss",
    "term_id": "term-01299"
  },
  {
    "adopted": false,
    "canonical_term": "regularized loss function",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01679"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "regularized loss function",
    "term_id": "term-01300"
  },
  {
    "adopted": false,
    "canonical_term": "rehabilitation",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01680"
    ],
    "evidence_status": "database_assigned",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "term": "rehabilitation",
    "term_id": "term-01301"
  },
  {
    "adopted": false,
    "canonical_term": "residual",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01709"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "residual",
    "term_id": "term-01326"
  },
  {
    "adopted": false,
    "canonical_term": "residual connections",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01710"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "residual connections",
    "term_id": "term-01327"
  },
  {
    "adopted": false,
    "canonical_term": "robust",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01741"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "robust",
    "term_id": "term-01352"
  },
  {
    "adopted": false,
    "canonical_term": "robust predictions",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01742"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "robust predictions",
    "term_id": "term-01353"
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
    "canonical_term": "signal variability",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01833"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "signal variability",
    "term_id": "term-01408"
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
    "canonical_term": "signals offer",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01851"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "signals offer",
    "term_id": "term-01415"
  },
  {
    "adopted": false,
    "canonical_term": "stability",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01904"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "stability",
    "term_id": "term-01458"
  },
  {
    "adopted": false,
    "canonical_term": "standardization",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01905"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "standardization",
    "term_id": "term-01459"
  },
  {
    "adopted": false,
    "canonical_term": "standardization to optimize",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01906"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "standardization to optimize",
    "term_id": "term-01460"
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
    "canonical_term": "temporal muscle",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02025"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "temporal muscle",
    "term_id": "term-01527"
  },
  {
    "adopted": false,
    "canonical_term": "temporal muscle dynamics",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02026"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "temporal muscle dynamics",
    "term_id": "term-01528"
  },
  {
    "adopted": false,
    "canonical_term": "through",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-02058",
      "evidence-02059"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4284878820",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "through",
    "term_id": "term-01555"
  },
  {
    "adopted": false,
    "canonical_term": "through bilstm",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02060"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "through bilstm",
    "term_id": "term-01556"
  },
  {
    "adopted": false,
    "canonical_term": "time-domain",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02071"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "time-domain",
    "term_id": "term-01564"
  },
  {
    "adopted": false,
    "canonical_term": "time-domain feature extraction",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02072"
    ],
    "evidence_status": "database_assigned",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "term": "time-domain feature extraction",
    "term_id": "term-01565"
  },
  {
    "adopted": false,
    "canonical_term": "time-domain features",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02073"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "time-domain features",
    "term_id": "term-01566"
  },
  {
    "adopted": false,
    "canonical_term": "training",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-02095",
      "evidence-02096"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3121018641",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "training",
    "term_id": "term-01584"
  },
  {
    "adopted": false,
    "canonical_term": "training stability",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02097"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "training stability",
    "term_id": "term-01585"
  },
  {
    "adopted": false,
    "canonical_term": "transformer",
    "category": "unclassified",
    "document_frequency": 3,
    "evidence_ids": [
      "evidence-02101",
      "evidence-02102",
      "evidence-02103",
      "evidence-02104"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4416190202",
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "transformer",
    "term_id": "term-01589"
  },
  {
    "adopted": false,
    "canonical_term": "transformer architectures",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02105"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "transformer architectures",
    "term_id": "term-01590"
  },
  {
    "adopted": false,
    "canonical_term": "transformer encoder",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02106"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "transformer encoder",
    "term_id": "term-01591"
  },
  {
    "adopted": false,
    "canonical_term": "variability",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02165"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "variability",
    "term_id": "term-01646"
  },
  {
    "adopted": false,
    "canonical_term": "variability and complexity",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02166"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "variability and complexity",
    "term_id": "term-01647"
  },
  {
    "adopted": false,
    "canonical_term": "yet",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02243"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "yet",
    "term_id": "term-01716"
  },
  {
    "adopted": false,
    "canonical_term": "yet predicting",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02244"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "yet predicting",
    "term_id": "term-01717"
  },
  {
    "adopted": false,
    "canonical_term": "yet predicting continuous",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02245"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W7133186646"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "yet predicting continuous",
    "term_id": "term-01718"
  }
]
```

## 证据与引用 URL
```
[
  {
    "evidence_id": "evidence-00007",
    "evidence_level": "A",
    "excerpt": "10",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00008",
    "evidence_level": "A",
    "excerpt": "10 degrees",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00026",
    "evidence_level": "A",
    "excerpt": "8",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00032",
    "evidence_level": "A",
    "excerpt": "absolute",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00034",
    "evidence_level": "A",
    "excerpt": "absolute error",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00043",
    "evidence_level": "A",
    "excerpt": "Accurate",
    "locator": "title",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00045",
    "evidence_level": "A",
    "excerpt": "Accurate Prediction",
    "locator": "title",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00047",
    "evidence_level": "A",
    "excerpt": "accurately",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00048",
    "evidence_level": "A",
    "excerpt": "accurately predict",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00049",
    "evidence_level": "A",
    "excerpt": "accurately predict 10",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00050",
    "evidence_level": "A",
    "excerpt": "achieves",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00051",
    "evidence_level": "A",
    "excerpt": "achieves a mean",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00070",
    "evidence_level": "A",
    "excerpt": "advancing",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00071",
    "evidence_level": "A",
    "excerpt": "advancing human-machine",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00072",
    "evidence_level": "A",
    "excerpt": "advancing human-machine interfaces",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00141",
    "evidence_level": "A",
    "excerpt": "angles",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00142",
    "evidence_level": "A",
    "excerpt": "Angles",
    "locator": "title",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00150",
    "evidence_level": "A",
    "excerpt": "Angles From Semg",
    "locator": "title",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00151",
    "evidence_level": "A",
    "excerpt": "angles is challenging",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00165",
    "evidence_level": "A",
    "excerpt": "applies",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00166",
    "evidence_level": "A",
    "excerpt": "applies dimensionality",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00167",
    "evidence_level": "A",
    "excerpt": "applies dimensionality reduction",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00168",
    "evidence_level": "A",
    "excerpt": "architectures",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00169",
    "evidence_level": "A",
    "excerpt": "architectures to accurately",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00213",
    "evidence_level": "A",
    "excerpt": "bidirectional",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00215",
    "evidence_level": "A",
    "excerpt": "bidirectional long",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00217",
    "evidence_level": "A",
    "excerpt": "bidirectional long short-term",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00220",
    "evidence_level": "A",
    "excerpt": "BiLSTM",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00221",
    "evidence_level": "A",
    "excerpt": "BiLSTM and models",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00247",
    "evidence_level": "A",
    "excerpt": "captures",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00248",
    "evidence_level": "A",
    "excerpt": "captures temporal",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00249",
    "evidence_level": "A",
    "excerpt": "captures temporal muscle",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00257",
    "evidence_level": "A",
    "excerpt": "challenging",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00258",
    "evidence_level": "A",
    "excerpt": "challenging due",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00307",
    "evidence_level": "A",
    "excerpt": "complexity",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00309",
    "evidence_level": "A",
    "excerpt": "comprehensive",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00311",
    "evidence_level": "A",
    "excerpt": "comprehensive preprocessing",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00312",
    "evidence_level": "A",
    "excerpt": "comprehensive preprocessing pipeline",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00320",
    "evidence_level": "A",
    "excerpt": "connections",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00321",
    "evidence_level": "A",
    "excerpt": "connections for training",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00332",
    "evidence_level": "A",
    "excerpt": "continuous",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00337",
    "evidence_level": "A",
    "excerpt": "continuous hand",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00338",
    "evidence_level": "A",
    "excerpt": "continuous hand joint",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00395",
    "evidence_level": "A",
    "excerpt": "custom",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00396",
    "evidence_level": "A",
    "excerpt": "custom regularized",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00397",
    "evidence_level": "A",
    "excerpt": "custom regularized loss",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00403",
    "evidence_level": "A",
    "excerpt": "dataset",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00408",
    "evidence_level": "A",
    "excerpt": "DB8",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00409",
    "evidence_level": "A",
    "excerpt": "DB8 dataset",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00417",
    "evidence_level": "A",
    "excerpt": "degrees",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00418",
    "evidence_level": "A",
    "excerpt": "degrees of freedom",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00426",
    "evidence_level": "A",
    "excerpt": "dependencies",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00452",
    "evidence_level": "A",
    "excerpt": "dimensionality",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00453",
    "evidence_level": "A",
    "excerpt": "dimensionality reduction",
    "locator": "database_keywords",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00454",
    "evidence_level": "A",
    "excerpt": "dimensionality reduction",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00467",
    "evidence_level": "A",
    "excerpt": "DOF",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00470",
    "evidence_level": "A",
    "excerpt": "due",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00471",
    "evidence_level": "A",
    "excerpt": "due to signal",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00500",
    "evidence_level": "A",
    "excerpt": "dynamics",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00501",
    "evidence_level": "A",
    "excerpt": "dynamics through",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00502",
    "evidence_level": "A",
    "excerpt": "dynamics through BiLSTM",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00516",
    "evidence_level": "A",
    "excerpt": "efficiency",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00558",
    "evidence_level": "A",
    "excerpt": "electromyography",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00584",
    "evidence_level": "A",
    "excerpt": "employs",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00585",
    "evidence_level": "A",
    "excerpt": "employs standardization",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00586",
    "evidence_level": "A",
    "excerpt": "encoder",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00592",
    "evidence_level": "A",
    "excerpt": "enhance",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00593",
    "evidence_level": "A",
    "excerpt": "enhance efficiency",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00594",
    "evidence_level": "A",
    "excerpt": "enhanced",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00595",
    "evidence_level": "A",
    "excerpt": "enhanced by residual",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00596",
    "evidence_level": "A",
    "excerpt": "ensuring",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00597",
    "evidence_level": "A",
    "excerpt": "ensuring robust",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00598",
    "evidence_level": "A",
    "excerpt": "ensuring robust predictions",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00607",
    "evidence_level": "A",
    "excerpt": "error",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00680",
    "evidence_level": "A",
    "excerpt": "extracts",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00681",
    "evidence_level": "A",
    "excerpt": "extracts time-domain",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00682",
    "evidence_level": "A",
    "excerpt": "extracts time-domain features",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00702",
    "evidence_level": "A",
    "excerpt": "features",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00755",
    "evidence_level": "A",
    "excerpt": "freedom",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00760",
    "evidence_level": "A",
    "excerpt": "function",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00762",
    "evidence_level": "A",
    "excerpt": "function mitigates",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00763",
    "evidence_level": "A",
    "excerpt": "function mitigates overfitting",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00791",
    "evidence_level": "A",
    "excerpt": "hand",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00792",
    "evidence_level": "A",
    "excerpt": "Hand",
    "locator": "title",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00793",
    "evidence_level": "A",
    "excerpt": "hand joint",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00794",
    "evidence_level": "A",
    "excerpt": "Hand Joint",
    "locator": "title",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00795",
    "evidence_level": "A",
    "excerpt": "hand joint angles",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00796",
    "evidence_level": "A",
    "excerpt": "Hand Joint Angles",
    "locator": "title",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00797",
    "evidence_level": "A",
    "excerpt": "hand joints-metacarpophalangeal",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00873",
    "evidence_level": "A",
    "excerpt": "human-machine",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00875",
    "evidence_level": "A",
    "excerpt": "human-machine interaction",
    "locator": "database_keywords",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00876",
    "evidence_level": "A",
    "excerpt": "human-machine interfaces",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00881",
    "evidence_level": "A",
    "excerpt": "hybrid",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00883",
    "evidence_level": "A",
    "excerpt": "hybrid model",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00884",
    "evidence_level": "A",
    "excerpt": "hybrid model integrating",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00927",
    "evidence_level": "A",
    "excerpt": "integrating",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00928",
    "evidence_level": "A",
    "excerpt": "integrating bidirectional",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00929",
    "evidence_level": "A",
    "excerpt": "integrating bidirectional long",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00946",
    "evidence_level": "A",
    "excerpt": "interfaces",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00947",
    "evidence_level": "A",
    "excerpt": "interphalangeal",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00995",
    "evidence_level": "A",
    "excerpt": "joint",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00996",
    "evidence_level": "A",
    "excerpt": "Joint",
    "locator": "title",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01038",
    "evidence_level": "A",
    "excerpt": "joint angles",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01039",
    "evidence_level": "A",
    "excerpt": "Joint Angles",
    "locator": "title",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01058",
    "evidence_level": "A",
    "excerpt": "joints-metacarpophalangeal",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01128",
    "evidence_level": "A",
    "excerpt": "long",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01131",
    "evidence_level": "A",
    "excerpt": "long short-term",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01135",
    "evidence_level": "A",
    "excerpt": "long short-term memory",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01136",
    "evidence_level": "A",
    "excerpt": "long-range",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01137",
    "evidence_level": "A",
    "excerpt": "long-range dependencies",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01142",
    "evidence_level": "A",
    "excerpt": "loss",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01143",
    "evidence_level": "A",
    "excerpt": "loss function",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01144",
    "evidence_level": "A",
    "excerpt": "loss function mitigates",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01194",
    "evidence_level": "A",
    "excerpt": "MCP",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01199",
    "evidence_level": "A",
    "excerpt": "mean",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01201",
    "evidence_level": "A",
    "excerpt": "mean absolute",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01203",
    "evidence_level": "A",
    "excerpt": "mean absolute error",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01224",
    "evidence_level": "A",
    "excerpt": "memory",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01229",
    "evidence_level": "A",
    "excerpt": "metacarpophalangeal joint",
    "locator": "database_keywords",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01234",
    "evidence_level": "A",
    "excerpt": "mitigates",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01235",
    "evidence_level": "A",
    "excerpt": "mitigates overfitting",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01250",
    "evidence_level": "A",
    "excerpt": "model",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01251",
    "evidence_level": "A",
    "excerpt": "model achieves",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01257",
    "evidence_level": "A",
    "excerpt": "model captures",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01258",
    "evidence_level": "A",
    "excerpt": "model captures temporal",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01262",
    "evidence_level": "A",
    "excerpt": "model integrating",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01263",
    "evidence_level": "A",
    "excerpt": "model integrating bidirectional",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01277",
    "evidence_level": "A",
    "excerpt": "models",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01278",
    "evidence_level": "A",
    "excerpt": "models long-range",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01279",
    "evidence_level": "A",
    "excerpt": "models long-range dependencies",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01339",
    "evidence_level": "A",
    "excerpt": "muscle",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01345",
    "evidence_level": "A",
    "excerpt": "muscle dynamics",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01346",
    "evidence_level": "A",
    "excerpt": "muscle dynamics through",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01385",
    "evidence_level": "A",
    "excerpt": "NinaPro",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01388",
    "evidence_level": "A",
    "excerpt": "NinaPro DB8",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01389",
    "evidence_level": "A",
    "excerpt": "NinaPro DB8 dataset",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01394",
    "evidence_level": "A",
    "excerpt": "non-invasive",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01395",
    "evidence_level": "A",
    "excerpt": "non-invasive pathway",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01411",
    "evidence_level": "A",
    "excerpt": "novel",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01412",
    "evidence_level": "A",
    "excerpt": "novel hybrid",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01413",
    "evidence_level": "A",
    "excerpt": "novel hybrid model",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01429",
    "evidence_level": "A",
    "excerpt": "offer",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01430",
    "evidence_level": "A",
    "excerpt": "offer a non-invasive",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01438",
    "evidence_level": "A",
    "excerpt": "optimize",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01439",
    "evidence_level": "A",
    "excerpt": "optimize performance",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01445",
    "evidence_level": "A",
    "excerpt": "overfitting",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01446",
    "evidence_level": "A",
    "excerpt": "overfitting regularization",
    "locator": "database_keywords",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01465",
    "evidence_level": "A",
    "excerpt": "pathway",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01466",
    "evidence_level": "A",
    "excerpt": "pathway for advancing",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01490",
    "evidence_level": "A",
    "excerpt": "performance",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01508",
    "evidence_level": "A",
    "excerpt": "PIP",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01509",
    "evidence_level": "A",
    "excerpt": "pipeline",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01510",
    "evidence_level": "A",
    "excerpt": "pipeline extracts",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01511",
    "evidence_level": "A",
    "excerpt": "pipeline extracts time-domain",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01528",
    "evidence_level": "A",
    "excerpt": "predict",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01529",
    "evidence_level": "A",
    "excerpt": "predict 10",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01530",
    "evidence_level": "A",
    "excerpt": "predict 10 degrees",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01542",
    "evidence_level": "A",
    "excerpt": "predicting",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01543",
    "evidence_level": "A",
    "excerpt": "predicting continuous",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01544",
    "evidence_level": "A",
    "excerpt": "predicting continuous hand",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01554",
    "evidence_level": "A",
    "excerpt": "Prediction",
    "locator": "title",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01564",
    "evidence_level": "A",
    "excerpt": "Prediction of Hand",
    "locator": "title",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01569",
    "evidence_level": "A",
    "excerpt": "predictions",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01572",
    "evidence_level": "A",
    "excerpt": "preprocessing",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01573",
    "evidence_level": "A",
    "excerpt": "preprocessing pipeline",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01574",
    "evidence_level": "A",
    "excerpt": "preprocessing pipeline extracts",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01598",
    "evidence_level": "A",
    "excerpt": "proposes",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01600",
    "evidence_level": "A",
    "excerpt": "proposes a novel",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01601",
    "evidence_level": "A",
    "excerpt": "prosthetic control",
    "locator": "database_keywords",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01606",
    "evidence_level": "A",
    "excerpt": "proximal",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01607",
    "evidence_level": "A",
    "excerpt": "proximal interphalangeal",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01608",
    "evidence_level": "A",
    "excerpt": "proximal interphalangeal joint",
    "locator": "database_keywords",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01670",
    "evidence_level": "A",
    "excerpt": "reduction",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01677",
    "evidence_level": "A",
    "excerpt": "regularized",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01678",
    "evidence_level": "A",
    "excerpt": "regularized loss",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01679",
    "evidence_level": "A",
    "excerpt": "regularized loss function",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01680",
    "evidence_level": "A",
    "excerpt": "rehabilitation",
    "locator": "database_keywords",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01709",
    "evidence_level": "A",
    "excerpt": "residual",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01710",
    "evidence_level": "A",
    "excerpt": "residual connections",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01741",
    "evidence_level": "A",
    "excerpt": "robust",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01742",
    "evidence_level": "A",
    "excerpt": "robust predictions",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01773",
    "evidence_level": "A",
    "excerpt": "sEMG",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01774",
    "evidence_level": "A",
    "excerpt": "Semg",
    "locator": "title",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01795",
    "evidence_level": "A",
    "excerpt": "Semg Signals",
    "locator": "title",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01818",
    "evidence_level": "A",
    "excerpt": "short-term",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01822",
    "evidence_level": "A",
    "excerpt": "short-term memory",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01830",
    "evidence_level": "A",
    "excerpt": "signal",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01833",
    "evidence_level": "A",
    "excerpt": "signal variability",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01844",
    "evidence_level": "A",
    "excerpt": "signals",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01845",
    "evidence_level": "A",
    "excerpt": "Signals",
    "locator": "title",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01851",
    "evidence_level": "A",
    "excerpt": "signals offer",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01904",
    "evidence_level": "A",
    "excerpt": "stability",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01905",
    "evidence_level": "A",
    "excerpt": "standardization",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01906",
    "evidence_level": "A",
    "excerpt": "standardization to optimize",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01961",
    "evidence_level": "A",
    "excerpt": "Surface",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01977",
    "evidence_level": "A",
    "excerpt": "surface electromyography",
    "locator": "database_keywords",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01991",
    "evidence_level": "A",
    "excerpt": "Surface electromyography",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02019",
    "evidence_level": "A",
    "excerpt": "temporal",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02025",
    "evidence_level": "A",
    "excerpt": "temporal muscle",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02026",
    "evidence_level": "A",
    "excerpt": "temporal muscle dynamics",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02059",
    "evidence_level": "A",
    "excerpt": "through",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02060",
    "evidence_level": "A",
    "excerpt": "through BiLSTM",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02071",
    "evidence_level": "A",
    "excerpt": "time-domain",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02072",
    "evidence_level": "A",
    "excerpt": "time-domain feature extraction",
    "locator": "database_keywords",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02073",
    "evidence_level": "A",
    "excerpt": "time-domain features",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02096",
    "evidence_level": "A",
    "excerpt": "training",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02097",
    "evidence_level": "A",
    "excerpt": "training stability",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02104",
    "evidence_level": "A",
    "excerpt": "Transformer",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02105",
    "evidence_level": "A",
    "excerpt": "Transformer architectures",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02106",
    "evidence_level": "A",
    "excerpt": "Transformer encoder",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02165",
    "evidence_level": "A",
    "excerpt": "variability",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02166",
    "evidence_level": "A",
    "excerpt": "variability and complexity",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02243",
    "evidence_level": "A",
    "excerpt": "yet",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02244",
    "evidence_level": "A",
    "excerpt": "yet predicting",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02245",
    "evidence_level": "A",
    "excerpt": "yet predicting continuous",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W7133186646",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W7133186646",
    "supports": "Field observation only; not semantic equivalence or relevance."
  }
]
```

## 译文
未分析，留空供人工填写。

## 创新点
未分析，留空供人工填写。

## 用户笔记
