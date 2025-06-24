from dotenv import load_dotenv
load_dotenv()

import streamlit as st 
import os
import google.generativeai as genai
from PIL import Image

from pages.footnote import showHeader, showFooter


def configure_generative_ai():
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    genai.configure(api_key=api_key)

def initialize_generative_model(api_key):
    return genai.GenerativeModel(api_key)

def get_response(model, question):
    response = model.generate_content(question)
    return response.text

def content_generation():
    showHeader()
    showFooter()

    st.title("ContentGenius")    
    st.caption("*by* [*Joseph B. Rivera*]()")

    st.markdown("<br>", unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Usage", "Customization", "Test our Product"])

    with tab1:
        st.markdown(
        """
        ### Overview
        """)

        image_path = "app/images/congenius_overview.jpg"
        imageM = Image.open(image_path)
        st.image(imageM, caption="Image by Paul Barlow from Pixabay", width=600)

        st.write(""" 
                   ContentGenius is an AI tool founded on cutting-edge natural language processing technology. Its primary objective is to aid users in producing coherent and meaningful content across an extensive array of topics. By employing state-of-the-art architecture, it generates text of good quality and contextual relevance based on the provided prompts. 

                   The app excels in generating text that mirrors human-like qualities by ensuring grammatical correctness, coherence, and contextual appropriateness. It can generate text in diverse styles and tones that includes informative, persuasive, narrative, technical, and more. It can also be prose or non-prose.

                   Users direct the content generation process by supplying prompts or instructions to the application, ranging from specific questions and partial sentences to general topic descriptions. The AI model meticulously analyzes the prompt and produces a response accordingly.

                   With its comprehensive features, this AI application offers users a robust and versatile tool for creating high-quality text content across various domains. Its advanced natural language processing capabilities, coupled with continuous enhancements based on user feedback, position it as an invaluable resource for a broad spectrum of writing and communication needs.                
                
                """
                )
        
    with tab2:
        st.markdown(
        """
        ### Usage
        """)

        image_path = "app/images/congenius_usage.jpg"
        imageM = Image.open(image_path)
        st.image(imageM, caption="Image by Pexels from Pixabay", width=600)       

        st.write("""                  
                ContentGenius offers substantial benefits, particularly within business settings. Below are several essential applications of the app:

                **1. Content Creation**

                It can assist in generating high-quality content for websites, blogs, social media platforms, or marketing materials. It can quickly produce engaging articles, product descriptions, promotional content, and more so time and resources can be saved. It can generate text tailored to specific target audiences that can help businesses drive conversions and enhance their marketing efforts.

                **2. Customer Support and FAQs**

                It can be used to automate customer support processes by generating responses to common customer inquiries or frequently asked questions. This can help provide instant, accurate, and consistent support that improve customer satisfaction and reduce the workload on support teams.

                **3. Internal Communication and Documentation**

                It can assist in creating internal communication materials, such as employee newsletters, memos, or reports. It can generate concise summaries of lengthy documents, assist in drafting emails, or provide writing assistance to improve overall communication within the organization.

                **4. Idea Generation and Brainstorming**

                Its ability to generate text based on prompts can be valuable during idea generation and brainstorming sessions. It can provide diverse perspectives, suggest creative solutions, or offer alternative viewpoints. This helps organizations explore new ideas and approaches.

                These are just a few examples of how ContentGenius can be used. Its versatility, speed, and accuracy in generating text content make it a valuable asset for organizations across industries, enhancing productivity, improving customer experiences, and supporting various functions.
               
                """
                    )
        
    
    with tab3:
        st.markdown(
        """
        ### Customization
        """)

        image_path = "app/images/congenius_customization.jpg"
        imageM = Image.open(image_path)
        st.image(imageM, caption="Image by Monoar Rahman Rony from Pixabay", width=600)        

        st.write("""                  
                ContentGenius offers various customization options to tailor its text generation capabilities to your specific needs. Here are some key customization features:

                **1. Prompt Engineering**

                You can customize the prompts to influence the generated output. By refining and optimizing them, you can guide the app to generate text that aligns with your desired style, tone, or specific requirements. You can also specify the desired length of the generated text. 

                **2. Style and Tone**

                You can customize the style and tone of the generated text. For example, you can request it to generate content in a formal or informal tone, adjust the level of technicality, or specify a specific writing style (e.g., professional, conversational, persuasive).

                **3. Domain-Specific Fine-Tuning**

                It can be fine-tuned on specific domains or datasets to enhance its performance in generating content for your industry or certain topics. You can provide additional training data or domain-specific prompts to improve its understanding and output quality in a specific field.

                By leveraging these customization features, you can fine-tune ContentGenius to generate text that suits to your specific needs, whether it iss for marketing content, customer support, internal communication, or any other use case relevant to their business.
                
                """
                )   


    with tab4:        
        st.markdown(
        """
        ### Provide a specific prompt or topic

        """)   

        configure_generative_ai()
        model_name = "gemini-pro"
        model = initialize_generative_model(model_name)

        input_text = st.text_input("Write here: ", key='input')
        submit_button = st.button("Ask the question")

        if submit_button:
            response_text = get_response(model, input_text)
            st.subheader("The response is")
            st.write(response_text)

if __name__ == "__main__":
    content_generation()
