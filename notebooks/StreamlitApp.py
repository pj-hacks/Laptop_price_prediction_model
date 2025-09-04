import streamlit as st
import joblib
import numpy as np
import pandas as pd

#import os
#pipeline_path = os.path.join("notebooks", "models", "laptop_price_pipeline.pkl")
#pipeline = joblib.load(pipeline_path)
pipeline = joblib.load("notebooks/models/laptop_price_pipeline.pkl")


st.title("Laptop Price Prediction App For Group H")
st.write("Fill in the details below to predict the laptop price.")

# --- Input fields ---
company = st.selectbox("Company", ["Dell", "Apple", "HP", "Lenovo", "Asus", "Acer", "MSI", "Toshiba"])  
opsys   = st.selectbox("Operating System", ["Windows", "MacOS", "Linux", "No OS"])  

ram     = st.number_input("RAM (GB)", min_value=2, max_value=64, value=8, step=2)  
weight  = st.number_input("Weight (kg)", min_value=0.5, max_value=5.0, value=1.5, step=0.1)  

screen_w = st.number_input("Screen Width (px)", min_value=800, max_value=4000, value=1920, step=100)  
screen_h = st.number_input("Screen Height (px)", min_value=600, max_value=2500, value=1080, step=100)  

# --- Prediction button ---
if st.button("Predict Price"):
    # Create dataframe with same column names as training
    input_data = pd.DataFrame([{
        "Company_std": company,
        "OpSys_std": opsys,
        "Ram_GB": ram,
        "Weight_kg": weight,
        "Screen_W": screen_w,
        "Screen_H": screen_h
    }])
    
    # Predict
    prediction = pipeline.predict(input_data)[0]
    
    st.success(f"Estimated Laptop Price: **${prediction:,.2f}**")
