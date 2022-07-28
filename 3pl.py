from itertools import count
import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as py
import plotly.graph_objects as go
from streamlit_option_menu import option_menu


uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
     bytes_data = uploaded_file.read()
     st.write("filename:", uploaded_file.name)
     st.write(bytes_data)