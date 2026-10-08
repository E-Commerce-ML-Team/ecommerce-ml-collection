# E-Commerce Repeat Purchase Prediction

## Project Overview

This project predicts whether an e-commerce customer is likely to make a repeat purchase based on their historical purchasing behavior.

The project uses the UCI Online Retail dataset and applies customer-level feature engineering and machine learning to predict future purchasing activity.

## Objectives

- Analyze e-commerce customer purchasing behavior.
- Perform data cleaning and exploratory data analysis.
- Create customer-level behavioral features.
- Predict whether a customer will make a repeat purchase.
- Evaluate the classification model using standard metrics.
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
- Monetary Value
- Average Order Value
- Total Items Purchased
- Customer Tenure

### 3. Target Variable

A temporal approach was used to define repeat purchase behavior.

Historical transactions before September 1, 2011 were used to create customer features.

Customers who made at least one purchase during the future period were classified as repeat purchasers.

### 4. Machine Learning Model

A Random Forest Classifier was used to predict repeat purchase behavior.

## Model Performance

| Metric | Score |
|---|---:|
| Accuracy | 63.40% |
| Precision | 68.69% |
| Recall | 69.57% |
| F1 Score | 69.12% |
| ROC-AUC | 69.56% |

## Streamlit Application

A Streamlit-based web application is included in this project.

The application allows users to enter customer information such as:

- Recency
- Purchase Frequency
- Total Historical Spending
- Average Order Value
- Total Items Purchased
- Customer Tenure

The application then predicts the probability of a repeat purchase.

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
ecommerce-repeat-purchase/
│
├── app.py
├── repeat_purchase_model.pkl
├── repeat_purchase.ipynb
├── Online Retail.xlsx
├── requirements.txt
└── README.md