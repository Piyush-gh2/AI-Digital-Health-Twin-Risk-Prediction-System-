import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

def train_model():
    data = pd.read_csv("health_data.csv")
    
    X = data[["steps", "sleep_hours", "heart_rate"]]
    y = data["risk_score"]
    
    model = LinearRegression()
    model.fit(X, y)
    
    with open("health_model.pkl", "wb") as f:
        pickle.dump(model, f)

def predict_risk(steps, sleep, heart_rate):
    with open("health_model.pkl", "rb") as f:
        model = pickle.load(f)
    
    prediction = model.predict([[steps, sleep, heart_rate]])
    return prediction[0]