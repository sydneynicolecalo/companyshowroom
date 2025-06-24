import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pages.footnote import showHeader, showFooter

def sampledashboard():
    showHeader()
    showFooter()

    st.title('Sample Dashboards')
    st.caption("*by* [*Mike Maillis*](),[*Valli Mamadov*](),[*Ashish Babaria*]()")

    tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Usage", "Customization", "Explore the dashboards"])
    
    with tab1:
        st.markdown(
            """
            ### Introduction
            """)
        st.write("""

            Power BI dashboards offer comprehensive and dynamic insights into key organizational functions, including Finance, HR, and Supply Chain. These dashboards leverage robust data visualization tools to transform raw data into actionable intelligence, providing a holistic view of financial performance, human resources metrics, and supply chain operations. 

            In the Finance domain, Power BI enables users to analyze budgetary information, track expenses, and monitor financial trends. This empowers organizations to make informed decisions by identifying spending patterns, evaluating cost-saving opportunities, and optimizing financial resources effectively. With Power BI, users can track expenses in real-time, ensuring prompt monitoring and reconciliation of financial transactions while identifying discrepancies and maintaining accurate financial records.

            The HR dashboard in Power BI provides a visual representation of workforce metrics that aids in strategic workforce planning. It allows HR professionals to identify areas for improvement, implement targeted strategies, and boost employee satisfaction. Additionally, it helps track turnover rates over time, analyze causes, and develop retention strategies. By leveraging Power BI's capabilities, HR teams can optimize recruitment processes, identify effective sourcing channels, and diversify the talent pool through valuable insights into talent acquisition data.

            In the Supply Chain realm, Power BI dashboards provide organizations with the tools to optimize inventory management by offering real-time visibility into stock levels, demand patterns, and supplier performance. This enables businesses to adjust inventory levels, identify potential stockouts, and optimize reorder points. By monitoring supply chain efficiency, they can track key performance indicators (KPIs) like order cycle time, on-time delivery, and fill rate. This allows them to identify bottlenecks, streamline processes, and enhance overall supply chain performance.

            Overall, Power BI dashboards empower businesses with the insights needed to enhance operational efficiency and drive strategic initiatives across Finance, HR, and Supply Chain departments.
                        
            """)
    
    with tab2:
        st.markdown(
            """
            ### Usage
            """)
        
        
        st.write("Finance, HR, and Supply Chain dashboards can be utilized in many ways. The specific usage of each dashboard may vary based on the organization's needs and priorities.")
        
        st.markdown("#### Finance Dashboard")        
        st.write("""
                **1. Financial Performance Analysis**

                A Finance dashboard allows organizations to monitor and analyze key financial metrics such as revenue, expenses, and profitability ratios. It helps finance teams identify trends, compare actuals against targets, and make informed decisions to optimize financial performance.

                **2. Budgetary Control** 

                With a Finance dashboard, organizations can track budget allocation, monitor spending patterns, and identify cost-saving opportunities. It enables finance teams to ensure adherence to budgets, identify variances, and adjust financial strategies as needed.

                **3. Cash Flow Management** 

                A Finance dashboard provides real-time visibility into cash flow, accounts receivable, and accounts payable. It helps organizations track cash inflows and outflows, identify potential liquidity issues, and optimize cash flow management for improved financial stability.
                """)
        
        st.markdown("#### HR Dashboard")
        st.write("""
                **1. Workforce Analytics** 

                An HR dashboard allows organizations to analyze key workforce metrics such as employee engagement, turnover rates, and performance ratings. It helps HR professionals identify trends, assess the effectiveness of HR programs, and make data-driven decisions to improve employee satisfaction and retention.

                **2. Talent Acquisition and Recruitment** 

                With an HR dashboard, organizations can track recruitment metrics such as time-to-hire, source of hire, and candidate demographics. It enables HR teams to optimize recruitment processes, identify effective sourcing channels, and make informed decisions to build a diverse and talented workforce.

                **3. Training and Development** 

                An HR dashboard provides insights into training completion rates, skills gaps, and learning program effectiveness. It helps organizations identify training needs, track employee development progress, and make strategic decisions to enhance employee skills and capabilities.
                """)

        st.markdown("#### Supply Chain Dashboard")
        st.write("""

                **1. Inventory Management** 

                A Supply Chain dashboard enables organizations to monitor inventory levels, track stockouts, and analyze demand patterns. It helps supply chain managers optimize inventory levels, identify potential stockouts or excess stock, and make data-driven decisions to ensure efficient inventory management.

                **2. Supplier Performance Monitoring** 

                With a Supply Chain dashboard, organizations can track supplier metrics such as delivery accuracy, lead times, and quality performance. It helps supply chain teams assess supplier performance, identify underperforming suppliers, and negotiate better terms to optimize the supply chain.

                **3. Logistics and Fulfillment Optimization** 

                A Supply Chain dashboard provides insights into key logistics metrics like order cycle time, on-time delivery, and fill rate. It helps organizations identify bottlenecks in the logistics process, streamline operations, and improve overall supply chain efficiency for better customer satisfaction.

              """)
    
    with tab3:
        st.markdown(
            """
            ### Customization
            """)
        st.write("The customization of the dashboards involves tailoring the metrics, visualizations, and functionalities to the specific needs and objectives of the organization. This allows users to focus on the most relevant data and insights for their decision-making processes.")
    
        st.markdown("#### Finance Dashboard")        
        st.write("""
                **1. Customized Metrics** 

                Organizations can customize the Finance dashboard by selecting specific financial metrics relevant to their business, such as revenue growth, net profit margin, or return on investment. This allows them to focus on the metrics that align with their financial goals and strategies.

                **2. Visualization Options** 

                Finance dashboards can be customized by choosing different visualization options, such as line charts, bar graphs, or pie charts, to present financial data in a visually appealing and understandable manner. Users can also customize color schemes and layouts to suit their preferences.

                **3. Drill-down and Filters** 

                Users can customize the Finance dashboard by incorporating drill-down capabilities and filters. This allows them to analyze financial data at different levels of detail, such as by department, product category, or time period, providing deeper insights and facilitating more targeted decision-making.

                 """)
        
        st.markdown("#### HR Dashboard")
        st.write("""
                 **1. Key HR Metrics** 

                Organizations can customize the HR dashboard by selecting the most relevant HR metrics for their specific needs, such as employee turnover rate, training hours per employee, or diversity and inclusion metrics. This ensures that the dashboard focuses on the metrics that align with their HR goals and strategies.

                **2. Employee Segmentation** 

                HR dashboards can be customized to segment employee data based on various criteria, such as department, location, or job level. This allows HR professionals to analyze HR metrics for different employee groups, identify trends, and tailor HR strategies and interventions accordingly.

                **3. Alert Notifications** 

                Customizations can include setting up alert notifications within the HR dashboard. For example, HR teams can receive automatic alerts when certain metrics exceed predefined thresholds, such as high turnover rates or low employee engagement scores. This helps HR professionals proactively address issues and take timely actions.

                 """)
        
        st.markdown("#### Supply Chain Dashboard")
        st.write("""
                 **1. Supply Chain Metrics** 

                Organizations can customize the Supply Chain dashboard by selecting the most relevant supply chain metrics for their specific needs, such as inventory turnover ratio, order fill rate, or transportation costs. This ensures that the dashboard focuses on the metrics that align with their supply chain goals and strategies.

                **2. Data Integration** 

                Customizations can involve integrating data from various systems and sources into the Supply Chain dashboard. This allows organizations to have a comprehensive view of the supply chain by combining data from inventory management systems, ERP systems, or logistics platforms, providing a holistic and real-time perspective.

                **3. Geographical Visualization** 

                Supply Chain dashboards can be customized to include geographical visualizations, such as maps or heatmaps, to display supply chain network nodes, transportation routes, or distribution centers. This helps organizations visualize and analyze supply chain operations across different locations, facilitating optimization and decision-making.

                 """)

    with tab4:
        st.markdown("### Finance Reporting Dashboard")
        st.components.v1.iframe(
            "https://app.powerbi.com/view?r=eyJrIjoiYjkzYTg3YmQtYWRmNy00ZTQ5LTg4YmYtYzhlMWRmMTFkNmI0IiwidCI6Ijk3MzljOGZhLWQ0MGUtNDYyYy1hYWFkLWEzMGJkZDVmNGUzZCIsImMiOjl9",
            height=700, scrolling=True)
        st.text("")
        st.markdown("### Human Resources Dashboard")
        st.components.v1.iframe(
            "https://app.powerbi.com/view?r=eyJrIjoiYzEwZGEyMjctYTVjMC00N2I4LThhNWUtYjRiOWYxMGJhNDZiIiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9",
            height=700, scrolling=True)
        st.text("")
        st.markdown("### Supply Chain Dashboard")
        st.components.v1.iframe(
            "https://app.powerbi.com/view?r=eyJrIjoiZjBlMjhkNzgtZmY3MC00MTJkLTlhMjQtODI3NjEwYzAxMmJjIiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9&pageName=ReportSection46bc6f724d93a5eb9d8b",
            height=700, scrolling=True)

