from pages import ui

import streamlit as st
from pages.footnote import *
from PIL import Image

def aboutus():
    showHeader()

    st.title("Data Science and Analytics Team")
    st.write("The Data Science and Data Analytics Showroom is developed by MDI Novare DS&A Team.")

    st.write("")
    image1 = Image.open(r'app/images/nicolecalo.jpg')
    st.image(image1, width=300)
    st.subheader('Sydney Nicole Calo - Senior Data Scientist')
    st.write('Sydney is currently a Senior Data Scientist at MDI-Novare. She has worked on time series, anomaly detection, churn, next best offer, anti-money laundering dashboards, web app development among other data science projects during her stay in the company. She has a background in Data Science, Business Analytics and Market Research Consulting, as well as Corporate Governance and FinTech. She graduated from AB Development Studies, focusing on Development Management from a top university in the Philippines, and also earned a Minor in Chinese Studies. Previously, she studied BS Applied Physics. She is intermediately fluent in Mandarin and is currently pursuing online studies from a university in China. Sydney is also a classically trained singer and pop song composer, with two albums on Spotify. In her free time, Sydney enjoys walks in nature and the occasional visits to the beach. She is also a foodie and has a pet shih-pom shih-poo dog named Moochi, as well as 22 cats.')

    st.write("")
    image2 = Image.open(r'app/images/michaeljeffdelossantos.jpg')
    st.image(image2, width=300)
    st.subheader('Michael Jeff Delos Santo - Lead Data Analyst')
    st.write("Jeff is a Lead Data Analyst at MDI-Novare. He’s currently leading the Data Analytics team in migrating and developing dashboards into a single reporting service for an Energy Company. He took part in data stewardship for a Telecommunications company's data governance implementation. He as well developed dashboards for a Banking Company. He also handles enablement training for Tableau. He started his professional career as an Office Support in a local call center company and took an interest in data analysis from friends' influence. Jeff loves finding shortcuts in repetitive tasks (work smart, not hard). He graduates Bachelor of Technology in Power Plant Engineering from the Technological University of the Philippines - Manila. He cooks a legitimate Batangas Lomi. He loves exploring the world on two wheels, actually, it’s not just motorcycles, it’s more about long-distance riding and driving. He loves memorizing OPM rap songs even in the absence of singing talent.")

    st.write("")
    image3 = Image.open(r'app/images/annearrobio.jpg')
    st.image(image3, width=300)
    st.subheader('Anne Clara Arrobio - Senior Data Analyst')
    st.write('Anne is a Senior Data Analyst in MDI-Novare. She studied BS Management Information Systems and started to work in an airline company as a data analyst fresh out of college. She handled the creation of reports and dashboards for the loyalty program. She was also eventually assigned to the strategy office to handle the reports and dashboards of Sales & Marketing, Project Management, and Aircraft Engineering. She started her graduate studies in Data Science three years after working in the airline. Currently, in MDI-Novare, she is working on developing dashboards and supporting the system integration for an energy company. She has also worked on finance analytics, time series analysis, automatic speech recognition, text-to-speech, and sentiment analysis. Throughout the years, she has gained experience in using Teradata SQL, Oracle SQL, Tableau, PowerBI, and Python. Anne loves to travel and explore the culture of different places. She loves getting lost in a new city or island. She also loves to go running, spinning (bike), obstacle course racing, swimming, and playing volleyball. She also loves to crochet and knit her own bags and clothes. Anne is not so fond of watching TV shows and movies, but her favorite show is New Girl which she has watched over ten times. Anne loves to sing too, especially when it’s Harry Styles on the radio.')

    st.write("")
    image4 = Image.open(r'app/images/garretalegre.jpeg')
    st.image(image4, width=300)
    st.subheader('Garret Christopher T. Alegre - Senior Data Analyst')
    st.write('Garret is a Senior Data Analyst in MDI-Novare. He studied BS Information System and is currently taking a Masters in Information Systems. Currently in MDI-Novare, he is working on developing dashboards and supporting the system integration for an energy company. He also worked on some initiatives regarding analysis together with the research and development team. Garret loves to travel on a motorcycle and advocates riding to work. During the weekend he loves being involved in outdoor activities like practical shooting and binge drinking. He also loves to cook and fancy pets like leopard geckos. In addition, Garret is currently looking for thesis topics.')

    st.write("")
    image5 = Image.open(r'app/images/dennisngungie.jpg')
    st.image(image5, width=300)
    st.subheader('Dennis Ngungie - Senior Data Analyst')
    st.write('Dennis is a Senior Data Analyst in MDI-Novare and studied BS Information Systems and is currently taking a Masters in Information Systems. He started off as an IT Business Analyst and eventually drifted his career to data analytics. He is currently involved in a project where he developed an end-to-end dashboard for a telecommunication company to monitor the daily operation activity of data ingestion. In addition to that, he supports the creation of finance analytics reports and is involved in client proposal presentations. During the weekend he loves being involved in outdoor activities and binge drinking at night and working on the next day.')

    st.write("")
    image6 = Image.open(r'app/images/christinemallare.jpg')
    st.image(image6, width=300)
    st.subheader('Christine Mallare - Lead Data Analyst')
    st.write('Christine is a Lead Data Analyst in MDI-Novare and studied BS Psychology. Prior to MDI I started working in a start-up company and supported developing reports in government election surveys using tableau. She was deployed in one of the biggest telecommunication in the Philippines to do POC for Talend, as part of the engineers on that POC, and delivered exceptional results for the POC that led (MDI/Novare) getting the project, She was also able to be part of the 2019 awardees Pinnacle Award and Reliable Implementer. She is currently involved in a project for an Electric Company that develops end-to-end reports that support system integration. Her Friday night usually is for Netflix series, (Korean English Etc.) with a glass of wine just for relaxing, but on a weekend she makes sure that her time is for family, just staying at home or sometimes outside activities) and most especially have lots of time with her pet dog to do some walking in the fields or just outside the unit.')

    st.write("")
    image7 = Image.open(r'app/images/joycemunar.JPG')
    st.image(image7, width=300)
    st.subheader('Christine Joyce Munar - Senior Data Analyst')
    st.write('Joyce is currently working as a Senior Data Analyst at MDI- Novare. She studied BS Information Systems and she has a background in Business Analytics as well as experience in working for a Telecommunication company, which made her familiar with Account reconciliation, provisioning processes, and creating reports for Account monitoring activities. Currently, in MDI-Novare, she is working on the development of reports and supporting system integration for an energy company. During weekends, she likes to watch movies and play online games. She also likes to travel and enjoys visiting the beach. She loves food and enjoys grocery shopping. In addition, Joyce also loves to spend time with her three furbabies.')

    st.write("")
    image8 = Image.open(r'app/images/ronaldtabora.jpg')
    st.image(image8, width=300)
    st.subheader('Ronald S. Tabora - Senior Data Analyst')
    st.write('Ronald is a new member of the team who had just joined in September of this year, and is currently a Senior Data Analyst. He has been working in the Information Technology industry for different clients since 2006 and has primarily used different Business Intelligence tools throughout the years such as MicroStrategy, SAP BusinessObjects (Web Intelligence), Tableau Desktop, and PowerBI Desktop. He has also worked on Data Integration projects using different SQL versions such as PL/SQL, T-SQL, PL/pgSQL, Proc SQL, to name a few. He studied BS Computer Science and Information Technology. In his spare time, he reads theological books, does computer art using Blender3D, plays music on his electro-acoustic guitar, and is someone who also happens to have music uploads in Spotify, and is a virtual resident in The Elder Scrolls Online, and not forgetting to mention that he is sort of serving as a guardian to his parents as both are in their senior years.')

    st.write("")
    image8 = Image.open(r'app/images/jetregencia.jpeg')
    st.image(image8, width=300)
    st.subheader('Josiah Eleazar “Jet” Regencia - Senior Data Scientist')
    st.write("Jet is currently a Senior Data Scientist at MDi Novare.He studied BS Computer Science during his college years and after which he started his career as a software engineer for a startup fintech company. After 5 months with the company, Jet decided to pursue a full time MS Computer Science under the scholarship of DOST-ERDT. He tackled developing a test framework for Software-Defined Networks for his thesis. From time to time, Jet accepts online freelance jobs for web scraping, SCADA development work and other short-term technical projects. Now working as a Senior Data Scientist at MDi Novare, Jet has participated in client projects developing predictive models for a power utility company in order to predict impacted transformers 2 months ahead of time. Aside from that, Jet has performed proof of concepts for sentiment analysis for various potential clients. Currently, Jet is working with the same power utility replacing their SAP software for cost allocation. Outside work, Jet is a simple guy who would just want to chill and enjoy sports.")

    st.write("")
    #image9 = Image.open('images/')
    #st.image(image9, width=300)
    st.subheader('Kyle Fretzie R. Regino - Lead Data Scientist')
    st.write("Kylie is a Lead Data Scientist at MDi Novare and studied BS Computer Engineering with a Major in Embedded Systems. She is a founding member of MDi Novare's Data Science team and was part of the team that began development of IRIS, MDi Novare's attendance monitoring system. In her time at MDi Novare, she was able to explore different roles such as business analyst, data analyst, QA, web and mobile developer, and (her favorite) data scientist. Currently, she is working with Meralco in the EDM team, doing data analytics work. Kylie loves going to beaches and doing 40-foot cliff dives, but she can't swim. She also loves watching sunsets and beautiful scenes of nature, stargazing, and loves to travel. Coffee runs in her veins. She currently has three children (doggies) that demand attention all the time.")

    st.write("Copyright © Novare. All rights reserved.")
    showFooter()


