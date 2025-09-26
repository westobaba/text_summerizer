from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from app.model import summarize_text

def run_summary_pipeline():
    sample_text = "Your input text here"
    summary = summarize_text(sample_text)
    print(summary)

with DAG(
    'summarization_pipeline',
    start_date=datetime(2025, 1, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:
    task = PythonOperator(
        task_id='summarize_text_task',
        python_callable=run_summary_pipeline
    )
