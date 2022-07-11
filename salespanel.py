from itertools import count
import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as py
import plotly.graph_objects as go
from streamlit_option_menu import option_menu


st.set_page_config(page_title="Moduspace Dashboard",
                   page_icon=":bar_chart:",
                   layout="wide"
)

selected = option_menu(
    menu_title=None,
    options=["Home", "Projects","Contact"],
    icons=["house", "book", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    )

if selected == "Home":
    st.title(f"You have selected {selected}")
if selected == "Projects":
    st.title(f"You have selected {selected}")
if selected == "Contact":
    st.title(f"You have selected {selected}")


df = pd.read_csv("Jan.csv")

st.sidebar.header("Please filter here:")
country = st.sidebar.multiselect(
    "Select a Country:",
    options=df["Country"].unique(),
    default=df["Country"].unique(),
)

date = st.sidebar.multiselect(
    "Select a Month:",
    options=df["Date"].unique(),
    default=df["Date"].unique(),
)

status = st.sidebar.multiselect(
    "Select a Status:",
    options=df["Status"].unique(),
    default=df["Status"].unique(),
)

df_selection = df.query(
    "Country == @country & Date == @date & Status == @status"
    
)

# ----- Main page ------


st.title(":bar_chart: MODUSPACE Dashboard")
st.markdown("###")

# TOP KPI's

sgd_currency = 1
day = 30

total_sales = int(df_selection["Total"].sum())
average_sales_by_transaction = round(df_selection["Total"].mean(),2)
average_sales_by_day = df_selection["Date"]

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total Sales")
    st.subheader(f"SGD $ {round(total_sales):,}"

)

with middle_column:
    st.subheader("Average Sales per Day")
    st.subheader(f"SGD $ {round(total_sales / day):,}"

)

with right_column:
    st.subheader("Average Sales per transaction")
    st.subheader(f"SGD $ {round(average_sales_by_transaction):,}"

)

st.markdown("----")

# sales by models

sales_by_product_line = (
    df_selection.groupby(by=["Model"]).sum().sort_values(by="Total")
)

fig_product_sales = px.bar(
    sales_by_product_line,
    x="Total",
    y=sales_by_product_line.index,
    orientation="h",
    title="<b>Sale by Product Model</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
    template="plotly_white",

)

sales_by_country = (
    df_selection.groupby(by=["Country"]).sum().sort_values(by="Total")
)


fig_product_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False,))

)   

fig_country_sales = px.bar(
    sales_by_country,
    x="Total",
    y=sales_by_country.index,
    orientation="h",
    title="<b>Sale by Country</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_country),
    template="plotly_white",

)


fig_country_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False,))

)

st.plotly_chart(fig_product_sales, use_container_width=True)
st.markdown("---")
st.plotly_chart(fig_country_sales, use_container_width=True)

with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("This is done by Jack Sim")
        st.title("This is a sales report")
        st.write("[Link to Sales Report >](https://books.zoho.com/app/675823659#/reports/salesorderdetails?filter_by=PreviousMonth&from_date=2022-06-01&order_substatus=&select_columns=%5B%7B%22field%22%3A%22current_sub_status%22%2C%22group%22%3A%22salesorder%22%7D%2C%7B%22field%22%3A%22date%22%2C%22group%22%3A%22salesorder%22%7D%2C%7B%22field%22%3A%22shipment_date%22%2C%22group%22%3A%22salesorder%22%7D%2C%7B%22field%22%3A%22salesorder_number%22%2C%22group%22%3A%22salesorder%22%7D%2C%7B%22field%22%3A%22customer_name%22%2C%22group%22%3A%22salesorder%22%7D%2C%7B%22field%22%3A%22bcy_total%22%2C%22group%22%3A%22salesorder%22%7D%2C%7B%22field%22%3A%22billing_country%22%2C%22group%22%3A%22salesorder%22%7D%2C%7B%22field%22%3A%22payment_terms%22%2C%22group%22%3A%22contact%22%7D%5D&status_filter=draft%2Cpending%2Copen%2Cclosed%2Cpartially_invoiced%2Cinvoiced%2Cnot_invoiced&to_date=2022-06-30)")

    with right_column:
        st.subheader("FUCK YOU")
        st.write("testtest")






















