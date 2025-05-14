import sys
import os
import unittest
import pandas as pd
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from etl.transform.drop_rows import remove_un_set_rows

class TestRemoveUnSetRows(unittest.TestCase):
    def test_remove_un_set_rows(self):

        data = pd.DataFrame({
            'isFunny': [True, False, True],
            'name': ['Card A', 'Card B', 'Card C']
        })

        result = remove_un_set_rows(data)

        expected = pd.DataFrame({
            'isFunny': [False],
            'name': ['Card B']
        })

        pd.testing.assert_frame_equal(result.reset_index(drop=True), expected.reset_index(drop=True))
        
if __name__ == "__main__":
    unittest.main()