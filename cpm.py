import pandas as pd
import numpy as np
import streamlit as st
import warnings
import sys
# import plotly.figure_factory as ff


warnings.filterwarnings("ignore")


# st.image("9gs.jpg")
# st.write("Please click the arrow '>' on the top left to proceed")
st.write("Click '>' on top left to see more ")
st.sidebar.image("9gs.jpg")
st.sidebar.title("Main Menu")
st.sidebar.write('<div style="position: fixed; bottom: 10px; left: 10px; font-size: 10px;">Copyrights to 9GS, developed by AFF </div>', unsafe_allow_html=True)

formside = st.sidebar.form("side_form")
choose = formside.radio("Choose which data you want to see",["CPM","OS data"], index=None)
formside.form_submit_button("Submit")

if (choose == "CPM"):
    st.title("CPM")
    st.image('cpmnnew.png', caption='CPM')
    st.image('cpmnew.png', caption='CPM')

elif (choose == "OS data"):
    st.title("OS data")

    # st.header("Capacitance data")
    df = pd.read_csv("Capacitance Data.csv")
    # st.dataframe(df)
   
    #permittivity = pd.read_csv("Permittivity.csv")
    df2 = pd.read_csv("Capacitance1.csv")
    #st.dataframe(df2)

    freq_slider_start = st.slider("Slider for Start Frequency", 50, 100000, 50)
    freq_slider_end = st.slider("Slider for End Frequency", freq_slider_start, 100000, 100000)
    
    #filtered_capacitance = df2.loc[(df2['Frequency'] >= freq_slider_start) & (df2['Frequency'] <= freq_slider_end)]
            
    #st.header("Capacitance(Cp)")
    # st.line_chart(filtered_capacitance, x="Frequency", use_container_width=True)


    # st.header("Inductance data")
    df3 = pd.read_csv("Inductance Data.csv")
    # st.dataframe(df3)
   
    #permittivity = pd.read_csv("Permittivity.csv")
    df4 = pd.read_csv("Inductance1.csv")
    #st.dataframe(df2)

    # filtered_Inductance = df4.loc[(df4['Frequency'] >= freq_slider_start) & (df4['Frequency'] <= freq_slider_end)]
    # st.line_chart(filtered_Inductance, x="Frequency", use_container_width=True)



    # st.header("Resistance data")
    df5 = pd.read_csv("Resistance Data.csv")
    # st.dataframe(df5)
   

    df6 = pd.read_csv("Resistance1.csv")


    # filtered_Resistance = df6.loc[(df6['Frequency'] >= freq_slider_start) & (df6['Frequency'] <= freq_slider_end)]
    # st.line_chart(filtered_Resistance, x="Frequency", use_container_width=True)

#..........................................................................................................................................................

    filtered_capacitance = df2.loc[(df2['Frequency'] >= freq_slider_start) & (df2['Frequency'] <= freq_slider_end)]
    label = ":blue[Chart for Capacitance] " 

    filtered_Inductance = df4.loc[(df4['Frequency'] >= freq_slider_start) & (df4['Frequency'] <= freq_slider_end)]
    label1 = ":blue[Chart for Inductance] " 

    filtered_Resistance = df6.loc[(df6['Frequency'] >= freq_slider_start) & (df6['Frequency'] <= freq_slider_end)]
    label2 = ":blue[Chart for Resistance] " 



    
    with st.expander(label):
        st.line_chart(filtered_capacitance, x="Frequency", use_container_width=True)
        st.write("capacitance vs frequency whole data")
        st.dataframe(df)
    with st.expander(label1):
        st.line_chart(filtered_Inductance, x="Frequency", use_container_width=True)
        st.write("Inductance vs frequency whole data")
        st.dataframe(df3)
    with st.expander(label2):
        st.line_chart(filtered_Resistance, x="Frequency", use_container_width=True)
        st.write("Resistance vs frequency whole data")
        st.dataframe(df5)
