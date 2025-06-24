import streamlit as st

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import random
import os
import pickle

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import OneClassSVM
from sklearn.ensemble import IsolationForest
from sklearn.decomposition import PCA

from sklearn.pipeline import Pipeline

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_recall_curve

# import eif

from pages.footnote import showHeader, showFooter

# Helper Functions


def getCounts(df, col="is_anomaly"):
    df_counts = df[col].value_counts().to_frame()
    df_counts["pct"] = df[col].value_counts(normalize=True)
    return df_counts


def get_min_pcs(X, n=0.99):
    pca = PCA(svd_solver="full")
    new_X2 = pca.fit_transform(X)

    var_explained = pca.explained_variance_ratio_

    fig, ax = plt.subplots(1, 2, figsize=(16, 6))
    ax[0].plot(np.arange(1, len(var_explained) + 1), var_explained)
    ax[0].set_xlabel("PC")
    ax[0].set_ylabel("variance explained")

    cum_var_explained = var_explained.cumsum()
    ax[1].plot(np.arange(1, len(cum_var_explained) + 1), cum_var_explained, "-o")
    ax[1].set_ylim(bottom=0)
    ax[1].set_xlabel("PC")
    ax[1].set_ylabel("cumulative variance explained")

    return np.searchsorted(cum_var_explained, n) + 1


def plotConfMat(clf, X, y, **kwargs):
    y_pred = clf.predict(X)

    # map predictions to 0, 1
    if "mapper" in kwargs:
        y_pred = kwargs["mapper"](y_pred)

    # plot the confusion matrix
    confmat = confusion_matrix(y_true=y, y_pred=y_pred)

    fig, ax = plt.subplots(figsize=(4, 4))
    ax.matshow(confmat, cmap="Blues", alpha=0.3)

    for i in range(confmat.shape[0]):
        for j in range(confmat.shape[1]):
            ax.text(x=j, y=i, s=confmat[i, j], va="center", ha="center")
    ax.set_xlabel("Predicted Label")
    ax.set_ylabel("Actual Label")
    ax.grid(False)
    ax.vlines(x=0.5, ymin=-0.5, ymax=1.5, color=(0.8, 0.8, 0.8))
    ax.hlines(y=0.5, xmin=-0.5, xmax=1.5, color=(0.8, 0.8, 0.8))

    # design
    if "title" in kwargs:
        fig.suptitle(
            kwargs["title"],
        )
        print(kwargs["title"])

    if "ticklabels" in kwargs:
        ticklabels = kwargs["ticklabels"]
        ax.set_xticklabels([""] + ticklabels)
        ax.set_yticklabels([""] + ticklabels)
        print(classification_report(y, y_pred, target_names=kwargs["ticklabels"]))
    else:
        print(classification_report(y, y_pred))

    plt.tight_layout()

    return fig


def mapPreds(x):
    if x == -1:
        return 1
    elif x == 1:
        return 0
    else:
        return x


def process_data(df1, df2):
    # Check the Null Values
    st.write("Check the number of null values in the data.")
    st.write(df1.isna().sum())
    st.write(df2.isna().sum())
    st.write("Filled in null values with mean of each column.")
    df1.dropna(inplace=True)
    df2.dropna(inplace=True)

    # Train-Val-Test Split

    st.subheader("Train-Val-Test Split")

    df1.drop("Date", axis=1, inplace=True)
    df2.drop("Date", axis=1, inplace=True)

    # anomaly = df1[df1.is_anomaly==1]
    # non_anomaly  = df1[df1.is_anomaly==0]

    code1 = """anomaly = df1[df1.is_anomaly==1]
    non_anomaly  = df1[df1.is_anomaly==0]"""
    st.code(code1, language="python")

    RANDOM_SEED = 42

    # split the not_impacted data, the test+val size is equal to the count of impacted
    # train, val = train_test_split(df1,test_size=0.4,shuffle =True, random_state=RANDOM_SEED, stratify=anomaly)

    getCounts(df1)
    getCounts(df2)

    X_train = df1.drop("is_anomaly", axis=1)
    y_train = df1["is_anomaly"]

    X_test = df2.drop("is_anomaly", axis=1)
    y_test = df2["is_anomaly"]

    code2 = """X_train = df1.drop('is_anomaly', axis=1)
    y_train = df1['is_anomaly']

    X_test = df2.drop('is_anomaly', axis=1)
    y_test = df2['is_anomaly']"""
    st.code(code2, language="python")

    # Scaling

    st.subheader("Scaling")

    scaler = MinMaxScaler()

    X_train_scaled = scaler.fit_transform(X_train)

    code3 = """scaler = MinMaxScaler()

    X_train_scaled = scaler.fit_transform(X_train)"""
    st.code(code3, language="python")

    min_pcs = get_min_pcs(X_train_scaled)
    print(min_pcs)
    # st.pyplot(min_pcs)

    pca = PCA(n_components=min_pcs, svd_solver="full")
    X_train_pca = pca.fit_transform(X_train_scaled)

    # One Class SVM

    st.subheader("One Class SVM")

    map_Preds = np.vectorize(mapPreds)

    clf_svm = OneClassSVM(gamma="scale", nu=0.05, verbose=True)
    svm_model = Pipeline(
        [("scaler", scaler), ("pca", pca), ("clf", clf_svm)], verbose=True
    )
    svm_model.fit(X_train)

    # plotConfMat(svm_model, X_train, y_train, title='OneClassSVM Train Set')
    ConfMat = plotConfMat(
        svm_model,
        X_test,
        y_test,
        title="OneClassSVM Test Set",
        mapper=map_Preds,
        ticklabels=["Not Anomaly", "Anomaly"],
    )
    st.pyplot(ConfMat)

    # note
    st.subheader("Want some help?")
    st.text(
        """For more help with your Anomaly Detection needs, feel free to contact us 
        at dsa.info@mdinovare.com."""
    )


def anomaly_app():
    showHeader()
    showFooter()

    st.title("Anomaly Detection")
    #st.header("One Class SVM")

    st.markdown("<br>", unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(
        ["Overview", "Usage", "Customization", "Test our Product"]
    )

    with tab1:
        st.markdown(
            """
            ### Introduction
            """
        )
        st.write("""
            In today's rapidly evolving digital landscape, where the sheer volume and complexity of data pose considerable challenges, anomalies can exert profound effects on businesses. Ranging from potential security breaches to operational inefficiencies, the ramifications underscore the need for robust anomaly detection tools. This anomaly detection app stands as a powerful solution meticulously designed to help businesses identify and rectify irregularities within their data. Using advanced machine learning algorithms, this app automatically detects and flags any unusual patterns or outliers, furnishing businesses with invaluable insights and actionable information.

            A pivotal feature of this app lies in its ability to analyze extensive volumes of data in real-time. Continuously monitoring incoming data streams, it swiftly identifies deviations from expected patterns that empowers businesses to proactively respond to potential issues. This real-time detection capability proves especially critical in industries like finance, cybersecurity, and manufacturing, where prompt intervention can avert substantial losses or damages.

            Beyond real-time monitoring, the app distinguishes itself through its flexibility and adaptability. Seamlessly integrating into existing data systems, it can be effortlessly customized to cater to the specific needs of diverse industries and use cases. Whether tasked with monitoring customer transactions, network traffic, or equipment performance, it can be tailored to suit one's unique requirements. Additionally, incorporating a user-friendly interface can be prioritized to facilitate intuitive data exploration and visualization. This ensures accessibility for both data experts and non-technical users alike.

            Security is paramount, acknowledging the sensitivity of the data under analysis and the need to protect it from unauthorized access. The app employs robust encryption and access control measures that guarantee the confidentiality and integrity of the data. Moreover, the highest data privacy standards are adhered to, ensuring compliance with relevant regulations. This commitment provides organizations with peace of mind, assuring the secure utilization of the app in alignment with stringent privacy protocols.
            """)
                 
    with tab2:
        st.markdown(
            """
            ### Usage
            """
        )
        st.write("""
            The anomaly detection application finds different uses across various industries because of its ability to identify irregular patterns or deviations from expected behavior within datasets. Some notable usages include:

            **1. Fraud Detection** 

            The anomaly detection app is widely used in the financial industry to detect fraudulent activities. By analyzing patterns and behaviors in transactions, it can identify unusual activities such as unauthorized access, suspicious transactions, or unusual spending patterns. This helps financial institutions and businesses prevent financial losses and protect their customers from fraudulent activities.

            **2. Network Security** 

            The anomaly detection app also plays a crucial role in identifying and preventing cybersecurity threats. It monitors network traffic and detect any abnormal behaviors or activities that may indicate a security breach or intrusion attempt. By analyzing network data in real-time, it can quickly identify and respond to potential threats, helping organizations protect their sensitive data and maintain the integrity of their networks.

            **3. Equipment and Asset Monitoring** 

            The anomaly detection app is a valuable tool in industries that rely on equipment and asset performance, such as manufacturing, energy, and healthcare. It can monitor sensor data, machine metrics, or equipment performance indicators to identify deviations from normal operating conditions. with this, businesses can proactively address potential equipment failures, minimize downtime, and optimize maintenance schedules. As a result, they save costs and improve operational efficiency.

            **4. Quality Assurance** 

            The anomaly detection app is also used in quality assurance processes to identify defects or inconsistencies in products or services. By analyzing data from production lines, customer feedback, or quality control metrics, it can detect anomalies that may indicate manufacturing defects, service errors, or deviations from established quality standards. This enables businesses to take corrective actions to improve product quality, enhance customer satisfaction, and maintain their brand reputation.
            """)
    
    with tab3:
        st.markdown(
            """
            ### Customization
            """
        )
        st.write("""
            The anomaly detection application can be customized in a number of ways. These customization options empower businesses to adapt the app to their specific data, objectives, and operational workflows.  Here are ways in which it can be customized:

            **1. Threshold Customization**
            
            Users can define their own thresholds. This customization enables businesses to set specific criteria based on their unique requirements and domain knowledge. They can adjust parameters such as the level of deviation from normal behavior that triggers an anomaly alert, the sensitivity of the detection algorithm, or the confidence level required to flag an anomaly. This flexibility allows businesses to fine-tune the app's performance to their specific needs.

            **2. Feature Selection** 

            Users can select and prioritize the features or variables to be analyzed. Different variables may have varying degrees of importance or relevance in detecting anomalies depending on the specific use case. By allowing them to choose which features to include or exclude from the analysis, the app can focus on the most critical aspects of the data and improve detection accuracy. This customization empowers businesses to tailor the app to their specific data characteristics and objectives.

            **3. Alert and Notification Setting** 

            The anomaly detection app can be customized by giving users control over the alert and notification settings. Users can define the preferred communication channels (e.g., email, SMS, dashboard notifications) and set the frequency and severity of alerts according to their operational needs. This customization allows businesses to prioritize and manage the alerts based on their specific workflows, ensuring that relevant stakeholders are promptly informed about detected anomalies. Users can also customize the format and content of the alerts to provide actionable information and facilitate efficient response and investigation processes.

            """)
    
    with tab4:
        st.markdown(
            """
            ### Test our Product
            """
        )

        random.seed(42)
        np.random.seed(42)

        # Data Preparation

        #st.subheader("Data Preparation")
        st.markdown(
            '**Naming Columns:** Prepare your data set as follows: First, name the unique identifier column exactly "ID" (without the quotation marks). Second, name the date-time column "Date". Third, name the column that determines an anomaly as either 1 or 0 as "is_anomaly".'
        )
        st.markdown(
            "**Splitting Data by Year:** Split your data by year into two separate CSV files, df1.csv and df2.csv, where df1 contains the data from earlier years and df2 contains the data for the current or latest year."
        )

        sample_data1 = pd.read_csv(r'app/data/df1_chunk0.csv')
        sample_data2 = pd.read_csv(r'app/data/df2_chunk0.csv')
        
        fu1 = st.file_uploader("Upload df1.csv")
        fu2 = st.file_uploader("Upload df2.csv")
        
        if fu1 is None:
            st.write("You can use this sample dataset as df1. Click the button below.")
            st.download_button(label="Download df1.csv data",
                               data=sample_data1.to_csv(index = False).encode('utf-8'),
                               file_name='df1_chunk0.csv')
        if fu2 is None:
            st.write("You can use this sample dataset as df2. Click the button below.")
            st.download_button(label="Download df2.csv data",
                               data=sample_data2.to_csv(index = False).encode('utf-8'),
                               file_name='df2_chunk0.csv')
            
        if fu1 is not None and fu2 is not None:
            df1 = pd.read_csv(fu1)
            st.write("Display the df1 dataframe.")
            df1.set_index("ID", inplace=True)
            st.dataframe(df1)

            code_a = """df1.set_index('ID', inplace=True)"""
            st.code(code_a, language="python")

            df2 = pd.read_csv(fu2)
            st.write("Display the df2 dataframe.")
            df2.set_index("ID", inplace=True)

            code_a = """df2.set_index('ID', inplace=True)"""
            st.code(code_a, language="python")
            st.dataframe(df2)

            process_data(df1, df2)
