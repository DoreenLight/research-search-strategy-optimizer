---
{
  "authors": [
    "Engin Kaya",
    "Hande Argunsah"
  ],
  "case_id": "semg-joint-angle",
  "doi": "https://doi.org/10.1080/10255842.2024.2400318",
  "human_judgments": [],
  "innovation_points": "",
  "model_judgments": [],
  "model_promoted_to_human": false,
  "paper_id": "https://openalex.org/W4402270704",
  "pmid": "39235388",
  "publication_year": 2024,
  "reading_status": "\u5f85\u786e\u8ba4",
  "reading_status_options": [
    "\u5f85\u786e\u8ba4",
    "\u5f85\u8bfb",
    "\u5df2\u8bfb"
  ],
  "relevance_status": "\u5f85\u4eba\u5de5\u786e\u8ba4",
  "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
  "schema_version": "p3-reading-export-0.1",
  "source_run_ids": [
    "run-plan-7e6e33787081"
  ],
  "source_title": "Computer Methods in Biomechanics \u0026 Biomedical Engineering",
  "source_url": "https://openalex.org/W4402270704",
  "title": "Exploring the contribution of joint angles and sEMG signals on joint torque prediction accuracy using LSTM-based deep learning techniques",
  "translation": ""
}
---

# 阅读任务

状态默认为 **待确认**；可人工改为 **待读** / **已读**。模型相关性不代表人工确认。

## 标题
```
Exploring the contribution of joint angles and sEMG signals on joint torque prediction accuracy using LSTM-based deep learning techniques
```

## 作者
```
[
  "Engin Kaya",
  "Hande Argunsah"
]
```

## 年份 / DOI / PMID
```
{
  "doi": "https://doi.org/10.1080/10255842.2024.2400318",
  "pmid": "39235388",
  "publication_year": 2024
}
```

## 摘要
```
Machine learning (ML) has been used to predict lower extremity joint torques from joint angles and surface electromyography (sEMG) signals. This study trained three bidirectional Long Short-Term Memory (LSTM) models, which utilize joint angle, sEMG, and combined modalities as inputs, using a publicly accessible dataset to estimate joint torques during normal walking and assessed the performance of models, that used specific inputs independently plus the accuracy of the joint-specific torque prediction. The performance of each model was evaluated using normalized root mean square error (nRMSE) and Pearson correlation coefficient (PCC). Each model's median scores for the PCC and nRMSE values were highly convergent and the bulk of the mean nRMSE values of all joints were less than 10%. The ankle joint torque was the most successfully predicted output, having a mean nRMSE of less than 9% for all models. The knee joint torque prediction has reached the highest accuracy with a mean nRMSE of 11% and the hip joint torque prediction of 10%. The PCC values of each model were significantly high and remarkably comparable for the ankle (∼ 0.98), knee (∼ 0.92), and hip (∼ 0.95) joints. The model obtained significantly close accuracy with single and combined input modalities, indicating that one of either input may be sufficient for predicting the torque of a particular joint, obviating the need for the other in certain contexts.
```

## 来源
```
{
  "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
  "source_title": "Computer Methods in Biomechanics \u0026 Biomedical Engineering",
  "source_url": "https://openalex.org/W4402270704"
}
```

## 检索 / 运行 ID
```
{
  "case_id": "semg-joint-angle",
  "plan_ids": [
    "plan-7e6e33787081"
  ],
  "source_run_ids": [
    "run-plan-7e6e33787081"
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
    "canonical_term": "11",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00011"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "11",
    "term_id": "term-00009"
  },
  {
    "adopted": false,
    "canonical_term": "9",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00027"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "9",
    "term_id": "term-00024"
  },
  {
    "adopted": false,
    "canonical_term": "accessible",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00035"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "accessible",
    "term_id": "term-00029"
  },
  {
    "adopted": false,
    "canonical_term": "accessible dataset",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00036"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "accessible dataset",
    "term_id": "term-00030"
  },
  {
    "adopted": false,
    "canonical_term": "accuracy",
    "category": "unclassified",
    "document_frequency": 3,
    "evidence_ids": [
      "evidence-00037",
      "evidence-00038",
      "evidence-00039",
      "evidence-00040"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3013651137",
      "https://openalex.org/W4402270704",
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "accuracy",
    "term_id": "term-00031"
  },
  {
    "adopted": false,
    "canonical_term": "accuracy using lstm-based",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00041"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "accuracy using lstm-based",
    "term_id": "term-00032"
  },
  {
    "adopted": false,
    "canonical_term": "all",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00076"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "all",
    "term_id": "term-00065"
  },
  {
    "adopted": false,
    "canonical_term": "all joints",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00077"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "all joints",
    "term_id": "term-00066"
  },
  {
    "adopted": false,
    "canonical_term": "all models",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00078"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "all models",
    "term_id": "term-00067"
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
    "canonical_term": "angles and semg",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00143"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "angles and semg",
    "term_id": "term-00101"
  },
  {
    "adopted": false,
    "canonical_term": "angles and surface",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00144"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "angles and surface",
    "term_id": "term-00102"
  },
  {
    "adopted": false,
    "canonical_term": "ankle",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00154"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "ankle",
    "term_id": "term-00109"
  },
  {
    "adopted": false,
    "canonical_term": "ankle joint",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00156"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "ankle joint",
    "term_id": "term-00111"
  },
  {
    "adopted": false,
    "canonical_term": "ankle joint torque",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00157"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "ankle joint torque",
    "term_id": "term-00112"
  },
  {
    "adopted": false,
    "canonical_term": "ankle torque",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00158"
    ],
    "evidence_status": "database_assigned",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "term": "ankle torque",
    "term_id": "term-00113"
  },
  {
    "adopted": false,
    "canonical_term": "assessed",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00173"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "assessed",
    "term_id": "term-00127"
  },
  {
    "adopted": false,
    "canonical_term": "assessed the performance",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00174"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "assessed the performance",
    "term_id": "term-00128"
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
    "canonical_term": "bidirectional lstm",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00218"
    ],
    "evidence_status": "database_assigned",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "term": "bidirectional lstm",
    "term_id": "term-00155"
  },
  {
    "adopted": false,
    "canonical_term": "bulk",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00230"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "bulk",
    "term_id": "term-00167"
  },
  {
    "adopted": false,
    "canonical_term": "coefficient",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00282",
      "evidence-00283"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "coefficient",
    "term_id": "term-00215"
  },
  {
    "adopted": false,
    "canonical_term": "combined",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00293"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "combined",
    "term_id": "term-00225"
  },
  {
    "adopted": false,
    "canonical_term": "combined modalities",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00294"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "combined modalities",
    "term_id": "term-00226"
  },
  {
    "adopted": false,
    "canonical_term": "contribution",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00353"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "contribution",
    "term_id": "term-00270"
  },
  {
    "adopted": false,
    "canonical_term": "contribution of joint",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00354"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "contribution of joint",
    "term_id": "term-00271"
  },
  {
    "adopted": false,
    "canonical_term": "convergent",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00360"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "convergent",
    "term_id": "term-00275"
  },
  {
    "adopted": false,
    "canonical_term": "correlation",
    "category": "unclassified",
    "document_frequency": 3,
    "evidence_ids": [
      "evidence-00373",
      "evidence-00374",
      "evidence-00375",
      "evidence-00376"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3013651137",
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "correlation",
    "term_id": "term-00284"
  },
  {
    "adopted": false,
    "canonical_term": "correlation coefficient",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00380",
      "evidence-00381"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "correlation coefficient",
    "term_id": "term-00288"
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
    "canonical_term": "dataset to estimate",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00405"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "dataset to estimate",
    "term_id": "term-00307"
  },
  {
    "adopted": false,
    "canonical_term": "deep",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00412"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "deep",
    "term_id": "term-00314"
  },
  {
    "adopted": false,
    "canonical_term": "deep learning",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00413"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "deep learning",
    "term_id": "term-00315"
  },
  {
    "adopted": false,
    "canonical_term": "deep learning techniques",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00414"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "deep learning techniques",
    "term_id": "term-00316"
  },
  {
    "adopted": false,
    "canonical_term": "during",
    "category": "unclassified",
    "document_frequency": 5,
    "evidence_ids": [
      "evidence-00472",
      "evidence-00473",
      "evidence-00474",
      "evidence-00475",
      "evidence-00476"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W1918406696",
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4284878820",
      "https://openalex.org/W4402270704",
      "https://openalex.org/W4416190202"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "during",
    "term_id": "term-00370"
  },
  {
    "adopted": false,
    "canonical_term": "during normal",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00487"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "during normal",
    "term_id": "term-00381"
  },
  {
    "adopted": false,
    "canonical_term": "during normal walking",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00488"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "during normal walking",
    "term_id": "term-00382"
  },
  {
    "adopted": false,
    "canonical_term": "each",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00505",
      "evidence-00506"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704",
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "each",
    "term_id": "term-00397"
  },
  {
    "adopted": false,
    "canonical_term": "each model",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00507"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "each model",
    "term_id": "term-00398"
  },
  {
    "adopted": false,
    "canonical_term": "each model's",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00508"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "each model's",
    "term_id": "term-00399"
  },
  {
    "adopted": false,
    "canonical_term": "each model's median",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00509"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "each model's median",
    "term_id": "term-00400"
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
    "canonical_term": "estimate",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00614",
      "evidence-00615"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "estimate",
    "term_id": "term-00479"
  },
  {
    "adopted": false,
    "canonical_term": "estimate joint",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00616",
      "evidence-00617"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "estimate joint",
    "term_id": "term-00480"
  },
  {
    "adopted": false,
    "canonical_term": "estimate joint torques",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00619"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "estimate joint torques",
    "term_id": "term-00482"
  },
  {
    "adopted": false,
    "canonical_term": "evaluated",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00638"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "evaluated",
    "term_id": "term-00494"
  },
  {
    "adopted": false,
    "canonical_term": "evaluated using normalized",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00639"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "evaluated using normalized",
    "term_id": "term-00495"
  },
  {
    "adopted": false,
    "canonical_term": "exploring",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00658"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "exploring",
    "term_id": "term-00512"
  },
  {
    "adopted": false,
    "canonical_term": "exploring the contribution",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00659"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "exploring the contribution",
    "term_id": "term-00513"
  },
  {
    "adopted": false,
    "canonical_term": "extremity",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00687"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "extremity",
    "term_id": "term-00538"
  },
  {
    "adopted": false,
    "canonical_term": "extremity joint",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00688"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "extremity joint",
    "term_id": "term-00539"
  },
  {
    "adopted": false,
    "canonical_term": "extremity joint torques",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00689"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "extremity joint torques",
    "term_id": "term-00540"
  },
  {
    "adopted": false,
    "canonical_term": "gait",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00777"
    ],
    "evidence_status": "database_assigned",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "term": "gait",
    "term_id": "term-00612"
  },
  {
    "adopted": false,
    "canonical_term": "has",
    "category": "unclassified",
    "document_frequency": 3,
    "evidence_ids": [
      "evidence-00798",
      "evidence-00799",
      "evidence-00800"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W2091022037",
      "https://openalex.org/W4284878820",
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "has",
    "term_id": "term-00629"
  },
  {
    "adopted": false,
    "canonical_term": "has been used",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00802"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "has been used",
    "term_id": "term-00631"
  },
  {
    "adopted": false,
    "canonical_term": "has reached",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00804"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "has reached",
    "term_id": "term-00633"
  },
  {
    "adopted": false,
    "canonical_term": "having",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00812"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "having",
    "term_id": "term-00640"
  },
  {
    "adopted": false,
    "canonical_term": "having a mean",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00813"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "having a mean",
    "term_id": "term-00641"
  },
  {
    "adopted": false,
    "canonical_term": "highest",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00827"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "highest",
    "term_id": "term-00651"
  },
  {
    "adopted": false,
    "canonical_term": "highest accuracy",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00828"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "highest accuracy",
    "term_id": "term-00652"
  },
  {
    "adopted": false,
    "canonical_term": "highly",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00829"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "highly",
    "term_id": "term-00653"
  },
  {
    "adopted": false,
    "canonical_term": "highly convergent",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00830"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "highly convergent",
    "term_id": "term-00654"
  },
  {
    "adopted": false,
    "canonical_term": "hip",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00835",
      "evidence-00836"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W1918406696",
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "hip",
    "term_id": "term-00659"
  },
  {
    "adopted": false,
    "canonical_term": "hip torque",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00845"
    ],
    "evidence_status": "database_assigned",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "term": "hip torque",
    "term_id": "term-00668"
  },
  {
    "adopted": false,
    "canonical_term": "independently",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00904"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "independently",
    "term_id": "term-00716"
  },
  {
    "adopted": false,
    "canonical_term": "independently plus",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00905"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "independently plus",
    "term_id": "term-00717"
  },
  {
    "adopted": false,
    "canonical_term": "inputs",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00924"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "inputs",
    "term_id": "term-00732"
  },
  {
    "adopted": false,
    "canonical_term": "inputs independently",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00925"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "inputs independently",
    "term_id": "term-00733"
  },
  {
    "adopted": false,
    "canonical_term": "inputs independently plus",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00926"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "inputs independently plus",
    "term_id": "term-00734"
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
    "canonical_term": "joint angles",
    "category": "unclassified",
    "document_frequency": 6,
    "evidence_ids": [
      "evidence-01020",
      "evidence-01021",
      "evidence-01022",
      "evidence-01023",
      "evidence-01024",
      "evidence-01025"
    ],
    "evidence_status": "database_assigned",
    "paper_ids": [
      "https://openalex.org/W1918406696",
      "https://openalex.org/W2076757040",
      "https://openalex.org/W2086303648",
      "https://openalex.org/W2091022037",
      "https://openalex.org/W4284878820",
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "term": "joint angles",
    "term_id": "term-00788"
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
    "canonical_term": "joint torque",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01045",
      "evidence-01046",
      "evidence-01047"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4284878820",
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "joint torque",
    "term_id": "term-00792"
  },
  {
    "adopted": false,
    "canonical_term": "joint torque prediction",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01048"
    ],
    "evidence_status": "database_assigned",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "term": "joint torque prediction",
    "term_id": "term-00793"
  },
  {
    "adopted": false,
    "canonical_term": "joint torque prediction",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01049",
      "evidence-01050"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "joint torque prediction",
    "term_id": "term-00794"
  },
  {
    "adopted": false,
    "canonical_term": "joint torques",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01051"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "joint torques",
    "term_id": "term-00795"
  },
  {
    "adopted": false,
    "canonical_term": "joint torques during",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01052"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "joint torques during",
    "term_id": "term-00796"
  },
  {
    "adopted": false,
    "canonical_term": "joint-specific",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01053"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "joint-specific",
    "term_id": "term-00797"
  },
  {
    "adopted": false,
    "canonical_term": "joint-specific torque",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01054"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "joint-specific torque",
    "term_id": "term-00798"
  },
  {
    "adopted": false,
    "canonical_term": "joint-specific torque prediction",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01055"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "joint-specific torque prediction",
    "term_id": "term-00799"
  },
  {
    "adopted": false,
    "canonical_term": "joints",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01056"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "joints",
    "term_id": "term-00800"
  },
  {
    "adopted": false,
    "canonical_term": "joints were less",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01057"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "joints were less",
    "term_id": "term-00801"
  },
  {
    "adopted": false,
    "canonical_term": "knee",
    "category": "unclassified",
    "document_frequency": 4,
    "evidence_ids": [
      "evidence-01064",
      "evidence-01065",
      "evidence-01066",
      "evidence-01067",
      "evidence-01068"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W1918406696",
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402270704",
      "https://openalex.org/W4416190202"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "knee",
    "term_id": "term-00808"
  },
  {
    "adopted": false,
    "canonical_term": "knee joint",
    "category": "unclassified",
    "document_frequency": 4,
    "evidence_ids": [
      "evidence-01075",
      "evidence-01076",
      "evidence-01077",
      "evidence-01078",
      "evidence-01079"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W1918406696",
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402270704",
      "https://openalex.org/W4416190202"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "knee joint",
    "term_id": "term-00815"
  },
  {
    "adopted": false,
    "canonical_term": "knee joint torque",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01085"
    ],
    "evidence_status": "database_assigned",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "term": "knee joint torque",
    "term_id": "term-00818"
  },
  {
    "adopted": false,
    "canonical_term": "knee joint torque",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01086"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "knee joint torque",
    "term_id": "term-00819"
  },
  {
    "adopted": false,
    "canonical_term": "learning",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01096",
      "evidence-01097",
      "evidence-01098"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3013651137",
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "learning",
    "term_id": "term-00829"
  },
  {
    "adopted": false,
    "canonical_term": "learning techniques",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01100"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "learning techniques",
    "term_id": "term-00831"
  },
  {
    "adopted": false,
    "canonical_term": "less",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01107",
      "evidence-01108"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704",
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "less",
    "term_id": "term-00836"
  },
  {
    "adopted": false,
    "canonical_term": "less than",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01109",
      "evidence-01110"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704",
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "less than",
    "term_id": "term-00837"
  },
  {
    "adopted": false,
    "canonical_term": "less than 10",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01112"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "less than 10",
    "term_id": "term-00839"
  },
  {
    "adopted": false,
    "canonical_term": "less than 9",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01113"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "less than 9",
    "term_id": "term-00840"
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
    "canonical_term": "lower",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01146",
      "evidence-01147"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3013651137",
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "lower",
    "term_id": "term-00867"
  },
  {
    "adopted": false,
    "canonical_term": "lower extremity",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01148"
    ],
    "evidence_status": "database_assigned",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "term": "lower extremity",
    "term_id": "term-00868"
  },
  {
    "adopted": false,
    "canonical_term": "lower extremity",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01149"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "lower extremity",
    "term_id": "term-00869"
  },
  {
    "adopted": false,
    "canonical_term": "lower extremity joint",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01150"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "lower extremity joint",
    "term_id": "term-00870"
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
    "canonical_term": "lstm-based",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01163"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "lstm-based",
    "term_id": "term-00882"
  },
  {
    "adopted": false,
    "canonical_term": "lstm-based deep",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01164"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "lstm-based deep",
    "term_id": "term-00883"
  },
  {
    "adopted": false,
    "canonical_term": "lstm-based deep learning",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01165"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "lstm-based deep learning",
    "term_id": "term-00884"
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
    "canonical_term": "machine learning",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01170"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "machine learning",
    "term_id": "term-00887"
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
    "canonical_term": "mean nrmse",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01204"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "mean nrmse",
    "term_id": "term-00913"
  },
  {
    "adopted": false,
    "canonical_term": "mean nrmse values",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01205"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "mean nrmse values",
    "term_id": "term-00914"
  },
  {
    "adopted": false,
    "canonical_term": "mean square",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01208",
      "evidence-01209"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "mean square",
    "term_id": "term-00917"
  },
  {
    "adopted": false,
    "canonical_term": "mean square error",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01210",
      "evidence-01211"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "mean square error",
    "term_id": "term-00918"
  },
  {
    "adopted": false,
    "canonical_term": "median",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01219"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "median",
    "term_id": "term-00925"
  },
  {
    "adopted": false,
    "canonical_term": "median scores",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01220"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "median scores",
    "term_id": "term-00926"
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
    "canonical_term": "ml",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01236"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "ml",
    "term_id": "term-00939"
  },
  {
    "adopted": false,
    "canonical_term": "modalities",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01237"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "modalities",
    "term_id": "term-00940"
  },
  {
    "adopted": false,
    "canonical_term": "modalities as inputs",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01238"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "modalities as inputs",
    "term_id": "term-00941"
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
    "canonical_term": "model was evaluated",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01270"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "model was evaluated",
    "term_id": "term-00963"
  },
  {
    "adopted": false,
    "canonical_term": "model's",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01272"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "model's",
    "term_id": "term-00965"
  },
  {
    "adopted": false,
    "canonical_term": "model's median",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01273"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "model's median",
    "term_id": "term-00966"
  },
  {
    "adopted": false,
    "canonical_term": "model's median scores",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01274"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "model's median scores",
    "term_id": "term-00967"
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
    "canonical_term": "most",
    "category": "unclassified",
    "document_frequency": 4,
    "evidence_ids": [
      "evidence-01285",
      "evidence-01286",
      "evidence-01287",
      "evidence-01288"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W1918406696",
      "https://openalex.org/W2091022037",
      "https://openalex.org/W4284878820",
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "most",
    "term_id": "term-00976"
  },
  {
    "adopted": false,
    "canonical_term": "most successfully",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01291"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "most successfully",
    "term_id": "term-00979"
  },
  {
    "adopted": false,
    "canonical_term": "most successfully predicted",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01292"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "most successfully predicted",
    "term_id": "term-00980"
  },
  {
    "adopted": false,
    "canonical_term": "normal",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01400"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "normal",
    "term_id": "term-01065"
  },
  {
    "adopted": false,
    "canonical_term": "normal walking",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01401"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "normal walking",
    "term_id": "term-01066"
  },
  {
    "adopted": false,
    "canonical_term": "normalized",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01402"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "normalized",
    "term_id": "term-01067"
  },
  {
    "adopted": false,
    "canonical_term": "normalized root",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01403"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "normalized root",
    "term_id": "term-01068"
  },
  {
    "adopted": false,
    "canonical_term": "normalized root mean",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01404"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "normalized root mean",
    "term_id": "term-01069"
  },
  {
    "adopted": false,
    "canonical_term": "nrmse",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01418"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "nrmse",
    "term_id": "term-01080"
  },
  {
    "adopted": false,
    "canonical_term": "nrmse of 11",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01419"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "nrmse of 11",
    "term_id": "term-01081"
  },
  {
    "adopted": false,
    "canonical_term": "nrmse of less",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01420"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "nrmse of less",
    "term_id": "term-01082"
  },
  {
    "adopted": false,
    "canonical_term": "nrmse values",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01421"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "nrmse values",
    "term_id": "term-01083"
  },
  {
    "adopted": false,
    "canonical_term": "output",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01444"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "output",
    "term_id": "term-01105"
  },
  {
    "adopted": false,
    "canonical_term": "pcc",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01476"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "pcc",
    "term_id": "term-01135"
  },
  {
    "adopted": false,
    "canonical_term": "pcc and nrmse",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01477"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "pcc and nrmse",
    "term_id": "term-01136"
  },
  {
    "adopted": false,
    "canonical_term": "pearson",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01478",
      "evidence-01479"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "pearson",
    "term_id": "term-01137"
  },
  {
    "adopted": false,
    "canonical_term": "pearson correlation",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01480",
      "evidence-01481"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "pearson correlation",
    "term_id": "term-01138"
  },
  {
    "adopted": false,
    "canonical_term": "pearson correlation coefficient",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01482",
      "evidence-01483"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "pearson correlation coefficient",
    "term_id": "term-01139"
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
    "canonical_term": "performance of each",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01492"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "performance of each",
    "term_id": "term-01144"
  },
  {
    "adopted": false,
    "canonical_term": "performance of models",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01493"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "performance of models",
    "term_id": "term-01145"
  },
  {
    "adopted": false,
    "canonical_term": "plus",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01514"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "plus",
    "term_id": "term-01166"
  },
  {
    "adopted": false,
    "canonical_term": "plus the accuracy",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01515"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "plus the accuracy",
    "term_id": "term-01167"
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
    "canonical_term": "predict lower",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01533"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "predict lower",
    "term_id": "term-01183"
  },
  {
    "adopted": false,
    "canonical_term": "predict lower extremity",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01534"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "predict lower extremity",
    "term_id": "term-01184"
  },
  {
    "adopted": false,
    "canonical_term": "predicted",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01537",
      "evidence-01538"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "predicted",
    "term_id": "term-01187"
  },
  {
    "adopted": false,
    "canonical_term": "predicted output",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01541"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "predicted output",
    "term_id": "term-01190"
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
    "canonical_term": "prediction accuracy",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01555",
      "evidence-01556"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3013651137",
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "prediction accuracy",
    "term_id": "term-01195"
  },
  {
    "adopted": false,
    "canonical_term": "prediction has",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01557"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "prediction has",
    "term_id": "term-01196"
  },
  {
    "adopted": false,
    "canonical_term": "prediction has reached",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01558"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "prediction has reached",
    "term_id": "term-01197"
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
    "canonical_term": "publicly accessible",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01613"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "publicly accessible",
    "term_id": "term-01242"
  },
  {
    "adopted": false,
    "canonical_term": "publicly accessible dataset",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01614"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "publicly accessible dataset",
    "term_id": "term-01243"
  },
  {
    "adopted": false,
    "canonical_term": "reached",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01631"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "reached",
    "term_id": "term-01260"
  },
  {
    "adopted": false,
    "canonical_term": "reached the highest",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01632"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "reached the highest",
    "term_id": "term-01261"
  },
  {
    "adopted": false,
    "canonical_term": "root",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01745",
      "evidence-01746"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "root",
    "term_id": "term-01356"
  },
  {
    "adopted": false,
    "canonical_term": "root mean",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01747",
      "evidence-01748"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "root mean",
    "term_id": "term-01357"
  },
  {
    "adopted": false,
    "canonical_term": "root mean square",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01749",
      "evidence-01750"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "root mean square",
    "term_id": "term-01358"
  },
  {
    "adopted": false,
    "canonical_term": "scores",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01758"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "scores",
    "term_id": "term-01366"
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
    "canonical_term": "signals on joint",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01854"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "signals on joint",
    "term_id": "term-01418"
  },
  {
    "adopted": false,
    "canonical_term": "specific",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01887"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "specific",
    "term_id": "term-01444"
  },
  {
    "adopted": false,
    "canonical_term": "specific inputs",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01888"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "specific inputs",
    "term_id": "term-01445"
  },
  {
    "adopted": false,
    "canonical_term": "specific inputs independently",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01889"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "specific inputs independently",
    "term_id": "term-01446"
  },
  {
    "adopted": false,
    "canonical_term": "square",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01900",
      "evidence-01901"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "square",
    "term_id": "term-01456"
  },
  {
    "adopted": false,
    "canonical_term": "square error",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01902",
      "evidence-01903"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "square error",
    "term_id": "term-01457"
  },
  {
    "adopted": false,
    "canonical_term": "successfully",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01938"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "successfully",
    "term_id": "term-01483"
  },
  {
    "adopted": false,
    "canonical_term": "successfully predicted",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01939"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "successfully predicted",
    "term_id": "term-01484"
  },
  {
    "adopted": false,
    "canonical_term": "successfully predicted output",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01940"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "successfully predicted output",
    "term_id": "term-01485"
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
    "canonical_term": "techniques",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02017"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "techniques",
    "term_id": "term-01520"
  },
  {
    "adopted": false,
    "canonical_term": "than",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-02032",
      "evidence-02033"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704",
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "than",
    "term_id": "term-01534"
  },
  {
    "adopted": false,
    "canonical_term": "than 10",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02035"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "than 10",
    "term_id": "term-01536"
  },
  {
    "adopted": false,
    "canonical_term": "than 9",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02036"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "than 9",
    "term_id": "term-01537"
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
    "canonical_term": "three bidirectional",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02052"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "three bidirectional",
    "term_id": "term-01549"
  },
  {
    "adopted": false,
    "canonical_term": "three bidirectional long",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02053"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "three bidirectional long",
    "term_id": "term-01550"
  },
  {
    "adopted": false,
    "canonical_term": "torque",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-02074",
      "evidence-02075",
      "evidence-02076"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4284878820",
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "torque",
    "term_id": "term-01567"
  },
  {
    "adopted": false,
    "canonical_term": "torque prediction",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02078",
      "evidence-02079"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "torque prediction",
    "term_id": "term-01569"
  },
  {
    "adopted": false,
    "canonical_term": "torque prediction accuracy",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02080"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "torque prediction accuracy",
    "term_id": "term-01570"
  },
  {
    "adopted": false,
    "canonical_term": "torque prediction has",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02081"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "torque prediction has",
    "term_id": "term-01571"
  },
  {
    "adopted": false,
    "canonical_term": "torques",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02082"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "torques",
    "term_id": "term-01572"
  },
  {
    "adopted": false,
    "canonical_term": "torques during",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02083"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "torques during",
    "term_id": "term-01573"
  },
  {
    "adopted": false,
    "canonical_term": "torques during normal",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02084"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "torques during normal",
    "term_id": "term-01574"
  },
  {
    "adopted": false,
    "canonical_term": "torques from joint",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02085"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "torques from joint",
    "term_id": "term-01575"
  },
  {
    "adopted": false,
    "canonical_term": "trained",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02092"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "trained",
    "term_id": "term-01581"
  },
  {
    "adopted": false,
    "canonical_term": "trained three",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02093"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "trained three",
    "term_id": "term-01582"
  },
  {
    "adopted": false,
    "canonical_term": "trained three bidirectional",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02094"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "trained three bidirectional",
    "term_id": "term-01583"
  },
  {
    "adopted": false,
    "canonical_term": "used",
    "category": "unclassified",
    "document_frequency": 5,
    "evidence_ids": [
      "evidence-02142",
      "evidence-02143",
      "evidence-02144",
      "evidence-02145",
      "evidence-02146"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3013651137",
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4284878820",
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "used",
    "term_id": "term-01627"
  },
  {
    "adopted": false,
    "canonical_term": "used specific",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02149"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "used specific",
    "term_id": "term-01630"
  },
  {
    "adopted": false,
    "canonical_term": "used specific inputs",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02150"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "used specific inputs",
    "term_id": "term-01631"
  },
  {
    "adopted": false,
    "canonical_term": "used to predict",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02153"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "used to predict",
    "term_id": "term-01634"
  },
  {
    "adopted": false,
    "canonical_term": "utilize",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02155"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "utilize",
    "term_id": "term-01636"
  },
  {
    "adopted": false,
    "canonical_term": "utilize joint",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02156"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "utilize joint",
    "term_id": "term-01637"
  },
  {
    "adopted": false,
    "canonical_term": "utilize joint angle",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02157"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "utilize joint angle",
    "term_id": "term-01638"
  },
  {
    "adopted": false,
    "canonical_term": "values",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02162"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "values",
    "term_id": "term-01643"
  },
  {
    "adopted": false,
    "canonical_term": "values of all",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02163"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "values of all",
    "term_id": "term-01644"
  },
  {
    "adopted": false,
    "canonical_term": "values were highly",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02164"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "values were highly",
    "term_id": "term-01645"
  },
  {
    "adopted": false,
    "canonical_term": "walking",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02182"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "walking",
    "term_id": "term-01662"
  },
  {
    "adopted": false,
    "canonical_term": "walking and assessed",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02183"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "walking and assessed",
    "term_id": "term-01663"
  },
  {
    "adopted": false,
    "canonical_term": "which",
    "category": "unclassified",
    "document_frequency": 4,
    "evidence_ids": [
      "evidence-02204",
      "evidence-02205",
      "evidence-02206",
      "evidence-02207"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3013651137",
      "https://openalex.org/W4284878820",
      "https://openalex.org/W4402270704",
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "which",
    "term_id": "term-01682"
  },
  {
    "adopted": false,
    "canonical_term": "which utilize",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02213"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "which utilize",
    "term_id": "term-01688"
  },
  {
    "adopted": false,
    "canonical_term": "which utilize joint",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02214"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4402270704"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "which utilize joint",
    "term_id": "term-01689"
  }
]
```

## 证据与引用 URL
```
[
  {
    "evidence_id": "evidence-00006",
    "evidence_level": "A",
    "excerpt": "10",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00011",
    "evidence_level": "A",
    "excerpt": "11",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00027",
    "evidence_level": "A",
    "excerpt": "9",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00035",
    "evidence_level": "A",
    "excerpt": "accessible",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00036",
    "evidence_level": "A",
    "excerpt": "accessible dataset",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00038",
    "evidence_level": "A",
    "excerpt": "accuracy",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00039",
    "evidence_level": "A",
    "excerpt": "accuracy",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00041",
    "evidence_level": "A",
    "excerpt": "accuracy using LSTM-based",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00076",
    "evidence_level": "A",
    "excerpt": "all",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00077",
    "evidence_level": "A",
    "excerpt": "all joints",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00078",
    "evidence_level": "A",
    "excerpt": "all models",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00103",
    "evidence_level": "A",
    "excerpt": "angle",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00138",
    "evidence_level": "A",
    "excerpt": "angles",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00139",
    "evidence_level": "A",
    "excerpt": "angles",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00143",
    "evidence_level": "A",
    "excerpt": "angles and sEMG",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00144",
    "evidence_level": "A",
    "excerpt": "angles and surface",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00154",
    "evidence_level": "A",
    "excerpt": "ankle",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00156",
    "evidence_level": "A",
    "excerpt": "ankle joint",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00157",
    "evidence_level": "A",
    "excerpt": "ankle joint torque",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00158",
    "evidence_level": "A",
    "excerpt": "ankle torque",
    "locator": "database_keywords",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00173",
    "evidence_level": "A",
    "excerpt": "assessed",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00174",
    "evidence_level": "A",
    "excerpt": "assessed the performance",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00212",
    "evidence_level": "A",
    "excerpt": "bidirectional",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00214",
    "evidence_level": "A",
    "excerpt": "bidirectional Long",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00216",
    "evidence_level": "A",
    "excerpt": "bidirectional Long Short-Term",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00218",
    "evidence_level": "A",
    "excerpt": "bidirectional LSTM",
    "locator": "database_keywords",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00230",
    "evidence_level": "A",
    "excerpt": "bulk",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00283",
    "evidence_level": "A",
    "excerpt": "coefficient",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00293",
    "evidence_level": "A",
    "excerpt": "combined",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00294",
    "evidence_level": "A",
    "excerpt": "combined modalities",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00353",
    "evidence_level": "A",
    "excerpt": "contribution",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00354",
    "evidence_level": "A",
    "excerpt": "contribution of joint",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00360",
    "evidence_level": "A",
    "excerpt": "convergent",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00376",
    "evidence_level": "A",
    "excerpt": "correlation",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00381",
    "evidence_level": "A",
    "excerpt": "correlation coefficient",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00402",
    "evidence_level": "A",
    "excerpt": "dataset",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00405",
    "evidence_level": "A",
    "excerpt": "dataset to estimate",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00412",
    "evidence_level": "A",
    "excerpt": "deep",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00413",
    "evidence_level": "A",
    "excerpt": "deep learning",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00414",
    "evidence_level": "A",
    "excerpt": "deep learning techniques",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00475",
    "evidence_level": "A",
    "excerpt": "during",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00487",
    "evidence_level": "A",
    "excerpt": "during normal",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00488",
    "evidence_level": "A",
    "excerpt": "during normal walking",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00505",
    "evidence_level": "A",
    "excerpt": "each",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00507",
    "evidence_level": "A",
    "excerpt": "each model",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00508",
    "evidence_level": "A",
    "excerpt": "Each model's",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00509",
    "evidence_level": "A",
    "excerpt": "Each model's median",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00555",
    "evidence_level": "A",
    "excerpt": "electromyography",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00605",
    "evidence_level": "A",
    "excerpt": "error",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00615",
    "evidence_level": "A",
    "excerpt": "estimate",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00617",
    "evidence_level": "A",
    "excerpt": "estimate joint",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00619",
    "evidence_level": "A",
    "excerpt": "estimate joint torques",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00638",
    "evidence_level": "A",
    "excerpt": "evaluated",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00639",
    "evidence_level": "A",
    "excerpt": "evaluated using normalized",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00658",
    "evidence_level": "A",
    "excerpt": "Exploring",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00659",
    "evidence_level": "A",
    "excerpt": "Exploring the contribution",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00687",
    "evidence_level": "A",
    "excerpt": "extremity",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00688",
    "evidence_level": "A",
    "excerpt": "extremity joint",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00689",
    "evidence_level": "A",
    "excerpt": "extremity joint torques",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00777",
    "evidence_level": "A",
    "excerpt": "gait",
    "locator": "database_keywords",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00800",
    "evidence_level": "A",
    "excerpt": "has",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00802",
    "evidence_level": "A",
    "excerpt": "has been used",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00804",
    "evidence_level": "A",
    "excerpt": "has reached",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00812",
    "evidence_level": "A",
    "excerpt": "having",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00813",
    "evidence_level": "A",
    "excerpt": "having a mean",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00827",
    "evidence_level": "A",
    "excerpt": "highest",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00828",
    "evidence_level": "A",
    "excerpt": "highest accuracy",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00829",
    "evidence_level": "A",
    "excerpt": "highly",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00830",
    "evidence_level": "A",
    "excerpt": "highly convergent",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00836",
    "evidence_level": "A",
    "excerpt": "hip",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00845",
    "evidence_level": "A",
    "excerpt": "hip torque",
    "locator": "database_keywords",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00904",
    "evidence_level": "A",
    "excerpt": "independently",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00905",
    "evidence_level": "A",
    "excerpt": "independently plus",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00924",
    "evidence_level": "A",
    "excerpt": "inputs",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00925",
    "evidence_level": "A",
    "excerpt": "inputs independently",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00926",
    "evidence_level": "A",
    "excerpt": "inputs independently plus",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00990",
    "evidence_level": "A",
    "excerpt": "joint",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00991",
    "evidence_level": "A",
    "excerpt": "joint",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01005",
    "evidence_level": "A",
    "excerpt": "joint angle",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01025",
    "evidence_level": "A",
    "excerpt": "joint angles",
    "locator": "database_keywords",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01035",
    "evidence_level": "A",
    "excerpt": "joint angles",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01036",
    "evidence_level": "A",
    "excerpt": "joint angles",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01046",
    "evidence_level": "A",
    "excerpt": "joint torque",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01047",
    "evidence_level": "A",
    "excerpt": "joint torque",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01048",
    "evidence_level": "A",
    "excerpt": "joint torque prediction",
    "locator": "database_keywords",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01049",
    "evidence_level": "A",
    "excerpt": "joint torque prediction",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01050",
    "evidence_level": "A",
    "excerpt": "joint torque prediction",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01051",
    "evidence_level": "A",
    "excerpt": "joint torques",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01052",
    "evidence_level": "A",
    "excerpt": "joint torques during",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01053",
    "evidence_level": "A",
    "excerpt": "joint-specific",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01054",
    "evidence_level": "A",
    "excerpt": "joint-specific torque",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01055",
    "evidence_level": "A",
    "excerpt": "joint-specific torque prediction",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01056",
    "evidence_level": "A",
    "excerpt": "joints",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01057",
    "evidence_level": "A",
    "excerpt": "joints were less",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01067",
    "evidence_level": "A",
    "excerpt": "knee",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01078",
    "evidence_level": "A",
    "excerpt": "knee joint",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01085",
    "evidence_level": "A",
    "excerpt": "knee joint torque",
    "locator": "database_keywords",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01086",
    "evidence_level": "A",
    "excerpt": "knee joint torque",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01097",
    "evidence_level": "A",
    "excerpt": "learning",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01098",
    "evidence_level": "A",
    "excerpt": "learning",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01100",
    "evidence_level": "A",
    "excerpt": "learning techniques",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01107",
    "evidence_level": "A",
    "excerpt": "less",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01109",
    "evidence_level": "A",
    "excerpt": "less than",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01112",
    "evidence_level": "A",
    "excerpt": "less than 10",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01113",
    "evidence_level": "A",
    "excerpt": "less than 9",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01127",
    "evidence_level": "A",
    "excerpt": "Long",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01130",
    "evidence_level": "A",
    "excerpt": "Long Short-Term",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01134",
    "evidence_level": "A",
    "excerpt": "Long Short-Term Memory",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01147",
    "evidence_level": "A",
    "excerpt": "lower",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01148",
    "evidence_level": "A",
    "excerpt": "lower extremity",
    "locator": "database_keywords",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01149",
    "evidence_level": "A",
    "excerpt": "lower extremity",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01150",
    "evidence_level": "A",
    "excerpt": "lower extremity joint",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01162",
    "evidence_level": "A",
    "excerpt": "LSTM",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01163",
    "evidence_level": "A",
    "excerpt": "LSTM-based",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01164",
    "evidence_level": "A",
    "excerpt": "LSTM-based deep",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01165",
    "evidence_level": "A",
    "excerpt": "LSTM-based deep learning",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01168",
    "evidence_level": "A",
    "excerpt": "Machine",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01170",
    "evidence_level": "A",
    "excerpt": "Machine learning",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01197",
    "evidence_level": "A",
    "excerpt": "mean",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01204",
    "evidence_level": "A",
    "excerpt": "mean nRMSE",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01205",
    "evidence_level": "A",
    "excerpt": "mean nRMSE values",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01209",
    "evidence_level": "A",
    "excerpt": "mean square",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01211",
    "evidence_level": "A",
    "excerpt": "mean square error",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01219",
    "evidence_level": "A",
    "excerpt": "median",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01220",
    "evidence_level": "A",
    "excerpt": "median scores",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01222",
    "evidence_level": "A",
    "excerpt": "Memory",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01236",
    "evidence_level": "A",
    "excerpt": "ML",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01237",
    "evidence_level": "A",
    "excerpt": "modalities",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01238",
    "evidence_level": "A",
    "excerpt": "modalities as inputs",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01248",
    "evidence_level": "A",
    "excerpt": "model",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01270",
    "evidence_level": "A",
    "excerpt": "model was evaluated",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01272",
    "evidence_level": "A",
    "excerpt": "model's",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01273",
    "evidence_level": "A",
    "excerpt": "model's median",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01274",
    "evidence_level": "A",
    "excerpt": "model's median scores",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01275",
    "evidence_level": "A",
    "excerpt": "models",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01288",
    "evidence_level": "A",
    "excerpt": "most",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01291",
    "evidence_level": "A",
    "excerpt": "most successfully",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01292",
    "evidence_level": "A",
    "excerpt": "most successfully predicted",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01400",
    "evidence_level": "A",
    "excerpt": "normal",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01401",
    "evidence_level": "A",
    "excerpt": "normal walking",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01402",
    "evidence_level": "A",
    "excerpt": "normalized",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01403",
    "evidence_level": "A",
    "excerpt": "normalized root",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01404",
    "evidence_level": "A",
    "excerpt": "normalized root mean",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01418",
    "evidence_level": "A",
    "excerpt": "nRMSE",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01419",
    "evidence_level": "A",
    "excerpt": "nRMSE of 11",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01420",
    "evidence_level": "A",
    "excerpt": "nRMSE of less",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01421",
    "evidence_level": "A",
    "excerpt": "nRMSE values",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01444",
    "evidence_level": "A",
    "excerpt": "output",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01476",
    "evidence_level": "A",
    "excerpt": "PCC",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01477",
    "evidence_level": "A",
    "excerpt": "PCC and nRMSE",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01479",
    "evidence_level": "A",
    "excerpt": "Pearson",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01481",
    "evidence_level": "A",
    "excerpt": "Pearson correlation",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01483",
    "evidence_level": "A",
    "excerpt": "Pearson correlation coefficient",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01488",
    "evidence_level": "A",
    "excerpt": "performance",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01492",
    "evidence_level": "A",
    "excerpt": "performance of each",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01493",
    "evidence_level": "A",
    "excerpt": "performance of models",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01514",
    "evidence_level": "A",
    "excerpt": "plus",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01515",
    "evidence_level": "A",
    "excerpt": "plus the accuracy",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01527",
    "evidence_level": "A",
    "excerpt": "predict",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01533",
    "evidence_level": "A",
    "excerpt": "predict lower",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01534",
    "evidence_level": "A",
    "excerpt": "predict lower extremity",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01538",
    "evidence_level": "A",
    "excerpt": "predicted",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01541",
    "evidence_level": "A",
    "excerpt": "predicted output",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01549",
    "evidence_level": "A",
    "excerpt": "prediction",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01550",
    "evidence_level": "A",
    "excerpt": "prediction",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01556",
    "evidence_level": "A",
    "excerpt": "prediction accuracy",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01557",
    "evidence_level": "A",
    "excerpt": "prediction has",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01558",
    "evidence_level": "A",
    "excerpt": "prediction has reached",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01612",
    "evidence_level": "A",
    "excerpt": "publicly",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01613",
    "evidence_level": "A",
    "excerpt": "publicly accessible",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01614",
    "evidence_level": "A",
    "excerpt": "publicly accessible dataset",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01631",
    "evidence_level": "A",
    "excerpt": "reached",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01632",
    "evidence_level": "A",
    "excerpt": "reached the highest",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01746",
    "evidence_level": "A",
    "excerpt": "root",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01748",
    "evidence_level": "A",
    "excerpt": "root mean",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01750",
    "evidence_level": "A",
    "excerpt": "root mean square",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01758",
    "evidence_level": "A",
    "excerpt": "scores",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01769",
    "evidence_level": "A",
    "excerpt": "sEMG",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01770",
    "evidence_level": "A",
    "excerpt": "sEMG",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01794",
    "evidence_level": "A",
    "excerpt": "sEMG signals",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01816",
    "evidence_level": "A",
    "excerpt": "Short-Term",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01820",
    "evidence_level": "A",
    "excerpt": "Short-Term Memory",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01841",
    "evidence_level": "A",
    "excerpt": "signals",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01842",
    "evidence_level": "A",
    "excerpt": "signals",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01854",
    "evidence_level": "A",
    "excerpt": "signals on joint",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01887",
    "evidence_level": "A",
    "excerpt": "specific",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01888",
    "evidence_level": "A",
    "excerpt": "specific inputs",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01889",
    "evidence_level": "A",
    "excerpt": "specific inputs independently",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01901",
    "evidence_level": "A",
    "excerpt": "square",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01903",
    "evidence_level": "A",
    "excerpt": "square error",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01938",
    "evidence_level": "A",
    "excerpt": "successfully",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01939",
    "evidence_level": "A",
    "excerpt": "successfully predicted",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01940",
    "evidence_level": "A",
    "excerpt": "successfully predicted output",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01958",
    "evidence_level": "A",
    "excerpt": "surface",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01974",
    "evidence_level": "A",
    "excerpt": "surface electromyography",
    "locator": "database_keywords",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01988",
    "evidence_level": "A",
    "excerpt": "surface electromyography",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02017",
    "evidence_level": "A",
    "excerpt": "techniques",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02032",
    "evidence_level": "A",
    "excerpt": "than",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02035",
    "evidence_level": "A",
    "excerpt": "than 10",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02036",
    "evidence_level": "A",
    "excerpt": "than 9",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02051",
    "evidence_level": "A",
    "excerpt": "three",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02052",
    "evidence_level": "A",
    "excerpt": "three bidirectional",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02053",
    "evidence_level": "A",
    "excerpt": "three bidirectional Long",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02075",
    "evidence_level": "A",
    "excerpt": "torque",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02076",
    "evidence_level": "A",
    "excerpt": "torque",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02078",
    "evidence_level": "A",
    "excerpt": "torque prediction",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02079",
    "evidence_level": "A",
    "excerpt": "torque prediction",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02080",
    "evidence_level": "A",
    "excerpt": "torque prediction accuracy",
    "locator": "title",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02081",
    "evidence_level": "A",
    "excerpt": "torque prediction has",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02082",
    "evidence_level": "A",
    "excerpt": "torques",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02083",
    "evidence_level": "A",
    "excerpt": "torques during",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02084",
    "evidence_level": "A",
    "excerpt": "torques during normal",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02085",
    "evidence_level": "A",
    "excerpt": "torques from joint",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02092",
    "evidence_level": "A",
    "excerpt": "trained",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02093",
    "evidence_level": "A",
    "excerpt": "trained three",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02094",
    "evidence_level": "A",
    "excerpt": "trained three bidirectional",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02146",
    "evidence_level": "A",
    "excerpt": "used",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02149",
    "evidence_level": "A",
    "excerpt": "used specific",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02150",
    "evidence_level": "A",
    "excerpt": "used specific inputs",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02153",
    "evidence_level": "A",
    "excerpt": "used to predict",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02155",
    "evidence_level": "A",
    "excerpt": "utilize",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02156",
    "evidence_level": "A",
    "excerpt": "utilize joint",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02157",
    "evidence_level": "A",
    "excerpt": "utilize joint angle",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02162",
    "evidence_level": "A",
    "excerpt": "values",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02163",
    "evidence_level": "A",
    "excerpt": "values of all",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02164",
    "evidence_level": "A",
    "excerpt": "values were highly",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02182",
    "evidence_level": "A",
    "excerpt": "walking",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02183",
    "evidence_level": "A",
    "excerpt": "walking and assessed",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02206",
    "evidence_level": "A",
    "excerpt": "which",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02213",
    "evidence_level": "A",
    "excerpt": "which utilize",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02214",
    "evidence_level": "A",
    "excerpt": "which utilize joint",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4402270704",
    "retrieved_at": "2026-10-18T03:22:37.359068+00:00",
    "run_ids": [
      "run-plan-7e6e33787081"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4402270704",
    "supports": "Field observation only; not semantic equivalence or relevance."
  }
]
```

## 译文
未分析，留空供人工填写。

## 创新点
未分析，留空供人工填写。

## 用户笔记
