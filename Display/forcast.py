
import streamlit as st
import yfinance as yf
from datetime import date
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go
import pandas as pd




class PreditionCharts():
    def __init__(self):
        pass
    def display():
        # Sets a five year time period for stock data
        start = "2018-01-01"
        today = date.today()
        

        #Creates input box defaulting to Apple ticker
        selected_stock = st.sidebar.text_input("Select a ticker for predition", value="AAPL")

        st.title(f"Stock Prediction Charts {selected_stock}📈")

        #creates slider widget in the sidebar
        n_years = st.sidebar.slider("Years of predition:", 1, 4)
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

        st.subheader(f"{selected_stock} 5 Year Dataframe")
        st.write(data)

        #Plots the data from dataframe
        def plot_raw_data():
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=data["Date"], y=data["Open"], name='stock_open'))
            fig.add_trace(go.Scatter(x=data["Date"], y=data["Close"], name='stock_close'))
            fig.layout.update(title_text=f"{selected_stock} 5y Ticker Data", xaxis_rangeslider_visible=True)
            st.plotly_chart(fig)

        #Calls the plot_raw_data method above
        plot_raw_data()

        #Method to create predition charts
        def plot_predictions():
            
            #prepars data to be modeled for Prophet
            df_train = data[['Date', 'Close']]
            df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

            #creates instance of prophet and creates a predictive dataframe
            m = Prophet()
            m.fit(df_train)
            future = m.make_future_dataframe(periods=period)
            
            st.subheader(f"{selected_stock} Prediction Data")
            forcast = m.predict(future)

            #writes the forcasted Dataframe
            st.write(forcast)

            #Plots the predition chart and displays
            fig1 = plot_plotly(m, forcast)
            fig1.update_layout(title=f"{selected_stock} Predition Chart", 
                        xaxis_title="Date",
                        yaxis_title="Price",
                        xaxis_rangeslider_visible=True,
                            )
            st.plotly_chart(fig1)


            # displays the forcast components to the page 
            st.write("forcast Components")
            fig2 = m.plot_components(forcast)
            st.write(fig2)
        
        #Calls the plot prediction method above
        plot_predictions()
