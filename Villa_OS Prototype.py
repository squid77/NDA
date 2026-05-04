import requests


def fetch_telemetry():
    # Replace with your actual key or use Streamlit Secrets (see Step 3)
    api_key = st.secrets["OPENWEATHER_API_KEY"]
    lat, lon = 9.6421, -85.1685  # Santa Teresa coordinates
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"

    try:
        response = requests.get(url).json()
        temp = response['main']['temp']
        wind = response['wind']['speed']
        humidity = response['main']['humidity']

        # Predictive Logic: Higher wind = higher aero-salinity risk
        risk_score = min(100, int(wind * 10))
        return temp, wind, humidity, risk_score
    except:
        return "N/A", "N/A", "N/A", 0


# UI Integration
temp, wind, hum, risk = fetch_telemetry()

st.markdown("### 🛰️ LIVE TELEMETRY: SANTA TERESA")
t_col1, t_col2, t_col3 = st.columns(3)
with t_col1:
    st.metric("Temperature", f"{temp}°C")
with t_col2:
    st.metric("Wind Speed", f"{wind} m/s")
with t_col3:
    st.metric("Salinity Risk", f"{risk}%", delta="-2%" if risk < 50 else "HIGH")