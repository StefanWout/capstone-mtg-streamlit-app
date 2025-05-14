import sys
import os
import unittest
import pandas as pd
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from etl.transform.drop_rows import remove_basicland_rows

class TestRemoveBasiclandRows(unittest.TestCase):
    def test_remove_basicland_rows(self):
        # Input DataFrame
        data = pd.DataFrame({
            'name': ['Plains', 'Island', 'Swamp', 'Mountain', 'Forest', 'Card A']
        })

        # Apply the function
        result = remove_basicland_rows(data)

        # Expected DataFrame
        expected = pd.DataFrame({
            'name': ['Card A']
        })

        # Assert the result matches the expected output
        pd.testing.assert_frame_equal(result.reset_index(drop=True), expected.reset_index(drop=True))
        print("Test is running...")

if __name__ == "__main__":
    unittest.main()