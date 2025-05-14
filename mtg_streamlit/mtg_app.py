import streamlit as st
import pandas as pd
import numpy as np
from components.most_printed import most_printed
from components.mono_color_distribution import mono_color_distribution
from components.multi_color_distribution import multi_color_distribution
from components.creature_type_count import creature_type_count
from components.set_mapping import mtg_set_mapping
from components.card_type_count import card_type_count

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
    '{T}': '🔄',
}
# Can replace unicode symbols with their respective png images later as 
# there are special hybrid symbols that haven't been added yet


def replace_mana_symbols(mana_cost):
    if pd.isnull(mana_cost):
        return mana_cost
    for symbol, replacement in mana_symbol_mapping.items():
        mana_cost = mana_cost.replace(symbol, replacement)
    return mana_cost

def replace_mana_symbols_in_text(text):
    if pd.isnull(text):
        return text
    for symbol, replacement in mana_symbol_mapping.items():
        text = text.replace(symbol, replacement)
    return text

def load_data(nrows):
    data = pd.read_csv('../data/cleaned_cards.csv', nrows=nrows)
    return data

def main():
    st.title('Magic: The Gathering:')
    st.subheader('Exploring Card Data Over 30+ years of game design')

    data = load_data(25539)
    
    # Replace mana symbols in the manaCost and text columns
    data['manaCost'] = data['manaCost'].apply(replace_mana_symbols)
    data['text'] = data['text'].apply(replace_mana_symbols_in_text)


    # Add a filter for set names mapped from set codes
    st.sidebar.subheader('Filter by Set Name')
    unique_set_codes = sorted(set(','.join(data['printings'].dropna().str.strip()).split(','))) 
    set_name_mapping = {code.strip(): mtg_set_mapping.get(code.strip(), f"unknown small set: ({code.strip()})") for code in unique_set_codes}
    set_names = ["All Sets"] + sorted(set_name_mapping.values()) 
    selected_set_name = st.sidebar.selectbox('Select a Set Name', set_names)

    # Get the set code corresponding to the selected set name
    selected_set_code = next((code for code, name in set_name_mapping.items() if name == selected_set_name), None)

    if selected_set_name == "All Sets":
        filtered_data = data 
    else:
        selected_set_code = next((code for code, name in set_name_mapping.items() if name == selected_set_name), None)
        filtered_data = data[data['printings'].str.contains(selected_set_code, na=False)] if selected_set_code else data

    gameplay_data = filtered_data[['name', 'manaCost', 'type', 'text', 'power', 'toughness']]
    
    
    st.subheader('The Basics')
    st.write("Number of cards in the selected set: ", len(filtered_data))
    st.write(gameplay_data)

    # most_printed(filtered_data)
    mono_color_distribution(filtered_data)
    multi_color_distribution(filtered_data)
    card_type_count(filtered_data)
    creature_type_count(filtered_data)

if __name__ == "__main__":
    main()