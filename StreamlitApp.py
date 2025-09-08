import streamlit as st
import joblib
import pandas as pd
import numpy as np
import os

# --- Load the trained pipeline ---
model_path = os.path.join("models", "laptop_price_pipeline.pkl")

if os.path.exists(model_path):
    pipeline = joblib.load(model_path)
else:
    st.error(f"Model not found at {model_path}. Please make sure the file exists.")
    st.stop()

# --- App title ---
st.title("Laptop Price Prediction App for Group H")
st.write("Fill in the details below to predict the laptop price.")

# --- Input fields ---
company = st.selectbox(
    "Company",
    ["Dell", "Apple", "HP", "Lenovo", "Asus", "Acer", "MSI", "Toshiba"]
)
opsys = st.selectbox(
    "Operating System",
    ["Windows", "MacOS", "Linux", "No OS"]
)

ram = st.number_input("RAM (GB)", min_value=2, max_value=64, value=8, step=2)
weight = st.number_input("Weight (kg)", min_value=0.5, max_value=5.0, value=1.5, step=0.1)

screen_w = st.number_input("Screen Width (px)", min_value=800, max_value=4000, value=1920, step=100)
screen_h = st.number_input("Screen Height (px)", min_value=600, max_value=2500, value=1080, step=100)

inches = st.number_input("Screen Size (inches)", min_value=10.0, max_value=20.0, value=15.6, step=0.1)
storage_gb = st.number_input("Storage (GB)", min_value=64, max_value=2000, value=512, step=64)

# --- Compute PPI ---
ppi = ((screen_w ** 2 + screen_h ** 2) ** 0.5) / inches

# --- Prediction button ---
if st.button("Predict Price"):
    # Create dataframe with the same column names as used during training
    input_data = pd.DataFrame([{
        "Company_std": company,
        "OpSys_std": opsys,
        "Ram_GB": ram,
        "Weight_kg": weight,
        "Screen_W": screen_w,
        "Screen_H": screen_h,
        "Storage_GB": storage_gb,
        "Inches": inches,
        "PPI": ppi
    }])

    st.write("Input Data Preview:")
    st.dataframe(input_data)

    # Predict
    prediction = pipeline.predict(input_data)[0]
    st.success(f"Estimated Laptop Price: **${prediction:,.2f}**")
