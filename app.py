import streamlit as st
import yfinance as yf

st.title("Stock Market Dashboard")

ticker = st.text_input("Enter Stock Ticker (e.g., AAPL):", "AAPL")
data = yf.download(ticker, period="1mo", interval="1d")

if not data.empty:
    st.write(f"Showing data for {ticker}")
    st.line_chart(data['Close'])
else:
    st.write("Ticker not found.")