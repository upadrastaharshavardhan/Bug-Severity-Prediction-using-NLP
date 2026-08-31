# Research Package - Project 8
## Bug Severity Prediction using NLP

Complete research paper, documentation, metrics, and full codebase.

**Key metrics:** Accuracy 95.60% | Macro F1 0.955 | Critical F1 0.968

## Contents
- paper/ (PDF + MD)
- docs/
- results/
- codebase/ (full Project 8 source)

## Reproduce
```bash
cd codebase
pip install -r requirements.txt
python scripts/generate_data.py --n-samples 4000 --seed 42
python scripts/train.py
```
