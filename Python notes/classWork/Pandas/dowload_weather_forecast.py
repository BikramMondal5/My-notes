import requests

# Example: Weather forecast for New Delhi
url = (
    "https://api.open-meteo.com/v1/forecast?"
    "latitude=28.61&longitude=77.23&hourly=temperature_2m,relative_humidity_2m&format=csv"
)

# Send request
response = requests.get(url)

# Save as CSV file
with open("weather_forecast.csv", "wb") as f:
    f.write(response.content)

print("✅ Weather forecast CSV downloaded as 'weather_forecast.csv'")
