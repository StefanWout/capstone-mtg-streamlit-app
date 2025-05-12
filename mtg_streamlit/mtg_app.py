import streamlit as st
import pandas as pd
import numpy as np
from components.mostPrinted import mostPrinted

def load_data(nrows):
        # Load the data from the CSV file
        data = pd.read_csv('../data/cleaned_cards.csv', nrows=nrows)
        return data

def main ():
    st.title('Magic: The Gathering:')
    st.subheader('Exploring Card Data Over 30+ years of game design')

    data = load_data(25539)

    gameplay_data = data[['name', 'manaCost', 'type', 'text', 'power', 'toughness', 'printings']]

    st.subheader('The Basics')
    st.write(gameplay_data)
    
    mostPrinted(data)
    

if __name__ == "__main__":
    main()