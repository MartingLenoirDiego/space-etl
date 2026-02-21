import pandas as pd
from sqlalchemy import text
from models.database import engine
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def get_solar_flares_df():
    query = "SELECT * FROM solar_flares ORDER BY begin_time"
    return pd.read_sql(query, engine)

def get_cme_df():
    query = "SELECT * FROM cmes ORDER BY start_time"
    return pd.read_sql(query, engine)

def get_asteroids_df():
    query = "SELECT * FROM asteroids ORDER BY close_approach_date"
    return pd.read_sql(query, engine)

def report_solar_activity():
    df = get_solar_flares_df()
    if df.empty:
        print("Aucune donnée d'éruptions solaires")
        return

    df["date"] = pd.to_datetime(df["begin_time"]).dt.date
    df["week"] = pd.to_datetime(df["begin_time"]).dt.isocalendar().week

    print("\n☀️ RAPPORT ACTIVITÉ SOLAIRE")
    print(f"Total éruptions : {len(df)}")
    print(f"Répartition par classe :\n{df['class_type'].value_counts()}")

    fig = make_subplots(rows=2, cols=1,
    subplot_titles=["Éruptions par jour", "Répartition par classe"],
    specs=[[{"type": "xy"}], [{"type": "domain"}]])

    daily = df.groupby("date").size().reset_index(name="count")
    fig.add_trace(go.Bar(x=daily["date"], y=daily["count"], name="Éruptions"), row=1, col=1)

    class_counts = df["class_type"].value_counts().reset_index()
    class_counts.columns = ["classe", "count"]
    fig.add_trace(go.Pie(labels=class_counts["classe"], values=class_counts["count"], name="Classes"), row=2, col=1)

    fig.update_layout(title="Analyse de l'activité solaire", paper_bgcolor="rgba(0,0,0,0)")
    fig.write_html("analysis/solar_report.html")
    print("✅ Rapport sauvegardé : analysis/solar_report.html")

def report_asteroids():
    df = get_asteroids_df()
    if df.empty:
        print("Aucune donnée d'astéroïdes")
        return

    print("\n☄️ RAPPORT ASTÉROÏDES")
    print(f"Total astéroïdes : {len(df)}")
    print(f"Potentiellement dangereux : {df['is_hazardous'].sum()}")
    print(f"Distance moyenne : {df['miss_distance_km'].mean():,.0f} km")
    print(f"Vitesse moyenne : {df['velocity_kmh'].mean():,.0f} km/h")

    fig = make_subplots(rows=1, cols=2,
    subplot_titles=["Distance vs Diamètre", "Dangereux vs Non dangereux"],
    specs=[[{"type": "xy"}, {"type": "domain"}]])

    df["hazard_label"] = df["is_hazardous"].map({True: "⚠️ Dangereux", False: "✅ Non dangereux"})

    fig.add_trace(go.Scatter(
        x=df["miss_distance_km"],
        y=df["diameter_max"],
        mode="markers",
        marker=dict(
            color=df["is_hazardous"].map({True: "red", False: "green"}),
            size=8
        ),
        text=df["name"],
        name="Astéroïdes"
    ), row=1, col=1)

    hazard_counts = df["hazard_label"].value_counts().reset_index()
    hazard_counts.columns = ["label", "count"]
    fig.add_trace(go.Pie(
        labels=hazard_counts["label"],
        values=hazard_counts["count"],
        marker=dict(colors=["red", "green"])
    ), row=1, col=2)

    fig.update_layout(title="Analyse des astéroïdes", paper_bgcolor="rgba(0,0,0,0)")
    fig.write_html("analysis/asteroids_report.html")
    print("✅ Rapport sauvegardé : analysis/asteroids_report.html")

if __name__ == "__main__":
    report_solar_activity()
    report_asteroids()