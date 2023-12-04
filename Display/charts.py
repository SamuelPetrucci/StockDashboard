
import streamlit as st
import yfinance as yf
from plotly import graph_objs as go
import pandas as pd

class ChartData():
    def __init__(self):
        pass
    def display(self):
                
        selected_stock = st.text_input("Select a ticker for predition", value="AAPL")

        ##Create a date input box to adjust the date range for the data
        start = st.date_input("Start Date", value=pd.to_datetime("2018-01-01"))
        end = st.date_input("End Date", value=pd.to_datetime("today"))

        ##Retrives data from the yfinance API
        def load_data(ticker):
            data = yf.download(ticker, start=start, end=end)
            data.reset_index(inplace=True)
            return data
        
        ##Gives feedback on the data upload
        data_load_state = st.text("Loading data...")
        data = load_data(selected_stock)
        data_load_state.text("Data Loaded Succesfully!")



        #Logic to plot a line graph and a Candle Stick Chart
        def plot_charts():
            fig1 = go.Figure()
            fig1.add_trace(go.Scatter(x=data["Date"], y=data["Open"], name='stock_open'))
            fig1.add_trace(go.Scatter(x=data["Date"], y=data["Close"], name='stock_close'))

            fig1.update_layout(title=f"{selected_stock} Candlestick Chart", 
                        xaxis_title="Date",
                        yaxis_title="Price",
                        xaxis_rangeslider_visible=True,
                            )

            st.plotly_chart(fig1)

            
        ##Logic to plot a candlestick chart 
        def candle_plot():

            fig2 = go.Figure(data=[go.Candlestick(
                                    x=data["Date"],
                                    open=data["Open"],
                                    high=data["High"],
                                    low=data["Low"],
                                    close=data["Close"]
                                    )])
                                    
            #Writes the labes for the graph
            fig2.update_layout(title=f"{selected_stock} Candlestick Chart", 
                        xaxis_title="Date",
                        yaxis_title="Price",
                        xaxis_rangeslider_visible=True,
                            )
                        

            #Plotting figure
            st.plotly_chart(fig2)

        #makes a call to the plot methods
        plot_charts()
        candle_plot()

        #writes out the panas dataframe
        st.subheader("All Time Data")
        st.write(data)