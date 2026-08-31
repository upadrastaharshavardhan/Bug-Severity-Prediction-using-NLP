from __future__ import annotations
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
import gradio as gr
from src.pipeline.predictor import SeverityPredictor
from src.utils.helpers import load_config

def build_demo(artifacts_dir="artifacts", config_path="config/config.yaml"):
    cfg = load_config(config_path)
    predictor = SeverityPredictor.load(artifacts_dir, config_path)

    def predict_fn(title, description):
        r = predictor.predict(title=title, description=description)
        return (f"### Severity: **{r['severity']}**\n\n"
                f"**Confidence:** {r['confidence']:.1%}\n\n"
                f"**Cleaned input:** `{r['cleaned_input']}`")

    demo = gr.Interface(
        fn=predict_fn,
        inputs=[
            gr.Textbox(label="Bug title", value="Production database completely down"),
            gr.Textbox(lines=4, label="Description",
                       value="Primary DB unreachable. All customer transactions failing. Immediate revenue impact."),
        ],
        outputs=gr.Markdown(),
        title=cfg.get("gradio", {}).get("title", "Bug Severity Predictor"),
        description=cfg.get("gradio", {}).get("description", ""),
        examples=[
            ["Production database completely down", "Primary DB unreachable. All transactions failing."],
            ["Footer copyright year outdated", "Footer still shows previous year. Purely cosmetic."],
            ["Checkout fails for 30% of users", "Intermittent payment errors. Significant conversion drop."],
            ["Typo in error message on form validation", "Misspelled word in validation toast. Low impact."],
        ],
        allow_flagging="never",
    )
    return demo

if __name__ == "__main__":
    build_demo().launch(share=False, server_name="0.0.0.0")
