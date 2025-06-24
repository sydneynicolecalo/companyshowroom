import pandas as pd
#import pandas_profiling
import streamlit as st
from streamlit_pandas_profiling import st_profile_report
from pages.footnote import showHeader, showFooter
from config import TRIAL_ACCESS
from PIL import Image


def data_profiling():
    showHeader()
    showFooter()

    st.title("Data Profiling")
    st.write("*by* [*Leo Julongbayan*]()")

    tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Usage", "Customization","Test our Product"])
    #tab1, tab2, tab3, tab4 = st.columns(4)

    with tab1:
        #st.subheader("Introduction")
        st.markdown(
            """
            ### Introduction
            **Pandas-profiling** generates an interactive exploratory data analysis (EDA) tables and visualizations. 
            This tool is the extension of basic pandas function which automatically 
            generates a standardized univariate and multivariate report for data understanding. 
            """)
        imageB = Image.open(r"app/images/pandasprofilinglogo.png")
        st.image(imageB, caption="Image by Kaustubh Gupta", width=700)

        st.markdown(
            """    
            This application provides a lot of features that are useful in data exploratory, data quality checking, 
            basic data analysis for wide range of dataset and data types.
            
            The report contains three additional sections:

            *   **Overview**: mostly global details about the dataset (number of records, number of variables, overall missigness and duplicates, memory footprint)
            *   **Alerts**: a comprehensive and automatic list of potential data quality issues (high correlation, skewness, uniformity, zeros, missing values, constant values, between others)
            *   **Reproduction**: technical details about the analysis (time, version and configuration)
            
            """)

    with tab2:
        st.markdown("""
            ### Usage
            #### Data types
            Types, when going beyond the the logical data types such as integer, floats, etc, are a powerful 
            abstraction for effective data analysis, allowing analysis under higher level lenses. 
            Currently, pandas-profiling recognizes the following types:
            *    Boolean
            *    Numerical
            *    Date (and Datetime)
            *    Categorical
            *    URL
            *    Path
            *    File
            *    Image
            #### Data quality alerts
            """)
        imageB1 = Image.open(r"app/images/dataprofiling_alerts.png")
        st.image(imageB1)
        st.markdown("""
            The Alerts section of the report includes a comprehensive and automatic list of potential data quality issues. 
            Although useful, the decision on whether an alert is in fact a data quality issue always requires domain validation. 
            Some of the warnings refer to a specific column, others refer to inter-column relationships and others are 
            dataset-wide. 
            """)
        st.table()
        st.markdown("""
            For each column, the following information (whenever relevant for the column type) is presented in an interactive report:
            *   **Type inference**: detect the types of columns in a DataFrame
            *   **TEssentials**: type, unique values, indication of missing values
            *   **TQuantile statistics**: minimum value, Q1, median, Q3, maximum, range, interquartile range
            *   **TDescriptive statistics**: mean, mode, standard deviation, sum, median absolute deviation, coefficient of variation, kurtosis, skewness
            *   **TMost frequent and extreme values**
            *   **THistograms**: categorical and numerical
            *   **TCorrelations**: high correlation warnings, based on different correlation metrics (Spearman, Pearson, Kendall, Cramér’s V, Phik)
            *   **TMissing values**: through counts, matrix, heatmap and dendrograms
            *   **TDuplicate rows**: list of the most common duplicated rows
            *   **TText analysis**: most common categories (uppercase, lowercase, separator), scripts (Latin, Cyrillic) and blocks (ASCII, Cyrilic)
            *   **File and Image analysis**: file sizes, creation dates, dimensions, indication of truncated images and existance of EXIF metadata
            
            """)
    with tab3:
        st.markdown("""
            ### Customization
        """)

        st.write("You may have noticed that column summaries are specific to the data types of each feature in your data if you have used pandas-profiling in the past. The average surface area of a series of shapely geometries or the set of domain names in a series of email addresses could not, however, be automatically computed until recently because those summaries could not be customized. It is now possible to fully modify type identification logic, summary methods, and end-to-end report customisation, including customized renderings, thanks to the recently finished conversion of pandas-profiling to the visions type system.")
    with tab4:
        st.subheader("Product Preview")
        #st.write("Generate data profile report using pandas package!")

        sample_data = pd.read_csv(r'app/data/Titanic.csv')


        # Setup file upload
        uploaded_file = (st.file_uploader(label="Upload your CSV or Excel file. No data formatting required.",
                                                  type=['csv', 'xlsx', 'xls']))
        st.write("You can use sample data. Click the button below.")
        st.download_button(label="Download sample Titanic.csv data",
                                                 data=sample_data.to_csv(index=False).encode('utf-8'),
                                                 file_name='Titanic.csv')

        #st.write(uploaded_file)
        if uploaded_file is None:
            #st.error("Please enter dataset in the sidebar.")
            st.empty
        elif uploaded_file.type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' and uploaded_file is not None:
            try:
                df = pd.read_excel(uploaded_file)
            except:
                st.error("Please make sure to follow the data format.")
        else:
            df = pd.read_csv(uploaded_file)



        try:
            if uploaded_file:
                st.subheader(f"Analysis for {uploaded_file.name}")

                if TRIAL_ACCESS:
                    # Sampling the dataset for trial
                    st.warning("Note: For trial access, profiling will only be limited to first 5 columns and 100 randomized observations.")
                    df = df.sample(n=100, random_state=1)
                    df = df.iloc[:,:4]


        except:
            st.empty()

        try:
            pr = df.profile_report()
            st_profile_report(pr)
        except:
            st.empty()

