import streamlit as st
import yfinance as yf
import requests
import Token as tk
from plotly import graph_objs as go


#Writes the Sidebar label
st.sidebar.write("Filters")

#page options
options = ("Prediction Charts", "Stock Chart", "News Articles" )

#page selector
option = st.sidebar.selectbox("select a Dashboard", options=options)

#Writes the option name as a header for each page
st.header(option)

#Determines the logic that will be used depending on the page that is selected
if option == "Prediction Chart":
    st.subheader("Locgic For Prediction charts")
    pass

if option == "Stock data":
    st.subheader("Logic For Stock Data Chart")
    pass

if option == "News Articles":
    #st.subheader("Logic for Twitter threads")

    symbol = st.sidebar.text_input("Symbol", value="AAPL", max_chars=10)

    key = "7cf017f18b3a46d5bd97397bc0f00290"

    r = requests.get(f"https://newsapi.org/v2/everything?q={symbol}&apiKey={tk.NEWS_KEY}")
    
    news_data = r.json()

    if r.status_code == 200:
        articles = news_data.get("articles", [])
        for article in articles:
            st.write("Source:", article["source"]["name"])
            st.write("Title:", article["title"])
            st.write("Description:", article["description"])
            st.write("URL:", article["url"])
            st.write("Published At:", article["publishedAt"])
            st.write("")
    else:
        st.write(f"Error: {r.status_code}")



  

        


   
  