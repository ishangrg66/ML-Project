import streamlit as st
import joblib
import numpy as np

model = joblib.load("traffic_model.pkl") 

# Mapping dictionaries (used in manual encoding)
time_map = {'Morning': 0, 'Afternoon': 1, 'Evening': 2, 'Night': 3}
day_map = {'Weekday': 0, 'Weekend': 1}
weather_map = {'Sunny': 0, 'Rainy': 1, 'Foggy': 2, 'Snowy': 3}
road_map = {'Highway': 0, 'Local': 1, 'One-way': 2, 'Mountain': 3}
reverse_level_map = {0: 'Low', 1: 'Medium', 2: 'High'}

# App title
st.title("🚦Traffic Congestion Level Predictor")
st.write("Enter the road and weather conditions below to predict traffic congestion level.")

# Input fields
time_of_day = st.selectbox("Time of Day", list(time_map.keys()))
day_type = st.selectbox("Day Type", list(day_map.keys()))
weather = st.selectbox("Weather", list(weather_map.keys()))
road_type = st.selectbox("Road Type", list(road_map.keys()))

vehicle_count = st.number_input("Vehicle Count (approx.)", min_value=0, step=1)
road_lanes = st.number_input("Number of Road Lanes", min_value=1, max_value=6, step=1)
vehicle_mix_ratio = st.slider("Vehicle Mix Ratio (0: all small cars, 1: all heavy vehicles)", 0.0, 1.0, 0.5, step=0.01)

# Prediction button
if st.button("Predict"):
    # Encode categorical inputs
    input_data = [
        time_map[time_of_day],
        day_map[day_type],
        weather_map[weather],
        road_map[road_type],
        vehicle_count,
        road_lanes,
        vehicle_mix_ratio
    ]
    
    prediction = model.predict([input_data])[0]
    result = reverse_level_map[prediction]
    
    st.success(f"Predicted Congestion Level: **{result}**")
