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

    st.header("Capacitance data")
    df = pd.read_csv("Capacitance_Data.csv")
    st.dataframe(df)
   
    #permittivity = pd.read_csv("Permittivity.csv")
    df2 = pd.read_csv("Capacitance1.csv")
    #st.dataframe(df2)

    freq_slider_start = st.slider("Slider for Start Frequency", 50, 100000, 50)
    freq_slider_end = st.slider("Slider for End Frequency", freq_slider_start, 100000, 100000)
    filtered_capacitance = df2.loc[(df2['Frequency'] >= freq_slider_start) & (df2['Frequency'] <= freq_slider_end)]
            
    st.header("Capacitance(Cp)")
    st.line_chart(filtered_capacitance, x="Frequency", use_container_width=True)
    
