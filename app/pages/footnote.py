import streamlit as st
from PIL import Image

def showHeader():
    imageA = Image.open(r"app/images/mdinovarelogo.png")
    st.image(imageA)

def showFooter():
    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}     
            footer:after {
            content:'© 2022 MDI Novare. 9/F MDi Corporate Center, 39th Street, cor. 10th Ave., Taguig, Metro Manila, Philippines, 1634.'; 
            visibility: visible;
            display: block;
            position: relative;
            padding: 5px;
            top: 2px;
            }
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
