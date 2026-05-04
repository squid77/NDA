import streamlit as st
import pandas as pd
import numpy as np
import time
import base64
from datetime import datetime

# --- CONFIGURATION & BRANDING ---
# This MUST be the first Streamlit command executed
st.set_page_config(
    page_title="Nicoya Systems | Villa OS",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- UI STYLING ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Urbanist:wght@400;700;900&display=swap');

    .stApp {
        background-color: #0a0f1a;
        color: #deff9a;
        font-family: 'Urbanist', sans-serif;
    }

    .metric-card {
        background-color: rgba(222, 255, 154, 0.05);
        border: 1px solid #deff9a;
        padding: 20px;
        border-radius: 5px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- APP LOGIC ---
st.title("⚡ NICOYA SYSTEMS | VILLA OS")
st.subheader("Infrastructure Intelligence Registry | Santa Teresa, CR")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="metric-card"><h3>REGISTRY STATUS</h3><h1>ACTIVE</h1></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="metric-card"><h3>NODES ENROLLED</h3><h1>20</h1></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="metric-card"><h3>SYSTEM HEALTH</h3><h1>98.2%</h1></div>', unsafe_allow_html=True)

st.write(f"Telemetry Active as of: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")