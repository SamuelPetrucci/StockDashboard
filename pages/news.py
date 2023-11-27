import requests
import streamlit as st
import Token as tk

st.set_page_config(
    page_title="News",
    page_icon="📰",
)


symbol = st.sidebar.text_input("Symbol", value="AAPL", max_chars=10)

key = tk.NEWS_KEY
r = requests.get(f"https://newsapi.org/v2/everything?q={symbol}&apiKey={key}")

news_data = r.json()

try:
    articles = news_data.get("articles", [])
    for article in articles:
        st.write("Source:", article["source"]["name"])
        st.write("Title:", article["title"])
        st.write("Description:", article["description"])
        st.write("URL:", article["url"])
        st.write("Published At:", article["publishedAt"])
        st.write("")
except:
    st.write(f"Error: {r.status_code}")


