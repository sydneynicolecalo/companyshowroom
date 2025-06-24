import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pages.footnote import showHeader, showFooter

def hrdashboard():
    showHeader()
    showFooter()

    st.title('HR Dashboard')
    st.caption("*by* [*Christine Joyce Munar*],[*Christine Mallare*]() ")

    tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Usage", "Customization", "Test our Product"])
    with tab1:
        st.markdown(
            """
            ### Introduction
            """)
        st.write("MDI-Novare HR Dashboard Tableau representation. Define the High Level Dashboard Requirements to be supported based on decisions or activities to be supported for each End User. Organizations tried to study the impact of attrition and employee cases on their business performance over different periods of time. This dashboard illustrates the descriptive analysis of HR data using simple visualizations like bar charts, highlight tables,and text tables as its features and logic. The data visualizations presented in this report can be used in some common applications and various industries such as (1) Human Resource, (2) Food, (3) Agriculture, (4) Retail, (5) Manufacturing, (6) Transport & Logistics, (7) Lifestyle (e.g., Hotels, Entertainment, Tourism), (8) Construction and (9) Education.")
    with tab2:
        st.markdown(
            """
            ### Usage
            """)
        st.write("This dashboard is mainly useful for exploratory data analysis. Specific applications include (1) Employee attrition, (2) Attrition reversal, (3) Performance Strengthening Plan, (4) Employee and Labor cases, (5) Covid Cases, (6) Employee retention. Visualizations used are bar chart for salary comparison and cases, highlight table for monthly attrition and reasons for leaving, and lastly text table for summary of counts and employee details. This dashboard utilizes data that is provided by MDI-Novare Human resource. It includes employee details containing their hiring date, date of separation, Years of Tenure, Position Title, Reason for leaving, etc.. It also contains the consolidated data for employee and labor cases, as well as the identified number of covid cases in the company. Actionable Insights are comparison of target compensation based on Job description and identify cost value to be declared for the Talent Value Optimization roadmap.")
    with tab3:
        st.markdown(
            """
            ### Customization
            """)
        st.write("""For Integration and Automation, the HR Dashboard can be scheduled to run automatically and fetch monthly attrition data. Other data sources can be integrated within Tableau to include business-related datasets. On the other hand, Variations and Options. Users can customize the report to incorporate their branding based on their objective and targets. Visuals and dashboard layout can also be tweaked according to dashboard content required to support the priority of End User decision-making processes or activities. Lastly, Limitations. This is limited to descriptive analysis of weather and business KPIs.""")
    with tab4:

        st.markdown("### HR Dashboard")
        st.components.v1.iframe(
            "https://public.tableau.com/views/HRDashboard_16668630305540/AttritionSummary?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link",
            height=700, scrolling=True)