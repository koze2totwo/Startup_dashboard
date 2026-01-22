import streamlit as st
import pandas as pd
 
#import
df = pd.read_csv("startup_cleaned.csv")

#streamlit_main_begin
st.sidebar.title("Startup Funding Analysis")

op = st.sidebar.selectbox("Select",['Overall analysis','Startup','Investor'])

if op == 'Overall analysis':
  
    st.title("Overall analysis")
elif op == 'Startup':
    st.sidebar.selectbox('Select startup',set(df['startup'].str.split(',').sum()))
    btn1=st.sidebar.button("Find startup details")
    st.title("Startup overview")

if op == 'Investor':
    st.sidebar.selectbox('Select investor',sorted(set(df['investors'].str.split(',').sum())))
    btn1=st.sidebar.button("Find Investor details")
    st.title("Investor overview")