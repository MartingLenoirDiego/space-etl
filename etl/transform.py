from datetime import datetime

def transform_solar_flares(raw_data):
    flares = []
    for f in raw_data:
        if not f.get("flrID"):
            continue
        flares.append({
            "flr_id": f["flrID"],
            "begin_time": datetime.fromisoformat(f["beginTime"]) if f.get("beginTime") else None,
            "peak_time": datetime.fromisoformat(f["peakTime"]) if f.get("peakTime") else None,
            "end_time": datetime.fromisoformat(f["endTime"]) if f.get("endTime") else None,
            "class_type": f.get("classType"),
            "active_region": f.get("activeRegionNum"),
        })
    print(f"✅ {len(flares)} éruptions transformées")
    return flares

def transform_cme(raw_data):
    cmes = []
    for c in raw_data:
        if not c.get("activityID"):
            continue
        cmes.append({
            "cme_id": c["activityID"],
            "start_time": datetime.fromisoformat(c["startTime"]) if c.get("startTime") else None,
            "note": c.get("note", "")[:500] if c.get("note") else None,
        })
    print(f"✅ {len(cmes)} CME transformées")
    return cmes

def transform_asteroids(raw_data):
    asteroids = []
    for neo in raw_data:
        try:
            approach = neo["close_approach_data"][0]
            asteroids.append({
                "neo_id": neo["id"],
                "name": neo["name"],
                "diameter_min": neo["estimated_diameter"]["meters"]["estimated_diameter_min"],
                "diameter_max": neo["estimated_diameter"]["meters"]["estimated_diameter_max"],
                "is_hazardous": neo["is_potentially_hazardous_asteroid"],
                "close_approach_date": datetime.strptime(approach["close_approach_date_full"], "%Y-%b-%d %H:%M"),
                "velocity_kmh": float(approach["relative_velocity"]["kilometers_per_hour"]),
                "miss_distance_km": float(approach["miss_distance"]["kilometers"]),
            })
        except (KeyError, IndexError):
            continue
    print(f"✅ {len(asteroids)} astéroïdes transformés")
    return asteroids