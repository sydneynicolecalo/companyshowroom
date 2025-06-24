from pages import ui
from PIL import Image

import streamlit as st
import itertools
from pages.footnote import *

def category(name, description=None):
    ui.colored_header(name, ui.color("novare-lightblue"), description)
    # st.write("")


def app(name, description, image, link):
    imagePIL = Image.open(image)
    st.image(imagePIL)
    st.markdown(f"##### {name}")
    st.caption(f"{description}")
    st.write("")

def home():
    showHeader()
    showFooter()
    st.title("Data Science Showroom")
    st.write(
        "Explore our different Data Science tools from Data Wrangling to Machine learning. "
        "Use them as leverage to gain competitive advantage and achieve cost efficiency. "
    )

    st.write("[Sign up]()", " now to gain trial access! ")

    category("Exploratory Data Analysis")

    col1, col2, col3 = st.columns(3)
    with col1:
        app(
            "Data Profiling",
            "Dissect the data using pandas data profiling.",
            r"app/images/dataprofiling.gif",
            "",
        )

    with col2:
        st.empty()

    with col3:
        st.empty()

    category("Machine Learning")
    col1, col2, col3 = st.columns(3)
    with col1:
        app(
            "Time Series Forecasting",
            "Forecast time series data using FB Prophet.",
            r"app/images/fbprophet.png",
            "https://leojulongbayannovare-time-series-prophet-fbprophet-zq24ee.streamlitapp.com/",
        )
    with col2:
        app(
            "Churn Prevention",
            "A speech-to-text transcription app. Upload a .wav file, transcribe it, download it!",
            r"app/images/churnprevention.png",
            "https://share.streamlit.io/streamlit/example-app-speech-to-text-transcription/main",
        )
    with col3:
        app(
            "Sentiment Analysis",
            "A text analysis dashboard. Type in a term to view the corresponding Twitter sentiment",
            r"app/images/SentimentAnalysis.png",
            "https://share.streamlit.io/streamlit/example-app-twitter-analyzer/main",
        )

    st.markdown("""
        
    """,unsafe_allow_html=True)
    # st.header("About Us")
    # gallery_link = "https://www.novare.com.hk/about-us/"
    # st.write("Developed by Data Science and Analytics Team.")
    # st.write("")
    # st.write("")
    # st.write("Copyright © Novare. All rights reserved.")


