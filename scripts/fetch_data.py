import requests
import pandas as pd
import os

# Define a few U.S. cities with coordinates
cities = {
    "St. Louis": {"lat": 38.6270, "lon": -90.1994},
    "Phoenix": {"lat": 33.4484, "lon": -112.0740},
    "New York": {"lat": 40.7128, "lon": -74.0060},
    "Seattle": {"lat": 47.6062, "lon": -122.3321},
    "Miami": {"lat": 25.7617, "lon": -80.1918},
    "Los Angeles": {"lat": 34.0522, "lon": -118.2437}
}

# Define years and output directory
years = list(range(2010, 2025))
output_dir = "data/raw"
os.makedirs(output_dir, exist_ok=True)

# Fetch data from Open-Meteo Historical Weather API
for city, coords in cities.items():
    records = []
    for year in years:
        url = (
            f"https://archive-api.open-meteo.com/v1/archive?"
            f"latitude={coords['lat']}&longitude={coords['lon']}"
            f"&start_date={year}-06-01&end_date={year}-08-31"
            f"&daily=temperature_2m_max,temperature_2m_min"
            f"&timezone=America/Chicago"
        )
        print(f"Fetching {city}, {year}...")
        r = requests.get(url)
        r.raise_for_status()
        data = r.json()

        if "daily" not in data:
            print(f"⚠️ No data returned for {city} ({year}). Skipping.")
            continue

        df = pd.DataFrame({
            "date": data["daily"]["time"],
            "tmax": data["daily"]["temperature_2m_max"],
            "tmin": data["daily"]["temperature_2m_min"]
        })
        df["tavg"] = df[["tmax", "tmin"]].mean(axis=1)
        df["city"] = city
        df["year"] = year
        records.append(df)

    if records:
        city_df = pd.concat(records)
        out_path = f"{output_dir}/{city.replace(' ', '_')}_summer.csv"
        city_df.to_csv(out_path, index=False)
        print(f"Saved data for {city} to {out_path}.")
    else:
        print(f"⚠️ No valid data found for {city} in all years.")
