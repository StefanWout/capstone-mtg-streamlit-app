import streamlit as st
import pandas as pd
import numpy as np

def most_printed(data):
    data['printings_count'] = data['printings'].apply(lambda x: len(str(x).split(',')) if pd.notnull(x) else 0)
    longest_printings_card = data.loc[data['printings_count'].idxmax()]


    st.subheader('The Most Printed Card in the Selected Set')
    st.write(f"Name: {longest_printings_card['name']}")
    st.write(f"text: {longest_printings_card['text']}")
    st.write(f"Number of Printings: {longest_printings_card['printings_count']}")