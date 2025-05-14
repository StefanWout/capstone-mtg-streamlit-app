import streamlit as st
import pandas as pd
import numpy as np

def card_type_count(data):
    types_series = data['types'].dropna().str.split(', ').explode()
    type_counts = types_series.value_counts().reset_index()
    type_counts.columns = ['Card Type', 'Count']
    st.subheader('Card Type Count')
    st.bar_chart(type_counts.set_index('Card Type')['Count'])