import joblib
import numpy as np

def predict_customer(data_input):
    # Models load karna
    churn_model = joblib.load('churn_model.pkl')
    rev_model = joblib.load('revenue_model.pkl')
    
    # Prediction
    churn_prob = churn_model.predict_proba(data_input)[0][1]
    predicted_revenue = rev_model.predict(data_input[['Tenure', 'MonthlyCharges']])[0]
    
    # Risk Level (Optional Task Image)
    risk = "Low"
    if churn_prob > 0.6: risk = "High"
    elif churn_prob > 0.3: risk = "Medium"
    
    return churn_prob, risk, predicted_revenue