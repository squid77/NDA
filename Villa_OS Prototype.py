import streamlit as st
import pandas as pd
import numpy as np
import time
import base64
from datetime import datetime

# --- CONFIGURATION & BRANDING ---
st.set_page_config(page_title="Nicoya Systems | Villa OS", layout="wide", initial_sidebar_state="expanded")

# Custom CSS for the V10 Tactical HUD Aesthetic
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Urbanist:wght@400;700;900&display=swap');

    :root { --accent: #deff9a; --bg: #0a0f1a; }

    .stApp { background-color: var(--bg); color: #f5f5f5; font-family: 'Urbanist', sans-serif; }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] { background-color: #050810; border-right: 1px solid rgba(222, 255, 154, 0.1); }

    /* Tactical HUD Cards */
    .hud-card {
        background: rgba(10, 15, 26, 0.85);
        border: 1px solid rgba(222, 255, 154, 0.1);
        padding: 20px;
        border-radius: 4px;
        position: relative;
        margin-bottom: 20px;
    }
    .hud-card::before { content: ''; position: absolute; top: -1px; left: -1px; width: 10px; height: 10px; border-top: 2px solid var(--accent); border-left: 2px solid var(--accent); }

    .mono { font-family: 'Space Mono', monospace; font-size: 0.8rem; letter-spacing: 0.1rem; }
    .accent { color: var(--accent); }
    .critical { color: #ef4444; }

    /* Buttons */
    .stButton>button {
        background-color: transparent;
        color: var(--accent);
        border: 1px solid var(--accent);
        border-radius: 0px;
        font-family: 'Space Mono', monospace;
        text-transform: uppercase;
        width: 100%;
        transition: 0.3s;
    }
    .stButton>button:hover { background-color: var(--accent); color: black; }
    </style>
""", unsafe_allow_html=True)


# --- MOCK DATA GENERATION ---
def get_telemetry():
    return {
        "salinity": np.random.uniform(35, 55),
        "voltage": np.random.uniform(102, 115),
        "cistern": np.random.uniform(40, 95),
        "temp": np.random.uniform(28, 34)
    }


# --- VIEW: ADMIN (THE GOVERNOR) ---
def admin_view():
    st.markdown("<h1 class='italic'>GOVERNANCE <span class='accent'>COMMAND</span></h1>", unsafe_allow_html=True)
    st.markdown("<p class='mono opacity-50'>PORTFOLIO_OVERSIGHT // REGISTRY_001</p>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(
            "<div class='hud-card'><p class='hud-label mono'>ACTIVE NODES</p><h2 class='accent'>03 <span style='font-size:1rem; color:grey;'>/ 20</span></h2></div>",
            unsafe_allow_html=True)
    with col2:
        st.markdown(
            "<div class='hud-card'><p class='hud-label mono'>SYSTEM INTEGRITY</p><h2 class='accent'>98.4%</h2></div>",
            unsafe_allow_html=True)
    with col3:
        st.markdown(
            "<div class='hud-card'><p class='hud-label mono'>TOTAL TAX MITIGATED</p><h2 class='accent'>$1,420.50</h2></div>",
            unsafe_allow_html=True)
    with col4:
        st.markdown(
            "<div class='hud-card'><p class='hud-label mono'>NETWORK UPTIME</p><h2 class='accent'>99.99%</h2></div>",
            unsafe_allow_html=True)

    st.subheader("Global Registry Status")
    nodes = pd.DataFrame({
        "NODE_ID": ["ST-01", "ST-02", "ST-03"],
        "STATUS": ["NOMINAL", "WARNING", "NOMINAL"],
        "SALINITY": ["42mg", "58mg", "31mg"],
        "WATER": ["84%", "42%", "91%"]
    })
    st.table(nodes)


# --- VIEW: TECHNICIAN (THE STEWARD) ---
def technician_view():
    st.markdown("<h1 class='italic'>TACTICAL <span class='accent'>FIELD HUD</span></h1>", unsafe_allow_html=True)
    st.markdown("<p class='mono opacity-50'>OPERATIONAL_DIRECTIVES // ACTIVE_SCAN</p>", unsafe_allow_html=True)

    t = get_telemetry()

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown(f"""
            <div class='hud-card'>
                <h3 class='mono accent'>ACTIVE DIRECTIVE: NODE_ST-02</h3>
                <p>Status: <span class='critical'>CRITICAL_SALINITY_DETECTED</span></p>
                <p class='mono'>Recommendation: Initiate Freshwater Rinse Cycle (Protocol 04)</p>
            </div>
        """, unsafe_allow_html=True)

        if st.button("EXECUTE HARDENING PROTOCOL 04"):
            with st.status("Executing Rinse Cycle...", expanded=True) as status:
                st.write("Isolating exterior HVAC nodes...")
                time.sleep(1)
                st.write("Calibrating pump pressure...")
                time.sleep(1)
                st.write("Desalination complete.")
                status.update(label="Directive Executed Successfully", state="complete", expanded=False)

    with col2:
        st.markdown("<div class='hud-card'>", unsafe_allow_html=True)
        st.write("**Real-time Telemetry**")
        st.metric("Aero-Salinity", f"{t['salinity']:.1f} mg/m³", delta="4.2", delta_color="inverse")
        st.metric("Grid Stability", f"{t['voltage']:.1f} V", delta="-2.1")
        st.metric("Cistern Delta", f"{t['cistern']:.1f} %", delta="0.5")
        st.markdown("</div>", unsafe_allow_html=True)


# --- VIEW: OWNER (THE SOVEREIGN) ---
def owner_view():
    st.markdown("<h1 class='italic'>SOVEREIGN <span class='accent'>PORTAL</span></h1>", unsafe_allow_html=True)
    st.markdown("<p class='mono opacity-50'>ASSET_ID: ST-01 // THE_MONOLITH</p>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='hud-card'>", unsafe_allow_html=True)
        st.subheader("Asset Health Index")
        st.write("Your property is currently performing at **94% efficiency**.")
        chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['Power', 'Water', 'Salt Mitigation'])
        st.line_chart(chart_data)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='hud-card'>", unsafe_allow_html=True)
        st.subheader("Infrastructure ROI")
        st.markdown(f"### Current 'Salt-Air Tax' Mitigated: <span class='accent'>$42.50 / day</span>",
                    unsafe_allow_html=True)
        st.write(
            "Through automated rinsing and grid isolation, we have prevented an estimated $1,200 in mechanical decay this month.")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='hud-card'>", unsafe_allow_html=True)
        st.write("**Active Defenses**")
        st.write("✅ Surge Protection: Active")
        st.write("✅ Cistern Autonomy: 14 Days")
        st.write("✅ Corrosion Shield: Level 1 (Nominal)")
        st.markdown("</div>", unsafe_allow_html=True)


# --- MAIN APP LOGIC ---
def main():
    # Sidebar Navigation
    st.sidebar.markdown(f"<h2 class='accent italic'>NICOYA SYSTEMS</h2>", unsafe_allow_html=True)
    st.sidebar.markdown("<p class='mono' style='font-size:0.6rem;'>GOVERNANCE OS v1.0</p>", unsafe_allow_html=True)

    view = st.sidebar.radio("SELECT COMMAND INTERFACE",
                            ["ADMIN (GOVERNOR)", "TECHNICIAN (STEWARD)", "OWNER (SOVEREIGN)"])

    st.sidebar.markdown("---")
    st.sidebar.markdown(f"<p class='mono'>SYSTEM_TIME: {datetime.now().strftime('%H:%M:%S')} UTC</p>",
                        unsafe_allow_html=True)
    st.sidebar.markdown("<p class='mono'>ENCRYPTION: AES-256</p>", unsafe_allow_html=True)

    if view == "ADMIN (GOVERNOR)":
        admin_view()
    elif view == "TECHNICIAN (STEWARD)":
        technician_view()
    else:
        owner_view()


if __name__ == "__main__":
    main()