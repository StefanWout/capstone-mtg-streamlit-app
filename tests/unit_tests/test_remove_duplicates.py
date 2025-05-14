import sys
import os
import unittest
import pandas as pd
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from etl.transform.drop_rows import remove_duplicates

class TestRemoveDuplicates(unittest.TestCase):
    def test_remove_duplicates(self):
    
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
        
if __name__ == "__main__":
    unittest.main()