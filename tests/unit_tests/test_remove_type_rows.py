import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
import pandas as pd
from etl.transform.drop_rows import remove_type_rows

def test_remove_type_rows():
   
    data = pd.DataFrame({
        'type': ['Vanguard', 'Plane', 'Scheme', 'Creature'],
        'name': ['Card A', 'Card B', 'Card C', 'Card D']
    })

    result = remove_type_rows(data)

    expected = pd.DataFrame({
        'type': ['Creature'],
        'name': ['Card D']
    })

    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected.reset_index(drop=True))