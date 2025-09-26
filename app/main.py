from fastapi import FastAPI
from pydantic import BaseModel
from src.model import summarize_text

app = FastAPI(title="Text Summarizer API")

class TextRequest(BaseModel):
    text: str

@app.post("/summarize/")
def summarize(request: TextRequest):
    summary = summarize_text(request.text)
    return {"summary": summary}
