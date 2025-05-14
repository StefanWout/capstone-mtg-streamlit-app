import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
import pandas as pd
from etl.transform.drop_columns import remove_useless_columns

def test_remove_useless_columns():
    
    test_data = pd.DataFrame({
        'name': ['Card A', 'Card B', 'Card C'],
        'attractionLights': [1, 2, 3],
        'boosterTypes': ['Type1', 'Type2', 'Type3'],
        'colorIndicator': ['Red', 'Blue', 'Green'],
        'number': ['123', '456', '789']
    })

    removeable_columns = ['attractionLights', 'boosterTypes', 'colorIndicator']

    expected_data = pd.DataFrame({
        'name': ['Card A', 'Card B', 'Card C'],
        'number': ['123', '456', '789']
    })

    result = remove_useless_columns(test_data, removeable_columns)

    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_data)