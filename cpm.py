import pandas as pd
import numpy as np
import streamlit as st
import warnings
import sys
# import plotly.figure_factory as ff


warnings.filterwarnings("ignore")


st.sidebar.title("Main Menu")
formside = st.sidebar.form("side_form")
choose = formside.radio("Choose which data you want to see",["CPM","OS data"], index=None)
formside.form_submit_button("Submit")

if (choose == "CPM"):
    st.title("OS data and CPM")
    st.image('cpm.png', caption='CPM')

elif (choose == "OS data"):
    st.title("OS data")
    st.header("capacitance")

    df = pd.read_csv("Capacitance Data")
    st.dataframe(df)
    
