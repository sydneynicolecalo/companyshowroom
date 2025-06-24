import streamlit as st
from PIL import Image

from streamlit_option_menu import option_menu

from pages.home import home
from pages.aboutus import aboutus
from pages.signup import signin
from pages.contact_us import contact_us
from pages.showroom import showroom
from pages.app_data_profiling import data_profiling
from pages.app_fbprophet import fbprophet
from pages.app_churn import churn_app
from pages.app_sentiment import app_sentiment
from pages.da_showroom import da_showroom
from pages.app_anomaly import anomaly_app
# from pages.app_accuweather import accuweather
# from pages.app_datafeeds import datafeeds
# from pages.app_hr import hrdashboard
from pages.app_sample import sampledashboard
from pages.customerjourney import customerjourneydashboard
from pages.app_crime import web_application
from pages.app_image2blog import image_content
from pages.app_contentgenius import content_generation
from pages.database import database

class Sidebar:
    header = st.sidebar.empty()
    sidebar = st.sidebar.empty()
    logged_user = st.sidebar.empty()

    def __init__(self):
        self.selected = "Home"

        self.menu_options = {
            "Home": {"icon": "house", "function": home},
            "About Us": {"icon": "info-circle", "function": aboutus},
            "Contact Us": {"icon": "envelope", "function": contact_us},
            "Sign In": {"icon": "list-task", "function": signin},
            "Data Science Showroom": {"icon": "house", "function": showroom},
            "Crime Detection": {"icon": "caret-right-fill", "function": web_application},
            "Image2Blog": {"icon": "caret-right-fill", "function": image_content},
            "ContentGenius": {"icon": "caret-right-fill", "function": content_generation},           
            "Data Profiling": {"icon": "caret-right-fill", "function": data_profiling},
            "Time Series Forecast": {"icon": "caret-right-fill", "function": fbprophet},
            "Churn Prediction": {"icon": "caret-right-fill", "function": churn_app},
            "Anomaly Detection": {"icon": "caret-right-fill", "function": anomaly_app},
            "Sentiment Analysis": {"icon": "caret-right-fill", "function": app_sentiment},
            "Data Analytics Showroom": {"icon": "house", "function": da_showroom},
            #"Accuweather": {"icon": "caret-right-fill", "function": accuweather},
            #"Data Feeds": {"icon": "caret-right-fill", "function": datafeeds},
            #"HR Dashboard": {"icon": "caret-right-fill", "function": hrdashboard},
            "Sample Dashboards": {"icon": "caret-right-fill", "function": sampledashboard},
            "Customer Journey Dashboard": {"icon": "caret-right-fill", "function": customerjourneydashboard},
            "Database": {"icon": "info-circle", "function": database},
        }

        self.auth_options = [
            "Data Science Showroom",
            "Crime Detection",
            "Image2Blog",
            "ContentGenius",
            "Churn Prediction",
            "Anomaly Detection",
            "Sentiment Analysis",
            "Time Series Forecast",
            "Data Analytics Showroom",
            "Customer Journey Dashboard",
            "Sample Dashboards",
            "Contact Us"
        ]
        self.public_options = [
            "Sign In",
            "Home",
            "Crime Detection",
            "Image2Blog",
            "ContentGenius",
            "Churn Prediction",
            "Anomaly Detection",
            "Sentiment Analysis",
            "Time Series Forecast",
            "Sentiment Analysis",
            "Data Analytics Showroom",
            "Customer Journey Dashboard",
            "Sample Dashboards",
            "Contact Us"
        ]

    # def web_application(self):        
    # #     # web_design = WebDesign()      
    # #     # web_design.web_application()
    #      web_application()

    def render(self):
        self.header.empty()
        with self.header.container():
            imageA = Image.open(r"app/images/mdinovarelogo.png")
            st.image(imageA)
            st.write("")


        #self.sidebar.empty()
        if st.session_state.authenticated is True:
            with self.logged_user:
                st.write(f"Logged in as {st.session_state.username}")
            sidebar_options = self.auth_options
        else:
            sidebar_options = self.public_options

        sidebar_icons = [self.menu_options[i]["icon"] for i in sidebar_options]

        with self.sidebar:
            self.selected = option_menu(
                None,
                sidebar_options,
                icons=sidebar_icons,
                menu_icon="cast",
                default_index=0,
                orientation="vertical",
                styles={
                    "container": {
                        "padding": "0!important",
                        "background-color": "#FFFFFF",
                    },
                    "icon": {"color": "orange", "font-size": "15px"},
                    "nav-link": {
                        "font-size": "15px",
                        "text-align": "left",
                        "margin": "0px",
                        "--hover-color": "#eee",
                    },
                    "nav-link-selected": {"background-color": "#006FB6"},
                },
            )

    def clear(self):
        self.header.empty()
        self.sidebar.empty()
        self.logged_user.empty()
        # Hide the entire sidebar if possible
