import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pages.footnote import showHeader, showFooter

def customerjourneydashboard():
    showHeader()
    showFooter()

    st.title('Customer Journey Dashboard')
    st.caption("*by* [*Ron Tabora*]()")

    tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Usage", "Customization", "Test the Dashboard"])
    with tab1:
        st.markdown(
            """
            ### Introduction
            """)
        
        st.write("""
                The customer journey dashboard is a powerful tool that enables businesses to gain valuable insights into customers' interactions and experiences throughout their entire journey with the brand. By analyzing various touchpoints and stages of the customer journey, companies can identify pain points, optimize customer interactions, and ultimately enhance customer satisfaction and loyalty. 

                The dashboard helps track and measure the effectiveness of different acquisition channels and campaigns. By analyzing data such as website traffic, social media engagement, and advertising metrics, businesses can gain insights into which channels and campaigns are driving the most valuable customers. These insights enable companies to optimize their marketing strategies, allocate resources effectively, and attract customers who are more likely to have a positive experience with the brand.

                The dashboard provides a comprehensive view of various engagement touchpoints, such as website visits, app usage, email interactions, and customer support interactions. By analyzing this data, businesses can identify patterns and trends in customer behavior, preferences, and needs. This information can be used to personalize the customer experience, tailor marketing messages, and optimize product or service offerings.

                The dashboard helps track conversion metrics and provides insights into the factors that influence customers' decision-making process. By analyzing data such as conversion rates, cart abandonment rates, and customer feedback, businesses can identify barriers to conversion and implement strategies to overcome them. 

                The dashboard assists in tracking customer retention metrics. By understanding the factors that contribute to customer loyalty, businesses can develop effective retention strategies. This may involve personalized communication, loyalty programs, proactive customer support, and continuous product or service improvements. 

                By leveraging this powerful tool, businesses can gain insights into customer behavior, preferences, and pain points, enabling them to optimize marketing strategies, personalize customer interactions, and enhance the overall customer experience. By continuously monitoring and analyzing the customer journey, companies can identify opportunities for improvement and take proactive measures to exceed customer expectations.

                 """)
    with tab2:
        st.markdown(
            """
            ### Usage
            """)
        st.write("""
                 A customer journey dashboard can come in many shapes and sizes. However, to ensure its success, it should make it easy and accessible for the organization to monitor, interact with, understand customer data and drill down to the information needed to improve the customer experience. It is very helpful in so many ways such as the following:

                **1. Identify Customer Experience Gaps**

                By analyzing customer journey metrics and feedback, businesses can pinpoint areas where customers may be experiencing friction, dissatisfaction, or confusion. This insight allows them to take proactive measures to address these gaps and enhance the overall customer experience.

                **2. Optimize Marketing and Sales Strategies** 

                By tracking metrics such as conversion rates, customer acquisition costs, and engagement rates, businesses can identify which marketing channels, campaigns, or touchpoints are performing well or underperforming. This information enables them to optimize their strategies, allocate resources effectively, and improve ROI.

                **3. Personalized Customer Interactions**

                The dashboard helps businesses understand customer preferences, behavior, and needs throughout the customer journey. By segmenting customers based on their characteristics and tracking their interactions, businesses can deliver personalized experiences and targeted messaging. This level of personalization enhances customer engagement, satisfaction, and loyalty, as customers feel understood and valued by the brand.

                **4. Measure and Improve Customer Retention** 

                By tracking customer retention metrics, such as churn rate and customer lifetime value, and analyzing customer behavior, businesses can identify factors contributing to customer attrition and take proactive steps to improve customer retention. The dashboard helps businesses implement retention strategies, such as loyalty programs, proactive support, or personalized offers, to enhance customer loyalty and increase customer lifetime value.

                By leveraging the insights provided by the dashboard, businesses can enhance the overall customer experience, drive customer loyalty, and achieve business growth.

                 """)
    
    with tab3:
        st.markdown(
            """
            ### Customization
            """)
        
        st.write("""

                A customer journey dashboard can be customized based on the specific needs and goals of a business. Here are some ways in which it can be customized:

                **1. Key Metrics and KPIs** 

                Businesses can select the key metrics and key performance indicators (KPIs) that align with their specific objectives and industry. This allows them to focus on the metrics that are most relevant to their customer journey and business goals.

                **2. Visualization and Reporting** 

                Businesses can choose the types of charts, graphs, or tables that best represent the data and facilitate easy understanding. It may include bar charts, line graphs, pie charts, or heatmaps. Additionally, they can determine the frequency and format of reporting, such as daily, weekly, or monthly reports, and whether they are presented as visual dashboards or exported as PDF or Excel files.

                **3. Integration with Data Sources** 

                Businesses can connect the dashboard with their internal systems, such as CRM (Customer Relationship Management) software, marketing automation platforms, or customer support tools, to gather relevant data. Additionally, they can integrate external data sources, such as social media analytics or website analytics, to gain a comprehensive view of the customer journey.

                **4. Alert and Notification Settings** 

                Customization options can include setting up alerts and notifications based on specific metrics or thresholds. This allows businesses to receive real-time updates or automated notifications when certain metrics deviate from the desired benchmarks. These alerts enable businesses to take immediate action and address any issues or opportunities as they arise.

                Customizing the dashboard enables businesses to focus on the metrics and data sources that matter most, analyze customer behavior and performance effectively, and make data-driven decisions to enhance the customer experience and drive business growth.
                """) 
    
    with tab4:
        st.markdown("### Customer Journey Dashboard")
        st.caption("*Design courtesy of Search Foresight*")
        st.components.v1.iframe("https://lookerstudio.google.com/embed/reporting/c5226fc4-24b1-428f-9cbd-2894af0145c5/page/QzYj",
            height=700, scrolling=True)
