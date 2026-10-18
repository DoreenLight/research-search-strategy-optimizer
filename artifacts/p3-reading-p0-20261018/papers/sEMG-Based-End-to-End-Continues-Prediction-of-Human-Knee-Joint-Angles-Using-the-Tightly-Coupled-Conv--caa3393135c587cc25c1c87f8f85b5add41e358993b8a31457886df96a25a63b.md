---
{
  "authors": [
    "Tuanjie Liang",
    "Ning Sun",
    "Qiong Wang",
    "Jingyu Bu",
    "Long Li",
    "Yuhao Chen",
    "Menglin Cao",
    "Jin Ma",
    "Tian Liu"
  ],
  "case_id": "semg-joint-angle",
  "doi": "https://doi.org/10.1109/jbhi.2023.3304639",
  "human_judgments": [],
  "innovation_points": "",
  "model_judgments": [],
  "model_promoted_to_human": false,
  "paper_id": "https://openalex.org/W4385757465",
  "pmid": "37566511",
  "publication_year": 2023,
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
  "source_title": "IEEE Journal of Biomedical and Health Informatics",
  "source_url": "https://openalex.org/W4385757465",
  "title": "sEMG-Based End-to-End Continues Prediction of Human Knee Joint Angles Using the Tightly Coupled Convolutional Transformer Model",
  "translation": ""
}
---

# 阅读任务

状态默认为 **待确认**；可人工改为 **待读** / **已读**。模型相关性不代表人工确认。

## 标题
```
sEMG-Based End-to-End Continues Prediction of Human Knee Joint Angles Using the Tightly Coupled Convolutional Transformer Model
```

## 作者
```
[
  "Tuanjie Liang",
  "Ning Sun",
  "Qiong Wang",
  "Jingyu Bu",
  "Long Li",
  "Yuhao Chen",
  "Menglin Cao",
  "Jin Ma",
  "Tian Liu"
]
```

## 年份 / DOI / PMID
```
{
  "doi": "https://doi.org/10.1109/jbhi.2023.3304639",
  "pmid": "37566511",
  "publication_year": 2023
}
```

## 摘要
```
Wearable exoskeleton robots can promote the rehabilitation of patients with physical dysfunction. And improving human-computer interaction performance is a significant challenge for exoskeleton robots. The traditional feature extraction process based on surface Electromyography(sEMG) is complex and requires manual intervention, making real-time performance difficult to guarantee. In this study, we propose an end-to-end method to predict human knee joint angles based on sEMG signals using a tightly coupled convolutional transformer (TCCT) model. We first collected sEMG signals from 5 healthy subjects. Then, the envelope was extracted from the noise-removed sEMG signal and used as the input to the model. Finally, we developed the TCCT model to predict the knee joint angle after 100 ms. For the prediction performance, we used the Root Mean Square Error(RMSE), Pearson Correlation Coefficient(CC), and Adjustment R2as metrics to evaluate the error between the actual knee angle and the predicted knee angle. The results show that the model can predict the human knee angle quickly and accurately. The mean RMSE, Adjustment R2, and (CC) values of the model are 3.79°, 0.96, and 0.98, respectively, which are better than traditional deep learning models such as Informer (4.14, 0.95, 0.98), CNN (5.56, 0.89, 0.96) and CNN-BiLSTM (3.97, 0.95, 0.98). In addition, the prediction time of our proposed model is only 11.67 ± 0.67 ms, which is less than 100 ms. Therefore, the real-time and accuracy of the model can meet the continuous prediction of human knee joint angle in practice.
```

## 来源
```
{
  "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
  "source_title": "IEEE Journal of Biomedical and Health Informatics",
  "source_url": "https://openalex.org/W4385757465"
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
    "canonical_term": "100",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00009"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "100",
    "term_id": "term-00007"
  },
  {
    "adopted": false,
    "canonical_term": "100 ms",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00010"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "100 ms",
    "term_id": "term-00008"
  },
  {
    "adopted": false,
    "canonical_term": "5",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00021",
      "evidence-00022"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "5",
    "term_id": "term-00019"
  },
  {
    "adopted": false,
    "canonical_term": "5 healthy",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00023"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "5 healthy",
    "term_id": "term-00020"
  },
  {
    "adopted": false,
    "canonical_term": "5 healthy subjects",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00024"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "5 healthy subjects",
    "term_id": "term-00021"
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
    "canonical_term": "actual",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00064"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "actual",
    "term_id": "term-00053"
  },
  {
    "adopted": false,
    "canonical_term": "actual knee",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00065"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "actual knee",
    "term_id": "term-00054"
  },
  {
    "adopted": false,
    "canonical_term": "actual knee angle",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00066"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "actual knee angle",
    "term_id": "term-00055"
  },
  {
    "adopted": false,
    "canonical_term": "adjustment",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00067"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "adjustment",
    "term_id": "term-00056"
  },
  {
    "adopted": false,
    "canonical_term": "adjustment r2as",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00068"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "adjustment r2as",
    "term_id": "term-00057"
  },
  {
    "adopted": false,
    "canonical_term": "adjustment r2as metrics",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00069"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "adjustment r2as metrics",
    "term_id": "term-00058"
  },
  {
    "adopted": false,
    "canonical_term": "after",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00073"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "after",
    "term_id": "term-00062"
  },
  {
    "adopted": false,
    "canonical_term": "after 100",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00074"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "after 100",
    "term_id": "term-00063"
  },
  {
    "adopted": false,
    "canonical_term": "after 100 ms",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00075"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "after 100 ms",
    "term_id": "term-00064"
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
    "canonical_term": "angle after",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00107"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "angle after",
    "term_id": "term-00082"
  },
  {
    "adopted": false,
    "canonical_term": "angle after 100",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00108"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "angle after 100",
    "term_id": "term-00083"
  },
  {
    "adopted": false,
    "canonical_term": "angle quickly",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00125"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "angle quickly",
    "term_id": "term-00096"
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
    "canonical_term": "angles based",
    "category": "unclassified",
    "document_frequency": 3,
    "evidence_ids": [
      "evidence-00145",
      "evidence-00146",
      "evidence-00147",
      "evidence-00148"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3013651137",
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "angles based",
    "term_id": "term-00103"
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
    "canonical_term": "based on surface",
    "category": "unclassified",
    "document_frequency": 3,
    "evidence_ids": [
      "evidence-00190",
      "evidence-00191",
      "evidence-00192",
      "evidence-00193"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3013651137",
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "based on surface",
    "term_id": "term-00136"
  },
  {
    "adopted": false,
    "canonical_term": "between",
    "category": "unclassified",
    "document_frequency": 3,
    "evidence_ids": [
      "evidence-00201",
      "evidence-00202",
      "evidence-00203"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3013651137",
      "https://openalex.org/W4284878820",
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "between",
    "term_id": "term-00143"
  },
  {
    "adopted": false,
    "canonical_term": "between the actual",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00208"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "between the actual",
    "term_id": "term-00148"
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
    "canonical_term": "can predict",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00238"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "can predict",
    "term_id": "term-00174"
  },
  {
    "adopted": false,
    "canonical_term": "can promote",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00239"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "can promote",
    "term_id": "term-00175"
  },
  {
    "adopted": false,
    "canonical_term": "cc",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00252"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "cc",
    "term_id": "term-00188"
  },
  {
    "adopted": false,
    "canonical_term": "challenge",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00255"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "challenge",
    "term_id": "term-00191"
  },
  {
    "adopted": false,
    "canonical_term": "challenge for exoskeleton",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00256"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "challenge for exoskeleton",
    "term_id": "term-00192"
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
    "canonical_term": "collected",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00286"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "collected",
    "term_id": "term-00218"
  },
  {
    "adopted": false,
    "canonical_term": "collected semg",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00287"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "collected semg",
    "term_id": "term-00219"
  },
  {
    "adopted": false,
    "canonical_term": "collected semg signals",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00288"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "collected semg signals",
    "term_id": "term-00220"
  },
  {
    "adopted": false,
    "canonical_term": "complex",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00305"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "complex",
    "term_id": "term-00234"
  },
  {
    "adopted": false,
    "canonical_term": "complex and requires",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00306"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "complex and requires",
    "term_id": "term-00235"
  },
  {
    "adopted": false,
    "canonical_term": "continues",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00324"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "continues",
    "term_id": "term-00252"
  },
  {
    "adopted": false,
    "canonical_term": "continues prediction",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00325"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "continues prediction",
    "term_id": "term-00253"
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
    "canonical_term": "convolutional transformer",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00368",
      "evidence-00369"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "convolutional transformer",
    "term_id": "term-00280"
  },
  {
    "adopted": false,
    "canonical_term": "convolutional transformer model",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00370"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "convolutional transformer model",
    "term_id": "term-00281"
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
    "canonical_term": "coupled",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00385",
      "evidence-00386"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "coupled",
    "term_id": "term-00292"
  },
  {
    "adopted": false,
    "canonical_term": "coupled convolutional",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00387",
      "evidence-00388"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "coupled convolutional",
    "term_id": "term-00293"
  },
  {
    "adopted": false,
    "canonical_term": "coupled convolutional transformer",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00389",
      "evidence-00390"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "coupled convolutional transformer",
    "term_id": "term-00294"
  },
  {
    "adopted": false,
    "canonical_term": "developed",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00435",
      "evidence-00436"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "developed",
    "term_id": "term-00336"
  },
  {
    "adopted": false,
    "canonical_term": "developed the tcct",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00438"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "developed the tcct",
    "term_id": "term-00338"
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
    "canonical_term": "difficult to guarantee",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00451"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "difficult to guarantee",
    "term_id": "term-00349"
  },
  {
    "adopted": false,
    "canonical_term": "dysfunction",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00504"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "dysfunction",
    "term_id": "term-00396"
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
    "canonical_term": "end-to-end",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00587",
      "evidence-00588"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "end-to-end",
    "term_id": "term-00457"
  },
  {
    "adopted": false,
    "canonical_term": "end-to-end continues",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00589"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "end-to-end continues",
    "term_id": "term-00458"
  },
  {
    "adopted": false,
    "canonical_term": "end-to-end continues prediction",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00590"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "end-to-end continues prediction",
    "term_id": "term-00459"
  },
  {
    "adopted": false,
    "canonical_term": "end-to-end prediction",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00591"
    ],
    "evidence_status": "database_assigned",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "term": "end-to-end prediction",
    "term_id": "term-00460"
  },
  {
    "adopted": false,
    "canonical_term": "envelope",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00599"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "envelope",
    "term_id": "term-00468"
  },
  {
    "adopted": false,
    "canonical_term": "envelope was extracted",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00600"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "envelope was extracted",
    "term_id": "term-00469"
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
    "canonical_term": "error between",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00609"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "error between",
    "term_id": "term-00474"
  },
  {
    "adopted": false,
    "canonical_term": "evaluate",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00636"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "evaluate",
    "term_id": "term-00492"
  },
  {
    "adopted": false,
    "canonical_term": "evaluate the error",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00637"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "evaluate the error",
    "term_id": "term-00493"
  },
  {
    "adopted": false,
    "canonical_term": "exoskeleton",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00645"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "exoskeleton",
    "term_id": "term-00501"
  },
  {
    "adopted": false,
    "canonical_term": "exoskeleton robots",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00646"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "exoskeleton robots",
    "term_id": "term-00502"
  },
  {
    "adopted": false,
    "canonical_term": "exoskeleton robots can",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00647"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "exoskeleton robots can",
    "term_id": "term-00503"
  },
  {
    "adopted": false,
    "canonical_term": "extracted",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00672",
      "evidence-00673"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "extracted",
    "term_id": "term-00525"
  },
  {
    "adopted": false,
    "canonical_term": "extraction",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00675",
      "evidence-00676"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3013651137",
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "extraction",
    "term_id": "term-00527"
  },
  {
    "adopted": false,
    "canonical_term": "extraction process",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00678"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "extraction process",
    "term_id": "term-00529"
  },
  {
    "adopted": false,
    "canonical_term": "extraction process based",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00679"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "extraction process based",
    "term_id": "term-00530"
  },
  {
    "adopted": false,
    "canonical_term": "feature",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00690",
      "evidence-00691"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3013651137",
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "feature",
    "term_id": "term-00541"
  },
  {
    "adopted": false,
    "canonical_term": "feature extraction",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00693",
      "evidence-00694"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3013651137",
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "feature extraction",
    "term_id": "term-00543"
  },
  {
    "adopted": false,
    "canonical_term": "feature extraction process",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00695"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "feature extraction process",
    "term_id": "term-00544"
  },
  {
    "adopted": false,
    "canonical_term": "finally",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00722",
      "evidence-00723"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "finally",
    "term_id": "term-00566"
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
    "canonical_term": "first collected",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00726"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "first collected",
    "term_id": "term-00568"
  },
  {
    "adopted": false,
    "canonical_term": "first collected semg",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00727"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "first collected semg",
    "term_id": "term-00569"
  },
  {
    "adopted": false,
    "canonical_term": "guarantee",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00790"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "guarantee",
    "term_id": "term-00624"
  },
  {
    "adopted": false,
    "canonical_term": "healthy",
    "category": "unclassified",
    "document_frequency": 4,
    "evidence_ids": [
      "evidence-00814",
      "evidence-00815",
      "evidence-00816",
      "evidence-00817"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W1918406696",
      "https://openalex.org/W4284878820",
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "healthy",
    "term_id": "term-00642"
  },
  {
    "adopted": false,
    "canonical_term": "healthy subjects",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00822",
      "evidence-00823"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "healthy subjects",
    "term_id": "term-00647"
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
    "canonical_term": "human knee",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00861",
      "evidence-00862"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "human knee",
    "term_id": "term-00679"
  },
  {
    "adopted": false,
    "canonical_term": "human knee angle",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00863"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "human knee angle",
    "term_id": "term-00680"
  },
  {
    "adopted": false,
    "canonical_term": "human knee joint",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00864",
      "evidence-00865"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "human knee joint",
    "term_id": "term-00681"
  },
  {
    "adopted": false,
    "canonical_term": "human-computer",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00869"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "human-computer",
    "term_id": "term-00685"
  },
  {
    "adopted": false,
    "canonical_term": "human-computer interaction",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00870"
    ],
    "evidence_status": "database_assigned",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "term": "human-computer interaction",
    "term_id": "term-00686"
  },
  {
    "adopted": false,
    "canonical_term": "human-computer interaction",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00871"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "human-computer interaction",
    "term_id": "term-00687"
  },
  {
    "adopted": false,
    "canonical_term": "human-computer interaction performance",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00872"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "human-computer interaction performance",
    "term_id": "term-00688"
  },
  {
    "adopted": false,
    "canonical_term": "improving",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00897"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "improving",
    "term_id": "term-00709"
  },
  {
    "adopted": false,
    "canonical_term": "improving human-computer",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00898"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "improving human-computer",
    "term_id": "term-00710"
  },
  {
    "adopted": false,
    "canonical_term": "improving human-computer interaction",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00899"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "improving human-computer interaction",
    "term_id": "term-00711"
  },
  {
    "adopted": false,
    "canonical_term": "input",
    "category": "unclassified",
    "document_frequency": 3,
    "evidence_ids": [
      "evidence-00921",
      "evidence-00922",
      "evidence-00923"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4284878820",
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "input",
    "term_id": "term-00731"
  },
  {
    "adopted": false,
    "canonical_term": "interaction",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00942",
      "evidence-00943"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "interaction",
    "term_id": "term-00748"
  },
  {
    "adopted": false,
    "canonical_term": "interaction performance",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00944"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "interaction performance",
    "term_id": "term-00749"
  },
  {
    "adopted": false,
    "canonical_term": "intervention",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00949"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "intervention",
    "term_id": "term-00754"
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
    "canonical_term": "joint angle after",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01008"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "joint angle after",
    "term_id": "term-00780"
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
    "canonical_term": "joint angles based",
    "category": "unclassified",
    "document_frequency": 3,
    "evidence_ids": [
      "evidence-01040",
      "evidence-01041",
      "evidence-01042",
      "evidence-01043"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3013651137",
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "joint angles based",
    "term_id": "term-00790"
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
    "canonical_term": "knee angle",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01070"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "knee angle",
    "term_id": "term-00810"
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
    "canonical_term": "knee joint angle",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01080",
      "evidence-01081"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4416190202"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "knee joint angle",
    "term_id": "term-00816"
  },
  {
    "adopted": false,
    "canonical_term": "knee joint angles",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01082",
      "evidence-01083",
      "evidence-01084"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W1918406696",
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "knee joint angles",
    "term_id": "term-00817"
  },
  {
    "adopted": false,
    "canonical_term": "making",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01176",
      "evidence-01177"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "making",
    "term_id": "term-00893"
  },
  {
    "adopted": false,
    "canonical_term": "making real-time",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01178"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "making real-time",
    "term_id": "term-00894"
  },
  {
    "adopted": false,
    "canonical_term": "making real-time performance",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01179"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "making real-time performance",
    "term_id": "term-00895"
  },
  {
    "adopted": false,
    "canonical_term": "manual",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01181"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "manual",
    "term_id": "term-00897"
  },
  {
    "adopted": false,
    "canonical_term": "manual intervention",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01182"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "manual intervention",
    "term_id": "term-00898"
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
    "canonical_term": "metrics",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01230"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "metrics",
    "term_id": "term-00933"
  },
  {
    "adopted": false,
    "canonical_term": "metrics to evaluate",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01231"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "metrics to evaluate",
    "term_id": "term-00934"
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
    "canonical_term": "model can",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01254"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "model can",
    "term_id": "term-00948"
  },
  {
    "adopted": false,
    "canonical_term": "model can predict",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01255"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "model can predict",
    "term_id": "term-00949"
  },
  {
    "adopted": false,
    "canonical_term": "model to predict",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01267"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "model to predict",
    "term_id": "term-00960"
  },
  {
    "adopted": false,
    "canonical_term": "ms",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01327"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "ms",
    "term_id": "term-01004"
  },
  {
    "adopted": false,
    "canonical_term": "noise-removed",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01390"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "noise-removed",
    "term_id": "term-01055"
  },
  {
    "adopted": false,
    "canonical_term": "noise-removed semg",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01391"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "noise-removed semg",
    "term_id": "term-01056"
  },
  {
    "adopted": false,
    "canonical_term": "noise-removed semg signal",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01392"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "noise-removed semg signal",
    "term_id": "term-01057"
  },
  {
    "adopted": false,
    "canonical_term": "patients",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01473",
      "evidence-01474"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4284878820",
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "patients",
    "term_id": "term-01133"
  },
  {
    "adopted": false,
    "canonical_term": "patients with physical",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01475"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "patients with physical",
    "term_id": "term-01134"
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
    "canonical_term": "performance difficult",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01491"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "performance difficult",
    "term_id": "term-01143"
  },
  {
    "adopted": false,
    "canonical_term": "physical",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01500"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "physical",
    "term_id": "term-01152"
  },
  {
    "adopted": false,
    "canonical_term": "physical dysfunction",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01501"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "physical dysfunction",
    "term_id": "term-01153"
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
    "canonical_term": "predict human",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01531"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "predict human",
    "term_id": "term-01181"
  },
  {
    "adopted": false,
    "canonical_term": "predict human knee",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01532"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "predict human knee",
    "term_id": "term-01182"
  },
  {
    "adopted": false,
    "canonical_term": "predict the human",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01535"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "predict the human",
    "term_id": "term-01185"
  },
  {
    "adopted": false,
    "canonical_term": "predict the knee",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01536"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "predict the knee",
    "term_id": "term-01186"
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
    "canonical_term": "predicted knee",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01539"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "predicted knee",
    "term_id": "term-01188"
  },
  {
    "adopted": false,
    "canonical_term": "predicted knee angle",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01540"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "predicted knee angle",
    "term_id": "term-01189"
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
    "canonical_term": "prediction of human",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01565"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "prediction of human",
    "term_id": "term-01202"
  },
  {
    "adopted": false,
    "canonical_term": "prediction performance",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01568"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "prediction performance",
    "term_id": "term-01205"
  },
  {
    "adopted": false,
    "canonical_term": "process",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01577"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "process",
    "term_id": "term-01214"
  },
  {
    "adopted": false,
    "canonical_term": "process based",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01578"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "process based",
    "term_id": "term-01215"
  },
  {
    "adopted": false,
    "canonical_term": "promote",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01581",
      "evidence-01582"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4284878820",
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "promote",
    "term_id": "term-01218"
  },
  {
    "adopted": false,
    "canonical_term": "promote the rehabilitation",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01585"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "promote the rehabilitation",
    "term_id": "term-01221"
  },
  {
    "adopted": false,
    "canonical_term": "propose",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01586"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "propose",
    "term_id": "term-01222"
  },
  {
    "adopted": false,
    "canonical_term": "propose an end-to-end",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01587"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "propose an end-to-end",
    "term_id": "term-01223"
  },
  {
    "adopted": false,
    "canonical_term": "quickly",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01625"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "quickly",
    "term_id": "term-01254"
  },
  {
    "adopted": false,
    "canonical_term": "r2as",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01626"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "r2as",
    "term_id": "term-01255"
  },
  {
    "adopted": false,
    "canonical_term": "r2as metrics",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01627"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "r2as metrics",
    "term_id": "term-01256"
  },
  {
    "adopted": false,
    "canonical_term": "real-time",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01635",
      "evidence-01636"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "real-time",
    "term_id": "term-01264"
  },
  {
    "adopted": false,
    "canonical_term": "real-time motion prediction",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01637"
    ],
    "evidence_status": "database_assigned",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "term": "real-time motion prediction",
    "term_id": "term-01265"
  },
  {
    "adopted": false,
    "canonical_term": "real-time performance",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01638"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "real-time performance",
    "term_id": "term-01266"
  },
  {
    "adopted": false,
    "canonical_term": "real-time performance difficult",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01639"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "real-time performance difficult",
    "term_id": "term-01267"
  },
  {
    "adopted": false,
    "canonical_term": "rehabilitation",
    "category": "unclassified",
    "document_frequency": 4,
    "evidence_ids": [
      "evidence-01681",
      "evidence-01682",
      "evidence-01683",
      "evidence-01684"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3013651137",
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "rehabilitation",
    "term_id": "term-01302"
  },
  {
    "adopted": false,
    "canonical_term": "rehabilitation of patients",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01686"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "rehabilitation of patients",
    "term_id": "term-01304"
  },
  {
    "adopted": false,
    "canonical_term": "rehabilitation robotics",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01687",
      "evidence-01688"
    ],
    "evidence_status": "database_assigned",
    "paper_ids": [
      "https://openalex.org/W2072588720",
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "term": "rehabilitation robotics",
    "term_id": "term-01305"
  },
  {
    "adopted": false,
    "canonical_term": "requires",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01706"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "requires",
    "term_id": "term-01323"
  },
  {
    "adopted": false,
    "canonical_term": "requires manual",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01707"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "requires manual",
    "term_id": "term-01324"
  },
  {
    "adopted": false,
    "canonical_term": "requires manual intervention",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01708"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "requires manual intervention",
    "term_id": "term-01325"
  },
  {
    "adopted": false,
    "canonical_term": "results",
    "category": "unclassified",
    "document_frequency": 5,
    "evidence_ids": [
      "evidence-01719",
      "evidence-01720",
      "evidence-01721",
      "evidence-01722",
      "evidence-01723"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W1918406696",
      "https://openalex.org/W3013651137",
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "results",
    "term_id": "term-01336"
  },
  {
    "adopted": false,
    "canonical_term": "results show",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01727",
      "evidence-01728"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "results show",
    "term_id": "term-01340"
  },
  {
    "adopted": false,
    "canonical_term": "rmse",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01735"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "rmse",
    "term_id": "term-01347"
  },
  {
    "adopted": false,
    "canonical_term": "robots",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01737",
      "evidence-01738"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465",
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "robots",
    "term_id": "term-01349"
  },
  {
    "adopted": false,
    "canonical_term": "robots can",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01739"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "robots can",
    "term_id": "term-01350"
  },
  {
    "adopted": false,
    "canonical_term": "robots can promote",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01740"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "robots can promote",
    "term_id": "term-01351"
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
    "canonical_term": "semg signal",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01789"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "semg signal",
    "term_id": "term-01385"
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
    "canonical_term": "semg-based end-to-end",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01804"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "semg-based end-to-end",
    "term_id": "term-01391"
  },
  {
    "adopted": false,
    "canonical_term": "semg-based end-to-end continues",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01805"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "semg-based end-to-end continues",
    "term_id": "term-01392"
  },
  {
    "adopted": false,
    "canonical_term": "show",
    "category": "unclassified",
    "document_frequency": 3,
    "evidence_ids": [
      "evidence-01823",
      "evidence-01824",
      "evidence-01825"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W2091022037",
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "show",
    "term_id": "term-01403"
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
    "canonical_term": "signal and used",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01831"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "signal and used",
    "term_id": "term-01406"
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
    "canonical_term": "signals from 5",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01850"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "signals from 5",
    "term_id": "term-01414"
  },
  {
    "adopted": false,
    "canonical_term": "significant",
    "category": "unclassified",
    "document_frequency": 3,
    "evidence_ids": [
      "evidence-01857",
      "evidence-01858",
      "evidence-01859"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W1918406696",
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "significant",
    "term_id": "term-01420"
  },
  {
    "adopted": false,
    "canonical_term": "significant challenge",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01860"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "significant challenge",
    "term_id": "term-01421"
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
    "canonical_term": "tcct",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02008"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "tcct",
    "term_id": "term-01511"
  },
  {
    "adopted": false,
    "canonical_term": "tcct model",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02009"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "tcct model",
    "term_id": "term-01512"
  },
  {
    "adopted": false,
    "canonical_term": "then",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-02037",
      "evidence-02038"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "then",
    "term_id": "term-01538"
  },
  {
    "adopted": false,
    "canonical_term": "tightly",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02065",
      "evidence-02066"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "tightly",
    "term_id": "term-01561"
  },
  {
    "adopted": false,
    "canonical_term": "tightly coupled",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02067",
      "evidence-02068"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "tightly coupled",
    "term_id": "term-01562"
  },
  {
    "adopted": false,
    "canonical_term": "tightly coupled convolutional",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02069",
      "evidence-02070"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "tightly coupled convolutional",
    "term_id": "term-01563"
  },
  {
    "adopted": false,
    "canonical_term": "traditional",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-02088",
      "evidence-02089"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "traditional",
    "term_id": "term-01578"
  },
  {
    "adopted": false,
    "canonical_term": "traditional feature",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02090"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "traditional feature",
    "term_id": "term-01579"
  },
  {
    "adopted": false,
    "canonical_term": "traditional feature extraction",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02091"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "traditional feature extraction",
    "term_id": "term-01580"
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
    "canonical_term": "transformer model",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02107"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "transformer model",
    "term_id": "term-01592"
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
    "canonical_term": "used the root",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02151"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "used the root",
    "term_id": "term-01632"
  },
  {
    "adopted": false,
    "canonical_term": "wearable",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02193"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "wearable",
    "term_id": "term-01672"
  },
  {
    "adopted": false,
    "canonical_term": "wearable exoskeleton",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02194"
    ],
    "evidence_status": "database_assigned",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "term": "wearable exoskeleton",
    "term_id": "term-01673"
  },
  {
    "adopted": false,
    "canonical_term": "wearable exoskeleton",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02195"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "wearable exoskeleton",
    "term_id": "term-01674"
  },
  {
    "adopted": false,
    "canonical_term": "wearable exoskeleton robots",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02196"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4385757465"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "wearable exoskeleton robots",
    "term_id": "term-01675"
  }
]
```

## 证据与引用 URL
```
[
  {
    "evidence_id": "evidence-00009",
    "evidence_level": "A",
    "excerpt": "100",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00010",
    "evidence_level": "A",
    "excerpt": "100 ms",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00022",
    "evidence_level": "A",
    "excerpt": "5",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00023",
    "evidence_level": "A",
    "excerpt": "5 healthy",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00024",
    "evidence_level": "A",
    "excerpt": "5 healthy subjects",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00046",
    "evidence_level": "A",
    "excerpt": "accurately",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00064",
    "evidence_level": "A",
    "excerpt": "actual",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00065",
    "evidence_level": "A",
    "excerpt": "actual knee",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00066",
    "evidence_level": "A",
    "excerpt": "actual knee angle",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00067",
    "evidence_level": "A",
    "excerpt": "Adjustment",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00068",
    "evidence_level": "A",
    "excerpt": "Adjustment R2as",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00069",
    "evidence_level": "A",
    "excerpt": "Adjustment R2as metrics",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00073",
    "evidence_level": "A",
    "excerpt": "after",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00074",
    "evidence_level": "A",
    "excerpt": "after 100",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00075",
    "evidence_level": "A",
    "excerpt": "after 100 ms",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00101",
    "evidence_level": "A",
    "excerpt": "angle",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00107",
    "evidence_level": "A",
    "excerpt": "angle after",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00108",
    "evidence_level": "A",
    "excerpt": "angle after 100",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00125",
    "evidence_level": "A",
    "excerpt": "angle quickly",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00135",
    "evidence_level": "A",
    "excerpt": "angles",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00136",
    "evidence_level": "A",
    "excerpt": "Angles",
    "locator": "title",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00148",
    "evidence_level": "A",
    "excerpt": "angles based",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00184",
    "evidence_level": "A",
    "excerpt": "based",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00187",
    "evidence_level": "A",
    "excerpt": "based on sEMG",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00193",
    "evidence_level": "A",
    "excerpt": "based on surface",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00203",
    "evidence_level": "A",
    "excerpt": "between",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00208",
    "evidence_level": "A",
    "excerpt": "between the actual",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00234",
    "evidence_level": "A",
    "excerpt": "can",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00238",
    "evidence_level": "A",
    "excerpt": "can predict",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00239",
    "evidence_level": "A",
    "excerpt": "can promote",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00252",
    "evidence_level": "A",
    "excerpt": "CC",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00255",
    "evidence_level": "A",
    "excerpt": "challenge",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00256",
    "evidence_level": "A",
    "excerpt": "challenge for exoskeleton",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00282",
    "evidence_level": "A",
    "excerpt": "Coefficient",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00286",
    "evidence_level": "A",
    "excerpt": "collected",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00287",
    "evidence_level": "A",
    "excerpt": "collected sEMG",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00288",
    "evidence_level": "A",
    "excerpt": "collected sEMG signals",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00305",
    "evidence_level": "A",
    "excerpt": "complex",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00306",
    "evidence_level": "A",
    "excerpt": "complex and requires",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00324",
    "evidence_level": "A",
    "excerpt": "Continues",
    "locator": "title",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00325",
    "evidence_level": "A",
    "excerpt": "Continues Prediction",
    "locator": "title",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00361",
    "evidence_level": "A",
    "excerpt": "convolutional",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00362",
    "evidence_level": "A",
    "excerpt": "Convolutional",
    "locator": "title",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00368",
    "evidence_level": "A",
    "excerpt": "convolutional transformer",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00369",
    "evidence_level": "A",
    "excerpt": "Convolutional Transformer",
    "locator": "title",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00370",
    "evidence_level": "A",
    "excerpt": "Convolutional Transformer Model",
    "locator": "title",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00375",
    "evidence_level": "A",
    "excerpt": "Correlation",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00380",
    "evidence_level": "A",
    "excerpt": "Correlation Coefficient",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00385",
    "evidence_level": "A",
    "excerpt": "coupled",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00386",
    "evidence_level": "A",
    "excerpt": "Coupled",
    "locator": "title",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00387",
    "evidence_level": "A",
    "excerpt": "coupled convolutional",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00388",
    "evidence_level": "A",
    "excerpt": "Coupled Convolutional",
    "locator": "title",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00389",
    "evidence_level": "A",
    "excerpt": "coupled convolutional transformer",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00390",
    "evidence_level": "A",
    "excerpt": "Coupled Convolutional Transformer",
    "locator": "title",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00435",
    "evidence_level": "A",
    "excerpt": "developed",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00438",
    "evidence_level": "A",
    "excerpt": "developed the TCCT",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00449",
    "evidence_level": "A",
    "excerpt": "difficult",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00451",
    "evidence_level": "A",
    "excerpt": "difficult to guarantee",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00504",
    "evidence_level": "A",
    "excerpt": "dysfunction",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00553",
    "evidence_level": "A",
    "excerpt": "Electromyography",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00587",
    "evidence_level": "A",
    "excerpt": "end-to-end",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00588",
    "evidence_level": "A",
    "excerpt": "End-to-End",
    "locator": "title",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00589",
    "evidence_level": "A",
    "excerpt": "End-to-End Continues",
    "locator": "title",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00590",
    "evidence_level": "A",
    "excerpt": "End-to-End Continues Prediction",
    "locator": "title",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00591",
    "evidence_level": "A",
    "excerpt": "end-to-end prediction",
    "locator": "database_keywords",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00599",
    "evidence_level": "A",
    "excerpt": "envelope",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00600",
    "evidence_level": "A",
    "excerpt": "envelope was extracted",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00604",
    "evidence_level": "A",
    "excerpt": "Error",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00609",
    "evidence_level": "A",
    "excerpt": "error between",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00636",
    "evidence_level": "A",
    "excerpt": "evaluate",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00637",
    "evidence_level": "A",
    "excerpt": "evaluate the error",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00645",
    "evidence_level": "A",
    "excerpt": "exoskeleton",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00646",
    "evidence_level": "A",
    "excerpt": "exoskeleton robots",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00647",
    "evidence_level": "A",
    "excerpt": "exoskeleton robots can",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00673",
    "evidence_level": "A",
    "excerpt": "extracted",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00676",
    "evidence_level": "A",
    "excerpt": "extraction",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00678",
    "evidence_level": "A",
    "excerpt": "extraction process",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00679",
    "evidence_level": "A",
    "excerpt": "extraction process based",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00691",
    "evidence_level": "A",
    "excerpt": "feature",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00694",
    "evidence_level": "A",
    "excerpt": "feature extraction",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00695",
    "evidence_level": "A",
    "excerpt": "feature extraction process",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00722",
    "evidence_level": "A",
    "excerpt": "Finally",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00724",
    "evidence_level": "A",
    "excerpt": "first",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00726",
    "evidence_level": "A",
    "excerpt": "first collected",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00727",
    "evidence_level": "A",
    "excerpt": "first collected sEMG",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00790",
    "evidence_level": "A",
    "excerpt": "guarantee",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00816",
    "evidence_level": "A",
    "excerpt": "healthy",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00822",
    "evidence_level": "A",
    "excerpt": "healthy subjects",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00855",
    "evidence_level": "A",
    "excerpt": "human",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00856",
    "evidence_level": "A",
    "excerpt": "Human",
    "locator": "title",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00861",
    "evidence_level": "A",
    "excerpt": "human knee",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00862",
    "evidence_level": "A",
    "excerpt": "Human Knee",
    "locator": "title",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00863",
    "evidence_level": "A",
    "excerpt": "human knee angle",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00864",
    "evidence_level": "A",
    "excerpt": "human knee joint",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00865",
    "evidence_level": "A",
    "excerpt": "Human Knee Joint",
    "locator": "title",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00869",
    "evidence_level": "A",
    "excerpt": "human-computer",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00870",
    "evidence_level": "A",
    "excerpt": "human-computer interaction",
    "locator": "database_keywords",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00871",
    "evidence_level": "A",
    "excerpt": "human-computer interaction",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00872",
    "evidence_level": "A",
    "excerpt": "human-computer interaction performance",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00897",
    "evidence_level": "A",
    "excerpt": "improving",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00898",
    "evidence_level": "A",
    "excerpt": "improving human-computer",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00899",
    "evidence_level": "A",
    "excerpt": "improving human-computer interaction",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00922",
    "evidence_level": "A",
    "excerpt": "input",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00942",
    "evidence_level": "A",
    "excerpt": "interaction",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00944",
    "evidence_level": "A",
    "excerpt": "interaction performance",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00949",
    "evidence_level": "A",
    "excerpt": "intervention",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00986",
    "evidence_level": "A",
    "excerpt": "joint",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00987",
    "evidence_level": "A",
    "excerpt": "Joint",
    "locator": "title",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01003",
    "evidence_level": "A",
    "excerpt": "joint angle",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01008",
    "evidence_level": "A",
    "excerpt": "joint angle after",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01032",
    "evidence_level": "A",
    "excerpt": "joint angles",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01033",
    "evidence_level": "A",
    "excerpt": "Joint Angles",
    "locator": "title",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01043",
    "evidence_level": "A",
    "excerpt": "joint angles based",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01065",
    "evidence_level": "A",
    "excerpt": "knee",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01066",
    "evidence_level": "A",
    "excerpt": "Knee",
    "locator": "title",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01070",
    "evidence_level": "A",
    "excerpt": "knee angle",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01076",
    "evidence_level": "A",
    "excerpt": "knee joint",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01077",
    "evidence_level": "A",
    "excerpt": "Knee Joint",
    "locator": "title",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01080",
    "evidence_level": "A",
    "excerpt": "knee joint angle",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01083",
    "evidence_level": "A",
    "excerpt": "knee joint angles",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01084",
    "evidence_level": "A",
    "excerpt": "Knee Joint Angles",
    "locator": "title",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01177",
    "evidence_level": "A",
    "excerpt": "making",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01178",
    "evidence_level": "A",
    "excerpt": "making real-time",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01179",
    "evidence_level": "A",
    "excerpt": "making real-time performance",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01181",
    "evidence_level": "A",
    "excerpt": "manual",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01182",
    "evidence_level": "A",
    "excerpt": "manual intervention",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01196",
    "evidence_level": "A",
    "excerpt": "Mean",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01208",
    "evidence_level": "A",
    "excerpt": "Mean Square",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01210",
    "evidence_level": "A",
    "excerpt": "Mean Square Error",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01230",
    "evidence_level": "A",
    "excerpt": "metrics",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01231",
    "evidence_level": "A",
    "excerpt": "metrics to evaluate",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01244",
    "evidence_level": "A",
    "excerpt": "model",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01245",
    "evidence_level": "A",
    "excerpt": "Model",
    "locator": "title",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01254",
    "evidence_level": "A",
    "excerpt": "model can",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01255",
    "evidence_level": "A",
    "excerpt": "model can predict",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01267",
    "evidence_level": "A",
    "excerpt": "model to predict",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01327",
    "evidence_level": "A",
    "excerpt": "ms",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01390",
    "evidence_level": "A",
    "excerpt": "noise-removed",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01391",
    "evidence_level": "A",
    "excerpt": "noise-removed sEMG",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01392",
    "evidence_level": "A",
    "excerpt": "noise-removed sEMG signal",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01474",
    "evidence_level": "A",
    "excerpt": "patients",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01475",
    "evidence_level": "A",
    "excerpt": "patients with physical",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01478",
    "evidence_level": "A",
    "excerpt": "Pearson",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01480",
    "evidence_level": "A",
    "excerpt": "Pearson Correlation",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01482",
    "evidence_level": "A",
    "excerpt": "Pearson Correlation Coefficient",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01487",
    "evidence_level": "A",
    "excerpt": "performance",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01491",
    "evidence_level": "A",
    "excerpt": "performance difficult",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01500",
    "evidence_level": "A",
    "excerpt": "physical",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01501",
    "evidence_level": "A",
    "excerpt": "physical dysfunction",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01526",
    "evidence_level": "A",
    "excerpt": "predict",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01531",
    "evidence_level": "A",
    "excerpt": "predict human",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01532",
    "evidence_level": "A",
    "excerpt": "predict human knee",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01535",
    "evidence_level": "A",
    "excerpt": "predict the human",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01536",
    "evidence_level": "A",
    "excerpt": "predict the knee",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01537",
    "evidence_level": "A",
    "excerpt": "predicted",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01539",
    "evidence_level": "A",
    "excerpt": "predicted knee",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01540",
    "evidence_level": "A",
    "excerpt": "predicted knee angle",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01546",
    "evidence_level": "A",
    "excerpt": "prediction",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01547",
    "evidence_level": "A",
    "excerpt": "Prediction",
    "locator": "title",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01565",
    "evidence_level": "A",
    "excerpt": "Prediction of Human",
    "locator": "title",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01568",
    "evidence_level": "A",
    "excerpt": "prediction performance",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01577",
    "evidence_level": "A",
    "excerpt": "process",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01578",
    "evidence_level": "A",
    "excerpt": "process based",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01582",
    "evidence_level": "A",
    "excerpt": "promote",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01585",
    "evidence_level": "A",
    "excerpt": "promote the rehabilitation",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01586",
    "evidence_level": "A",
    "excerpt": "propose",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01587",
    "evidence_level": "A",
    "excerpt": "propose an end-to-end",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01625",
    "evidence_level": "A",
    "excerpt": "quickly",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01626",
    "evidence_level": "A",
    "excerpt": "R2as",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01627",
    "evidence_level": "A",
    "excerpt": "R2as metrics",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01635",
    "evidence_level": "A",
    "excerpt": "real-time",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01637",
    "evidence_level": "A",
    "excerpt": "real-time motion prediction",
    "locator": "database_keywords",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01638",
    "evidence_level": "A",
    "excerpt": "real-time performance",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01639",
    "evidence_level": "A",
    "excerpt": "real-time performance difficult",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01683",
    "evidence_level": "A",
    "excerpt": "rehabilitation",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01686",
    "evidence_level": "A",
    "excerpt": "rehabilitation of patients",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01688",
    "evidence_level": "A",
    "excerpt": "rehabilitation robotics",
    "locator": "database_keywords",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01706",
    "evidence_level": "A",
    "excerpt": "requires",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01707",
    "evidence_level": "A",
    "excerpt": "requires manual",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01708",
    "evidence_level": "A",
    "excerpt": "requires manual intervention",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01722",
    "evidence_level": "A",
    "excerpt": "results",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01728",
    "evidence_level": "A",
    "excerpt": "results show",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01735",
    "evidence_level": "A",
    "excerpt": "RMSE",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01737",
    "evidence_level": "A",
    "excerpt": "robots",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01739",
    "evidence_level": "A",
    "excerpt": "robots can",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01740",
    "evidence_level": "A",
    "excerpt": "robots can promote",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01745",
    "evidence_level": "A",
    "excerpt": "Root",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01747",
    "evidence_level": "A",
    "excerpt": "Root Mean",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01749",
    "evidence_level": "A",
    "excerpt": "Root Mean Square",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01767",
    "evidence_level": "A",
    "excerpt": "sEMG",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01789",
    "evidence_level": "A",
    "excerpt": "sEMG signal",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01792",
    "evidence_level": "A",
    "excerpt": "sEMG signals",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01798",
    "evidence_level": "A",
    "excerpt": "sEMG-Based",
    "locator": "title",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01804",
    "evidence_level": "A",
    "excerpt": "sEMG-Based End-to-End",
    "locator": "title",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01805",
    "evidence_level": "A",
    "excerpt": "sEMG-Based End-to-End Continues",
    "locator": "title",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01825",
    "evidence_level": "A",
    "excerpt": "show",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01828",
    "evidence_level": "A",
    "excerpt": "signal",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01831",
    "evidence_level": "A",
    "excerpt": "signal and used",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01839",
    "evidence_level": "A",
    "excerpt": "signals",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01850",
    "evidence_level": "A",
    "excerpt": "signals from 5",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01859",
    "evidence_level": "A",
    "excerpt": "significant",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01860",
    "evidence_level": "A",
    "excerpt": "significant challenge",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01900",
    "evidence_level": "A",
    "excerpt": "Square",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01902",
    "evidence_level": "A",
    "excerpt": "Square Error",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01929",
    "evidence_level": "A",
    "excerpt": "subjects",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01956",
    "evidence_level": "A",
    "excerpt": "surface",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01972",
    "evidence_level": "A",
    "excerpt": "surface electromyography",
    "locator": "database_keywords",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01986",
    "evidence_level": "A",
    "excerpt": "surface Electromyography",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02008",
    "evidence_level": "A",
    "excerpt": "TCCT",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02009",
    "evidence_level": "A",
    "excerpt": "TCCT model",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02038",
    "evidence_level": "A",
    "excerpt": "Then",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02065",
    "evidence_level": "A",
    "excerpt": "tightly",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02066",
    "evidence_level": "A",
    "excerpt": "Tightly",
    "locator": "title",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02067",
    "evidence_level": "A",
    "excerpt": "tightly coupled",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02068",
    "evidence_level": "A",
    "excerpt": "Tightly Coupled",
    "locator": "title",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02069",
    "evidence_level": "A",
    "excerpt": "tightly coupled convolutional",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02070",
    "evidence_level": "A",
    "excerpt": "Tightly Coupled Convolutional",
    "locator": "title",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02089",
    "evidence_level": "A",
    "excerpt": "traditional",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02090",
    "evidence_level": "A",
    "excerpt": "traditional feature",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02091",
    "evidence_level": "A",
    "excerpt": "traditional feature extraction",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02101",
    "evidence_level": "A",
    "excerpt": "transformer",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02102",
    "evidence_level": "A",
    "excerpt": "Transformer",
    "locator": "title",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02107",
    "evidence_level": "A",
    "excerpt": "Transformer Model",
    "locator": "title",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02145",
    "evidence_level": "A",
    "excerpt": "used",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02151",
    "evidence_level": "A",
    "excerpt": "used the Root",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02193",
    "evidence_level": "A",
    "excerpt": "Wearable",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02194",
    "evidence_level": "A",
    "excerpt": "wearable exoskeleton",
    "locator": "database_keywords",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02195",
    "evidence_level": "A",
    "excerpt": "Wearable exoskeleton",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02196",
    "evidence_level": "A",
    "excerpt": "Wearable exoskeleton robots",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4385757465",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4385757465",
    "supports": "Field observation only; not semantic equivalence or relevance."
  }
]
```

## 译文
未分析，留空供人工填写。

## 创新点
未分析，留空供人工填写。

## 用户笔记
