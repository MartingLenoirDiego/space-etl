# 🚀 Space ETL Pipeline

An automated ETL pipeline that extracts, transforms, and loads space data from NASA APIs into a PostgreSQL database, with automated analysis reports.

## 📊 Features

- **Extract** — Solar flares, coronal mass ejections (CME), and near-Earth asteroids from NASA APIs
- **Transform** — Data cleaning, normalization and enrichment with Pandas
- **Load** — Storage in PostgreSQL with deduplication
- **Analysis** — Interactive HTML reports with Plotly
- **Scheduler** — Automated daily pipeline at 6:00 AM

## 🛠️ Tech Stack

- **Python 3.12**
- **SQLAlchemy** — ORM and database management
- **PostgreSQL** — Data storage
- **Pandas** — Data transformation
- **Plotly** — Interactive reports
- **APScheduler** — Pipeline automation
- **Docker** — PostgreSQL containerization

## 🚀 Getting Started
```bash
git clone https://github.com/MartingLenoirDiego/space-etl.git
cd space-etl
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file :
```
NASA_API_KEY=your_api_key_here
DATABASE_URL=postgresql://space_user:space_pass@localhost:5434/space_db
```

Start PostgreSQL :
```bash
docker compose up -d
```

Run the pipeline manually :
```bash
python main.py
```

Generate reports :
```bash
python -m analysis.reports
```

Start the scheduler :
```bash
python scheduler.py
```

## 📁 Project Structure
```
space-etl/
├── etl/
│   ├── extract.py      # NASA API data extraction
│   ├── transform.py    # Data cleaning and normalization
│   └── load.py         # PostgreSQL loading with deduplication
├── models/
│   └── database.py     # SQLAlchemy models and DB init
├── analysis/
│   └── reports.py      # Interactive Plotly reports
├── main.py             # Pipeline orchestrator
├── scheduler.py        # Automated daily scheduler
├── docker-compose.yml  # PostgreSQL container
└── requirements.txt
```

## 🔑 Environment Variables

| Variable | Description |
|----------|-------------|
| `NASA_API_KEY` | NASA Open API key (free at api.nasa.gov) |
| `DATABASE_URL` | PostgreSQL connection string |

## 📄 License
MIT
