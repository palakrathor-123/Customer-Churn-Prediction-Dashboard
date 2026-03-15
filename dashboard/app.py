import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Page configuration
st.set_page_config(page_title="Customer Churn Dashboard", layout="wide")

# Title
st.title("🎯 Customer Churn & Revenue Forecasting System")
st.markdown("Is system se aap customer ka churn risk aur expected revenue check kar sakte hain.")

# 1. Models Load karna (Make sure pkl files exist)
try:
    churn_model = joblib.load('churn_model.pkl')
    revenue_model = joblib.load('revenue_model.pkl')
except:
    st.error("Models nahi mile! Pehle 'model_training.py' run karke models save karein.")

# 2. Sidebar Inputs
st.sidebar.header("Customer Details")
tenure = st.sidebar.slider("Tenure (Months)", 1, 72, 12)
monthly_charges = st.sidebar.number_input("Monthly Charges ($)", min_value=10.0, max_value=200.0, value=50.0)
contract = st.sidebar.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
internet = st.sidebar.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

# 3. Main Dashboard Logic
if st.button("Predict Results"):
    # Input data ko model ke format mein convert karna
    # Note: encoded columns ka dhyan rakhna hoga jo training mein use huye the
    
    # Simple input for Revenue Model (Task 6)
    rev_input = np.array([[tenure, monthly_charges]])
    predicted_rev = revenue_model.predict(rev_input)[0]
    
    # Churn Prediction Logic
    # (Yahan aapko training features ke according dummy columns set karne honge)
    # Temporary example probability:
    churn_prob = np.random.random() # Replace with churn_model.predict_proba logic
    
    # Display Results
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Churn Risk Analysis")
        if churn_prob > 0.6:
            st.error(f"High Risk: {churn_prob:.2%}")
        elif churn_prob > 0.3:
            st.warning(f"Medium Risk: {churn_prob:.2%}")
        else:
            st.success(f"Low Risk: {churn_prob:.2%}")
            
    with col2:
        st.subheader("Revenue Forecast")
        st.metric(label="Predicted Total Charges", value=f"${predicted_rev:,.2f}")

# 4. Data Preview (Task 1 & 2)
if st.checkbox("Show Sample Dataset"):
    df = pd.read_csv("data/customer_churn.csv")
    st.write(df.head())