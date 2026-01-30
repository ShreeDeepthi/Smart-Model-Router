Cost-Control Smart Model Router
Overview

Cost-Control Smart Model Router is a backend system that intelligently routes user prompts to different models based on predicted difficulty.
It uses a lightweight text classification model to determine whether a request is simple, medium, or hard, and then forwards it to the appropriate model handler.
The goal is to reduce computation cost and improve efficiency by avoiding unnecessary use of expensive models.

Problem Statement

Using a single large model for all user prompts is inefficient and costly.
Simple tasks do not require powerful models, while complex tasks do.
This project solves that problem by introducing a smart routing layer.

Solution Approach

User sends a prompt to the API.

A trained text classifier predicts the difficulty level.

The router selects the appropriate model based on difficulty.

The request is logged for monitoring and analysis.

A response is returned to the user.

Technology Stack

Python

FastAPI (Backend API)

Uvicorn (ASGI Server)

scikit-learn (Machine Learning)

TF-IDF Vectorizer

Logistic Regression

Pandas

Joblib

Project Structure
smart-model-router/
│
├── app.py                # FastAPI application entry point
├── classifier.py         # Training script for difficulty classifier
├── router.py             # Model routing logic
├── logger.py             # Request logging utility
├── logs.txt              # Generated logs file
│
├── data/
│   └── training.csv      # Training dataset
│
├── models/
│   └── classifier.pkl    # Trained ML model
│
└── venv/                 # Virtual environment

File-by-File Explanation
app.py

Defines the FastAPI application and /predict endpoint.

Loads the trained classifier, predicts difficulty, routes the prompt, logs the request, and returns a JSON response.

classifier.py

Loads training data from training.csv.

Trains a TF-IDF + Logistic Regression model.

Saves the trained model as classifier.pkl.

router.py

Contains model handler functions for simple, medium, and hard requests.

Routes prompts to the correct handler based on predicted difficulty.

logger.py

Logs each request with timestamp, difficulty, and prompt.

Writes logs to logs.txt.

data/training.csv

Sample labeled dataset used to train the classifier.

Contains prompt text and corresponding difficulty labels.

models/classifier.pkl

Serialized trained machine learning model.

Loaded by the FastAPI backend during runtime.

logs.txt

Stores request history for debugging and monitoring.

Automatically created and updated during API calls.

Setup Instructions
Step 1: Create Virtual Environment
python -m venv venv


Activate the environment:

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate

Step 2: Install Dependencies
pip install fastapi uvicorn scikit-learn pandas joblib

Training the Classifier

Run the training script:

python classifier.py


Expected output:

Classifier trained and saved!


This creates:

models/classifier.pkl

Running the API Server
uvicorn app:app --reload


Server URL:

http://127.0.0.1:8000

Testing the API

Open the interactive API documentation:

http://127.0.0.1:8000/docs


Use the POST /predict endpoint.

Example input:

summarize this article


Example response:

{
  "prompt": "summarize this article",
  "difficulty": "simple",
  "response": "[SIMPLE MODEL] Processed: summarize this article"
}

Logging Format

Each request is logged in logs.txt as:

timestamp | difficulty | prompt


Example:

2026-01-29 15:23:30 | simple | summarize this article

Routing Logic
Difficulty	Routed Model
simple	Simple handler
medium	Medium handler
hard	Hard handler

(Current handlers are placeholders and can be replaced with real AI models.)

Use Cases

Cost-optimized AI systems

Multi-model orchestration

API gateways for LLMs

Intelligent backend routing layers

Future Enhancements

Integration with real LLM APIs (OpenAI, LLaMA, etc.)

Database-backed logging (PostgreSQL, SQLite)

Authentication and rate limiting

Prompt feedback and model retraining

Cost and latency tracking

Batch request handling

Project Status

Classifier implemented and tested

Routing logic functional

API tested via Swagger UI

Logging enabled

Ready for extension and production hardening
