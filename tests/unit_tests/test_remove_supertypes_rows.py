import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
import pandas as pd
from etl.transform.drop_rows import remove_supertypes_rows

def test_remove_supertypes_rows(self):

    data = pd.DataFrame({
        'supertypes': ['Host', 'Ongoing', 'World', 'Basic, Snow', 'Snow', 'Legendary'],
        'name': ['Card A', 'Card B', 'Card C', 'Card D', 'Card E', 'Card F']
    })

    result = remove_supertypes_rows(data)

    expected = pd.DataFrame({
        'supertypes': ['Legendary'],
        'name': ['Card F']
    })
    
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected.reset_index(drop=True))

