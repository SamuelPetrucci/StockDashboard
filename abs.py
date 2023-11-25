import streamlit as st
import requests
import yfinance as yf
import pandas as pd
from datetime import date
import streamlit as st
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go
import Token as tk



class PredictionChartPage:
    def __init__(self):
        pass

    def display(self):
            
        start = "2018-01-01"
        today = date.today()
        #.strftime("%Y-%m-%d")

        st.title("Stock Prediction")

        selected_stock = st.text_input("Select a ticker for predition", value="AAPL")

        n_years = st.slider("Years of predition:", 1, 4)
        period = n_years * 365


        @st.cache_data 
        def load_data(ticker):
            data = yf.download(ticker, start, today)
            data.reset_index(inplace=True)
            return data

        data_load_state = st.text("Loading data...")
        data = load_data(selected_stock)
        data_load_state.text("Data Loaded Succesfully!")

        st.subheader("Raw Dataframe")
        st.write(data.tail())

        def plot_raw_data():
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=data["Date"], y=data["Open"], name='stock_open'))
            fig.add_trace(go.Scatter(x=data["Date"], y=data["Close"], name='stock_close'))
            fig.layout.update(title_text="All time Ticker Data", xaxis_rangeslider_visible=True)
            st.plotly_chart(fig)

        plot_raw_data()


        df_train = data[['Date', 'Close']]
        df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

        m = Prophet()

        m.fit(df_train)
        future = m.make_future_dataframe(periods=period)

        forcast = m.predict(future)

        st.write(forcast.tail())

        fig1 = plot_plotly(m, forcast)
        st.plotly_chart(fig1)

        st.write("forcast Components")
        fig2 = m.plot_components(forcast)
        st.write(fig2)

class StockDataPage:
    def __init__(self):
        pass

    def display(self):

        selected_stock = st.text_input("Select a ticker for predition", value="AAPL")

        start = st.date_input("Start Date", value=pd.to_datetime("2018-01-01"))
        end = st.date_input("End Date", value=pd.to_datetime("today"))
        
  
        def load_data(ticker):
            data = yf.download(ticker, start=start, end=end)
            data.reset_index(inplace=True)
            return data

        data_load_state = st.text("Loading data...")
        data = load_data(selected_stock)
        data_load_state.text("Data Loaded Succesfully!")

        
        
        #Logic to plot a line graph and a Candle Stick Chart
        def plot_charts():
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=data["Date"], y=data["Open"], name='stock_open'))
            fig.add_trace(go.Scatter(x=data["Date"], y=data["Close"], name='stock_close'))
            fig.layout.update(title_text="Symbol Line Chart", xaxis_rangeslider_visible=True)
            st.plotly_chart(fig)
            
        def candle_plot():

            fig2 = go.Figure(data=[go.Candlestick(
                                    x=data["Date"],
                                    open=data["Open"],
                                    high=data["High"],
                                    low=data["Low"],
                                    close=data["Close"]
                                    )])
                                    
            
            fig2.update_layout(title=f"{selected_stock} Candlestick Chart", 
                        xaxis_title="Date",
                        yaxis_title="Stock Price",
                        xaxis_rangeslider_visible=True,
                         )
                        
    
            #Plotting figure
            st.plotly_chart(fig2)
        

        plot_charts()
        candle_plot()

        st.subheader("All Time Data")
        st.write(data)



class NewsArticlesPage:
    def __init__(self):
        pass

    def display(self):

       
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

        
