import streamlit as st
import yfinance as yf
import datetime


st.title(":red[Stock price] :blue[Analyzer!]")

st.header("By venkatesh.ch", divider="gray")

symbol = st.text_input("Please enter the ticker", "enter ticker")
ticker_data = yf.Ticker(symbol)

import streamlit as st

col1, col2,  = st.columns(2)

with col1:
    start_date = st.date_input("Please enter start data",datetime.date(2023,12,14))
    
with col2:
    end_Date = st.date_input("please enter end date", datetime.date(2024,12,14))

#start_date = st.date_input("Please enter start data",datetime.date(2023,12,14))
#end_Date = st.date_input("please enter end date", datetime.date(2024,12,14))

ticker_df =ticker_data.history(period="1d", start= start_date,end= end_Date)



st.write("Here is the day wise raw data!")
st.dataframe(ticker_df)

st.write("Price movement over time")
st.line_chart(ticker_df['Close'])

st.write("Volume moving overtime")
st.line_chart(ticker_df['Volume'])