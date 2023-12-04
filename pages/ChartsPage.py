
import streamlit as st
from Display.charts import ChartData

st.set_page_config(
    page_title="Stock Charts",
    page_icon="📊",
)

chart_instance = ChartData()

chart_instance.display()
