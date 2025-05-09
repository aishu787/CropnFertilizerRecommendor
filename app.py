import streamlit as st
import numpy as np
import pickle
from src.fertilizer_rules import recommend_fertilizer

# Load model components
model = pickle.load(open("models\crop_model.pkl", "rb"))
scaler = pickle.load(open("models\scaler.pkl", "rb"))
le = pickle.load(open("models\label_encoder.pkl", "rb"))

st.title("🌾 Smart Crop & Fertilizer Recommendation System")

st.write("Enter your soil and climate information:")

N = st.number_input("Nitrogen (N)", 0, 500, 90)
P = st.number_input("Phosphorus (P)", 0, 500, 40)
K = st.number_input("Potassium (K)", 0, 500, 40)
temperature = st.slider("Temperature (°C)", 0.0, 50.0, 25.0)
humidity = st.slider("Humidity (%)", 0.0, 100.0, 80.0)
ph = st.slider("pH", 0.0, 14.0, 6.5)
rainfall = st.slider("Rainfall (mm)", 0.0, 400.0, 200.0)

if st.button("Get Recommendation"):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    scaled_input = scaler.transform(input_data)
    prediction = model.predict(scaled_input)[0]
    crop = le.inverse_transform([prediction])[0]

    st.success(f"✅ Recommended Crop: {crop.title()}")

    st.write("💡 Fertilizer Recommendation:")
    for tip in recommend_fertilizer(crop, N, P, K):
        st.write("-", tip)
