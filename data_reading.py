import streamlit as st
import pandas as pd
import joblib  # For loading the trained model
from datetime import time as dt_time  # Avoids conflict with time module
import time
# Load your trained model
model = joblib.load('svr_model.pkl')

st.markdown("""
    <style>
    .title {
        color: #FFDB00;
        font-size: 48px;
        font-weight: bold;
        text-align: center;
    }
    .subtitle {
        color: cyan;  
        font-size: 24px;
        text-align: center;
        margin-bottom: 20px;
    }
    .centered-button {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 20px;
    }
    .centered-button button {
        background-color: #4CAF50;
        border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        transition-duration: 0.4s;
        cursor: pointer;
    }
    .centered-button button:hover {
        background-color: white;
        color: black;
        border: 2px solid #4CAF50;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="title">Solar Energy Prediction Using Weather Data</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">This application predicts how much solar energy will be generated based on the weather data provided.</div>', unsafe_allow_html=True)

st.sidebar.header("Sustainable Energy Information")

st.sidebar.subheader("Learn about Sustainable Energy")
sustainable_info = st.sidebar.selectbox(
    "Select a topic to learn more:",
    ("Overview", "Solar Energy", "Wind Energy", "Hydropower", "Geothermal Energy")
)

if sustainable_info == "Overview":
    st.sidebar.write("Sustainable energy involves using resources that are naturally replenished to generate power, reducing environmental impact.")
elif sustainable_info == "Solar Energy":
    st.sidebar.write("Solar energy harnesses power from the sun using photovoltaic cells or solar thermal systems.")
elif sustainable_info == "Wind Energy":
    st.sidebar.write("Wind energy captures the power of wind flow using wind turbines to generate electricity.")
elif sustainable_info == "Hydropower":
    st.sidebar.write("Hydropower generates electricity by harnessing the energy of flowing water.")
elif sustainable_info == "Geothermal Energy":
    st.sidebar.write("Geothermal energy utilizes heat from the Earth's interior to generate power.")

st.header("Solar Energy Prediction Inputs")
selected_date = st.text_input("Enter Date (1-31)")

month = st.text_input("Enter Month (1-12)")

hours = list(range(1, 25))
selected_time = st.selectbox("Select hour (24hr format)", hours)

pm25 = st.text_input("PM2.5 (µg/m³)")

pm10 = st.text_input("PM10 (µg/m³)")

temperature = st.text_input("Temperature (°C)")

humidity = st.text_input("Humidity (%)")

ozone = st.text_input("Ozone (ppb)")

wind_speed = st.text_input("Wind Speed (m/s)")

irradiance = st.text_input("Irradiance (kWh/m2)")

def predict_energy(selected_date, selected_time, pm25, pm10, temperature, humidity, ozone, wind_speed, irradiance):
    input_data = {
        'selected_date': selected_date,
        'month': int(month),
        'selected_time': selected_time,
        'pm25': float(pm25),
        'pm10': float(pm10),
        'temperature': float(temperature),
        'humidity': float(humidity),
        'ozone': float(ozone),
        'wind_speed': float(wind_speed),
        'irradiance': float(irradiance)
    }
    
    input_features = pd.DataFrame([input_data])
    
    prediction = model.predict(input_features)
    
    return prediction[0]

st.markdown('<div class="centered-button">', unsafe_allow_html=True)
if st.button("Predict"):
    energy_prediction = predict_energy(selected_date, selected_time, pm25, pm10, temperature, humidity, ozone, wind_speed, irradiance)
    st.write(f'Energy generated on {selected_date}th at {selected_time}:00 will be approximately: {energy_prediction:.2f} kWh')
    with st.spinner('Wait for it...'):
        time.sleep(1)
        # st.success('Done!')
    st.success('Prediction completed successfully!')
    st.balloons()
st.markdown('</div>', unsafe_allow_html=True)
