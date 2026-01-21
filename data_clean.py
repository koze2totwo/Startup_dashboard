import pandas as pd
import numpy as np 


#fn convert us to inr
def to_inr(dollar):
    inr = dollar * 82.5
    return inr/10000000


#import
df = pd.read_csv("startup_funding.csv")

#data_cleaning
df['Investors Name']=df["Investors Name"].fillna("Undisclosed")
#drop data with many missing data
df.drop(columns=['Remarks'],inplace=True)
#set index
df.set_index('Sr No',inplace=True)
#rename columns for better understanding
df.rename(columns={
    'Date dd/mm/yyyy':'date',
    'Startup Name':'startup',
    'Industry Vertical':'vertical',
    'SubVertical':'subvertical',
    'City  Location':'city',
    'Investors Name':'investors',
    'InvestmentnType':'round',
    'Amount in USD':'amount'    
    
},inplace=True)

#fill Nan
df['amount'] = df['amount'].fillna('0')

#replace string to integer str to convert to int
df['amount'] = df['amount'].str.replace(',','')
df['amount'] = df['amount'].str.replace('undisclosed','0')
df['amount'] = df['amount'].str.replace('unknown','0')
df['amount'] = df['amount'].str.replace('Undisclosed','0')
#get int values only
df = df[df['amount'].str.isdigit()]
#convert to float
df['amount'] = df['amount'].astype('float')

#usd to inr
df['amount'] = df['amount'].apply(to_inr)
#change str date to datetime type using coerce to ignore invalid strings, use formate make pandas convert date properly
df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y',errors='coerce')
print(df.shape)

#drop na rows
df = df.dropna(subset=['date','startup','vertical','city','investors','round','amount'])

#export file 
df.to_csv('startup_cleaned.csv',index=False)
