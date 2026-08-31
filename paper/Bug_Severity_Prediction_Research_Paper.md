---
title: "Bug Severity Prediction using Natural Language Processing"
author: "Research Documentation - Project 8"
date: "August 2026"
geometry: margin=1in
fontsize: 11pt
---

\newpage

# Bug Severity Prediction using Natural Language Processing

**Automatic Classification of Defect Severity from Bug Report Text**

---

**Abstract**

Assigning severity to bug reports is critical for prioritization but often inconsistent when done manually. This paper presents an NLP system that predicts severity (Critical, High, Medium, Low) from bug title and description using sentence embeddings and a multi-class classifier.

On a synthetic benchmark of 4,000 labeled bug reports, the model achieves **accuracy 95.6%**, **macro F1 0.955**, and strong per-class F1 scores (Critical 0.968, High 0.951, Medium 0.948, Low 0.953). The system supports automated triage assistance at bug intake.

**Keywords:** Bug Severity, Defect Triage, NLP, Sentence Embeddings, Software Maintenance

---

## 1. Introduction

Severity reflects business and technical impact. Automatic prediction reduces triage time and improves consistency. We frame severity assignment as multi-class text classification over title + description.

## 2. Related Work

Prior work uses keyword rules, topic models, and BERT-style classifiers. Sentence embeddings provide a strong, efficient baseline that generalizes across paraphrased impact language.

## 3. Methodology

**Input:** `Title: ... Description: ...`  
**Pipeline:** Preprocess -> MiniLM embedding -> Logistic Regression (balanced) / Random Forest -> severity label + confidence.

Severity language correlates with impact terms (outage, data breach, revenue vs cosmetic, typo, warning).

## 4. Experimental Setup

- 4,000 synthetic bugs across 4 severity classes (near-uniform)
- 80/20 stratified split
- Metrics: Accuracy, macro F1, per-class Precision/Recall/F1

## 5. Results

| Metric            | Value    |
|-------------------|----------|
| Accuracy          | **95.60%** |
| Macro F1          | **0.955** |
| Critical F1       | 0.968    |
| High F1           | 0.951    |
| Medium F1         | 0.948    |
| Low F1            | 0.953    |

Adjacent-class confusion (High/Medium) is the main residual error, which is operationally less costly than Critical/Low swaps.

## 6. Discussion

Impact-oriented vocabulary is well captured by dense embeddings. Production use should allow human override and continuous learning from triage corrections. Limitations: synthetic labels; real severity can be organization-specific.

## 7. Conclusion

NLP-based severity prediction achieves 95.6% accuracy and is practical for triage automation.

**Reproduce:**
```bash
python scripts/generate_data.py --n-samples 4000 --seed 42
python scripts/train.py
python scripts/evaluate.py
```

---

*End of Research Paper*
