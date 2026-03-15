# 🎯 Customer Churn Prediction & Revenue Forecasting System

The primary objective of this project is to analyze telecom customer data to predict which customers are likely to churn (leave the service) and to forecast future revenue.

## 🚀 Project Overview
Businesses can use this system to:
* Reduce customer loss.
* Improve retention strategies.
* Estimate future revenue.

---

## 🛠️ Technology Stack
This project utilizes the following technologies:

* *Programming:* Python
* *Data Analysis:* Pandas, NumPy
* *Visualization:* Matplotlib, Seaborn
* *Machine Learning:* Scikit-learn (Logistic Regression, Random Forest)
* *Dashboard:* Streamlit

---

## 📊 Dataset Description
The project uses the customer_churn.csv dataset, which contains the following customer details:
* *CustomerID:* Unique identifier for each customer.
* *Tenure:* Number of months the customer has stayed with the company.
* *MonthlyCharges:* The amount charged to the customer monthly.
* *TotalCharges:* The total amount charged to the customer.
* *Contract:* The contract term of the customer (Month-to-month, One year, Two year).
* *InternetService:* Customer’s internet service provider (DSL, Fiber optic, No).

---

## 🔗 Project Features
* *Data Cleaning and Preprocessing:* Handling missing values and categorical encoding.
* *Exploratory Data Analysis:* Visualizing churn patterns and demographics.
* *Churn Prediction:* Classification model to identify at-risk customers.
* *Revenue Forecasting:* Linear Regression to predict future revenue.
* *Interactive Dashboard:* Built with Streamlit for real-time analysis.

---

## 🔗 Project Structure

```text
customer_churn_project |── data |
customer_data.csv      |── notebooks |
analysis.ipynb         |── src | data_preprocessing.py |
churn_model.py         |── dashboard |
app.py                 |── requirements.txt

## How to Run the Project
### Install Dependencies
pip install -r requirements.txt
### Run Streamlit Dashboard
streamlit run dashboard/app.py

## Output
### 1. Interactive Dashboard
* *Real-time Prediction:* Users can input customer attributes (Tenure, Charges, Contract) to get instant churn risk and revenue forecasts.
* *Data Exploration:* A dynamic table view to inspect the sample dataset directly from the dashboard.

### 2. Model Performance
After training and evaluating the models, the following results were achieved:
* *Churn Prediction (Classification):* High accuracy in identifying customers at risk of leaving.
* *Revenue Forecasting (Regression):* Predicted TotalCharges with minimal error, helping in financial planning.

### 3. Customer Risk Segmentation
The dashboard classifies customers into three risk categories based on probability:
* *Low Risk:* Customers with a high probability of staying.
* *Medium Risk:* Customers who might need engagement or discounts.
* *High Risk:* Customers likely to churn soon, requiring immediate attention.

### 4. Visual Analysis
The project includes several visualizations (in the Jupyter Notebook and Dashboard):
* *Churn vs. Tenure:* Shows how loyalty increases over time.
* *Revenue Trends:* Visual representation of expected vs. actual revenue.

## Dashboard Preview
Screenshot 2026-03-15 210501

## Author
### Palak Rathore
