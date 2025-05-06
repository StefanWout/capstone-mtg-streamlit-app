import os
import pandas as pd


def load_cards_data():
    FILE_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'cards.csv')
    all_cards = pd.read_csv(FILE_PATH)
    return all_cards

card_data = load_cards_data()

print(card_data.isnull())