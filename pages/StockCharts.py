
import streamlit as st
import yfinance as yf
from plotly import graph_objs as go
import pandas as pd

st.set_page_config(
    page_title="Stock Charts",
    page_icon="📊",
)


selected_stock = st.text_input("Select a ticker for predition", value="AAPL")

start = st.date_input("Start Date", value=pd.to_datetime("2018-01-01"))
end = st.date_input("End Date", value=pd.to_datetime("today"))

@st.cache
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