# E-Commerce Customer Lifetime Value Prediction

## Project Overview

This project predicts the future Customer Lifetime Value (LTV) of e-commerce customers using their historical purchasing behavior.

The project uses the UCI Online Retail dataset and applies customer-level feature engineering and machine learning to estimate the amount a customer is expected to spend in the future.

## Objectives

- Analyze e-commerce customer purchasing behavior.
- Perform data cleaning and exploratory data analysis.
- Create customer-level behavioral features.
- Predict future customer lifetime value.
- Evaluate the regression model using standard metrics.
- Provide a simple Streamlit web application for predictions.

## Dataset

The project uses the Online Retail dataset containing transaction records from an e-commerce store.

The dataset includes information such as:

- Invoice Number
- Product Description
- Quantity
- Invoice Date
- Unit Price
- Customer ID
- Country

## Methodology

### 1. Data Preprocessing

- Removed duplicate records.
- Removed transactions with negative or zero quantities.
- Removed transactions with zero or negative prices.
- Removed records with missing Customer IDs.
- Converted InvoiceDate to datetime format.
- Created a TotalAmount feature.

### 2. Feature Engineering

Historical customer-level features were created:

- Recency
- Frequency
- Historical Monetary Value
- Average Order Value
- Total Items Purchased
- Customer Tenure

### 3. Target Variable

A temporal approach was used to predict future customer value.

Historical transactions before September 1, 2011 were used to create customer features.

The total amount spent by each customer during the future period was used as the Future LTV target.

Customers with no future purchases were assigned a Future LTV of zero.

### 4. Machine Learning Model

A Random Forest Regressor was used to predict Future Customer Lifetime Value.

## Model Performance

The model achieved the following results:

| Metric | Score |
|---|---:|
| MAE | 991.49 |
| RMSE | 5101.22 |
| R² Score | 0.4338 |

## Streamlit Application

A Streamlit-based web application is included in this project.

The application allows users to enter customer information such as:

- Recency
- Purchase Frequency
- Historical Spending
- Average Order Value
- Total Items Purchased
- Customer Tenure

The application then predicts the customer's future Lifetime Value.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook

## Project Structure

```text
ecommerce-customer-ltv/
│
├── app.py
├── ltv_model.pkl
├── ltv_prediction.ipynb
├── Online Retail.xlsx
├── requirements.txt
└── README.md