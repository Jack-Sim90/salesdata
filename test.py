import pandas as pd
import streamlit as st

df = pd.read_csv("jan.csv")


st.sidebar.header("Please filter here:")
country = st.sidebar.multiselect(
    "Select a Country:",
    options=df["currency_code"].unique(),
    default=df["currency_code"].unique(),

)


print(df["currency_code"].unique())

currency_code = 