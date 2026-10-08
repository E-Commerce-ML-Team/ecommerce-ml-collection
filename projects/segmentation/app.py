import streamlit as st
import pandas as pd
import joblib

# Load model and scaler
model = joblib.load("segmentation_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("E-Commerce Customer Segmentation")

st.write(
    "Enter customer purchasing behaviour to identify "
    "the customer's segment."
)

# Customer inputs
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

if st.button("Find Customer Segment"):

    input_data = pd.DataFrame(
        [[recency, frequency, monetary]],
        columns=[
            "Recency",
            "Frequency",
            "Monetary"
        ]
    )

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Predict cluster
    cluster = model.predict(input_scaled)[0]

    # Segment names
    segment_names = {
        0: "Regular / Low-Value Customer",
        1: "At-Risk / Inactive Customer",
        2: "VIP / Highly Loyal Customer",
        3: "Loyal / High-Value Customer"
    }

    segment = segment_names[cluster]

    st.subheader("Customer Segment")

    st.success(
        f"Cluster {cluster}: {segment}"
    )