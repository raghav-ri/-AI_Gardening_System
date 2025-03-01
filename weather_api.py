import requests

API_KEY = "b127eff9a42fcd74e4861c4fbc71c378"  # 🔹 Your actual API key
CITY = "Patna"  # 🔹 Change this to any city name (e.g., "Delhi", "Mumbai", etc.)

def get_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        print(f"Temperature: {temperature}°C, Humidity: {humidity}%")
        return temperature, humidity
    else:
        print("Error fetching weather data:", data["message"])
        return None, None

# Test the API
get_weather()
