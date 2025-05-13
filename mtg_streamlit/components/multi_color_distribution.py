import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

    
def multi_color_distribution(data):

    multi_color_data = data[data['colorIdentity'].apply(lambda x: isinstance(x, str) and len(x) > 1)]


    color_count = multi_color_data['colorIdentity'].value_counts()


    color_counts_df = color_count.reset_index()
    color_counts_df.columns = ['colorIdentity', 'count']
    
    color_mapping = {
        'G': 'rgb(0, 115, 62)',
        'U': 'rgb(14, 104, 171)',
        'R': 'rgb(211, 32, 42)',
        'W': 'rgb(249, 250, 244)',
        'B': 'rgb(21, 11, 0)'
    }

    # Sort the DataFrame by count in descending order
    color_counts_df = color_counts_df.sort_values(by='count', ascending=False)

    # Create a bar chart using Altair
    chart = alt.Chart(color_counts_df).mark_bar().encode(
        x=alt.X('colorIdentity', sort='-y', title='Color Identity'),
        y=alt.Y('count', title='Count'),
        tooltip=['colorIdentity', 'count']
    ).properties(
        width=600,
        height=400
    )

    st.subheader('Multi Color Distribution Across All Sets')
    st.altair_chart(chart, use_container_width=True)