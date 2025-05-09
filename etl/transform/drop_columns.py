import pandas as pd
from etl.extract.extract_all import load_cards_data

all_cards = load_cards_data()

removeable_columns = [
    'attractionLights', 
    'boosterTypes',
    'colorIndicator', 
    'duelDeck', 
    'finishes', 
    'hand', 
    'hasContentWarning', 
    'isOversized', 
    'isRebalanced', 
    'isStarter', 
    'isTimeshifted', 
    'originalPrintings', 
    'originalReleaseDate', 
    'promoTypes', 
    'purchaseUrls', 
    'rebalancedPrintings',
    'relatedCards', 
    'securityStamp', 
    'signature', 
    'sourceProducts', 
    'subsets', 
    'watermark',
    'isOnlineOnly',
    'isFunny',
    'hasFoil',
    'hasNonFoil',
    'isAlternative',
    'isFullArt',
    'isPromo',
    'isRebalanced'
    ]


def remove_useless_columns(all_cards, removeable_columns):
    for column in removeable_columns:
        try:
            all_cards = all_cards.drop(columns=[column], errors='raise')
        except KeyError:
            print(f"Warning: Column '{column}' not found in data.")
    return all_cards