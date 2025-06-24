from dotenv import load_dotenv
load_dotenv()

import streamlit as st 
import os
import google.generativeai as genai 
from PIL import Image

# from google.oauth2.credentials import Credentials
# from google.auth.transport.requests import Request
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build

from pages.footnote import showHeader, showFooter

def get_response(input_text, input_image):
    genai.configure(api_key=os.getenv("GOOGGLE_API_KEY"))
    model = genai.GenerativeModel("gemini-pro-vision")
    if input_text != "":
        response = model.generate_content([input_text, input_image])
    else:
        response = model.generate_content(input_image)
    return response.text


def image_content():
    showHeader()
    showFooter()
    
    st.title("Image2Blog")
    
    st.caption("*by* [*Joseph B. Rivera*]()")

    st.markdown("<br>", unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Usage", "Customization", "Test our Product"])

    with tab1:
        st.markdown(
        """
        ### Overview
        """)

        image_path = "app/images/im2blog_overview.jpg"
        imageM = Image.open(image_path)
        st.image(imageM, caption="Image by Paul Barlow from Pixabay", width=600)

        st.write(""" 
                Image2blog is an advanced artificial intelligence (AI) application that harnesses cutting-edge algorithms to convert visual imagery into a text. With its powerful blend of computer vision and natural language processing (NLP) technologies, this innovative tool empowers users to extract meaningful information by interpreting visual cues to generate meaningful textual representations based on inputted images.

                It goes beyond mere object recognition. It analyzes visual features, identifies relevant details, and makes coherent and informative descriptions. It strives to comprehend the context and relationships within the images, including spatial arrangements, object interactions, and even the subtle portrayal of emotions or sentiments. Moreover, it stimulates creative expression by providing a novel medium for generating descriptive and contextually rich text based on visual prompts, inspiring content creators across various domains. Thus, it opens up a realm of new possibilities for content analysis, accessibility, and creative expression.

                Transforming visual information into textual descriptions holds immense significance in facilitating accessibility for individuals with visual impairments. By converting visual content into text, it provides an alternative means for people who are visually impaired to perceive and comprehend visual information that would otherwise be inaccessible to them. Thus, they gain a deeper understanding of the visual content.

                With its focus on accuracy, context comprehension, and the exploration of visual narratives, Image2blog represents an exciting advancement in the field of AI-driven image-to-text conversion. It empowers users to unlock the potential of visual imagery in a textual format, revolutionizing industries, promoting accessibility, and fostering creativity.                
                """
                )
        
    with tab2:
        st.markdown(
        """
        ### Usage
        """)

        image_path = "app/images/im2blog_usage.jpg"
        imageM = Image.open(image_path)
        st.image(imageM, caption="Image by Jürgen from Pixabay", width=600)

        st.write("""                  
                Image2blog is a powerful AI application that offers a range of practical applications in various domains. Below are some of the several essential applications:

                **1. Accessibility for Visually Impaired Individuals**

                It enhances accessibility for individuals with visual impairments. By converting visual information into descriptive and contextual text, the app enables visually impaired individuals to access and comprehend visual contents that would otherwise be inaccessible to them. Whether it is images on websites, social media posts, educational materials, or any other visual content, it empowers them to perceive and understand them more effectively, fostering inclusivity and equal access to information.

                **2. Content Analysis and Description** 

                It can be a valuable tool for content analysis and description in various domains. For example, in the field of e-commerce, it can automatically generate detailed product descriptions based on product images that makes it easier for businesses to create comprehensive and engaging listings. In the field of media and entertainment, it can assist in generating textual summaries and descriptions of videos or multimedia content that facilitates content indexing and searchability. Additionally, in fields like art, design, or photography, it can provide rich textual descriptions of visual works that aides in cataloging, analysis, and curation.

                **3. Creative Writing and Content Creation** 

                It can serve as an inspirational tool for creative writing and content creation. Writers, bloggers, marketers, and advertisers can use it to generate vivid descriptions, story ideas, or ad copy based on visual prompts. By analyzing the visual features and context of images, it can spark creative ideas and provide unique perspectives that can be further developed into engaging narratives, articles, or marketing campaigns.

                These are just a few examples of the potential usages of the Image2blog app. Its versatility and ability to bridge the gap between visual content and textual representation offer opportunities for accessibility, content analysis, and creative endeavors across various industries and domains.

                """
                    )
        
    
    with tab3:
        st.markdown(
        """
        ### Customization
        """)

        image_path = "app/images/im2blog_customization.jpg"
        imageM = Image.open(image_path)
        st.image(imageM, caption="Image by Enrique from Pixabay", width=600)

        st.write("""                  
                There several more ways in which Image2blog can be customized to meet users' specific needs and preferences. These customization features enable users to have greater control, flexibility, and satisfaction.

                **1. Contextual Customization**

                It offers contextual customization options to align the generated text descriptions with specific contexts or domains. For instance, you can specify the intended audience or industry to allow the app to generate descriptions that are tailored to that particular context. This ensures that the generated text is not only accurate but also relevant and meaningful within the given context.

                **2. Image Recognition Customization** 

                Image2blog can provide customization features related to image recognition. You can specify certain objects, concepts, or features you want the app to focus on or exclude from the generated descriptions. This level of customization allows you to fine-tune the app's analysis and description of specific elements in the images to provide more targeted and precise textual representations.

                **3. Output Customization** 

                You can ask the app to use the style you want in the generated text, adding personal preferences for enjoyment. This customization feature can greatly enhance the accessibility and make it more inclusive and engaging for a wider range of users.

                By offering a wide range of customization options, Image2blog empowers you to personalize their experience, align the app with their specific requirements, and optimize its functionalities to suit their unique needs.

                """
                )   


    with tab4:        
        st.markdown(
        """
        ### Provide a specific prompt or topic

        """) 

        input_text = st.text_input("Input Prompt: ", key='input')
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
        input_image = ""

        if uploaded_file is not None:
            input_image = Image.open(uploaded_file)
            st.image(input_image, caption="Uploaded Image.", use_column_width=True)

        submit_button = st.button("Tell me something about the image.")

        if submit_button:
            response_text = get_response(input_text, input_image)
            st.subheader("The response is")
            st.write(response_text)

if __name__ == "__main__":
    image_content()
