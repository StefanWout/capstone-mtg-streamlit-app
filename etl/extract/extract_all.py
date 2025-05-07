import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv(dotenv_path="c:/Users/stefa/Documents/Digital Futures/capstone-mtg-streamlit-app/env.dev")

# Retrieve database connection details from environment variables
DB_NAME = os.getenv("TARGET_DB_NAME")
DB_USER = os.getenv("TARGET_DB_USER")
DB_PASSWORD = os.getenv("TARGET_DB_PASSWORD")
DB_HOST = os.getenv("TARGET_DB_HOST")
DB_PORT = os.getenv("TARGET_DB_PORT")

def load_cards_data():
    FILE_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'cards.csv')
    all_cards = pd.read_csv(FILE_PATH)
    return all_cards

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

if __name__ == "__main__":
    # Extract data from the CSV file
    card_data = load_cards_data()

    # Populate the PostgreSQL database
    populate_postgres(card_data)

