import streamlit as st
import pandas as pd
from web_function import load_data, set_forecast_data
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import joblib

def app(): 
    st.title("Forecast Curah Hujan")
    st.image("C:/Users/kevin/OneDrive/Pictures/newplot.png", caption="cuaca ekstrem", use_column_width=True)
