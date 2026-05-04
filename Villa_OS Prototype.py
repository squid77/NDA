import streamlit as st
import pandas as pd
import numpy as np
import requests
from datetime import datetime

# --- CONFIGURATION & BRANDING ---
st.set_page_config(
    page_title="Nicoya Systems | Villa OS",
    layout="wide",
    initial_sidebar_state="expanded"
)


# --- TELEMETRY LOGIC ---
def fetch_telemetry():
    try:
        # Pulling from Streamlit Secrets for Information Assurance
        api_key = st.secrets["dec41d297d9b33771164bcb8e894ce6f"]
        lat, lon = 9.6421, -85.1685  # Santa Teresa Coordinates
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"

        response = requests.get(url).json()
        temp = response['main']['temp']
        wind = response['wind']['speed']
        hum = response['main']['humidity']

        # Predictive Logic: Aero-salinity risk increases with wind speed
        risk = min(100, int(wind * 10))
        return temp, wind, hum, risk
    except Exception as e:
        # This will print the actual error message in your Streamlit Cloud Logs
        st.error(f"Telemetry Error: {e}")
        return "N/A", "N/A", "N/A", 0


# --- UI STYLING ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Urbanist:wght@400;700;900&display=swap');
    .stApp { background-color: #0a0f1a; color: #deff9a; font-family: 'Urbanist', sans-serif; }
    .metric-card {
        background-color: rgba(222, 255, 154, 0.05);
        border: 1px solid #deff9a;
        padding: 20px;
        border-radius: 5px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- DASHBOARD RENDERING ---
st.title("⚡ NICOYA SYSTEMS | VILLA OS")
st.subheader("Infrastructure Intelligence Registry | Santa Teresa, CR")

# Execute Telemetry Fetch
temp, wind, hum, risk = fetch_telemetry()

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f'<div class="metric-card"><h3>AIR TEMP</h3><h1>{temp}°C</h1></div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="metric-card"><h3>WIND SPEED</h3><h1>{wind} m/s</h1></div>', unsafe_allow_html=True)
with col3:
    st.markdown(f'<div class="metric-card"><h3>SALINITY RISK</h3><h1>{risk}%</h1></div>', unsafe_allow_html=True)

st.write(f"Last Telemetry Sync: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")