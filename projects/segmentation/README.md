# E-Commerce Customer Segmentation

## Project Overview

This project segments e-commerce customers into meaningful groups based on their purchasing behavior.

The project uses the UCI Online Retail dataset and applies RFM analysis and K-Means clustering to identify different customer segments.

## Objectives

- Analyze e-commerce customer purchasing behavior.
- Perform data cleaning and exploratory data analysis.
- Calculate customer RFM metrics.
- Apply K-Means clustering.
- Identify meaningful customer segments.
- Provide a simple Streamlit web application for customer segmentation.

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

### 2. RFM Analysis

Customer behavior was represented using three RFM metrics:

- Recency — number of days since the customer's most recent purchase.
- Frequency — number of unique purchases made by the customer.
- Monetary — total amount spent by the customer.

### 3. Feature Scaling

StandardScaler was used to standardize the RFM features before clustering.

### 4. Customer Segmentation

K-Means clustering was applied to divide customers into four segments.

The identified segments were:

- Regular / Low-Value
- At-Risk / Inactive
- VIP / Highly Loyal
- Loyal / High-Value

### 5. Model Evaluation

The clustering model achieved a Silhouette Score of approximately 0.6162.

## Cluster Summary

| Segment | Description |
|_________|_____________|
| Cluster 0 | Regular / Low-Value |
| Cluster 1 | At-Risk / Inactive |
| Cluster 2 | VIP / Highly Loyal |
| Cluster 3 | Loyal / High-Value |

## Streamlit Application

A Streamlit-based web application is included in this project.

The application allows users to enter:

- Recency
- Frequency
- Monetary Value

The application then predicts the customer's corresponding segment.

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
ecommerce-customer-segmentation/
│
├── app.py
├── segmentation_model.pkl
├── scaler.pkl
├── segmentation.ipynb
├── Online Retail.xlsx
├── requirements.txt
└── README.md