import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import joblib
import pickle
from sklearn.pipeline import Pipeline
from PIL import Image

from pages.footnote import showHeader, showFooter

def predict_crime(text):
    try:                
        models_dir = r'app/models/sentiment_analysis'
        model = 'crime_model.pkl'
        tfidf_v = 'crime_tfidf.pkl'
        svd_v = 'crime_svd.pkl'

        model = joblib.load(f'{models_dir}/{model}')
        tfidf_vec = joblib.load(f'{models_dir}/{tfidf_v}')
        svd_vec = joblib.load(f'{models_dir}/{svd_v}') 

        crime_pred = Pipeline(steps=[
            ('tfidf', tfidf_vec),
            ('svd', svd_vec),
            ('vc', model)
        ])

        classes_ = crime_pred.classes_
        crime_predicted = crime_pred.predict([text])
        crime_pred_proba = crime_pred.predict_proba([text])

        print(classes_)
        print(crime_pred)
        print(crime_pred_proba) 

        return crime_predicted, crime_pred_proba, classes_
        
    except Exception as e:
        print(f"An error occurred: {e}")
        raise e

def web_application():
    showHeader()
    showFooter()
    
    st.title("Text-Based Crime Detection System")

    st.caption("*by* [*Joseph B. Rivera*]()")

    st.markdown("<br>", unsafe_allow_html=True)
            
    tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Usage", "Customization", "Test our Product"]) 
        
    with tab1:
        st.markdown(
        """
        ### Overview
        """)
        
        image_path = "app/images/crime_overview.jpg"
        imageM = Image.open(image_path)
        st.image(imageM, caption="Image by Paul Barlow from Pixabay", width=600)

        st.write(""" 
                Financial crimes pose a significant threat to the stability and integrity of a country's financial system and economy. With the increasing ease of conducting online transactions, criminals have found new opportunities to exploit vulnerabilities and engage in illicit activities. The anonymous nature of online transactions and the global reach of the internet make it challenging to detect and prevent such crimes effectively.

                To address this issue, organization such as financial institutions and regulatory bodies must recognize the need for a robust tracking system that can monitor financial transactions in real-time, regardless of whether they occur online or offline. Traditional methods of tracking and detecting suspicious transactions are often inadequate due to the sheer volume, speed, and complexity of modern financial transactions.

                Artificial intelligence (AI) plays a crucial role in enhancing the capabilities of financial tracking systems. By leveraging AI technologies, such as machine learning and data analytics, financial institutions and regulatory bodies can more effectively identify patterns, anomalies, and potentially fraudulent activities. AI-powered systems can process vast amounts of data and quickly identify suspicious transactions, enabling early detection and intervention.

                By adopting advanced techniques and leveraging AI, these institutions can strengthen their abilities to combat financial crimes. Early detection and investigation of such crimes not only protect the financial system from collapse but also contribute to maintaining a healthy economy by deterring criminals and preserving public trust in the financial sector.

                The implementation of these advanced systems also considers privacy concerns and adhere to relevant legal and ethical frameworks to strike a balance between effective crime prevention and individual rights.
                    
                """
                )
        
    with tab2:
        st.markdown(
        """
        ### Usage
        """)

        image_path = "app/images/crime_usage.jpg"
        imageM = Image.open(image_path)
        st.image(imageM, caption="Image by Gerd Altmann from Pixabay", width=600)

        st.write("""                  

                As financial crimes continue to pose significant threats to the stability and integrity of financial systems worldwide, the adoption of advanced technologies like this becomes imperative. This application offers numerous benefits across various domains, including but not limited to:

                **1. Risk Assessment**
                    
                With its advanced capabilities, the application enables deep dives into intricate financial transactions, allowing for the identification of suspicious activities and potential fraudulent behavior. By analyzing large datasets, it uncovers hidden correlations and anomalies that human analysts might overlook, providing a higher level of accuracy and detection. The timely and proactive nature of the risk assessment enables swift responses and interventions. Financial institutions and regulatory bodies can stay ahead of emerging risks, take appropriate measures, and protect the integrity of the financial system.

                **2. Fraud Prevention**
                    
                This application monitors transactional data and detects suspicious activities indicative of fraud. By leveraging machine learning techniques, it can identify fraud patterns, flag suspicious transactions in real-time, and trigger immediate intervention. This proactive approach helps prevent financial losses, protect customers, and maintain the integrity of the financial system.

                **3. Compliance Monitoring**
                    
                Ensuring compliance with ever-evolving financial regulations is a complex task. This application enhances compliance monitoring by automating the analysis of vast amounts of data to identify compliance gaps and anomalies. This AI-powered compliance monitoring not only reduces the risk of penalties but also enhances transparency and trust in the financial sector.

                **4. Enhanced Investigation Capabilities**
                    
                Financial crime investigations often involve complex networks and intricate transactions. This application can identify relevant evidence, prioritize leads, and generate actionable insights, expediting investigations and increasing the chances of successful prosecutions. The ability to leverage AI in investigations enhances the effectiveness of law enforcement agencies and contributes to a more robust financial crime management ecosystem.

                **5. Operational Efficiency**
                    
                This application streamlines operational processes that leads to increased efficiency within financial institutions. By reducing manual workloads associated with transaction monitoring, fraud detection, and compliance tasks, it frees up human resources to focus on more strategic activities. It handles repetitive and time-consuming tasks with accuracy and speed, leading to cost savings, improved productivity, and enhanced customer service. Operational efficiency gains allow organizations to allocate resources effectively and respond swiftly to emerging financial crime threats.

                The integration of this application in financial crime management represents a significant leap forward in combating illicit activities within the financial sector. By harnessing the power of AI, financial institutions, regulatory bodies, and law enforcement agencies can proactively tackle financial crimes, safeguard financial systems, and protect stakeholders' interests.
                
                    """
                    )
        
        
    with tab3:
        st.markdown(
        """
        ### Customization
        """)

        image_path = "app/images/crime_customization.jpg"
        imageM = Image.open(image_path)
        st.image(imageM, caption="Image by WOKANDAPIX from Pixabay", width=600)

        st.write("""                  
                When you purchase our service for financial crime management utilizing AI, we tailor fit the application to your specific needs. Here are some of the ways we accomplish this:

                **1. Configurable Rules and Parameters**

                This allows you to set thresholds, define risk criteria, and configure fraud or anomaly detection rules based on your specific industry factors and organizational needs. You can adjust these rules and parameters to reflect your risk appetite, compliance standards, and business objectives.
                You can tailor fit the system to focus on the types of transactions or activities that are most relevant to your operations to ensure that the AI system is aligned with the specific risk profiles.

                **2. Integration with Internal Systems**

                With this integration, you gain a deeper understanding of your organization's activities and potential risks. By combining data from transaction monitoring platforms, customer databases, and risk management tools, our AI application can uncover hidden correlations, identify emerging patterns, and detect potential financial crimes more effectively. This comprehensive analysis empowers you to make informed decisions, mitigate risks promptly, and proactively protect your organization from illicit activities.

                **3. Adaptable Machine Learning Models**

                You have the ability to optimize the system's performance by leveraging your specific data patterns, industry knowledge, and evolving business environment.  As your business environment evolves, you have the flexibility to update and refine the models to ensure their effectiveness remains at the forefront of financial crime prevention. This level of customization ensures the continuous improvement of the application's ability to detect and prevent financial crimes specific to your operations.
            
                    """
                )      
    
        
    with tab4:        
        st.markdown(
        """
        ### Analyze Incidents through a Written Narrative
        """)

        # st.write(
        #     """
        #         This application utilizes natural language processing to predict crime types based on textual descriptions. 
        #         Explore how advanced algorithms can analyze narratives and provide insights into potential criminal activities. 
        #         Enter a description, and let the system unveil the predicted crime category along with its confidence level.
        #     """
        #     )
        
        with st.form(key='text_clf_form'):
            raw_text = st.text_area("Type Here")
            submit_text = st.form_submit_button(label='Submit')

        if submit_text:            
            crime_predicted, prediction_probability, classes_ = predict_crime(raw_text)              
            
            st.success("Your Narrative")
            st.write(raw_text)
            
            st.success("Crime Predicted")
            st.write(crime_predicted[0])
            st.write("Confidence: {}".format(np.max(prediction_probability)))

            st.success("Probabilities of Crimes Present")
            proba_df = pd.DataFrame(prediction_probability, columns=classes_)
            proba_df_sorted = proba_df.T.sort_values(by=0, ascending=False)                    
            proba_df_clean = proba_df_sorted.reset_index()
            proba_df_clean.columns = ["crimes", "probability"]
            
            fig = alt.Chart(proba_df_clean).mark_bar().encode(x=alt.X('crimes', axis=None, sort='-y'),y='probability',color='crimes')
            st.altair_chart(fig,use_container_width=True)          
                    
if __name__ == "__main__":
    web_application()
