import pandas as pd
from etl.extract.extract_all import load_cards_data

all_cards = load_cards_data()

removeable_columns = [
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
    ]


def remove_useless_columns(all_cards, removeable_columns):
    all_cards = all_cards.drop(columns=removeable_columns, errors='ignore')
