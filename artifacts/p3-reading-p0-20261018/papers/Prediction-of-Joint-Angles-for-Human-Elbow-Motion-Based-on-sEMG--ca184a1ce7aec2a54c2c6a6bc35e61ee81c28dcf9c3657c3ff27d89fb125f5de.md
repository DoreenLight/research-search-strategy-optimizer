---
{
  "authors": [
    "Jinqiang Wang",
    "Dianguo Cao",
    "Hongyu Liu",
    "Yuqiang Wu"
  ],
  "case_id": "semg-joint-angle",
  "doi": "https://doi.org/10.1109/cac63892.2024.10865675",
  "human_judgments": [],
  "innovation_points": "",
  "model_judgments": [],
  "model_promoted_to_human": false,
  "paper_id": "https://openalex.org/W4407450426",
  "pmid": null,
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
  "source_title": "China Automation Congress (CAC)",
  "source_url": "https://openalex.org/W4407450426",
  "title": "Prediction of Joint Angles for Human Elbow Motion Based on sEMG",
  "translation": ""
}
---

# 阅读任务

状态默认为 **待确认**；可人工改为 **待读** / **已读**。模型相关性不代表人工确认。

## 标题
```
Prediction of Joint Angles for Human Elbow Motion Based on sEMG
```

## 作者
```
[
  "Jinqiang Wang",
  "Dianguo Cao",
  "Hongyu Liu",
  "Yuqiang Wu"
]
```

## 年份 / DOI / PMID
```
{
  "doi": "https://doi.org/10.1109/cac63892.2024.10865675",
  "pmid": null,
  "publication_year": 2024
}
```

## 摘要
```
In the field of intelligent rehabilitation, the primary reliance is on rehabilitation robots, which often struggle to continuously respond to a patient's movement intentions in real-time and with accuracy. To improve the level of human-robot interaction (HRI) and provide personalized rehabilitation exercises with active patient participation, this study developed a joint angle prediction model using surface electromyography (sEMG). Initially, six healthy subjects were selected, and devices for sEMG and angle acquisition were employed to synchronize the collection of sEMG and elbow joint angle data for each participant. Subsequently, the preprocessed data were input into the designed Transformer-based joint angle prediction model. Finally, the performance of the Transformer-based model was compared with that of Recurrent Neural Networks (RNN) and Convolutional Neural Network-Long Short-Term Memory (CNN-LSTM) models. Experimental results indicate that the Transformer-based joint angle prediction model outperforms its counterparts, achieving a Mean Absolute Error (MAE) of less than 0.065, thereby suggesting its potential for future applications.
```

## 来源
```
{
  "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
  "source_title": "China Automation Congress (CAC)",
  "source_url": "https://openalex.org/W4407450426"
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
    "canonical_term": "0",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00001",
      "evidence-00002"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W1918406696",
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "0",
    "term_id": "term-00001"
  },
  {
    "adopted": false,
    "canonical_term": "065",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00004"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "065",
    "term_id": "term-00003"
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
    "canonical_term": "achieving",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00052"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "achieving",
    "term_id": "term-00041"
  },
  {
    "adopted": false,
    "canonical_term": "achieving a mean",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00053"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "achieving a mean",
    "term_id": "term-00042"
  },
  {
    "adopted": false,
    "canonical_term": "acquisition",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00054"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "acquisition",
    "term_id": "term-00043"
  },
  {
    "adopted": false,
    "canonical_term": "acquisition were employed",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00055"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "acquisition were employed",
    "term_id": "term-00044"
  },
  {
    "adopted": false,
    "canonical_term": "active",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00059"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "active",
    "term_id": "term-00048"
  },
  {
    "adopted": false,
    "canonical_term": "active patient",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00060"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "active patient",
    "term_id": "term-00049"
  },
  {
    "adopted": false,
    "canonical_term": "active patient participation",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00061"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "active patient participation",
    "term_id": "term-00050"
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
    "canonical_term": "angle acquisition",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00106"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "angle acquisition",
    "term_id": "term-00081"
  },
  {
    "adopted": false,
    "canonical_term": "angle data",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00112"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "angle data",
    "term_id": "term-00086"
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
    "canonical_term": "angles for human",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00149"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "angles for human",
    "term_id": "term-00104"
  },
  {
    "adopted": false,
    "canonical_term": "applications",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00162"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "applications",
    "term_id": "term-00117"
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
    "canonical_term": "cnn-lstm",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00277"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "cnn-lstm",
    "term_id": "term-00210"
  },
  {
    "adopted": false,
    "canonical_term": "cnn-lstm comparison",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00278"
    ],
    "evidence_status": "database_assigned",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "term": "cnn-lstm comparison",
    "term_id": "term-00211"
  },
  {
    "adopted": false,
    "canonical_term": "collection",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00289"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "collection",
    "term_id": "term-00221"
  },
  {
    "adopted": false,
    "canonical_term": "collection of semg",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00290"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "collection of semg",
    "term_id": "term-00222"
  },
  {
    "adopted": false,
    "canonical_term": "compared",
    "category": "unclassified",
    "document_frequency": 3,
    "evidence_ids": [
      "evidence-00301",
      "evidence-00302",
      "evidence-00303"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W1918406696",
      "https://openalex.org/W3121018641",
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "compared",
    "term_id": "term-00232"
  },
  {
    "adopted": false,
    "canonical_term": "continuously",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00345"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "continuously",
    "term_id": "term-00264"
  },
  {
    "adopted": false,
    "canonical_term": "continuously respond",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00346"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "continuously respond",
    "term_id": "term-00265"
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
    "canonical_term": "convolutional neural",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00366"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "convolutional neural",
    "term_id": "term-00278"
  },
  {
    "adopted": false,
    "canonical_term": "convolutional neural network-long",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00367"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "convolutional neural network-long",
    "term_id": "term-00279"
  },
  {
    "adopted": false,
    "canonical_term": "counterparts",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00384"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "counterparts",
    "term_id": "term-00291"
  },
  {
    "adopted": false,
    "canonical_term": "data",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00398"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "data",
    "term_id": "term-00302"
  },
  {
    "adopted": false,
    "canonical_term": "data for each",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00399"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "data for each",
    "term_id": "term-00303"
  },
  {
    "adopted": false,
    "canonical_term": "data were input",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00400"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "data were input",
    "term_id": "term-00304"
  },
  {
    "adopted": false,
    "canonical_term": "designed",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00427"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "designed",
    "term_id": "term-00328"
  },
  {
    "adopted": false,
    "canonical_term": "designed transformer-based",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00428"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "designed transformer-based",
    "term_id": "term-00329"
  },
  {
    "adopted": false,
    "canonical_term": "designed transformer-based joint",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00429"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "designed transformer-based joint",
    "term_id": "term-00330"
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
    "canonical_term": "developed a joint",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00437"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "developed a joint",
    "term_id": "term-00337"
  },
  {
    "adopted": false,
    "canonical_term": "devices",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00440"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "devices",
    "term_id": "term-00340"
  },
  {
    "adopted": false,
    "canonical_term": "devices for semg",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00441"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "devices for semg",
    "term_id": "term-00341"
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
    "canonical_term": "each participant",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00510"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "each participant",
    "term_id": "term-00401"
  },
  {
    "adopted": false,
    "canonical_term": "elbow",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00519"
    ],
    "evidence_status": "database_assigned",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "term": "elbow",
    "term_id": "term-00409"
  },
  {
    "adopted": false,
    "canonical_term": "elbow",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00520",
      "evidence-00521"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "elbow",
    "term_id": "term-00410"
  },
  {
    "adopted": false,
    "canonical_term": "elbow joint",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00522"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "elbow joint",
    "term_id": "term-00411"
  },
  {
    "adopted": false,
    "canonical_term": "elbow joint angle",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00523"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "elbow joint angle",
    "term_id": "term-00412"
  },
  {
    "adopted": false,
    "canonical_term": "elbow motion",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00524"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "elbow motion",
    "term_id": "term-00413"
  },
  {
    "adopted": false,
    "canonical_term": "elbow motion based",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00525"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "elbow motion based",
    "term_id": "term-00414"
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
    "canonical_term": "employed",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00582"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "employed",
    "term_id": "term-00452"
  },
  {
    "adopted": false,
    "canonical_term": "employed to synchronize",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00583"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "employed to synchronize",
    "term_id": "term-00453"
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
    "canonical_term": "exercises",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00643"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "exercises",
    "term_id": "term-00499"
  },
  {
    "adopted": false,
    "canonical_term": "exercises with active",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00644"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "exercises with active",
    "term_id": "term-00500"
  },
  {
    "adopted": false,
    "canonical_term": "experimental",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00650",
      "evidence-00651"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3013651137",
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "experimental",
    "term_id": "term-00506"
  },
  {
    "adopted": false,
    "canonical_term": "experimental results",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00652",
      "evidence-00653"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3013651137",
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "experimental results",
    "term_id": "term-00507"
  },
  {
    "adopted": false,
    "canonical_term": "experimental results indicate",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00655"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "experimental results indicate",
    "term_id": "term-00509"
  },
  {
    "adopted": false,
    "canonical_term": "field",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00718"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "field",
    "term_id": "term-00562"
  },
  {
    "adopted": false,
    "canonical_term": "field of intelligent",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00719"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "field of intelligent",
    "term_id": "term-00563"
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
    "canonical_term": "future",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00775"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "future",
    "term_id": "term-00610"
  },
  {
    "adopted": false,
    "canonical_term": "future applications",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00776"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "future applications",
    "term_id": "term-00611"
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
    "canonical_term": "hri",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00853"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "hri",
    "term_id": "term-00675"
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
    "canonical_term": "human elbow",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00859"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "human elbow",
    "term_id": "term-00677"
  },
  {
    "adopted": false,
    "canonical_term": "human elbow motion",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00860"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "human elbow motion",
    "term_id": "term-00678"
  },
  {
    "adopted": false,
    "canonical_term": "human-robot",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00877"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "human-robot",
    "term_id": "term-00692"
  },
  {
    "adopted": false,
    "canonical_term": "human-robot interaction",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00878"
    ],
    "evidence_status": "database_assigned",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "term": "human-robot interaction",
    "term_id": "term-00693"
  },
  {
    "adopted": false,
    "canonical_term": "human-robot interaction",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00879"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "human-robot interaction",
    "term_id": "term-00694"
  },
  {
    "adopted": false,
    "canonical_term": "improve",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00891",
      "evidence-00892"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4284878820",
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "improve",
    "term_id": "term-00704"
  },
  {
    "adopted": false,
    "canonical_term": "improve the level",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00894"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "improve the level",
    "term_id": "term-00706"
  },
  {
    "adopted": false,
    "canonical_term": "indicate",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-00906",
      "evidence-00907"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3013651137",
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "indicate",
    "term_id": "term-00718"
  },
  {
    "adopted": false,
    "canonical_term": "initially",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00918"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "initially",
    "term_id": "term-00728"
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
    "canonical_term": "intelligent",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00932"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "intelligent",
    "term_id": "term-00740"
  },
  {
    "adopted": false,
    "canonical_term": "intelligent rehabilitation",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00933"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "intelligent rehabilitation",
    "term_id": "term-00741"
  },
  {
    "adopted": false,
    "canonical_term": "intentions",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00940"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "intentions",
    "term_id": "term-00746"
  },
  {
    "adopted": false,
    "canonical_term": "intentions in real-time",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00941"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "intentions in real-time",
    "term_id": "term-00747"
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
    "canonical_term": "its counterparts",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00971"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "its counterparts",
    "term_id": "term-00774"
  },
  {
    "adopted": false,
    "canonical_term": "its potential",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-00974"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "its potential",
    "term_id": "term-00777"
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
    "canonical_term": "joint angle data",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01010"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "joint angle data",
    "term_id": "term-00782"
  },
  {
    "adopted": false,
    "canonical_term": "joint angle prediction",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01015",
      "evidence-01016"
    ],
    "evidence_status": "database_assigned",
    "paper_ids": [
      "https://openalex.org/W3013651137",
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "term": "joint angle prediction",
    "term_id": "term-00785"
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
    "canonical_term": "less than 0",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01111"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "less than 0",
    "term_id": "term-00838"
  },
  {
    "adopted": false,
    "canonical_term": "level",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01114"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "level",
    "term_id": "term-00841"
  },
  {
    "adopted": false,
    "canonical_term": "level of human-robot",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01115"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "level of human-robot",
    "term_id": "term-00842"
  },
  {
    "adopted": false,
    "canonical_term": "mae",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01171"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "mae",
    "term_id": "term-00888"
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
    "canonical_term": "model outperforms",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01265"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "model outperforms",
    "term_id": "term-00958"
  },
  {
    "adopted": false,
    "canonical_term": "model outperforms its",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01266"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "model outperforms its",
    "term_id": "term-00959"
  },
  {
    "adopted": false,
    "canonical_term": "model using surface",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01268"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "model using surface",
    "term_id": "term-00961"
  },
  {
    "adopted": false,
    "canonical_term": "model was compared",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01269"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "model was compared",
    "term_id": "term-00962"
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
    "canonical_term": "motion based",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01301"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "motion based",
    "term_id": "term-00985"
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
    "canonical_term": "movement intention recognition",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01320"
    ],
    "evidence_status": "database_assigned",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "term": "movement intention recognition",
    "term_id": "term-00999"
  },
  {
    "adopted": false,
    "canonical_term": "movement intentions",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01321"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "movement intentions",
    "term_id": "term-01000"
  },
  {
    "adopted": false,
    "canonical_term": "network-long",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01363"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "network-long",
    "term_id": "term-01032"
  },
  {
    "adopted": false,
    "canonical_term": "network-long short-term",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01364"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "network-long short-term",
    "term_id": "term-01033"
  },
  {
    "adopted": false,
    "canonical_term": "network-long short-term memory",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01365"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "network-long short-term memory",
    "term_id": "term-01034"
  },
  {
    "adopted": false,
    "canonical_term": "networks",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01366"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "networks",
    "term_id": "term-01035"
  },
  {
    "adopted": false,
    "canonical_term": "neural",
    "category": "unclassified",
    "document_frequency": 4,
    "evidence_ids": [
      "evidence-01367",
      "evidence-01368",
      "evidence-01369",
      "evidence-01370"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W1918406696",
      "https://openalex.org/W2072588720",
      "https://openalex.org/W4284878820",
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "neural",
    "term_id": "term-01036"
  },
  {
    "adopted": false,
    "canonical_term": "neural network-long",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01374"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "neural network-long",
    "term_id": "term-01040"
  },
  {
    "adopted": false,
    "canonical_term": "neural network-long short-term",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01375"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "neural network-long short-term",
    "term_id": "term-01041"
  },
  {
    "adopted": false,
    "canonical_term": "neural networks",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01376"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "neural networks",
    "term_id": "term-01042"
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
    "canonical_term": "often struggle",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01437"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "often struggle",
    "term_id": "term-01098"
  },
  {
    "adopted": false,
    "canonical_term": "outperforms",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01441"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "outperforms",
    "term_id": "term-01102"
  },
  {
    "adopted": false,
    "canonical_term": "outperforms its",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01442"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "outperforms its",
    "term_id": "term-01103"
  },
  {
    "adopted": false,
    "canonical_term": "outperforms its counterparts",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01443"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "outperforms its counterparts",
    "term_id": "term-01104"
  },
  {
    "adopted": false,
    "canonical_term": "participant",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01461"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "participant",
    "term_id": "term-01122"
  },
  {
    "adopted": false,
    "canonical_term": "participation",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01464"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "participation",
    "term_id": "term-01125"
  },
  {
    "adopted": false,
    "canonical_term": "patient",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01467",
      "evidence-01468"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W3013651137",
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "patient",
    "term_id": "term-01128"
  },
  {
    "adopted": false,
    "canonical_term": "patient participation",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01469"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "patient participation",
    "term_id": "term-01129"
  },
  {
    "adopted": false,
    "canonical_term": "patient's",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01470"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "patient's",
    "term_id": "term-01130"
  },
  {
    "adopted": false,
    "canonical_term": "patient's movement",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01471"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "patient's movement",
    "term_id": "term-01131"
  },
  {
    "adopted": false,
    "canonical_term": "patient's movement intentions",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01472"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "patient's movement intentions",
    "term_id": "term-01132"
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
    "canonical_term": "personalized",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01497"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "personalized",
    "term_id": "term-01149"
  },
  {
    "adopted": false,
    "canonical_term": "personalized rehabilitation",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01498"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "personalized rehabilitation",
    "term_id": "term-01150"
  },
  {
    "adopted": false,
    "canonical_term": "personalized rehabilitation exercises",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01499"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "personalized rehabilitation exercises",
    "term_id": "term-01151"
  },
  {
    "adopted": false,
    "canonical_term": "potential",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01521"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "potential",
    "term_id": "term-01173"
  },
  {
    "adopted": false,
    "canonical_term": "potential for future",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01522"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "potential for future",
    "term_id": "term-01174"
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
    "canonical_term": "prediction model outperforms",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01563"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "prediction model outperforms",
    "term_id": "term-01200"
  },
  {
    "adopted": false,
    "canonical_term": "prediction of joint",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01566"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "prediction of joint",
    "term_id": "term-01203"
  },
  {
    "adopted": false,
    "canonical_term": "preprocessed",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01570"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "preprocessed",
    "term_id": "term-01207"
  },
  {
    "adopted": false,
    "canonical_term": "preprocessed data",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01571"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "preprocessed data",
    "term_id": "term-01208"
  },
  {
    "adopted": false,
    "canonical_term": "primary",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01575"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "primary",
    "term_id": "term-01212"
  },
  {
    "adopted": false,
    "canonical_term": "primary reliance",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01576"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "primary reliance",
    "term_id": "term-01213"
  },
  {
    "adopted": false,
    "canonical_term": "provide",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01602"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "provide",
    "term_id": "term-01233"
  },
  {
    "adopted": false,
    "canonical_term": "provide personalized",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01603"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "provide personalized",
    "term_id": "term-01234"
  },
  {
    "adopted": false,
    "canonical_term": "provide personalized rehabilitation",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01604"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "provide personalized rehabilitation",
    "term_id": "term-01235"
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
    "canonical_term": "recurrent",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01663"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "recurrent",
    "term_id": "term-01284"
  },
  {
    "adopted": false,
    "canonical_term": "recurrent neural",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01664"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "recurrent neural",
    "term_id": "term-01285"
  },
  {
    "adopted": false,
    "canonical_term": "recurrent neural networks",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01665"
    ],
    "evidence_status": "database_assigned",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "term": "recurrent neural networks",
    "term_id": "term-01286"
  },
  {
    "adopted": false,
    "canonical_term": "recurrent neural networks",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01666"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "recurrent neural networks",
    "term_id": "term-01287"
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
    "canonical_term": "rehabilitation exercises",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01685"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "rehabilitation exercises",
    "term_id": "term-01303"
  },
  {
    "adopted": false,
    "canonical_term": "rehabilitation robots",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01689"
    ],
    "evidence_status": "database_assigned",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "term": "rehabilitation robots",
    "term_id": "term-01306"
  },
  {
    "adopted": false,
    "canonical_term": "rehabilitation robots",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01690"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "rehabilitation robots",
    "term_id": "term-01307"
  },
  {
    "adopted": false,
    "canonical_term": "reliance",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01703"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "reliance",
    "term_id": "term-01320"
  },
  {
    "adopted": false,
    "canonical_term": "respond",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01712"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "respond",
    "term_id": "term-01329"
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
    "canonical_term": "results indicate",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01726"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "results indicate",
    "term_id": "term-01339"
  },
  {
    "adopted": false,
    "canonical_term": "rnn",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01736"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "rnn",
    "term_id": "term-01348"
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
    "canonical_term": "selected",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01760"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "selected",
    "term_id": "term-01368"
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
    "canonical_term": "semg and angle",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01779"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "semg and angle",
    "term_id": "term-01376"
  },
  {
    "adopted": false,
    "canonical_term": "semg and elbow",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01780"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "semg and elbow",
    "term_id": "term-01377"
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
    "canonical_term": "six",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01873",
      "evidence-01874"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4284878820",
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "six",
    "term_id": "term-01432"
  },
  {
    "adopted": false,
    "canonical_term": "six healthy",
    "category": "unclassified",
    "document_frequency": 2,
    "evidence_ids": [
      "evidence-01875",
      "evidence-01876"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4284878820",
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "six healthy",
    "term_id": "term-01433"
  },
  {
    "adopted": false,
    "canonical_term": "six healthy subjects",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01878"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "six healthy subjects",
    "term_id": "term-01435"
  },
  {
    "adopted": false,
    "canonical_term": "struggle",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01925"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "struggle",
    "term_id": "term-01474"
  },
  {
    "adopted": false,
    "canonical_term": "struggle to continuously",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01926"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "struggle to continuously",
    "term_id": "term-01475"
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
    "canonical_term": "subjects were selected",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01936"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "subjects were selected",
    "term_id": "term-01481"
  },
  {
    "adopted": false,
    "canonical_term": "subsequently",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01937"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "subsequently",
    "term_id": "term-01482"
  },
  {
    "adopted": false,
    "canonical_term": "suggesting",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01941"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "suggesting",
    "term_id": "term-01486"
  },
  {
    "adopted": false,
    "canonical_term": "suggesting its",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01942"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "suggesting its",
    "term_id": "term-01487"
  },
  {
    "adopted": false,
    "canonical_term": "suggesting its potential",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01943"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "suggesting its potential",
    "term_id": "term-01488"
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
    "canonical_term": "synchronize",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01997"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "synchronize",
    "term_id": "term-01500"
  },
  {
    "adopted": false,
    "canonical_term": "synchronize the collection",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-01998"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "synchronize the collection",
    "term_id": "term-01501"
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
    "canonical_term": "than 0",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02034"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "than 0",
    "term_id": "term-01535"
  },
  {
    "adopted": false,
    "canonical_term": "thereby",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02040"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "thereby",
    "term_id": "term-01540"
  },
  {
    "adopted": false,
    "canonical_term": "thereby suggesting",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02041"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "thereby suggesting",
    "term_id": "term-01541"
  },
  {
    "adopted": false,
    "canonical_term": "thereby suggesting its",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02042"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "thereby suggesting its",
    "term_id": "term-01542"
  },
  {
    "adopted": false,
    "canonical_term": "transformer models",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02108"
    ],
    "evidence_status": "database_assigned",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "term": "transformer models",
    "term_id": "term-01593"
  },
  {
    "adopted": false,
    "canonical_term": "transformer-based",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02110"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "transformer-based",
    "term_id": "term-01595"
  },
  {
    "adopted": false,
    "canonical_term": "transformer-based joint",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02111"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "transformer-based joint",
    "term_id": "term-01596"
  },
  {
    "adopted": false,
    "canonical_term": "transformer-based joint angle",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02112"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "transformer-based joint angle",
    "term_id": "term-01597"
  },
  {
    "adopted": false,
    "canonical_term": "transformer-based model",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02113"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "transformer-based model",
    "term_id": "term-01598"
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
    "canonical_term": "which often",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02211"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "which often",
    "term_id": "term-01686"
  },
  {
    "adopted": false,
    "canonical_term": "which often struggle",
    "category": "unclassified",
    "document_frequency": 1,
    "evidence_ids": [
      "evidence-02212"
    ],
    "evidence_status": "observed_in_paper",
    "paper_ids": [
      "https://openalex.org/W4407450426"
    ],
    "relationship": "unclassified",
    "retrieval_status": "untested",
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "term": "which often struggle",
    "term_id": "term-01687"
  }
]
```

## 证据与引用 URL
```
[
  {
    "evidence_id": "evidence-00002",
    "evidence_level": "A",
    "excerpt": "0",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00004",
    "evidence_level": "A",
    "excerpt": "065",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00031",
    "evidence_level": "A",
    "excerpt": "Absolute",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00033",
    "evidence_level": "A",
    "excerpt": "Absolute Error",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00040",
    "evidence_level": "A",
    "excerpt": "accuracy",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00052",
    "evidence_level": "A",
    "excerpt": "achieving",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00053",
    "evidence_level": "A",
    "excerpt": "achieving a Mean",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00054",
    "evidence_level": "A",
    "excerpt": "acquisition",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00055",
    "evidence_level": "A",
    "excerpt": "acquisition were employed",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00059",
    "evidence_level": "A",
    "excerpt": "active",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00060",
    "evidence_level": "A",
    "excerpt": "active patient",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00061",
    "evidence_level": "A",
    "excerpt": "active patient participation",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00104",
    "evidence_level": "A",
    "excerpt": "angle",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00106",
    "evidence_level": "A",
    "excerpt": "angle acquisition",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00112",
    "evidence_level": "A",
    "excerpt": "angle data",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00122",
    "evidence_level": "A",
    "excerpt": "angle prediction",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00124",
    "evidence_level": "A",
    "excerpt": "angle prediction model",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00140",
    "evidence_level": "A",
    "excerpt": "Angles",
    "locator": "title",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00149",
    "evidence_level": "A",
    "excerpt": "Angles for Human",
    "locator": "title",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00162",
    "evidence_level": "A",
    "excerpt": "applications",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00186",
    "evidence_level": "A",
    "excerpt": "Based",
    "locator": "title",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00189",
    "evidence_level": "A",
    "excerpt": "Based on sEMG",
    "locator": "title",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00277",
    "evidence_level": "A",
    "excerpt": "CNN-LSTM",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00278",
    "evidence_level": "A",
    "excerpt": "CNN-LSTM comparison",
    "locator": "database_keywords",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00289",
    "evidence_level": "A",
    "excerpt": "collection",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00290",
    "evidence_level": "A",
    "excerpt": "collection of sEMG",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00303",
    "evidence_level": "A",
    "excerpt": "compared",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00345",
    "evidence_level": "A",
    "excerpt": "continuously",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00346",
    "evidence_level": "A",
    "excerpt": "continuously respond",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00364",
    "evidence_level": "A",
    "excerpt": "Convolutional",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00366",
    "evidence_level": "A",
    "excerpt": "Convolutional Neural",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00367",
    "evidence_level": "A",
    "excerpt": "Convolutional Neural Network-Long",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00384",
    "evidence_level": "A",
    "excerpt": "counterparts",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00398",
    "evidence_level": "A",
    "excerpt": "data",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00399",
    "evidence_level": "A",
    "excerpt": "data for each",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00400",
    "evidence_level": "A",
    "excerpt": "data were input",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00427",
    "evidence_level": "A",
    "excerpt": "designed",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00428",
    "evidence_level": "A",
    "excerpt": "designed Transformer-based",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00429",
    "evidence_level": "A",
    "excerpt": "designed Transformer-based joint",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00436",
    "evidence_level": "A",
    "excerpt": "developed",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00437",
    "evidence_level": "A",
    "excerpt": "developed a joint",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00440",
    "evidence_level": "A",
    "excerpt": "devices",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00441",
    "evidence_level": "A",
    "excerpt": "devices for sEMG",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00506",
    "evidence_level": "A",
    "excerpt": "each",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00510",
    "evidence_level": "A",
    "excerpt": "each participant",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00519",
    "evidence_level": "A",
    "excerpt": "elbow",
    "locator": "database_keywords",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00520",
    "evidence_level": "A",
    "excerpt": "elbow",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00521",
    "evidence_level": "A",
    "excerpt": "Elbow",
    "locator": "title",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00522",
    "evidence_level": "A",
    "excerpt": "elbow joint",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00523",
    "evidence_level": "A",
    "excerpt": "elbow joint angle",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00524",
    "evidence_level": "A",
    "excerpt": "Elbow Motion",
    "locator": "title",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00525",
    "evidence_level": "A",
    "excerpt": "Elbow Motion Based",
    "locator": "title",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00556",
    "evidence_level": "A",
    "excerpt": "electromyography",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00582",
    "evidence_level": "A",
    "excerpt": "employed",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00583",
    "evidence_level": "A",
    "excerpt": "employed to synchronize",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00606",
    "evidence_level": "A",
    "excerpt": "Error",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00643",
    "evidence_level": "A",
    "excerpt": "exercises",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00644",
    "evidence_level": "A",
    "excerpt": "exercises with active",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00651",
    "evidence_level": "A",
    "excerpt": "Experimental",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00653",
    "evidence_level": "A",
    "excerpt": "Experimental results",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00655",
    "evidence_level": "A",
    "excerpt": "Experimental results indicate",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00718",
    "evidence_level": "A",
    "excerpt": "field",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00719",
    "evidence_level": "A",
    "excerpt": "field of intelligent",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00723",
    "evidence_level": "A",
    "excerpt": "Finally",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00775",
    "evidence_level": "A",
    "excerpt": "future",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00776",
    "evidence_level": "A",
    "excerpt": "future applications",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00817",
    "evidence_level": "A",
    "excerpt": "healthy",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00823",
    "evidence_level": "A",
    "excerpt": "healthy subjects",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00853",
    "evidence_level": "A",
    "excerpt": "HRI",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00858",
    "evidence_level": "A",
    "excerpt": "Human",
    "locator": "title",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00859",
    "evidence_level": "A",
    "excerpt": "Human Elbow",
    "locator": "title",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00860",
    "evidence_level": "A",
    "excerpt": "Human Elbow Motion",
    "locator": "title",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00877",
    "evidence_level": "A",
    "excerpt": "human-robot",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00878",
    "evidence_level": "A",
    "excerpt": "human-robot interaction",
    "locator": "database_keywords",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00879",
    "evidence_level": "A",
    "excerpt": "human-robot interaction",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00892",
    "evidence_level": "A",
    "excerpt": "improve",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00894",
    "evidence_level": "A",
    "excerpt": "improve the level",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00907",
    "evidence_level": "A",
    "excerpt": "indicate",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00918",
    "evidence_level": "A",
    "excerpt": "Initially",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00923",
    "evidence_level": "A",
    "excerpt": "input",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00932",
    "evidence_level": "A",
    "excerpt": "intelligent",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00933",
    "evidence_level": "A",
    "excerpt": "intelligent rehabilitation",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00940",
    "evidence_level": "A",
    "excerpt": "intentions",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00941",
    "evidence_level": "A",
    "excerpt": "intentions in real-time",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00943",
    "evidence_level": "A",
    "excerpt": "interaction",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00970",
    "evidence_level": "A",
    "excerpt": "its",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00971",
    "evidence_level": "A",
    "excerpt": "its counterparts",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00974",
    "evidence_level": "A",
    "excerpt": "its potential",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00992",
    "evidence_level": "A",
    "excerpt": "joint",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-00993",
    "evidence_level": "A",
    "excerpt": "Joint",
    "locator": "title",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01006",
    "evidence_level": "A",
    "excerpt": "joint angle",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01010",
    "evidence_level": "A",
    "excerpt": "joint angle data",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01016",
    "evidence_level": "A",
    "excerpt": "joint angle prediction",
    "locator": "database_keywords",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01018",
    "evidence_level": "A",
    "excerpt": "joint angle prediction",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01037",
    "evidence_level": "A",
    "excerpt": "Joint Angles",
    "locator": "title",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01108",
    "evidence_level": "A",
    "excerpt": "less",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01110",
    "evidence_level": "A",
    "excerpt": "less than",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01111",
    "evidence_level": "A",
    "excerpt": "less than 0",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01114",
    "evidence_level": "A",
    "excerpt": "level",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01115",
    "evidence_level": "A",
    "excerpt": "level of human-robot",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01171",
    "evidence_level": "A",
    "excerpt": "MAE",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01198",
    "evidence_level": "A",
    "excerpt": "Mean",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01200",
    "evidence_level": "A",
    "excerpt": "Mean Absolute",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01202",
    "evidence_level": "A",
    "excerpt": "Mean Absolute Error",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01223",
    "evidence_level": "A",
    "excerpt": "Memory",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01249",
    "evidence_level": "A",
    "excerpt": "model",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01265",
    "evidence_level": "A",
    "excerpt": "model outperforms",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01266",
    "evidence_level": "A",
    "excerpt": "model outperforms its",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01268",
    "evidence_level": "A",
    "excerpt": "model using surface",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01269",
    "evidence_level": "A",
    "excerpt": "model was compared",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01276",
    "evidence_level": "A",
    "excerpt": "models",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01296",
    "evidence_level": "A",
    "excerpt": "Motion",
    "locator": "title",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01301",
    "evidence_level": "A",
    "excerpt": "Motion Based",
    "locator": "title",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01317",
    "evidence_level": "A",
    "excerpt": "movement",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01320",
    "evidence_level": "A",
    "excerpt": "movement intention recognition",
    "locator": "database_keywords",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01321",
    "evidence_level": "A",
    "excerpt": "movement intentions",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01363",
    "evidence_level": "A",
    "excerpt": "Network-Long",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01364",
    "evidence_level": "A",
    "excerpt": "Network-Long Short-Term",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01365",
    "evidence_level": "A",
    "excerpt": "Network-Long Short-Term Memory",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01366",
    "evidence_level": "A",
    "excerpt": "Networks",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01370",
    "evidence_level": "A",
    "excerpt": "Neural",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01374",
    "evidence_level": "A",
    "excerpt": "Neural Network-Long",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01375",
    "evidence_level": "A",
    "excerpt": "Neural Network-Long Short-Term",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01376",
    "evidence_level": "A",
    "excerpt": "Neural Networks",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01434",
    "evidence_level": "A",
    "excerpt": "often",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01437",
    "evidence_level": "A",
    "excerpt": "often struggle",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01441",
    "evidence_level": "A",
    "excerpt": "outperforms",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01442",
    "evidence_level": "A",
    "excerpt": "outperforms its",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01443",
    "evidence_level": "A",
    "excerpt": "outperforms its counterparts",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01461",
    "evidence_level": "A",
    "excerpt": "participant",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01464",
    "evidence_level": "A",
    "excerpt": "participation",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01468",
    "evidence_level": "A",
    "excerpt": "patient",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01469",
    "evidence_level": "A",
    "excerpt": "patient participation",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01470",
    "evidence_level": "A",
    "excerpt": "patient's",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01471",
    "evidence_level": "A",
    "excerpt": "patient's movement",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01472",
    "evidence_level": "A",
    "excerpt": "patient's movement intentions",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01489",
    "evidence_level": "A",
    "excerpt": "performance",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01497",
    "evidence_level": "A",
    "excerpt": "personalized",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01498",
    "evidence_level": "A",
    "excerpt": "personalized rehabilitation",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01499",
    "evidence_level": "A",
    "excerpt": "personalized rehabilitation exercises",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01521",
    "evidence_level": "A",
    "excerpt": "potential",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01522",
    "evidence_level": "A",
    "excerpt": "potential for future",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01551",
    "evidence_level": "A",
    "excerpt": "prediction",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01552",
    "evidence_level": "A",
    "excerpt": "Prediction",
    "locator": "title",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01561",
    "evidence_level": "A",
    "excerpt": "prediction model",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01563",
    "evidence_level": "A",
    "excerpt": "prediction model outperforms",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01566",
    "evidence_level": "A",
    "excerpt": "Prediction of Joint",
    "locator": "title",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01570",
    "evidence_level": "A",
    "excerpt": "preprocessed",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01571",
    "evidence_level": "A",
    "excerpt": "preprocessed data",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01575",
    "evidence_level": "A",
    "excerpt": "primary",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01576",
    "evidence_level": "A",
    "excerpt": "primary reliance",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01602",
    "evidence_level": "A",
    "excerpt": "provide",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01603",
    "evidence_level": "A",
    "excerpt": "provide personalized",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01604",
    "evidence_level": "A",
    "excerpt": "provide personalized rehabilitation",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01636",
    "evidence_level": "A",
    "excerpt": "real-time",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01663",
    "evidence_level": "A",
    "excerpt": "Recurrent",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01664",
    "evidence_level": "A",
    "excerpt": "Recurrent Neural",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01665",
    "evidence_level": "A",
    "excerpt": "recurrent neural networks",
    "locator": "database_keywords",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01666",
    "evidence_level": "A",
    "excerpt": "Recurrent Neural Networks",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01684",
    "evidence_level": "A",
    "excerpt": "rehabilitation",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01685",
    "evidence_level": "A",
    "excerpt": "rehabilitation exercises",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01689",
    "evidence_level": "A",
    "excerpt": "rehabilitation robots",
    "locator": "database_keywords",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01690",
    "evidence_level": "A",
    "excerpt": "rehabilitation robots",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01703",
    "evidence_level": "A",
    "excerpt": "reliance",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01712",
    "evidence_level": "A",
    "excerpt": "respond",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01723",
    "evidence_level": "A",
    "excerpt": "results",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01726",
    "evidence_level": "A",
    "excerpt": "results indicate",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01736",
    "evidence_level": "A",
    "excerpt": "RNN",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01738",
    "evidence_level": "A",
    "excerpt": "robots",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01760",
    "evidence_level": "A",
    "excerpt": "selected",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01771",
    "evidence_level": "A",
    "excerpt": "sEMG",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01772",
    "evidence_level": "A",
    "excerpt": "sEMG",
    "locator": "title",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01779",
    "evidence_level": "A",
    "excerpt": "sEMG and angle",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01780",
    "evidence_level": "A",
    "excerpt": "sEMG and elbow",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01817",
    "evidence_level": "A",
    "excerpt": "Short-Term",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01821",
    "evidence_level": "A",
    "excerpt": "Short-Term Memory",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01874",
    "evidence_level": "A",
    "excerpt": "six",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01876",
    "evidence_level": "A",
    "excerpt": "six healthy",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01878",
    "evidence_level": "A",
    "excerpt": "six healthy subjects",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01925",
    "evidence_level": "A",
    "excerpt": "struggle",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01926",
    "evidence_level": "A",
    "excerpt": "struggle to continuously",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01931",
    "evidence_level": "A",
    "excerpt": "subjects",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01936",
    "evidence_level": "A",
    "excerpt": "subjects were selected",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01937",
    "evidence_level": "A",
    "excerpt": "Subsequently",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01941",
    "evidence_level": "A",
    "excerpt": "suggesting",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01942",
    "evidence_level": "A",
    "excerpt": "suggesting its",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01943",
    "evidence_level": "A",
    "excerpt": "suggesting its potential",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01959",
    "evidence_level": "A",
    "excerpt": "surface",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01975",
    "evidence_level": "A",
    "excerpt": "surface electromyography",
    "locator": "database_keywords",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01989",
    "evidence_level": "A",
    "excerpt": "surface electromyography",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01997",
    "evidence_level": "A",
    "excerpt": "synchronize",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-01998",
    "evidence_level": "A",
    "excerpt": "synchronize the collection",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02033",
    "evidence_level": "A",
    "excerpt": "than",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02034",
    "evidence_level": "A",
    "excerpt": "than 0",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02040",
    "evidence_level": "A",
    "excerpt": "thereby",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02041",
    "evidence_level": "A",
    "excerpt": "thereby suggesting",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02042",
    "evidence_level": "A",
    "excerpt": "thereby suggesting its",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02108",
    "evidence_level": "A",
    "excerpt": "transformer models",
    "locator": "database_keywords",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "openalex_keyword",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02110",
    "evidence_level": "A",
    "excerpt": "Transformer-based",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02111",
    "evidence_level": "A",
    "excerpt": "Transformer-based joint",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02112",
    "evidence_level": "A",
    "excerpt": "Transformer-based joint angle",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02113",
    "evidence_level": "A",
    "excerpt": "Transformer-based model",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02207",
    "evidence_level": "A",
    "excerpt": "which",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02211",
    "evidence_level": "A",
    "excerpt": "which often",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  },
  {
    "evidence_id": "evidence-02212",
    "evidence_level": "A",
    "excerpt": "which often struggle",
    "locator": "abstract",
    "paper_id": "https://openalex.org/W4407450426",
    "retrieved_at": "2026-10-18T03:22:39.241825+00:00",
    "run_ids": [
      "run-plan-e7a1ff1c355c"
    ],
    "schema_version": "0.1",
    "source_type": "paper_metadata",
    "source_url": "https://openalex.org/W4407450426",
    "supports": "Field observation only; not semantic equivalence or relevance."
  }
]
```

## 译文
未分析，留空供人工填写。

## 创新点
未分析，留空供人工填写。

## 用户笔记
