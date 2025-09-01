import requests
import pandas as pd
from datetime import datetime, timedelta

# Coordinates
lat, lon = 22.5726, 88.3639
start = datetime.utcnow().date()
end = start + timedelta(days=6)

# API URL
url = (
    "https://api.open-meteo.com/v1/forecast"
    f"?latitude={lat}&longitude={lon}"
    f"&daily=temperature_2m_max,temperature_2m_min,precipitation_sum"
    f"&start_date={start}&end_date={end}"
    "&timezone=Asia/Kolkata"
)

# Fetch data
response = requests.get(url)
data = response.json()

# Convert to DataFrame
df = pd.DataFrame(data['daily'])

# Save to CSV
df.to_csv("kolkata_forecast_table.csv", index=False)

# Read CSV
df = pd.read_csv("kolkata_forecast_table.csv")

# (ii) Add Weekdays
df['Weekday'] = pd.to_datetime(df['time']).dt.day_name()

# (iii) Extract column
temp_max = df[['Weekday', 'temperature_2m_max']]

# (iv) Warm days > 31°C
warm_days = df[df['temperature_2m_max'] > 31][['Weekday', 'temperature_2m_max']]

print("Full DataFrame:\n", df)
print("\nTemperature Max with Weekdays:\n", temp_max)
print("\nWarm Days (>31°C):\n", warm_days)
