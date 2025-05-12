import os
import pandas as pd
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from etl.transform.clean_data import clean_all_cards



cleaned_cards = clean_all_cards()

file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'cleaned_cards.csv')

def save_to_csv(dataframe, file_path):

    try:
        dataframe.to_csv(file_path, index=False)
        print(f"Data successfully saved to '{file_path}'.")
    except Exception as e:
        print(f"Failed to save data to CSV: {e}")

if __name__ == "__main__":
    # Run the cleaning process
    cleaned_cards = clean_all_cards()

    # Save the cleaned data to a CSV
    file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'cleaned_cards.csv')
    save_to_csv(cleaned_cards, file_path)