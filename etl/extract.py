import requests
import os
from dotenv import load_dotenv
from datetime import date, timedelta

load_dotenv()

NASA_API_KEY = os.getenv("NASA_API_KEY")
BASE_URL = "https://api.nasa.gov"
DONKI_URL = "https://api.nasa.gov/DONKI"
NEO_URL = "https://api.nasa.gov/neo/rest/v1"

def extract_solar_flares(start_date: date, end_date: date):
    params = {
        "startDate": start_date.strftime("%Y-%m-%d"),
        "endDate": end_date.strftime("%Y-%m-%d"),
        "api_key": NASA_API_KEY
    }
    response = requests.get(f"{DONKI_URL}/FLR", params=params)
    response.raise_for_status()
    data = response.json()
    print(f"✅ {len(data)} éruptions solaires extraites")
    return data

def extract_cme(start_date: date, end_date: date):
    params = {
        "startDate": start_date.strftime("%Y-%m-%d"),
        "endDate": end_date.strftime("%Y-%m-%d"),
        "api_key": NASA_API_KEY
    }
    response = requests.get(f"{DONKI_URL}/CME", params=params)
    response.raise_for_status()
    data = response.json()
    print(f"✅ {len(data)} CME extraites")
    return data

def extract_asteroids(start_date: date, end_date: date):
    all_asteroids = []
    current = start_date

    while current < end_date:
        chunk_end = min(current + timedelta(days=7), end_date)
        params = {
            "start_date": current.strftime("%Y-%m-%d"),
            "end_date": chunk_end.strftime("%Y-%m-%d"),
            "api_key": NASA_API_KEY
        }
        response = requests.get(f"{NEO_URL}/feed", params=params)
        response.raise_for_status()
        data = response.json()

        for neos in data["near_earth_objects"].values():
            all_asteroids.extend(neos)

        current = chunk_end + timedelta(days=1)

    print(f"✅ {len(all_asteroids)} astéroïdes extraits")
    return all_asteroids