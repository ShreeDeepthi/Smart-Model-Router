from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import joblib
import os
from router import route_prompt
from logger import log_request

app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load classifier
classifier = joblib.load("models/classifier.pkl")

@app.post("/predict")
def predict(prompt: str):
    difficulty = classifier.predict([prompt])[0]
    response = route_prompt(prompt, difficulty)
    log_request(prompt, difficulty)

    return {
        "prompt": prompt,
        "difficulty": difficulty,
        "response": response
    }

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    favicon_path = "static/favicon.ico"
    if os.path.exists(favicon_path):
        return FileResponse(favicon_path)
    return None

@app.get("/")
def read_root():
    return {"message": "Welcome to the classifier API!"}
