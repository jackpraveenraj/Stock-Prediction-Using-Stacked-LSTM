import streamlit as st
from PIL import Image

st.write("""
# Stock Price Predictor Using LSTM:
Stock values is very valuable but extremely hard to predict correctly for any human being on their own. This project seeks to solve the problem of Stock Prices Prediction by utilizes Deep Learning models, Long-Short Term Memory (LSTM) Neural Network algorithm, to predict future stock values.\n
""")

st.sidebar.write("""
# Stock Price Prediction:
Predict Stock Price For The Next 30 Days
""")
option = st.sidebar.selectbox("Select Dataset",("AAPL","TATACONSUM"))


prof_image = Image.open('Created By Picture.png')
st.sidebar.image(prof_image)


st.write("""
# Dataset Sample:
Taken From Quandl\n
""")

import pandas as pd
df=pd.read_csv('AAPL.csv')
st.write(df.head())

st.write("""
# Prediction Graph:
Predict Values For The Next 30 Days\n
""")

graph_image = Image.open('30daypredict.png')
st.image(graph_image,width=500)