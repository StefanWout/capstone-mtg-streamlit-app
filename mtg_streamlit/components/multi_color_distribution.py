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
        'W': '⚪',  
        'U': '🔵', 
        'B': '⚫',  
        'R': '🔴',  
        'G': '🟢',
    }
    # Replace the colorIdentity values with their corresponding symbols#
    color_counts_df['colorIdentity'] = color_counts_df['colorIdentity'].apply(
    lambda x: ''.join(color_mapping.get(char, char) for char in x)
)
   
    # Sort the DataFrame by count in descending order
    color_counts_df = color_counts_df.sort_values(by='count', ascending=False)

    if color_counts_df.empty:
        st.subheader('Multi Color Distribution Across Selected Set')
        st.write("There are no multi-colored cards in this set.")
    else:
        chart = alt.Chart(color_counts_df).mark_bar().encode(
            x=alt.X(
            'colorIdentity',
            sort='-y',
            title='Color Identity',
            axis=alt.Axis(labelAngle=90, labelLimit=500)  # Ensure all labels are fully displayed
        ),
            y=alt.Y('count', title='Count'),
            tooltip=['colorIdentity', 'count']
        ).properties(
            width=600,
            height=600
        )

        st.subheader('Multi Color Distribution Across Selected Set')
        st.altair_chart(chart, use_container_width=True)