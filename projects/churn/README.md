# E-Commerce Customer Churn Prediction

## Project Overview

This project predicts whether an e-commerce customer is likely to churn based on their historical purchasing behavior.

The project uses the UCI Online Retail dataset and applies customer-level feature engineering and machine learning to identify customers who are likely to stop purchasing.

## Objectives

- Analyze e-commerce customer purchasing behavior.
- Perform data cleaning and exploratory data analysis.
- Create customer-level behavioral features.
- Predict customer churn using machine learning.
- Evaluate the model using classification metrics.
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

Customer-level features were created using historical transaction data:

- Recency
- Frequency
- Monetary Value
- Average Order Value
- Total Items Purchased
- Customer Tenure

### 3. Churn Definition

A temporal approach was used to define churn.

Historical transactions before September 1, 2011 were used to create customer features.

Customers who did not make a purchase during the future period were classified as churned.

### 4. Machine Learning Model

Random Forest Classifier was used for customer churn prediction.

## Model Performance

The model achieved the following results:

| Metric | Score |
|---|---:|
| Accuracy | 64.46% |
| Precision | 57.03% |
| Recall | 54.95% |
| F1 Score | 55.97% |
| ROC-AUC | 70.21% |

## Streamlit Application

A Streamlit-based web application is included in this project.

The application allows users to enter customer information such as:

- Recency
- Purchase Frequency
- Total Spending
- Average Order Value
- Total Items Purchased
- Customer Tenure

The application then predicts the customer's probability of churn.

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
ecommerce-customer-churn/
│
├── app.py
├── churn_prediction.ipynb
├── churn_model.pkl
├── customer_features.csv
├── Online Retail.xlsx
├── requirements.txt
└── README.md