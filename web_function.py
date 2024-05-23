import streamlit as st
import pandas as pd
import numpy as np

def load_data(file_path, index_col=None):
    # index_col akan diabaikan jika None
    df = pd.read_csv(file_path, index_col=index_col)
    return df
    
# Initialize forecast_df as an empty DataFrame
forecast_df = pd.DataFrame()

def set_forecast_data(df):
    global forecast_df
    forecast_df = df.copy()

def get_forecast_data():
    global forecast_df
    return forecast_df.copy()