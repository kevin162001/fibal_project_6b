import streamlit as st
from streamlit_option_menu import option_menu

import home, eda, forecast, about

st.set_page_config(
    page_title="Dashboard",
    layout="wide"
)
    
class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # Sidebar
        with st.sidebar:        
            app = option_menu(
                menu_title='Dashboard',
                options=['Home','Exploratory Data Analysis','Forecast','About'],
                icons=['house-fill','bi-thermometer-sun','bi-thermometer-snow','info-circle-fill'],
                menu_icon='bi-cast',
                default_index=0,
                styles={
                        "container": {"padding": "5!important","background-color":'#A2B5BF'},
                        "icon": {"color": "white", "font-size": "23px"}, 
                        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "gray"},
                        "nav-link-selected": {"background-color": "green"},}
                )

        # Menu
        if app == "Home":
            home.app()
        if app == "Exploratory Data Analysis":
            eda.app()    
        if app == "Forecast":
            forecast.app()        
        if app == 'About':
            about.app()     
             
          
             
    run()            