from src.model import predict_risk
from src.risk import risk_level

def health_analysis(steps, sleep, heart_rate):
    
    risk_score = predict_risk(steps, sleep, heart_rate)
    level = risk_level(risk_score)
    
    if level == "Low Risk":
        advice = "Maintain your healthy lifestyle."
    elif level == "Medium Risk":
        advice = "Increase activity and improve sleep."
    else:
        advice = "Consult a doctor and improve habits."
    
    return risk_score, level, advice