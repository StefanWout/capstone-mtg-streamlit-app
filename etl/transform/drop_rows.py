import pandas as pd
from etl.extract.extract_all import load_cards_data

all_cards = load_cards_data()

def remove_un_set_rows(all_cards):
    # Remove rows with values in the isFunny collumn as these cards are not used in the game
    # and are not needed for analysis
    
    if 'isFunny' in all_cards.columns:
        all_cards = all_cards[all_cards['isFunny'].isnull()]
    return all_cards

def remove_duplicate_cards(all_cards):
    # Remove duplicate rows based on the 'name' column
    all_cards = all_cards.drop_duplicates(subset='name', keep='first')
    return all_cards


