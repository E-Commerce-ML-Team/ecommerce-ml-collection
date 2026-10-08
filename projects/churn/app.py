import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("churn_model.pkl")

# Page title
st.title("E-Commerce Customer Churn Prediction")

st.write(
    "Enter the customer's information below to predict "
    "whether the customer is at risk of churn."
)

# Input fields
recency = st.number_input(
    "Recency (days)",
    min_value=0,
    value=30
)

frequency = st.number_input(
    "Purchase Frequency",
    min_value=1,
    value=5
)

monetary = st.number_input(
    "Total Spending",
    min_value=0.0,
    value=1000.0
)

average_order = st.number_input(
    "Average Order Value",
    min_value=0.0,
    value=200.0
)

total_items = st.number_input(
    "Total Items Purchased",
    min_value=1,
    value=20
)

tenure = st.number_input(
    "Customer Tenure (days)",
    min_value=0,
    value=200
)

# Prediction button
if st.button("Predict Churn"):

    input_data = pd.DataFrame([[
        recency,
        frequency,
        monetary,
        average_order,
        total_items,
        tenure
    ]], columns=[
        "Recency",
        "Frequency",
        "Monetary",
        "AverageOrderValue",
        "TotalItems",
        "Tenure"
    ])

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]

    st.subheader("Prediction Result")

    st.write(
        "Churn Probability:",
        round(probability * 100, 2),
        "%"
    )

    if prediction == 1:
        st.error("⚠️ Customer is at HIGH RISK of Churn")
    else:
        st.success("✅ Customer is likely to remain ACTIVE")