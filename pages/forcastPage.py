
import streamlit as st
from Display.forcast import PreditionCharts

st.set_page_config(
    page_title="Dashboard",
    page_icon="📈",
)

predition_intstance = PreditionCharts

predition_intstance.display()

