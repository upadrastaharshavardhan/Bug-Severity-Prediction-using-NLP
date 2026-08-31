from __future__ import annotations
from pathlib import Path
from typing import Any, Dict, List, Optional, Union
import yaml
from src.data.preprocessing import BugPreprocessor
from src.models.embeddings import EmbeddingModel
from src.models.classifier import SeverityClassifier

class SeverityPredictor:
    def __init__(self, embedder, classifier, preprocessor):
        self.embedder = embedder
        self.classifier = classifier
        self.preprocessor = preprocessor

    def predict(self, title: str = "", description: str = "",
                full_text: Optional[str] = None) -> Dict[str, Any]:
        if full_text is None:
            full_text = f"Title: {title}\nDescription: {description}"
        cleaned = self.preprocessor.clean(full_text)
        emb = self.embedder.encode([cleaned], show_progress=False)
        pred = self.classifier.predict_with_confidence(emb)[0]
        return {
            "severity": pred["severity"],
            "confidence": pred["confidence"],
            "cleaned_input": cleaned[:300],
        }

    def predict_batch(self, texts: List[str]) -> List[Dict]:
        cleaned = self.preprocessor.transform(texts)
        embs = self.embedder.encode(cleaned, show_progress=True)
        return self.classifier.predict_with_confidence(embs)

    @classmethod
    def load(cls, artifacts_dir: Union[str, Path], config_path: Optional[Union[str, Path]] = None):
        artifacts_dir = Path(artifacts_dir)
        if config_path is None:
            config_path = Path("config/config.yaml")
        with open(config_path) as f:
            cfg = yaml.safe_load(f)
        emb_cfg = cfg.get("embedding", {})
        embedder = EmbeddingModel(
            model_name=emb_cfg.get("model_name", "sentence-transformers/all-MiniLM-L6-v2"),
            device=emb_cfg.get("device"), normalize=emb_cfg.get("normalize", True),
        )
        classifier = SeverityClassifier.load(artifacts_dir / "classifier.joblib")
        preprocessor = BugPreprocessor(max_text_length=cfg.get("preprocessing", {}).get("max_text_length", 1000))
        return cls(embedder, classifier, preprocessor)
