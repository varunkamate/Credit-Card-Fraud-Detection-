import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained Random Forest model
with open("Random_Forest_best_model.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(page_title="Credit Card Fraud Detection", layout="wide")

# Title and description
st.title("💳 Credit Card Fraud Detection App")
st.write("""
This app predicts whether a given transaction is **fraudulent or legitimate** 
based on the model trained on the Credit Card dataset.
""")

# Define feature names
features = [
    'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11',
    'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20', 'V21',
    'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount'
]

st.subheader("Enter Feature Values")

# Create input fields for all features
input_data = {}
num_cols = 3
cols = st.columns(num_cols)

for i, feature in enumerate(features):
    with cols[i % num_cols]:
        input_data[feature] = st.number_input(
            f"{feature}", value=0.0, format="%.4f"
        )

# Convert to DataFrame
input_df = pd.DataFrame([input_data])

# Show input data
st.write("### Input Data Preview")
st.dataframe(input_df)

# Predict button
if st.button("Predict Transaction Type"):
    prediction = model.predict(input_df)
    result = "Fraudulent Transaction ❌" if prediction[0] == 1 else "Legitimate Transaction ✅"

    st.subheader("Prediction Result")
    st.success(result)

# Sidebar info
st.sidebar.header("About")
st.sidebar.info("""
This app uses a **Random Forest Classifier** trained on the 
Kaggle Credit Card Fraud Detection dataset.
""")
st.sidebar.write("Model File: `Random_Forest_best_model.pkl`")
