import joblib
import requests
import matplotlib.pyplot as plt
import streamlit as st

model = joblib.load('wether_pipe.lib')

url = 'http://api.weatherapi.com/v1/forecast.json?key=16cb276c09234a10bb654755220401&q=Bandar Abbas&days=3&aqi=no&alerts=no'
res = requests.get(url)

weather_data = res.json()
current_weather = weather_data['current']
forecast_weather = weather_data['forecast']['forecastday']

condition = []

for day in forecast_weather:
    for hour in day['hour']:
        condition.append([hour['temp_c'], hour['pressure_mb'], hour['humidity']])


production_forecast = model.predict(condition)


########################################################

st.title('Power Plant')

st.write("""
hello
""")
fig, ax = plt.subplots()
ax.plot(production_forecast)

st.pyplot(fig)
