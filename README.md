# 🧠 Bug Severity Prediction using NLP

### Research Package — Project 8

> **Automatically predict software bug severity from natural-language bug reports using Natural Language Processing and Machine Learning.**

[![Project](https://img.shields.io/badge/Research-Project%208-6366f1?style=for-the-badge)](#)
[![NLP](https://img.shields.io/badge/NLP-Bug%20Classification-8b5cf6?style=for-the-badge)](#)
[![Accuracy](https://img.shields.io/badge/Accuracy-95.60%25-10b981?style=for-the-badge)](#-results)
[![Macro F1](https://img.shields.io/badge/Macro%20F1-0.955-06b6d4?style=for-the-badge)](#-results)
[![Critical F1](https://img.shields.io/badge/Critical%20F1-0.968-f59e0b?style=for-the-badge)](#-results)
[![License](https://img.shields.io/badge/License-MIT-111827?style=for-the-badge)](LICENSE)

---

## 🚀 Project Overview

Software teams receive thousands of bug reports containing descriptions such as:

* Application crashes
* Data corruption
* Authentication failures
* UI defects
* Performance degradation
* Feature malfunctions
* Configuration problems

Manually assigning severity to every report is time-consuming and can lead to inconsistent prioritization.

This project develops an **NLP-powered bug severity prediction system** that analyzes the textual content of a bug report and automatically predicts its severity category.

The goal is to transform unstructured bug reports into an actionable classification signal that can support:

* 🐞 Automated bug triage
* 🚨 Critical issue identification
* 🎯 Engineering prioritization
* 📊 Quality analytics
* ⚡ Faster incident response
* 🤖 AI-assisted software maintenance

---

# 🎯 Problem Statement

Bug severity determines how urgently an issue should be addressed.

However, traditional severity assignment often depends on:

* Manual triage
* Developer experience
* Domain knowledge
* Subjective interpretation
* Large volumes of incoming reports
* Inconsistent classification between teams

The core research question is:

> **Can Natural Language Processing automatically learn the linguistic patterns associated with bug severity and provide reliable severity predictions for new bug reports?**

This project investigates that question through an end-to-end machine-learning pipeline.

---

# 💡 Proposed Solution

The system follows a complete NLP classification workflow:

```text
                    ┌─────────────────────────┐
                    │      Bug Report         │
                    │                         │
                    │ Summary + Description   │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │    Text Preprocessing   │
                    │                         │
                    │ Cleaning / Normalizing  │
                    │ Tokenization            │
                    │ Noise Removal           │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │   NLP Representation    │
                    │                         │
                    │ Text → Numerical        │
                    │ Feature Representation │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │   ML Classification     │
                    │                         │
                    │ Severity Prediction     │
                    └────────────┬────────────┘
                                 │
                                 ▼
              ┌──────────────────────────────────────┐
              │          Predicted Severity          │
              │                                      │
              │  Critical / High / Medium / Low ... │
              └──────────────────────────────────────┘
```

---

# 📊 Key Results

| Metric                |     Result |
| --------------------- | ---------: |
| **Accuracy**          | **95.60%** |
| **Macro F1**          |  **0.955** |
| **Critical-Class F1** |  **0.968** |

### 🏆 Performance Snapshot

```text
Accuracy       ███████████████████░  95.60%

Macro F1       ███████████████████░  0.955

Critical F1    ████████████████████  0.968
```

The strong Critical-class F1 is particularly important because critical bugs are the issues most likely to require immediate engineering attention.

> **Note:** These reported values are the project-level experimental metrics provided with this research package. Always refer to the files in `results/` for the detailed experimental outputs.

---

# 🔬 Research Contributions

This project is designed as a reproducible research artifact rather than only a demonstration application.

### 1. NLP-Based Severity Classification

Uses textual information contained in bug reports to learn severity-related patterns.

### 2. End-to-End ML Pipeline

Provides a complete workflow from synthetic/sample data generation through model training.

### 3. Reproducible Experiments

Experiments can be regenerated using deterministic seeds.

### 4. Research Documentation

The repository contains the research paper, supporting documentation, results, and implementation.

### 5. Software Engineering Application

Connects NLP classification directly to an important software-quality problem: automated bug triage.

---

# 🧩 System Architecture

```text
┌────────────────────────────────────────────────────────────┐
│                    BUG REPORT INGESTION                     │
│                                                            │
│  Summary │ Description │ Error Message │ Context           │
└───────────────────────────┬────────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────────┐
│                     TEXT PROCESSING                         │
│                                                            │
│  Cleaning → Normalization → Tokenization → Feature Prep   │
└───────────────────────────┬────────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────────┐
│                   NLP FEATURE SPACE                         │
│                                                            │
│          Convert Natural Language → Numeric Features       │
└───────────────────────────┬────────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────────┐
│                  SUPERVISED CLASSIFIER                      │
│                                                            │
│                  Learn Severity Patterns                    │
└───────────────────────────┬────────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────────┐
│                     PREDICTION                             │
│                                                            │
│       Severity Class + Confidence / Classification        │
└───────────────────────────┬────────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────────┐
│                    QA / TRIAGE SYSTEM                       │
│                                                            │
│   Prioritization │ Routing │ Analytics │ Engineering       │
└────────────────────────────────────────────────────────────┘
```

---

# 🧪 Experimental Workflow

The project follows a structured machine-learning experimentation process.

### Step 1 — Data Generation

Generate the reproducible experimental dataset:

```bash
python scripts/generate_data.py --n-samples 4000 --seed 42
```

### Step 2 — Text Preparation

Bug-report text is prepared for downstream NLP processing.

Typical preparation stages include:

```text
Raw Bug Report
      ↓
Text Cleaning
      ↓
Normalization
      ↓
Tokenization
      ↓
Feature Extraction
```

### Step 3 — Model Training

Train the classification pipeline:

```bash
python scripts/train.py
```

### Step 4 — Evaluation

The trained model is evaluated using classification metrics including:

* Accuracy
* Macro F1
* Class-level F1
* Critical-class performance
* Confusion analysis
* Other experiment-specific metrics available under `results/`

---

# 🧠 Why Macro F1 Matters

Accuracy alone can hide weaknesses when classes are imbalanced.

For example:

```text
                  Accuracy
                     │
                     ▼
              ┌─────────────┐
              │ 95.60%      │
              └─────────────┘
                     │
                     ▼
            ┌─────────────────┐
            │ Macro F1 = .955 │
            └─────────────────┘
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
   Class Balance          Critical Bugs
                              │
                              ▼
                       F1 = 0.968
```

Macro F1 gives each class equal importance, making it a useful complementary metric when evaluating severity classification.

---

# ⚙️ Reproducibility

One of the main goals of this package is to make the experiment easy to reproduce.

## Requirements

* Python 3.x
* pip
* Virtual environment recommended

## Installation

Clone the repository:

```bash
git clone https://github.com/upadrastaharshavardhan/Bug-Severity-Prediction-using-NLP.git
```

Enter the repository:

```bash
cd Bug-Severity-Prediction-using-NLP
```

Move into the implementation:

```bash
cd codebase
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Generate the dataset:

```bash
python scripts/generate_data.py --n-samples 4000 --seed 42
```

Train the model:

```bash
python scripts/train.py
```

---

# 📁 Repository Structure

```text
Bug-Severity-Prediction-using-NLP/
│
├── 📄 README.md
├── 📄 LICENSE
│
├── 📁 paper/
│   ├── 📄 Research Paper.pdf
│   └── 📄 Research Paper.md
│
├── 📁 docs/
│   ├── methodology
│   ├── experiment documentation
│   └── supporting material
│
├── 📁 results/
│   ├── metrics
│   ├── evaluation outputs
│   ├── figures
│   └── experiment artifacts
│
└── 📁 codebase/
    ├── 📁 scripts/
    │   ├── generate_data.py
    │   └── train.py
    │
    ├── 📄 requirements.txt
    └── project implementation
```

---

# 🔍 What the Model Learns

A bug report can contain linguistic signals associated with different severity levels.

Examples of potentially informative language include:

| Signal      | Example                             |
| ----------- | ----------------------------------- |
| Crash       | `application crashes on startup`    |
| Data Loss   | `records are permanently deleted`   |
| Blocking    | `users cannot continue after login` |
| Performance | `request takes several minutes`     |
| UI          | `button is incorrectly positioned`  |
| Functional  | `export produces incorrect result`  |

The NLP pipeline learns statistical relationships between these textual patterns and historical severity labels.

This enables automated classification of previously unseen reports.

---

# 🏢 Real-World Applications

The model can become a component inside a larger software-quality platform.

### 🐞 Bug Tracking

Automatically suggest severity when a new issue is created.

### 🚨 Incident Management

Identify potentially critical issues earlier.

### 🎯 Engineering Prioritization

Help teams rank incoming bugs.

### 🔄 CI/CD

Integrate severity prediction into automated development workflows.

### 📊 Quality Analytics

Analyze severity trends across releases and projects.

### 🤖 AI QA Agents

Use severity predictions as one signal inside an autonomous QA or software-maintenance agent.

---

# 🔌 Integration Concept

A future deployment could expose the model through an API:

```text
Jira / GitHub / ServiceNow
           │
           ▼
     Bug Report Created
           │
           ▼
     NLP Prediction API
           │
           ▼
   ┌───────────────────┐
   │ Severity: CRITICAL│
   │ Confidence: 96%   │
   └─────────┬─────────┘
             │
             ▼
     Automated Routing
             │
       ┌─────┴─────┐
       ▼           ▼
    P0 Queue    Engineering
```

This architecture could be extended with:

* REST API
* FastAPI
* Docker
* Kubernetes
* GitHub Actions
* Jira integration
* ServiceNow integration
* Monitoring
* Model versioning

---

# 📈 Future Research Directions

The current project establishes a strong NLP classification foundation. Several extensions can make the system substantially more powerful.

### 🔹 Transformer Models

Explore:

* BERT
* RoBERTa
* DeBERTa
* DistilBERT

### 🔹 Semantic Embeddings

Replace traditional sparse representations with contextual embeddings.

### 🔹 Confidence-Aware Prediction

Route uncertain predictions to human reviewers:

```text
Prediction
    │
    ├── High Confidence ──► Automatic Severity
    │
    └── Low Confidence ───► Human Review
```

### 🔹 Explainable AI

Identify which words, phrases, or semantic signals influenced the prediction.

### 🔹 Active Learning

Use human corrections to continuously improve the model.

### 🔹 Cross-Project Generalization

Evaluate whether models trained on one software project transfer effectively to another.

### 🔹 LLM-Based Triage

Combine traditional NLP models with LLM reasoning for richer bug understanding.

---

# 🧪 Suggested Production Architecture

```text
                   ┌──────────────────┐
                   │  Issue Tracker   │
                   │ Jira / GitHub    │
                   └────────┬─────────┘
                            │
                            ▼
                  ┌──────────────────┐
                  │ Ingestion Layer  │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │ NLP Preprocessor │
                  └────────┬─────────┘
                           │
                           ▼
              ┌──────────────────────────┐
              │ Severity Prediction API  │
              └────────────┬─────────────┘
                           │
                           ▼
              ┌──────────────────────────┐
              │ Prediction + Confidence  │
              └────────────┬─────────────┘
                           │
               ┌───────────┴───────────┐
               ▼                       ▼
        High Confidence          Low Confidence
               │                       │
               ▼                       ▼
       Automated Routing          Human Review
               │                       │
               └───────────┬───────────┘
                           ▼
                  ┌──────────────────┐
                  │ Feedback / ML Ops│
                  └──────────────────┘
```

---

# 📚 Research Package

This repository is organized as a complete research package containing:

| Component   | Purpose                                  |
| ----------- | ---------------------------------------- |
| `paper/`    | Research publication and manuscript      |
| `docs/`     | Methodology and supporting documentation |
| `results/`  | Experimental results and artifacts       |
| `codebase/` | Reproducible implementation              |
| `README.md` | Project documentation                    |

---

# 📝 Research Positioning

This project sits at the intersection of:

```text
Natural Language Processing
            +
Machine Learning
            +
Software Engineering
            +
Defect Management
            +
Automated Bug Triage
```

The broader objective is to demonstrate how AI can reduce manual effort in software-quality workflows while preserving measurable and reproducible evaluation.

---

# ⚠️ Limitations

The reported performance should be interpreted within the experimental setup used by this research package.

Important considerations for production deployment include:

* Dataset distribution may differ from real organizations.
* Severity labels can vary between projects.
* New bug terminology can cause distribution shift.
* Highly ambiguous reports may require human review.
* Performance should be validated against project-specific historical data.
* Model confidence should be monitored after deployment.

A production system should therefore use **human-in-the-loop review for uncertain predictions**.

---

# 🔐 Responsible Use

Severity prediction should be treated as a decision-support mechanism rather than an unquestionable source of truth.

Recommended production behavior:

```text
AI Prediction
      │
      ▼
Confidence Check
      │
 ┌────┴────┐
 ▼         ▼
High       Low
 │          │
 ▼          ▼
Automate   Human Review
```

---

# 📖 Related Research Context

Bug severity prediction has been explored using NLP, classical machine learning, embeddings, deep learning, and transformer-based approaches. Existing research demonstrates the usefulness of textual bug information for automated severity classification and triage.

This project focuses on building a **reproducible, self-contained research artifact** around the problem.

---

# 📜 License

This project is released under the **MIT License**.

See [`LICENSE`](LICENSE) for details.

---

# 👨‍💻 Author

**Upadrasta Harsha Vardhan**

Research & Engineering Project — Project 8

---

# ⭐ If You Find This Useful

Consider:

* ⭐ Starring the repository
* 🍴 Forking the project
* 🐛 Opening an issue
* 💡 Suggesting improvements
* 🔬 Extending the research
* 🤝 Contributing experiments

---

## 🔗 Repository

**Bug Severity Prediction using NLP**

https://github.com/upadrastaharshavardhan/Bug-Severity-Prediction-using-NLP

---

### 🚀 From Bug Reports → NLP → Severity Intelligence

> **Turning unstructured software defects into actionable engineering intelligence.**
