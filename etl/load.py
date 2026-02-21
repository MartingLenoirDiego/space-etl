from models.database import Session, SolarFlare, CME, Asteroid
from sqlalchemy.dialects.postgresql import insert

def load_solar_flares(flares):
    session = Session()
    inserted = 0
    try:
        for f in flares:
            exists = session.query(SolarFlare).filter_by(flr_id=f["flr_id"]).first()
            if not exists:
                session.add(SolarFlare(**f))
                inserted += 1
        session.commit()
        print(f"✅ {inserted} éruptions chargées en base")
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def load_cme(cmes):
    session = Session()
    inserted = 0
    try:
        for c in cmes:
            exists = session.query(CME).filter_by(cme_id=c["cme_id"]).first()
            if not exists:
                session.add(CME(**c))
                inserted += 1
        session.commit()
        print(f"✅ {inserted} CME chargées en base")
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def load_asteroids(asteroids):
    session = Session()
    inserted = 0
    try:
        for a in asteroids:
            exists = session.query(Asteroid).filter_by(neo_id=a["neo_id"]).first()
            if not exists:
                session.add(Asteroid(**a))
                inserted += 1
        session.commit()
        print(f"✅ {inserted} astéroïdes chargés en base")
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()