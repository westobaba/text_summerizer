import logging
from transformers import pipeline
from src.model import load_model

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def predict(text: str):
    model, tokenizer = load_model("./models/summarizer_model")
    summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)
    summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
    return summary[0]["summary_text"]

if __name__ == "__main__":
    sample = """Your long input text here..."""
    logger.info("🔮 Running prediction on sample text")
    print(predict(sample))
