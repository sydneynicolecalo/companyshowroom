from utilities.db_conn import connection
from pages import ui
import streamlit as st
from pages.footnote import *
import sqlalchemy as sqla
import pandas as pd

def database():
    showHeader()
    user_table = pd.read_sql('select * from user', connection)
    st.dataframe(user_table)
    st.text("")
    log_table = pd.read_sql('select * from log', connection)
    st.dataframe(log_table)
    showFooter()
