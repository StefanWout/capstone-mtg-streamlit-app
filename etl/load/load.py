from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="c:/Users/stefa/Documents/Digital Futures/capstone-mtg-streamlit-app/env.dev")

# Retrieve database connection details from environment variables
DB_NAME = os.getenv("TARGET_DB_NAME")
DB_USER = os.getenv("TARGET_DB_USER")
DB_PASSWORD = os.getenv("TARGET_DB_PASSWORD")
DB_HOST = os.getenv("TARGET_DB_HOST")
DB_PORT = os.getenv("TARGET_DB_PORT")


def populate_postgres(dataframe):
    # Create a database connection
    connection_string = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    engine = create_engine(connection_string)

    # Load the DataFrame into the PostgreSQL database
    table_name = "cards"
    try:
        dataframe.to_sql(table_name, engine, if_exists="replace", index=False)
        print(f"Data successfully loaded into the '{table_name}' table in the '{DB_NAME}' database.")
    except Exception as e:
        print(f"Failed to load data: {e}")