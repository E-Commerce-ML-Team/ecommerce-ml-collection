import streamlit as st
import pandas as pd
import joblib

model = joblib.load("repeat_purchase_model.pkl")

st.title("E-Commerce Repeat Purchase Prediction")

st.write(
    "Predict whether a customer is likely to make another purchase "
    "based on their previous purchasing behaviour."
)

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
    "Total Historical Spending",
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

if st.button("Predict Repeat Purchase"):

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
        "Repeat Purchase Probability:",
        round(probability * 100, 2),
        "%"
    )

    if prediction == 1:
        st.success("✅ Customer is likely to purchase again")
    else:
        st.warning("⚠️ Customer is unlikely to purchase again")