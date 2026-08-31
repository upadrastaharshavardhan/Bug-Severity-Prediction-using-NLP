# Bug Severity Prediction using NLP

**Project 8** – Predict bug severity (Critical / High / Medium / Low) from title and description using NLP.

## What it does

Given a bug report (title + description), the system predicts:

1. **Severity level**: Critical, High, Medium, or Low
2. **Confidence** score
3. Optional similar historical bugs of the same severity

## Key Features

- Synthetic bug generator with severity-correlated language
- Sentence-transformer embeddings + multi-class classifier
- Metrics: Accuracy, macro F1, per-class Precision/Recall/F1
- Gradio demo
- Colab-ready modular structure

## Quick Start

```bash
!pip install -r requirements.txt
!python scripts/generate_data.py --n-samples 4000
!python scripts/train.py
!python -m src.api.gradio_app
```

## Example

```python
from src.pipeline.predictor import SeverityPredictor
predictor = SeverityPredictor.load("artifacts")
result = predictor.predict(
    title="Production database down - all writes failing",
    description="Primary DB node unreachable. Customer transactions failing. Revenue impact."
)
print(result)  # {"severity": "Critical", "confidence": 0.94, ...}
```

## License

MIT
