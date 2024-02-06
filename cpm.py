import pandas as pd
import numpy as np
import streamlit as st
import warnings
import sys
# import plotly.figure_factory as ff


warnings.filterwarnings("ignore")


st.sidebar.image("9gs.jpg")
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

    df = pd.read_csv("Capacitance Data.csv")
    st.dataframe(df)

    #permittivity = pd.read_csv("Permittivity.csv")
    df2 = pd.read_csv("Capacitance1.csv")
    #st.dataframe(df2)
    
    # Rename the columns
    # new_column_names = {
    #     "G0": "GB4",
    #     "G1": "OS23-0002",
    #     "G2": "OS23-0003",
    #     "G3": "OS23-0004",
    #     "G4": "OS23-0005-110",
    #     "G5": "OS23-0005-110 (S)",
    #     "G6": "OS23-0005-120",
    #     "G7": "OS23-0005-120(S)",
    #     "G8": "OS24-0005-020",
    #     "G9": "OS24-0005-040",
    #     "G10": "OS24-0005-050",
    #     "G11": "OS24-0005-060",
    # }

    st.header("Capacitance(Cp)")
    st.line_chart(df2, x="Frequency", use_container_width=True)
    
