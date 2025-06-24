import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pages.footnote import showHeader, showFooter

def datafeeds():
    showHeader()
    showFooter()

    st.title('Data Feeds')
    st.caption("*by* [*Dennis Ngungie*]() ")

    tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Usage", "Customization", "Test our Product"])
    with tab1:
        st.markdown(
            """
            ### Introduction
            """)
        st.write("Data migration is a precarious situation in any business or organization. Gigabytes to terabytes of data are being moved, thousands of data objects are being updated, and hundreds of jobs are being deployed with tight scheduling in a critical span of time. To successfully accomplish the process requires the knowledge of the full end-to-end situation to make decisions, allocate resources, and troubleshoot problems along the way which a Data Migration Monitoring Dashboard will be of great help.")
        st.write("This dashboard helps the operation team to monitor the Talend execution job and also monitor the ingestion of data migration to find discrepancies and also monitor the processing stats of each data migration. It was developed during the development of data migration and created a visualization to visually track the process and has this feature to  closely monitor the Talend execution and data migration feed on one single platform and provide user-level knowledge without drilling through a bunch of logs and SQL scripting with this, it can be applied to an industry that can provide high-level information in data migration and Talend execution.")
    with tab2:
        st.markdown(
            """
            ### Usage
            """)
        st.write("This dashboard can be used in data migration projects of various industries. Developed using PowerBI and the dataset being consumed is from the log files and its interpretation is to check for job errors and variance. Once an error or variance is present, the operation team can perform a root cause analysis and ultimately fix the issue. On this dashboard we can identify the job success, error, running, and even the failed and long-running jobs (>30 mins runtime) on a specific date by using the slider. We can also check and monitor the ingestion from the source to its target destination tables if they were accurate using the MD5 hash check and record counts on a specific date. Lastly, we can show the processing stats of each migration end-to-end to have a better understanding of process duration and how many average record counts are being migrated and act as performance metrics to identify that need further tweaking in the resources or the job itself.")
    with tab3:
        st.markdown(
            """
            ### Customization
            """)
        st.write("""Essential is the freshness of information in the dashboard. Most of the time they require a start and end-of-day refresh while some require near real-time. The dataset and dashboard can be refreshed within 2 mins using PowerAutomate and the dashboard has a generic framework and can be modified easily by pointing out specific IDs but has a limitation that the gateway has a client-server side and not a cloud server. Similar refresh rates can also be accomplished by using job or process schedulers and automatons.""")
    with tab4:

        st.markdown("### Data Feeds Dashboard")
        st.components.v1.iframe(
            "https://app.powerbi.com/view?r=eyJrIjoiN2U2YmY4ZmQtOWUzYi00OGFhLThhMjItYzcxNzczYTRkZjAwIiwidCI6ImEyYWQ5ODdmLTY1MzEtNDkwNy04ZTE2LTI0NWU2MjljM2VlNSIsImMiOjEwfQ%3D%3D",
            height=700, scrolling=True)