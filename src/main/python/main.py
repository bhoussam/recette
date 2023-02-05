import streamlit as st

from src.main.python.back.filter import distinct_values
from src.main.python.back.load_data import get_data

df = get_data()


with st.sidebar:
    st.header('Filters')
    f_theme = st.multiselect(
        label="Theme",
        options=distinct_values(df['theme'])
    )
    f_ingredients = st.multiselect(
        label="Ingredients",
        options=distinct_values(df['ingredients'])
    )

if f_theme or f_ingredients:
    filtered_df = df[
        (df["theme"].isin(f_theme)) |
        (df["ingredients"].isin(f_ingredients))
    ]
    st.dataframe(filtered_df, use_container_width=True)
else:
    st.dataframe(df, use_container_width=True)
