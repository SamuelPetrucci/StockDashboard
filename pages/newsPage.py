from Display.news import NewsData
import streamlit as st


st.set_page_config(
    page_title="News",
    page_icon="📰",
)


# Create an instance of NewsData
news_instance = NewsData()

# Call the display method
news_instance.display()

