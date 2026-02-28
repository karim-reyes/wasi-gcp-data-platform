import pandas as pd
import sqlalchemy

db_user = "postgres"
db_password = "Wasi2026!"
db_host = "35.232.81.32"
db_name = "ventasdb"

engine = sqlalchemy.create_engine(
    f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:5432/{db_name}"
)

df = pd.read_csv("data/pagosTEST.csv")

# Asegurar formato fecha
df["fecha_pago"] = pd.to_datetime(df["fecha_pago"])

df.to_sql(
    "pagos",
    engine,
    if_exists="append",
    index=False
)

print("Carga a Cloud SQL completada")
