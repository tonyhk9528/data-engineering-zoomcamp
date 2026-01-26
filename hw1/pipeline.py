import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm
import click

dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64",
}

parse_dates = ["tpep_pickup_datetime", "tpep_dropoff_datetime"]

@click.command()
@click.option('--pg-user', default='root', help='PostgreSQL user')
@click.option('--pg-pass', default='root', help='PostgreSQL password')
@click.option('--pg-host', default='localhost', help='PostgreSQL host')
@click.option('--pg-port', default=5432, type=int, help='PostgreSQL port')
@click.option('--pg-db', default='ny_taxi', help='PostgreSQL database name')
@click.option('--target-table', default='yellow_taxi_data', help='Target table name')
def run(pg_user, pg_pass, pg_host, pg_port, pg_db, target_table):
    year = 2021
    month = 1

    pg_user = "root"
    pg_pass = "root"
    pg_host = "localhost"   # ✅ FIXED
    pg_port = 5432
    pg_db = "ny_taxi"

    target_table = "yellow_taxi_data"
    chunk_size = 100000

    prefix = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/"
    url = prefix + f"yellow_tripdata_{year}-{month:02d}.csv.gz"

    engine = create_engine(f"postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}")

    # Create table schema from a small sample (keeps dtypes)
    df_sample = pd.read_csv(url, nrows=100, dtype=dtype, parse_dates=parse_dates)
    df_sample.head(0).to_sql(name=table_name, con=engine, if_exists="replace", index=False)

    # Stream chunks
    df_iter = pd.read_csv(url, dtype=dtype, parse_dates=parse_dates, chunksize=chunk_size)

    for df_chunk in tqdm(df_iter):
        df_chunk.to_sql(
            name=table_name,
            con=engine,
            if_exists="append",
            index=False,
            method="multi",
            chunksize=1000,
        )
        print("Inserted:", len(df_chunk))

if __name__ == "__main__":
    run()
