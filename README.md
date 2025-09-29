📘 Text Summarizer

A machine learning project for text summarization using a trained deep learning model, wrapped in a FastAPI application and containerized with Docker.
This project is designed to be deployed on AWS using Elastic Container Registry (ECR) and EC2.

🚀 Features

Pre-trained text summarization model

REST API with FastAPI for serving summaries

Containerized using Docker

Deployable to AWS ECR and runnable on EC2 instances

Configurable via config.yaml

🏗️ Project Structure
text_summarizer/
│── .github/             # GitHub workflows and CI/CD configurations
│── app/                 # FastAPI application (API endpoints, serving logic)
│── logs/                # Logs generated during training/inference
│── src/                 # Source code for model training, preprocessing, utils
│
│── .gitignore           # Git ignore rules
│── config.yaml          # Configuration file (model, training, etc.)
│── data.json            # Example dataset / input data
│── Dockerfile           # Docker build instructions
│── LICENSE              # License file
│── README.md            # Project documentation
│── requirements.txt     # Python dependencies

⚙️ Installation (Local Development)

Clone the repository:

git clone https://github.com/westobaba/text_summarizer.git
cd text_summarizer


Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


Install dependencies:

pip install -r requirements.txt


Run the API locally:

uvicorn app.main:app --reload

🐳 Running with Docker

Build the Docker image:

docker build -t text_summarizer:latest .


Run the container:

docker run -d -p 8000:8000 text_summarizer:latest


API will be available at: http://localhost:8000

☁️ Deployment to AWS (ECR + EC2)

Authenticate Docker with ECR:

aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <account-id>.dkr.ecr.<region>.amazonaws.com


Tag and push your image to ECR:

docker tag text_summarizer:latest <account-id>.dkr.ecr.<region>.amazonaws.com/text_summarizer:latest
docker push <account-id>.dkr.ecr.<region>.amazonaws.com/text_summarizer:latest


Launch an EC2 instance, install Docker, and pull your image:

docker pull <account-id>.dkr.ecr.<region>.amazonaws.com/text_summarizer:latest
docker run -d -p 8000:8000 <account-id>.dkr.ecr.<region>.amazonaws.com/text_summarizer:latest

📩 API Example

POST /summarize

{
  "text": "Your long input text goes here..."
}


Response

{
  "summary": "Short summarized version."
}

📜 License

This project is licensed under the MIT License
.

Would you like me to also add a section on how to reduce your Docker image size (since it’s ~11GB), or keep the README focused just on usage/deployment?

You said:
make it a standard readme
ChatGPT said:

Got it 👍 — here’s a clean, standard-style README.md for your project:

Text Summarizer

This project implements a machine learning text summarization model served via a FastAPI REST API.
It is containerized with Docker and can be deployed to AWS using Elastic Container Registry (ECR) and EC2.

Features

Text summarization with a pre-trained model

REST API built with FastAPI

Dockerized for portability

Deployable to AWS (ECR + EC2)

Configurable with config.yaml

Project Structure
text_summarizer/
│── .github/             # GitHub workflows and automation
│── app/                 # FastAPI application (API endpoints)
│── logs/                # Application and training logs
│── src/                 # Model training, preprocessing, utilities
│
│── .gitignore           # Git ignore rules
│── config.yaml          # Project configuration
│── data.json            # Example dataset
│── Dockerfile           # Docker build instructions
│── LICENSE              # License file
│── README.md            # Project documentation
│── requirements.txt     # Python dependencies

Getting Started
Prerequisites

Python 3.11+

Docker

AWS CLI (for deployment)

Local Setup
git clone https://github.com/westobaba/text_summarizer.git
cd text_summarizer

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

pip install -r requirements.txt


Run locally:

uvicorn app.main:app --reload


API will be available at: http://localhost:8000

Docker Usage

Build the image:

docker build -t text_summarizer:latest .


Run the container:

docker run -d -p 8000:8000 text_summarizer:latest

Deployment to AWS

Authenticate Docker with ECR:

aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <account-id>.dkr.ecr.<region>.amazonaws.com


Tag and push your image:

docker tag text_summarizer:latest <account-id>.dkr.ecr.<region>.amazonaws.com/text_summarizer:latest
docker push <account-id>.dkr.ecr.<region>.amazonaws.com/text_summarizer:latest


On your EC2 instance, pull and run the container:

docker pull <account-id>.dkr.ecr.<region>.amazonaws.com/text_summarizer:latest
docker run -d -p 8000:8000 <account-id>.dkr.ecr.<region>.amazonaws.com/text_summarizer:latest

API Example

POST /summarize
Request:

{
  "text": "Your input text goes here..."
}


Response:

{
  "summary": "Short summarized version."
}

License

This project is licensed under the MIT License
.
