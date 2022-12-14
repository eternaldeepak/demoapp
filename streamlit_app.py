import pandas as pd
import streamlit as st
df = pd.read_csv(r"NIFTYdaily.csv", parse_dates=['Date'])
df.set_index('Date')
st.line_chart(df[['Close', 'Open']])