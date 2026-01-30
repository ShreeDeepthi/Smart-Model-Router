import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Load data
data = pd.read_csv("data/training.csv")

X = data["text"]
y = data["label"]

# ML Pipeline
model = Pipeline([
    ("vectorizer", TfidfVectorizer()),
    ("clf", LogisticRegression())
])

# Train
model.fit(X, y)

# Save model
joblib.dump(model, "models/classifier.pkl")

print("Classifier trained and saved!")
