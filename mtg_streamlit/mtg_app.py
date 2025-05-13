import streamlit as st
import pandas as pd
import numpy as np
from components.most_printed import most_printed
from components.mono_color_distribution import mono_color_distribution
from components.multi_color_distribution import multi_color_distribution

mana_symbol_mapping = {
    '{W}': '⚪',  
    '{U}': '🔵', 
    '{B}': '⚫',  
    '{R}': '🔴',  
    '{G}': '🟢',  
    '{C}': '⚙️',  
    '{0}': '0',
    '{X}': 'X',   
    '{1}': '1',   
    '{2}': '2',
    '{3}': '3',
    '{4}': '4',
    '{5}': '5',
    '{6}': '6',
    '{7}': '7',
    '{8}': '8',
    '{9}': '9',
    '{10}': '10',
}

def replace_mana_symbols(mana_cost):
    if pd.isnull(mana_cost):
        return mana_cost
    for symbol, replacement in mana_symbol_mapping.items():
        mana_cost = mana_cost.replace(symbol, replacement)
    return mana_cost

def load_data(nrows):
        # Load the data from the CSV file
        data = pd.read_csv('../data/cleaned_cards.csv', nrows=nrows)
        return data

def main():
    st.title('Magic: The Gathering:')
    st.subheader('Exploring Card Data Over 30+ years of game design')

    data = load_data(25539)
    
    data['manaCost'] = data['manaCost'].apply(replace_mana_symbols)

    gameplay_data = data[['name', 'manaCost', 'type', 'text', 'power', 'toughness', 'printings']]

    st.subheader('The Basics')
    st.write(gameplay_data)
    
    most_printed(data)
    
    mono_color_distribution(data)
    
    multi_color_distribution(data)

if __name__ == "__main__":
    main()