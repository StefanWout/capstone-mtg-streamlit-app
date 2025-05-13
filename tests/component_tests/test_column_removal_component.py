import pandas as pd
from etl.transform.drop_columns import remove_useless_columns

def test_remove_useless_columns():
    # Create test data
    test_data = pd.DataFrame({
        'name': ['Card A', 'Card B', 'Card C'],
        'attractionLights': [1, 2, 3],
        'boosterTypes': ['Type1', 'Type2', 'Type3'],
        'colorIndicator': ['Red', 'Blue', 'Green'],
        'number': ['123', '456', '789']
    })

    # Define columns to remove
    removeable_columns = ['attractionLights', 'boosterTypes', 'colorIndicator']

    # Expected output
    expected_data = pd.DataFrame({
        'name': ['Card A', 'Card B', 'Card C'],
        'number': ['123', '456', '789']
    })

    # Apply the function
    result = remove_useless_columns(test_data, removeable_columns)

    # Assert the result matches the expected output
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_data)
