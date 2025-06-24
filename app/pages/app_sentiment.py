import os
import joblib
import tweepy
import time
import re
import logging
import string
from datetime import datetime
import streamlit as st
import plotly_express as px
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from config import TRIAL_ACCESS

# from translator import Translator
from utilities.utils_language import get_language, remove_enter, translate_to_eng
from google.cloud import translate_v2 as translate
#from .twitter.twitter_search import get_tweets, tw_oauth
from textblob.translate import Translator
from textblob import TextBlob
from time import sleep
from matplotlib.colors import LinearSegmentedColormap
from wordcloud import WordCloud
from ast import literal_eval
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')
from pages.footnote import showHeader, showFooter

def app_sentiment():

    showHeader()
    showFooter()

    # configuration
    st.set_option('deprecation.showfileUploaderEncoding', False)

    # title of the app
    st.title("Sentiment Analysis")

    st.caption("*by* [*Kristian Villaruz*]() & [*Anne Clara Arrobio*]()")

    tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Usage", "Customization", "Test our Product"])
    with tab1:
        st.markdown(
            """
            ### Introduction
            """)
        st.write("""
                 
            The sentiment analysis app offers a robust solution for analyzing and interpreting sentiments expressed in text data. It utilizes advanced natural language processing and machine learning algorithms to accurately identify and classify sentiments. By providing comprehensive insights into customer opinions and perceptions, this app empowers businesses to make data-driven decisions.

            The app employs state-of-the-art natural language processing techniques to extract sentiments from textual data. It utilizes machine learning algorithms that have been trained on diverse datasets to ensure accurate sentiment classification. The app can handle a wide range of text sources, including social media posts, customer reviews, surveys, and news articles, allowing businesses to analyze sentiments from various channels.

            The app prioritizes user-friendliness and features an intuitive and easy-to-navigate interface. Users can seamlessly analyze sentiments in their text data, regardless of their technical background. The app supports multiple input formats, including text files, social media posts, and customer reviews, making it adaptable to various data sources.

            This app delivers a comprehensive solution for businesses seeking to understand and leverage customer sentiment. By utilizing it, they can gain valuable insights, make informed decisions, and enhance their products and services based on customer feedback.

            """)

    with tab2:
        st.markdown(
            """
            ### Usage
            """)
        st.write("""

            The uses of sentiment analysis app extend to various industries, such as e-commerce, hospitality, healthcare, and finance, where understanding and leveraging customer sentiment is key to success in today's highly competitive market. Here are some of its uses:

            **1. Social Media Monitoring** 

            Businesses can use the sentiment analysis app to monitor and analyze sentiments expressed on social media platforms. By tracking mentions, hashtags, and comments related to their brand or industry, they can gain insights into how their products or services are perceived by customers. This allows them to identify trends, detect potential issues, and respond promptly to customer feedback so they can improve their brand reputation and customer satisfaction.

            **2. Customer Feedback Analysis** 

            The sentiment analysis app is a valuable tools for analyzing online reviews, surveys, and customer support interactions. By automatically categorizing sentiments as positive, negative, or neutral, businesses can quickly identify common pain points or areas of improvement. This enables them to take targeted actions to address customer concerns, enhance their products or services, and ultimately increase customer loyalty.

            **3. Market Research** 

            This sentiment analysis app can be used to understand consumer opinions and preferences. By analyzing sentiments expressed in online forums, blogs, and news articles, businesses can gather valuable insights on consumer sentiment towards their brand, competitors, or industry. This information helps them make informed decisions, develop effective marketing strategies, and identify emerging trends to stay ahead of the competition.

            **4. Brand Reputation Management** 

            This sentiment analysis app can play a vital role in monitoring and managing brand reputation by automatically analyzing sentiments associated with the brand across various channels. By promptly identifying and addressing negative sentiments or potential crises, businesses can protect their brand image, mitigate reputational damage, and maintain a positive perception among their target audience.

            """)

    with tab3:
        st.markdown(
            """
            ### Customization
            """)
        st.write("""
            The sentiment analysis app can be customized in several ways to meet specific business needs and requirements. 

            **1. Domain-Specific Sentiment Lexicons** 

            The app's lexicon can be customized by incorporating domain-specific sentiment lexicons that capture industry-specific language and sentiments. This ensures that the app accurately interprets sentiments specific to the business domain.

            **2. Custom Sentiment Categories** 

            The app can be customized to detect and classify sentiments beyond the typical positive, negative, or neutral categories. Businesses can define their own sentiment categories that align with their specific needs. This allows them to focus on the aspects that matter most.

            **3. Integration with Internal Systems** 

            The app can be customized to integrate with internal systems or software used by the business. This integration enables seamless data transfer and analysis that allows businesses to analyze sentiments from their own databases, customer relationship management (CRM) systems, or feedback platforms.

            **4. User Interface Customization** 

            The app's user interface can be customized to align with the branding and visual preferences of the business. This includes customizing color schemes, logos, and layout designs. This not only enhances the user experience but also creates a cohesive and branded look and feel.

            **5. Custom Reporting and Analytics** 

            The app can be customized to generate reports and visualizations that align with business needs. This includes customizing the types of charts, graphs, or data visualizations used, as well as providing flexibility in the selection and presentation of sentiment analysis metrics and insights.

            """)
                 
    with tab4:
        st.markdown(
            """
            ### Test our Product
            """)

        st.warning("Note: For trial access, only first 30 rows will be used in sentiment analysis.")

        global df

        sample_data = pd.read_csv(r'app/data/amazondata.csv')

        uploaded_file = (
            st.file_uploader(label="Upload your CSV or Excel file. Please upload data with a column for the sentiments. ",
                             type=['csv', 'xlsx', 'xls']))
        if uploaded_file is None:
            st.write("You can use sample data. Click the button below.")
            st.download_button(label="Download sample amazondata.csv data",
                               data=sample_data.to_csv(index = False).encode('utf-8'),
                               file_name='amazondata.csv')

        if uploaded_file is None:
            st.empty()
        elif uploaded_file.type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' and uploaded_file is not None:
            try:
                df = pd.read_excel(uploaded_file)
            except:
                st.error("Please make sure to follow the data format.")
        else:
            try:
                df = pd.read_csv(uploaded_file)
            except:
                st.error("Please make sure to follow the data format.")
        if uploaded_file is not None and TRIAL_ACCESS:
            df = df.head(10)

        global numeric_columns
        global non_numeric_columns

        data_dir = 'data'
        models_dir = r'app/models/sentiment_analysis'

        src = 'app'
        data = 'SentimentAnalysisDemoData.csv'
        model = 'multinomialnb.pkl'

        pipeline = joblib.load(f'{models_dir}/{model}')
        vectorizer = joblib.load(f'{models_dir}/vectorizer.pkl')


        def stop_remover(x, stop_list):
            lst = []
            for i in x:
                if i.lower() not in stop_list:
                    lst.append(i.lower())
            return lst


        def run_demo(df):
            #st.title("Sentiment Analysis")
            global feedback_column

            try:
                if uploaded_file is not None:
                    try:
                        numeric_columns = list(df.select_dtypes(['float', 'int']).columns)
                        non_numeric_columns = list(df.select_dtypes(['object']).columns)
                        non_numeric_columns.append(None)
                        print(non_numeric_columns)
                    except Exception as e:
                        print(e)

                    col1, col2 = st.columns(2)
                    with col1:
                        table_select = st.selectbox(
                            label="Show the first 15 rows of the uploaded data?",
                            options=['Show', 'Hide']
                        )
                    with col2:
                        # st.subheader("Data Sentiment Analysis")
                        feedback_column = st.selectbox(
                            label="Please select the sentiment column.",
                            options=df.columns
                        )

                    if table_select == 'Show':
                        st.markdown("#### First 15 Rows")
                        st.dataframe(data=df.head(15))

                    print(f'Feedback column: {feedback_column}\ttype: {type(feedback_column)}')

                    if st.button("Process Data"):
                        df['translated'] = ''
                        df['sentiment'] = ''
                        feedbacks = df[feedback_column].values
                        f = st.empty()
                        t = st.empty()
                        s = st.empty()

                        with st.spinner(text="Analyzing sentiments..."):
                            for index, row in df.iterrows():  # feedback in feedbacks:

                                f.markdown(f'Feedback: {row[feedback_column]}')
                                time.sleep(1.0)
                                translated = translate_to_eng(row[feedback_column])
                                t.markdown(f'English Translation: {translated}')
                                # time.sleep(1.0)
                                #st.write(translated)
                                vect = vectorizer.transform(translated)
                                sentiment = pipeline.predict(vect)[0]
                                s.markdown(f'Sentiment: {sentiment}')
                                time.sleep(1.0)
                                f.markdown('')
                                t.markdown('')
                                s.markdown('')
                                df.at[index, 'translated'] = translated
                                df.at[index, 'sentiment'] = sentiment
                                time.sleep(1.0)
                        st.subheader("First 15 Rows Sentiment")
                        st.dataframe(data=df)

                        # Cleaning the original reviews for wordcloud output
                        stopwords = pd.read_csv('data/sentiment_analysis/stopwords.txt', sep=' ', header=None)
                        stopwords.columns = ['words']
                        custom = ['sana', 'po', 'yung', 'mas', 'ma', 'kasi', 'ninyo', 'kayo', 'nya', 'pag', 'naman', 'lang', 'no',
                                  'comment']
                        stop_list = stopwords['words'].values.tolist() + custom

                        # Applying Word Tokenization
                        df['word_tokenized'] = df[feedback_column].apply(word_tokenize)
                        df[feedback_column] = df['word_tokenized'].apply(lambda x: stop_remover(x, stop_list))
                        df[feedback_column] = df[feedback_column].apply(lambda x: ' '.join(x))
                        df = df.drop(['word_tokenized'], axis=1)
                        df.to_csv('data/sentiment_analysis/SentimentAnalysis.csv')

                        show_wordcloud(df)
            except Exception as e:
                print(e)


        def show_wordcloud(df):
            try:
                df_cat = {}
                comb = {}
                long_str = {}
                wordcloud = {}
                categories = list(set(df["sentiment"].tolist()))
                print(categories)
                colors = ["#BF0A30", "#002868"]
                cmap = LinearSegmentedColormap.from_list("mycmap", colors)

                for cat in categories:
                    df_cat[cat] = df[df["sentiment"] == cat]
                    comb[cat] = df_cat[cat][feedback_column].values.tolist()
                    long_str[cat] = ' '.join(comb[cat])

                    wordcloud[cat] = WordCloud(background_color="white", colormap=cmap, width=1000,
                                               height=300, max_font_size=500, relative_scaling=0.3,
                                               min_font_size=5)
                    wordcloud[cat].generate(long_str[cat])

                    st.subheader(f"Category {cat}")
                    st.image(image=wordcloud[cat].to_image(), caption=f"Category {cat}")

            except Exception as e:
                print(f'Exception: {e}')


        def tw_search():
            try:
                st.sidebar.subheader("Twitter Search")
                keywords = st.sidebar.text_input("Keyword")
                api = tw_oauth()

                tweet_list = {
                    'source': [],
                    'tweet': [],
                    'date_posted': [],
                    'translated': [],
                    'sentiment': []
                }

                f = st.empty()
                t = st.empty()
                s = st.empty()

                if keywords:
                    tweets = tweepy.Cursor(api.search, q=keywords)

                    for tweet in tweets.items():
                        row = remove_enter(tweet.text)

                        if row not in tweet_list['tweet']:
                            f.markdown(f'Tweet: {row}')
                            time.sleep(2.0)

                            translated = translate_to_eng(row)
                            t.markdown(f'English Transation: {translated}')
                            time.sleep(2.0)

                            vect = vectorizer.transform(translated)
                            sentiment = pipeline.predict(vect)[0]
                            s.markdown(f'Sentiment: {sentiment}')

                            time.sleep(3.0)
                            f.markdown('')
                            t.markdown('')
                            s.markdown('')

                            tweet_list['source'].append('Twitter')
                            tweet_list['tweet'].append(row)
                            tweet_list['date_posted'].append(tweet.created_at)
                            tweet_list['translated'].append(translated)
                            tweet_list['sentiment'].append(sentiment)

                    tweet_df = pd.DataFrame(tweet_list)
                    tweet_df.to_csv(f'LandbankTwitter{datetime.today()}.csv', index=False)
            except Exception as e:
                print(f"Error Except: {e}")

        try:
            run_demo(df)
        except Exception as e:
            #tw_search()
            print(e)
            st.empty()


#app_sentiment()










































