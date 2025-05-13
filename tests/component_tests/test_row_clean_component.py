import pandas as pd
from etl.transform.drop_rows import (
    remove_un_set_rows,
    remove_star_rows,
    remove_type_rows,
)


def test_remove_un_set_rows():
    # Create test data
    test_data = pd.DataFrame({
        'name': ['Card A', 'Card B', 'Card C'],
        'isFunny': [True, False, None],
        'number': ['123', '456', '789']
    })

    # Expected output
    expected_data = pd.DataFrame({
        'name': ['Card B', 'Card C'],
        'isFunny': [False, None],
        'number': ['456', '789']
    })

    # Apply the function
    result = remove_un_set_rows(test_data)

    # Assert the result matches the expected output
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_data)


def test_remove_star_rows():
    # Create test data
    test_data = pd.DataFrame({
        'name': ['Card A', 'Card B', 'Card C'],
        'number': ['123★', '456', '789']
    })

    # Expected output
    expected_data = pd.DataFrame({
        'name': ['Card B', 'Card C'],
        'number': ['456', '789']
    })

    # Apply the function
    result = remove_star_rows(test_data)

    # Assert the result matches the expected output
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_data)


def test_remove_type_rows():
    # Create test data
    test_data = pd.DataFrame({
        'name': ['Card A', 'Card B', 'Card C'],
        'type': ['Vanguard', 'Creature', 'Artifact']
    })

    # Expected output
    expected_data = pd.DataFrame({
        'name': ['Card B', 'Card C'],
        'type': ['Creature', 'Artifact']
    })

    # Apply the function
    result = remove_type_rows(test_data)

    # Assert the result matches the expected output
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_data)