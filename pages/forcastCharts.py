
import streamlit as st
import yfinance as yf
from datetime import date
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go
import pandas as pd

st.set_page_config(
    page_title="Stock Price Forcast",
    page_icon="📈",
)

start = "2018-01-01"
today = date.today()
#.strftime("%Y-%m-%d")

st.title("Stock Prediction Charts")

#Creates input box defaulting to Apple ticker
selected_stock = st.text_input("Select a ticker for predition", value="AAPL")

#creates slider widget 
n_years = st.slider("Years of predition:", 1, 4)
period = n_years * 365

#Loads pandas dataframe from yahoo finance API
@st.cache_data 
def load_data(ticker):
    data = yf.download(ticker, start, today)
    data.reset_index(inplace=True)
    return data

data_loading_state = st.text("Loading data...")
data = load_data(selected_stock)
data_loading_state.text("Data Loaded Succesfully!")

st.subheader("Dataframe")
st.write(data.tail())

#Plots the data from dataframe
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
