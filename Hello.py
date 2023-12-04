import streamlit as st


st.set_page_config(
    page_title="Welcome to My stock Dashboard",
    page_icon="👋",
)


st.write("# Welcome to My Stock Dashboard👋")

st.markdown(
    """
    I built this app to monitor stock data and predictions. 
    It features three main pages:
    - **Stock Charts Page:** Visualize historical stock data using Plotly.
    - **Prediction Charts Page:** Explore stock predictions using Facebook Prophet.
    - **Stock Article Page:** Stay informed with the latest stock news.

    The app utilizes Streamlit for the frontend, yfinance for market data, 
    fbprophet for predictions, and Plotly for data visualization.
    """

    """
    ## Future Plans 🚀

    In the future, I have exciting plans to enhance this Stock Dashboard:
    
    - **Live Trading Bot:** Integrate a stock trading bot that makes real-time trades based on a machine learning model.
    
    - **Machine Learning Model:** Develop and incorporate an advanced machine learning model for predicting market trends and optimizing trading strategies.
    """
)