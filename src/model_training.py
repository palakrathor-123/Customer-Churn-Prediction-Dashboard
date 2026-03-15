import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
import joblib
import os

def train_and_save_models():
    # 1. Data load karna
    path = 'data/customer_churn.csv'
    if not os.path.exists(path):
        print("Error: data/customer_churn.csv file nahi mili!")
        return

    df = pd.read_csv(path)
    
    # Preprocessing (Yes/No to 1/0)
    df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})
    
    # 2. Churn Model (Task 4)
    # Hum features vahi le rahe hain jo image mein hain
    X_churn = df[['Tenure', 'MonthlyCharges']] 
    y_churn = df['Churn']
    
    clf = RandomForestClassifier()
    clf.fit(X_churn, y_churn)
    joblib.dump(clf, 'churn_model.pkl')
    print("✓ churn_model.pkl save ho gayi!")

    # 3. Revenue Model (Task 6)
    X_rev = df[['Tenure', 'MonthlyCharges']]
    y_rev = df['TotalCharges']
    
    reg = LinearRegression()
    reg.fit(X_rev, y_rev)
    joblib.dump(reg, 'revenue_model.pkl')
    print("✓ revenue_model.pkl save ho gayi!")

# --- YEH LINE SABSE ZAROORI HAI ---
# Iske bina code kuch nahi karega
if __name__ == "__main__":
    train_and_save_models()