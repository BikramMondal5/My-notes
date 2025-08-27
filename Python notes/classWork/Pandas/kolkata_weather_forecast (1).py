import requests
import pandas as pd
from datetime import datetime, timedelta

# Coordinates for Kolkata
lat, lon = 22.5726, 88.3639

# Define the date range
start = datetime.utcnow().date()
end = start + timedelta(days=6)

url = (
    "https://api.open-meteo.com/v1/forecast"
    f"?latitude={lat}&longitude={lon}"
    f"&daily=temperature_2m_max,temperature_2m_min,precipitation_sum"
    f"&start_date={start}&end_date={end}"
    "&timezone=Asia/Kolkata"
)

response = requests.get(url)
data = response.json()

# Convert daily forecast part to DataFrame
df = pd.DataFrame(data["daily"])

# Save only the table to CSV
df.to_csv("kolkata_forecast_table.csv", index=False)
print("Saved only the table as 'kolkata_forecast_table.csv'")
# Read CSV into DataFrame
df = pd.read_csv("kolkata_forecast_table.csv")
# Convert 'time' column to datetime and extract weekday names
df["time"] = pd.to_datetime(df["time"])
df["Weekday"] = df["time"].dt.day_name()
#print(df)
# Extract a single column as Series
max_temperature = df[["Weekday", "temperature_2m_max"]]
min_temperature = df[["Weekday", "temperature_2m_min"]]

# Print the Series for maximum and minimum for temperature_2m_max
print(max_temperature)
print(min_temperature)
print('-----------------------')
#Trying to find max and min temperature values but the days are not coming correctly
print(max_temperature.max())
print(max_temperature.min())

# Find row with max temperature
max_row = df.loc[df["temperature_2m_max"].idxmax()]
# Find row with min temperature
min_row = df.loc[df["temperature_2m_max"].idxmin()]
print("Maximum Temperature:")
print(f"{max_row['Weekday']} ({max_row['time'].date()}): {max_row['temperature_2m_max']}°C")
print("\nMinimum Temperature:")
print(f"{min_row['Weekday']} ({min_row['time'].date()}): {min_row['temperature_2m_max']}°C")
#Publishing the number of warm days
warm_days = df[df["temperature_2m_max"] > 31]
print(f"Warm days: {len(warm_days)}")
print(warm_days[["Weekday", "temperature_2m_max"]])
