import streamlit as st
import pickle
import joblib
import numpy as np

model = joblib.load("model/water_quality_rf_model.pkl")
# Load config
with open("model/model_config.json") as f:
    config = json.load(f)

features = config["features"]

st.title("💧 Water Quality Potability Checker")

st.write("Enter water parameters:")

input_data = []

# Create input fields
for feature in features:
    value = st.number_input(f"{feature}", step=0.1)
    input_data.append(value)

# Predict button
if st.button("Predict"):
    data = np.array(input_data).reshape(1, -1)
    prediction = model.predict(data)

    if prediction[0] == 1:
        st.success("✅ Safe to Drink")
    else:
        st.error("❌ Not Safe to Drink")
