from sqlalchemy import create_engine, Column, Integer, Float, String, Boolean, DateTime, Text
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

engine = create_engine(os.getenv("DATABASE_URL"))
Session = sessionmaker(bind=engine)
Base = declarative_base()

class SolarFlare(Base):
    __tablename__ = "solar_flares"

    id = Column(Integer, primary_key=True, autoincrement=True)
    flr_id = Column(String, unique=True, nullable=False)
    begin_time = Column(DateTime)
    peak_time = Column(DateTime)
    end_time = Column(DateTime)
    class_type = Column(String)
    active_region = Column(Integer, nullable=True)
    created_at = Column(DateTime, server_default="now()")

class CME(Base):
    __tablename__ = "cmes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    cme_id = Column(String, unique=True, nullable=False)
    start_time = Column(DateTime)
    note = Column(Text, nullable=True)
    created_at = Column(DateTime, server_default="now()")

class Asteroid(Base):
    __tablename__ = "asteroids"

    id = Column(Integer, primary_key=True, autoincrement=True)
    neo_id = Column(String, unique=True, nullable=False)
    name = Column(String)
    diameter_min = Column(Float)
    diameter_max = Column(Float)
    is_hazardous = Column(Boolean)
    close_approach_date = Column(DateTime)
    velocity_kmh = Column(Float)
    miss_distance_km = Column(Float)
    created_at = Column(DateTime, server_default="now()")

def init_db():
    Base.metadata.create_all(engine)
    print("✅ Tables créées avec succès")

if __name__ == "__main__":
    init_db()