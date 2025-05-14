import sys
import os
import unittest
import pandas as pd
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from etl.transform.drop_rows import remove_digital_rows

class TestRemoveDigitalRows(unittest.TestCase):
    def test_remove_digital_rows(self):

        data = pd.DataFrame({
            'availability': ['arena', 'mtgo', 'paper', 'dreamcast', 'shandalar'],
            'name': ['Card A', 'Card B', 'Card C', 'Card D', 'Card E']
        })

        result = remove_digital_rows(data)

        expected = pd.DataFrame({
            'availability': ['paper'],
            'name': ['Card C']
        })

        pd.testing.assert_frame_equal(result.reset_index(drop=True), expected.reset_index(drop=True))
    
if __name__ == "__main__":
    unittest.main()