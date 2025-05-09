import pandas as pd
from etl.extract.extract_all import load_cards_data

all_cards = load_cards_data()

def remove_un_set_rows(all_cards):
    if 'isFunny' in all_cards.columns:
        all_cards = all_cards[all_cards['isFunny'] !=True]
    return all_cards

def remove_star_rows(all_cards):
    if 'number' in all_cards.columns:
        all_cards = all_cards[~all_cards['number'].str.contains('★', na=False)]
    return all_cards

def remove_duplicate_cards(all_cards):
    all_cards = all_cards.drop_duplicates(subset='name', keep='first')
    return all_cards

def remove_type_rows(all_cards):
    if 'type' in all_cards.columns:
        all_cards = all_cards[~all_cards['type'].str.contains('Vanguard', na=False)]
        all_cards = all_cards[~all_cards['type'].str.contains('Plane', na=False)]
        all_cards = all_cards[~all_cards['type'].str.contains('Scheme', na=False)]
    return all_cards

def remove_pmoa_rows(all_cards):
    if 'printings' in all_cards.columns:
            all_cards = all_cards[~all_cards['printings'].str.contains('PMOA', na=False)]
    return all_cards

def remove_basicland_rows(all_cards):
    if 'originalType' in all_cards.columns:
            all_cards = all_cards[~all_cards['originalType'].str.contains(r'Basic Land|Basic Snow Land', na=False)]
    return all_cards

def remove_subsets_rows(all_cards):
    if 'subsets' in all_cards.columns:
        all_cards = all_cards[all_cards['subsets'].isnull()]
    return all_cards

def remove_digital_rows(all_cards):
    if 'promavailabilityoTypes' in all_cards.columns:
            all_cards = all_cards[~all_cards['promoavailabilityTypes'].str.contains('arena', na=False)]
            all_cards = all_cards[~all_cards['promoavailabilityTypes'].str.contains('mtgo', na=False)]
            all_cards = all_cards[~all_cards['promoavailabilityTypes'].str.contains('dreamcast', na=False)]
            all_cards = all_cards[~all_cards['promoavailabilityTypes'].str.contains('shandalar', na=False)]
    return all_cards