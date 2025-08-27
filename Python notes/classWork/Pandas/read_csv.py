import pandas as pd
# Read CSV into DataFrame
df = pd.read_csv("weather_forecast.csv")
print(df)
# Extract a single column as Series
temperature = df["temperature"]
print(temperature)
