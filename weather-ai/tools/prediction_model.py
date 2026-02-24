import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))

def predict_temp(user_message, memory):

    weather = memory.get("weather")
    if not weather:
        return None

    features = np.array([[
        weather["temp"],
        weather["humidity"],
        weather["wind"],
        weather["pressure"]
    ]])

    pred = model.predict(features)[0]
    return round(pred, 2)
