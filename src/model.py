import logging
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import torch
import yaml

# Setup logging
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# Load config
with open("config.yaml") as f:
    config = yaml.safe_load(f)

model_name = config["huggingface_model"]
gen_config = config["summarization"]

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Create pipeline
summarizer = pipeline(
    "summarization",
    model=model,
    tokenizer=tokenizer,
    device=0 if torch.cuda.is_available() else -1
)

def summarize_text(text: str) -> str:
    try:
        result = summarizer(text, **gen_config)
        return result[0]["summary_text"]
    except Exception as e:
        logging.error(f"Error in summarization: {e}")
        return ""
