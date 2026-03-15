import pandas as pd

def load_and_clean_data(filepath):
    # Task 1: Load Data
    df = pd.read_csv(filepath)
    
    # Task 2: Data Cleaning
    df = df.dropna() # Missing values hatana
    
    # Categorical variables handle karna (Image Task 2)
    df_encoded = pd.get_dummies(df, columns=['Contract', 'InternetService'], drop_first=True)
    
    # Churn ko numeric banana
    if 'Churn' in df_encoded.columns:
        df_encoded['Churn'] = df_encoded['Churn'].map({'Yes': 1, 'No': 0})
        
    return df_encoded

if __name__ == "_main_":
    data = load_and_clean_data('data/customer_churn.csv')
    print("Data Preprocessing Done!")
    print(data.head())