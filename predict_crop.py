import pickle
import numpy as np
from weather_api import get_weather  # Import weather data function

# Load trained ML model
with open("crop_model.pkl", "rb") as file:
    model = pickle.load(file)

# Get real-time weather data
temperature, humidity = get_weather()

if temperature is not None and humidity is not None:
    # Dummy Rainfall Value (replace with actual data if available)
    rainfall = 200  

    # Make prediction using ML model
    input_data = np.array([[temperature, humidity, rainfall]])
    predicted_crop = model.predict(input_data)[0]

    print(f"✅ Recommended Crop: {predicted_crop}")
else:
    print("❌ Could not fetch weather data")
