import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
print("PYTHONPATH:", sys.path)
import unittest
import pandas as pd
from etl.extract.extract_all import load_cards_data

class TestLoadCardsData(unittest.TestCase):
    def test_extract_cards_data(self):
        
        all_cards = load_cards_data()
        
        self.assertIsInstance(all_cards, pd.DataFrame, "The result should be a Pandas DataFrame.")

        self.assertFalse(all_cards.empty, "The DataFrame should not be empty.")

        expected_columns = ['artist','artistIds','asciiName','availability','colorIdentity','colors','defense','edhrecRank','edhrecSaltiness','faceConvertedManaCost','faceManaValue','faceName','flavorText','hasAlternativeDeckLimit','isGameChanger','isReprint','isStorySpotlight','keywords','layout','leadershipSkills','loyalty','manaCost','manaValue','name','number','originalText','originalType','otherFaceIds','power','printings','rarity','setCode','side','subtypes','supertypes','text','toughness','type','types','uuid','variations'] 
        for column in expected_columns:
            self.assertIn(column, all_cards.columns, f"Missing expected column: {column}")

    def test_cleaned_cards_file(self):
      
        cleaned_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../data/cleaned_cards.csv'))
        
        self.assertTrue(os.path.exists(cleaned_file_path), "The cleaned_cards.csv file does not exist.")
        
        cleaned_cards = pd.read_csv(cleaned_file_path)

        self.assertIsInstance(cleaned_cards, pd.DataFrame, "The cleaned_cards.csv file should be loaded as a Pandas DataFrame.")

        self.assertFalse(cleaned_cards.empty, "The cleaned_cards.csv DataFrame should not be empty.")


if __name__ == '__main__':
    unittest.main()