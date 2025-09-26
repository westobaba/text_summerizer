import logging
from transformers import Trainer, TrainingArguments, DataCollatorForSeq2Seq
from datasets import load_from_disk
from src.model import load_model

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def train(output_dir="./models/summarizer_model"):
    # Load model + tokenizer
    model, tokenizer = load_model(output_dir)

    # Load dataset (make sure you saved it locally or in Colab)
    dataset = load_from_disk("samsum_dataset")

    def preprocess(batch):
        inputs = tokenizer(batch["dialogue"], max_length=512, truncation=True)
        labels = tokenizer(batch["summary"], max_length=128, truncation=True)
        return {"input_ids": inputs["input_ids"], "labels": labels["input_ids"]}

    dataset = dataset.map(preprocess, batched=True)

    # Data collator
    data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)

    # Training args
    args = TrainingArguments(
        output_dir=output_dir,
        num_train_epochs=1,
        per_device_train_batch_size=2,
        per_device_eval_batch_size=2,
        logging_steps=50,
        save_strategy="epoch",
        eval_strategy="epoch"
    )

    # Trainer
    trainer = Trainer(
        model=model,
        args=args,
        tokenizer=tokenizer,
        data_collator=data_collator,
        train_dataset=dataset["train"],
        eval_dataset=dataset["validation"]
    )

    logger.info("🚀 Starting training...")
    trainer.train()
    trainer.save_model(output_dir)
    tokenizer.save_pretrained(output_dir)
    logger.info(f"✅ Training complete. Model saved to {output_dir}")

if __name__ == "__main__":
    train()
