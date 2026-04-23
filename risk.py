def risk_level(score):
    if score > 60:
        return "High Risk"
    elif score > 40:
        return "Medium Risk"
    else:
        return "Low Risk"