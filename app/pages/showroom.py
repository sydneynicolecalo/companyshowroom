from pages import ui

import streamlit as st
from pages.footnote import *

def showroom():
    showHeader()
    st.title("Data Science Showroom")
    st.write(
        "Explore our different Data Science tools from Data Wrangling to Machine learning. "
        "Use them as leverage to gain competitive advantage and achieve cost efficiency. "
        "Try and experience them yourself."
    )

    showFooter()
