from etl.extract.extract_all import load_cards_data
from etl.transform.drop_columns import remove_useless_columns
from etl.transform.drop_rows import (
    remove_un_set_rows,
    # remove_star_rows,
    remove_type_rows,
    # remove_pmoa_rows,
    remove_basicland_rows,
    # remove_subsets_rows,
    remove_digital_rows,
    remove_supertypes_rows,
    remove_duplicates
)

def clean_all_cards():

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
        # 'availability',
        'borderColor',
        'cardParts',
        'faceFlavorName',
        'flavorName',
        'frameEffects',
        'frameVersion',
        'isReserved',
        'isTextless',
        'language',
        'life',
        ]

    all_cards = remove_un_set_rows(all_cards)
    # all_cards = remove_star_rows(all_cards)
    all_cards = remove_type_rows(all_cards)
    # all_cards = remove_pmoa_rows(all_cards)
    all_cards = remove_basicland_rows(all_cards)
    # all_cards = remove_subsets_rows(all_cards)
    all_cards = remove_digital_rows(all_cards)
    all_cards = remove_supertypes_rows(all_cards)
    all_cards = remove_duplicates(all_cards)

    all_cards = remove_useless_columns(all_cards, removeable_columns)

    return all_cards


