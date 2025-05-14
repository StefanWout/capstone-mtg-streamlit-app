import sys
import os
import unittest
import pandas as pd
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from etl.transform.drop_rows import remove_supertypes_rows

class TestRemoveSupertypesRows(unittest.TestCase):
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

if __name__ == "__main__":
    unittest.main()