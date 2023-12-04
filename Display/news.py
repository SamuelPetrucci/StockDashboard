import requests
import streamlit as st
import tokens.Token as tk

class NewsData():
    def __init__(self):
        pass


    def display(self):
        symbol = st.sidebar.text_input("Symbol", value="AAPL", max_chars=10)

        st.write(f"# {symbol} News📰")


        #Makes a request to the API
        r = requests.get(f"https://api.marketaux.com/v1/news/all?symbols={symbol}&filter_entities=true&language=en&api_token={tk.key}")

        # Creates the json format 
        news_data = r.json()

        #Writes Key components of the Json data to the Page
        articles = news_data.get("data")
        for article in articles:
            st.write("Source:", article["source"])
            st.write("Title:", article["title"])
            st.write("Description:", article["description"])
            st.write("URL:", article["url"])
            st.write("Published At:", article["published_at"])
            st.write("")
       


