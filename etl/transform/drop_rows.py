import pandas as pd
from etl.extract.extract_all import load_cards_data

all_cards = load_cards_data()

# def remove_promotional_rows(all_cards):
#     if 'setCode' in all_cards.columns:
#         all_cards = all_cards[all_cards['setCode'].str.len() != 4]
#     return all_cards

def remove_duplicates(all_cards):
    all_cards = all_cards.drop_duplicates(subset=['name', 'text'], keep='first')
    return all_cards

# def remove_duplicates_for_normal_layout(all_cards):
#     normal_layout_rows = all_cards[all_cards['layout'] == 'normal']
#     normal_layout_rows = normal_layout_rows.drop_duplicates(subset=['name', 'layout'], keep='first')
#     non_normal_layout_rows = all_cards[all_cards['layout'] != 'normal']
    
#     # Combine the two DataFrames
#     all_cards = pd.concat([normal_layout_rows, non_normal_layout_rows], ignore_index=True)
    
#     return all_cards

def remove_un_set_rows(all_cards):
    if 'isFunny' in all_cards.columns:
        all_cards = all_cards[all_cards['isFunny'] !=True]
    return all_cards

# def remove_star_rows(all_cards):
#     if 'number' in all_cards.columns:
#         all_cards = all_cards[~all_cards['number'].str.contains('★', na=False)]
#     return all_cards

def remove_type_rows(all_cards):
    if 'type' in all_cards.columns:
        all_cards = all_cards[~all_cards['type'].str.contains('Vanguard', na=False)]
        all_cards = all_cards[~all_cards['type'].str.contains('Plane', na=False)]
        all_cards = all_cards[~all_cards['type'].str.contains('Scheme', na=False)]
    return all_cards

# def remove_pmoa_rows(all_cards):
#     if 'printings' in all_cards.columns:
#             all_cards = all_cards[~all_cards['printings'].str.contains('PMOA', na=False)]
#     return all_cards

def remove_basicland_rows(all_cards):
    if 'name' in all_cards.columns:
        all_cards = all_cards[~all_cards['name'].str.match(r'^Snow-Covered Plains$|^Snow-Covered Island$|^Snow-Covered Swamp$|^Snow-Covered Mountain$|^Snow-Covered Forest$|^Plains$|^Island$|^Swamp$|^Mountain$|^Forest$', na=False)]
    return all_cards

# def remove_subsets_rows(all_cards):
#     if 'subsets' in all_cards.columns:
#         all_cards = all_cards[all_cards['subsets'].isnull()]
#     return all_cards

# def remove_digital_rows(all_cards):
#     if 'availability' in all_cards.columns:
#             all_cards = all_cards[~all_cards['availability'].str.contains('arena', na=False)]
#             all_cards = all_cards[~all_cards['availability'].str.contains('mtgo', na=False)]
#             all_cards = all_cards[~all_cards['availability'].str.contains('dreamcast', na=False)]
#             all_cards = all_cards[~all_cards['availability'].str.contains('shandalar', na=False)]
#     return all_cards

def remove_digital_rows(all_cards):
    if 'availability' in all_cards.columns:
            all_cards = all_cards[all_cards['availability'] != 'arena']
            all_cards = all_cards[all_cards['availability'] != 'mtgo']
            all_cards = all_cards[all_cards['availability'] != 'dreamcast']
            all_cards = all_cards[all_cards['availability'] != 'shandalar']
    return all_cards

def remove_supertypes_rows(all_cards):
    if 'supertypes' in all_cards.columns:
        all_cards = all_cards[~all_cards['supertypes'].str.contains('Host', na=False)]
        all_cards = all_cards[~all_cards['supertypes'].str.contains('Ongoing', na=False)]
        all_cards = all_cards[~all_cards['supertypes'].str.contains('World', na=False)]
        all_cards = all_cards[~all_cards['supertypes'].str.contains('Basic, Snow', na=False)]
        all_cards = all_cards[~all_cards['supertypes'].str.contains('Snow', na=False)]
    return all_cards