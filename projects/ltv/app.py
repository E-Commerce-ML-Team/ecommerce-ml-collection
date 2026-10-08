import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("ltv_model.pkl")

# Page title
st.title("E-Commerce Customer Lifetime Value Prediction")

st.write(
    "Enter the customer's historical purchasing information "
    "to predict their future customer lifetime value."
)

# Inputs
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

historical_monetary = st.number_input(
    "Historical Spending",
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

# Prediction
if st.button("Predict Customer LTV"):

    input_data = pd.DataFrame([[
        recency,
        frequency,
        historical_monetary,
        average_order,
        total_items,
        tenure
    ]], columns=[
        "Recency",
        "Frequency",
        "HistoricalMonetary",
        "AverageOrderValue",
        "TotalItems",
        "Tenure"
    ])

    prediction = model.predict(input_data)[0]

    st.subheader("Prediction Result")

    st.success(
        f"Predicted Future Customer Lifetime Value: ₹{prediction:,.2f}"
    )