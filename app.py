import streamlit as st
import pandas as pd
 
#import
df = pd.read_csv("startup_funding.csv")

#data_cleaning
df['Investors Name']=df["Investors Name"].fillna("Undisclosed")






#streamlit_main_begin
st.sidebar.title("Startup Funding Analysis")

op = st.sidebar.selectbox("Select",['Overall analysis','Startup','Investor'])

if op == 'Overall analysis':
  
    st.title("Overall analysis")
elif op == 'Startup':
    st.sidebar.selectbox('Select startup',sorted(df['Startup Name'].unique().tolist()))
    btn1=st.sidebar.button("Find startup details")
    st.title("Startup overview")

if op == 'Investor':
    st.sidebar.selectbox('Select investor',sorted(df['Investors Name'].unique().tolist()))
    btn1=st.sidebar.button("Find Investor details")
    st.title("Investor overview")