import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
import os

print("Loading dataset...")

# get folder where train.py exists
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

csv_path = os.path.join(BASE_DIR, "weather.csv")

df = pd.read_csv(csv_path)

print(df.head())

X = df[["temp", "humidity", "wind", "pressure"]]
y = df["next_temp"]

model = LinearRegression()
model.fit(X, y)

model_path = os.path.join(BASE_DIR, "model.pkl")

with open(model_path, "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved successfully")
