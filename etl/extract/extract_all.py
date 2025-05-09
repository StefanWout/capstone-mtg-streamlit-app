import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv(dotenv_path="c:/Users/stefa/Documents/Digital Futures/capstone-mtg-streamlit-app/env.dev")

DB_NAME = os.getenv("TARGET_DB_NAME")
DB_USER = os.getenv("TARGET_DB_USER")
DB_PASSWORD = os.getenv("TARGET_DB_PASSWORD")
DB_HOST = os.getenv("TARGET_DB_HOST")
DB_PORT = os.getenv("TARGET_DB_PORT")

def load_cards_data():
    FILE_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'cards.csv')
    all_cards = pd.read_csv(FILE_PATH)
    return all_cards

if __name__ == "__main__":

    card_data = load_cards_data()

    populate_postgres(card_data)

