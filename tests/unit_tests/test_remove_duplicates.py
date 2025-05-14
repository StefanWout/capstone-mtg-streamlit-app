import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
import pandas as pd
from etl.transform.drop_rows import remove_duplicates

def test_remove_duplicates():
   
    data = pd.DataFrame({
        'name': ['Card A', 'Card A', 'Card B'],
        'text': ['Some text', 'Some text', 'Other text']
    })

    result = remove_duplicates(data)

    expected = pd.DataFrame({
        'name': ['Card A', 'Card B'],
        'text': ['Some text', 'Other text']
    })

    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected.reset_index(drop=True))