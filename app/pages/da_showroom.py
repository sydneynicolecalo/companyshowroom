import streamlit as st
import streamlit.components.v1 as components
from pages.footnote import showHeader, showFooter

def da_showroom():
    showHeader()

    # embed streamlit docs in a streamlit app
    st.title("Data Analytics Showroom")
    st.write("")

    st.markdown("### Accuweather Dashboard - PowerBI")
    st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiNTI0MmY0YjUtYzVkZC00MTE3LWI2OTItNjM2NDNlZjYxOGUxIiwidCI6ImEyYWQ5ODdmLTY1MzEtNDkwNy04ZTE2LTI0NWU2MjljM2VlNSIsImMiOjEwfQ%3D%3D", height=700, scrolling=True)

    st.markdown("### Accuweather Dashboard - Tableau")
    st.components.v1.iframe("https://public.tableau.com/views/Accuweather-Tableau/ACTUALvsREALFEEL?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link")

    st.markdown("### Data Feeds Dashboard")
    st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiN2U2YmY4ZmQtOWUzYi00OGFhLThhMjItYzcxNzczYTRkZjAwIiwidCI6ImEyYWQ5ODdmLTY1MzEtNDkwNy04ZTE2LTI0NWU2MjljM2VlNSIsImMiOjEwfQ%3D%3D", height=700, scrolling=True)

    st.markdown("### HR Dashboard")
    st.components.v1.iframe("https://public.tableau.com/views/HRDashboard_16668630305540/AttritionSummary?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link")

   # st.markdown("#### Embedding Google Data Studio")
   # st.components.v1.iframe("https://datastudio.google.com/embed/reporting/1uYIXuUFbGwMA8Y8R2JFenPNG3fjuCaGG/page/mpeW", height=700, scrolling=True)

    # st.markdown("#### Embedding Power BI")
    # st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiNzcxNTdlY2ItYjFhYS00YjkyLThkMmEtMTQwYjVlYzExNjA0IiwidCI6ImQyYWY4YjViLTlhN2UtNGM4NS1hM2ZkLWI2OWE2Njk4YjdkNiJ9",
                          #  height=400, scrolling=True)

    ##reference https://www.tutorialspoint.com/power_bi/power_bi_sharing_dashboards.htm#

    # st.markdown("#### Embedding Tableau")
    # st.components.v1.iframe("https://public.tableau.com/views/JudicialSalarySurvey_0/NationalRankingsSalaryFigures?:language=en-US&:display_count=n&:origin=viz_share_link",
                          #  height=700, scrolling=True)

    showFooter()