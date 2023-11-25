import dashboard
import streamlit as st

# Writes the Sidebar label
st.sidebar.write("Filters")

# Page options
options = ("Prediction Chart", "Stock data", "News Articles",)

# Page selector
option = st.sidebar.selectbox("Select a Dashboard", options=options)

# Writes the option name as a header for each page
st.header(option)

# Determines the logic that will be used depending on the page that is selected
if option == "Prediction Chart":
    prediction_chart_page = abs.PredictionChartPage()
    prediction_chart_page.display()

if option == "Stock data":
    stock_data_page = abs.StockDataPage()
    stock_data_page.display()

if option == "News Articles":
    news_articles_page = abs.NewsArticlesPage()
    news_articles_page.display()

