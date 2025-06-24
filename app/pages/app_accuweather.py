import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pages.footnote import showHeader, showFooter

def accuweather():
    showHeader()
    showFooter()

    st.title('Accuweather')
    st.caption("*by* [*Anne Clara Arrobio*],[*Garret Christopher Alegre*],[*Loyd Nino Catolpos*],[*Michael Jeff Delos Santos*]()")

    tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Usage", "Customization", "Test our Product"])
    with tab1:
        st.markdown(
            """
            ### Introduction
            """)
        st.write("Organizations study the impact of weather on their business performance over different periods of time. This dashboard illustrates the descriptive analysis of Metro Manila Accuweather data using simple visualizations like bar charts, line charts, year-on-year comparisons, and tables and matrices. The data visualizations presented in this report are commonly used in various industries such as energy, food, agriculture, retail, manufacturing, transport & logistics, lifestyle (e.g., hotels, entertainment, tourism), construction, and education. Whether your tool of choice is Tableau or PowerBI, our team is able to create the same dashboard using the same dataset.")
    with tab2:
        st.markdown(
            """
            ### Usage
            """)
        st.write('This dashboard is mainly useful for exploratory data analysis. Some specific applications include (1) monitoring of equipment, production, and consumption, (2) supply chain management, (3) farming and harvest, (4) logistics and distribution, (5) timeliness, (6) monitoring of demand, and (7) project feasibility. The dashboards use several types of visualizations such as line chart, bar chart, highlight table, table, and shared/combined axis. This dashboard utilizes data that is retrieved from Accuweather using their API. It includes weather station codes, dates, time zone, maximum and minimum temperatures, wind chill measurements, wind speed, wind direction, humidity, sunshine, cloud cover, etc.')
    with tab3:
        st.markdown(
            """
            ### Customization
            """)
        st.write("""The Accuweather API can be scheduled to run automatically and fetch daily weather data. Other data sources can also be integrated within PowerBI and Tableau to include business-related datasets.In terms of design, users can customize the report to incorporate their branding. Also, the visuals and dashboard layout can be tweaked according to the viewer’s preference. Although it is easily customizable, the dashboard is currently limited to descriptive analysis of weather and business KPIs. Businesses can use the dashboard to gain insights and further their analyses to build data science models.""")
    with tab4:

        st.markdown("### Accuweather Dashboard - PowerBI")
        st.components.v1.iframe(
            "https://app.powerbi.com/reportEmbed?reportId=085f7651-0036-47d2-89c7-bc432199ac2b&autoAuth=true&ctid=0db5141a-d4cf-484e-845f-e287cfaea452",
            height=700, scrolling=True)

        st.markdown("### Accuweather Dashboard - Tableau")
        st.components.v1.iframe(
            "https://public.tableau.com/views/Accuweather-Tableau/ACTUALvsREALFEEL?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link",
            height=700, scrolling=True)
