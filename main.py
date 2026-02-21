from datetime import date, timedelta
from etl.extract import extract_solar_flares, extract_cme, extract_asteroids
from etl.transform import transform_solar_flares, transform_cme, transform_asteroids
from etl.load import load_solar_flares, load_cme, load_asteroids
from models.database import init_db

def run_pipeline(start_date: date, end_date: date):
    print(f"\n🚀 Démarrage du pipeline ETL ({start_date} → {end_date})\n")

    print("📡 Extraction...")
    raw_flares = extract_solar_flares(start_date, end_date)
    raw_cmes = extract_cme(start_date, end_date)
    raw_asteroids = extract_asteroids(start_date, end_date)

    print("\n🔧 Transformation...")
    flares = transform_solar_flares(raw_flares)
    cmes = transform_cme(raw_cmes)
    asteroids = transform_asteroids(raw_asteroids)

    print("\n💾 Chargement en base...")
    load_solar_flares(flares)
    load_cme(cmes)
    load_asteroids(asteroids)

    print("\n✅ Pipeline terminé avec succès !")

if __name__ == "__main__":
    init_db()
    end = date.today()
    start = end - timedelta(days=30)
    run_pipeline(start, end)