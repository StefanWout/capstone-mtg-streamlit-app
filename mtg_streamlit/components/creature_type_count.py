import streamlit as st
import pandas as pd
import numpy as np

def creature_type_count(data):
    subtypes_series = data['subtypes'].dropna().str.split(', ').explode()
    subtype_counts = subtypes_series.value_counts().reset_index()
    subtype_counts.columns = ['Subtype', 'Count']
    st.subheader('Creature Type Count')
    st.dataframe(subtype_counts)