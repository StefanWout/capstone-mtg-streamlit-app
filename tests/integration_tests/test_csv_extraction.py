import unittest
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
print("PYTHONPATH:", sys.path)
from etl.extract.extract_all import load_cards_data

class TestLoadCardsData(unittest.TestCase):
    def test_load_cards_data(self):
        
        all_cards = load_cards_data()
        
        self.assertIsInstance(all_cards, pd.DataFrame, "The result should be a Pandas DataFrame.")

        self.assertFalse(all_cards.empty, "The DataFrame should not be empty.")

        expected_columns = ['name', 'setCode', 'version'] 
        for column in expected_columns:
            self.assertIn(column, all_cards.columns, f"Missing expected column: {column}")

if __name__ == '__main__':
    unittest.main()