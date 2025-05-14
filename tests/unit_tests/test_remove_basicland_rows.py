import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
import pandas as pd
from etl.transform.drop_rows import remove_basicland_rows


def test_remove_basicland_rows():
    
    data = pd.DataFrame({
        'name': ['Plains', 'Island', 'Swamp', 'Mountain', 'Forest', 'Card A']
    })

    result = remove_basicland_rows(data)

    expected = pd.DataFrame({
        'name': ['Card A']
    })

    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected.reset_index(drop=True))