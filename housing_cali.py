import streamlit as st
import pandas as pd
import joblib
import os

# Set page config
st.set_page_config(page_title="Cali House Price Predictor", page_icon="🏠", layout="centered")

# Load pipeline
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
pipeline = joblib.load(os.path.join(BASE_DIR, "model_pipeline.pkl"))

# Custom CSS
st.markdown("""
    <style>
        body {
            background: linear-gradient(to right, #e0f7fa, #fff);
        }
        .stButton>button {
            background-color: #00695c;
            color: white;
        }
        .stButton>button:hover {
            background-color: #004d40;
        }
        .prediction {
            font-size: 24px;
            font-weight: bold;
            color: #00695c;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🏠 California Housing Price Predictor")
st.markdown("Enter details about a location in California and get an estimated **median house price** for that Block.")

# Sidebar Inputs in Two Columns
st.sidebar.header("🔧 Input Parameters")
col1, col2 = st.sidebar.columns(2)

with col1:
    longitude = st.number_input("Longitude", value=-118.0)
    housing_median_age = st.number_input("Median Age", value=30)
    total_rooms = st.number_input("Total Rooms", value=2000)
    population = st.number_input("Population", value=1000)
    median_income = st.number_input("Median Income (In Tens of Thousands $$)", value=3.0)

with col2:
    latitude = st.number_input("Latitude", value=34.0)
    total_bedrooms = st.number_input("Bedrooms", value=400)
    households = st.number_input("Households", value=500)
    ocean_proximity = st.selectbox("Ocean Proximity", [
        "<1H OCEAN", "INLAND", "ISLAND", "NEAR BAY", "NEAR OCEAN"
    ])

# 📝 Note for clarification
st.sidebar.markdown("---")
st.sidebar.markdown(
    "<small>📝 <i>The <strong>Median House Age</strong>, <strong>Total Rooms</strong>, <strong>Total Bedrooms</strong>, <strong>Population</strong>, and <strong>Households</strong> represent totals within the house's block, not just a single house.</i></small>",
    unsafe_allow_html=True
)

# Initialize session state
if "prediction_result" not in st.session_state:
    st.session_state.prediction_result = None

# Predict/Clear buttons
btn1, btn2 = st.columns([1, 1])
with btn1:
    if st.button("📈 Predict House Price"):
        input_df = pd.DataFrame([{
            "longitude": longitude,
            "latitude": latitude,
            "housing_median_age": housing_median_age,
            "total_rooms": total_rooms,
            "total_bedrooms": total_bedrooms,
            "population": population,
            "households": households,
            "median_income": median_income,
            "ocean_proximity": ocean_proximity
        }])

        prediction = pipeline.predict(input_df)[0]
        st.session_state.prediction_result = prediction

with btn2:
    if st.button("🗑️ Clear Result"):
        st.session_state.prediction_result = None

# Show prediction
if st.session_state.prediction_result is not None:
    st.markdown("---")
    st.markdown(
        f"<div class='prediction'>🏡 Predicted Median House Value: <br> <strong>${st.session_state.prediction_result:,.2f}</strong></div>",
        unsafe_allow_html=True
    )
