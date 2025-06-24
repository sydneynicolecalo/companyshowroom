import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly
from prophet.diagnostics import cross_validation
from prophet.diagnostics import performance_metrics
from prophet.plot import plot_cross_validation_metric
from pages.footnote import *

def fbprophet():
    showHeader()
    showFooter()

    # configuration
    st.set_option('deprecation.showfileUploaderEncoding', False)

    # Title
    st.title('Time Series Forecasting')

    st.caption("*by* [*Kristian Villaruz*]() & [Anne Clara Arrobio]()")

    # local_css('style.css')

    tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Usage", "Customization","Test our Product"])
    with tab1:
        st.markdown(
            """
            ### Introduction
            """)
        st.write("Making scientific projections based on data with historical time stamps is known as time series forecasting. It entails creating models through historical study, using them to draw conclusions and guide strategic decision-making in the future. The fact that the future result is wholly unknown at the time of the task and can only be anticipated through thorough analysis and evidence-based priors is an essential distinction in forecasting.")
        st.write("In order to produce forecasts and guide strategic decision-making, time series forecasting involves examining time series data using statistics and modeling. It's not always an accurate prediction, and forecast probabilities might vary greatly—especially when dealing with the variables that frequently fluctuate in time series data and with outside influences. predictive knowledge about whether events are more or less likely than other possible outcomes, though. Frequently, the projections might be more accurate the more complete the data we have. There is a significant difference between forecasting and 'prediction', even though they often mean the same thing. While prediction refers to future data generally, forecasting in some industries may relate to data at a specific future time point. Frequently, series forecasting.")

    with tab2:
        st.markdown(
            """
            ### Usage
            """)
        st.write("Numerous industries use forecasting in a variety of ways. Weather forecasting, climate forecasting, economic forecasting, healthcare forecasting, engineering forecasting, finance forecasting, retail forecasting, business forecasting, environmental studies forecasting, social studies forecasting, and many more practical applications are among them. Anyone who has reliable historical data can use time series analysis techniques to study it before modeling, forecasting, and predicting. The sole purpose of time series analysis for some companies is to make forecasting easier. Some technologies, like augmented analytics, can even choose forecasting as the best statistical technique if it provides the highest level of assurance.")

    with tab3:
        st.markdown(
            """
            ### Customization
            """)
        st.write("Naturally, when dealing with the unpredictable and the unknown, there are bounds. Time series forecasting isn't perfect, and not every case calls for it. The onus is on analysts and data teams to understand the boundaries of analysis and what their models can enable because there really isn't a clear-cut set of guidelines for when you should or shouldn't utilize forecasting. Every model won't fit every set of data or provide a response to every query. When data teams have the necessary data and forecasting capabilities to address a business concern, they should use time series forecasting. With clean, time-stamped data, good forecasting can find the real trends and patterns in past data. Analysts are able to distinguish between true insights and seasonal oscillations, as well as between random fluctuations and outliers. Data varies over time, as shown by time series analysis, and accurate forecasting can demonstrate which way the data is changing.")
    with tab4:
        st.markdown(
            """
            ### Test our Product
            """)

        # Data Preparation
        # Setup file upload
        sample_data = pd.read_csv(r'app/data/loan.csv')

        uploaded_file = (st.file_uploader(label="Upload your CSV or Excel file. Please follow the format in sample file below. ",
                                                  type=['csv', 'xlsx', 'xls']))
        if uploaded_file is None:
            st.write("You can use sample data. Click the button below.")
            st.download_button(label="Download sample loan.csv data",
                                                     data=sample_data.to_csv(index = False).encode('utf-8'),
                                                     file_name='loan.csv')

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

        if uploaded_file is not None:
            # Add a sidebar
            st.markdown('##### Parameter Settings')

            col1, col2, col3 = st.columns(3)
            # Horizon Forecast
            # st.markdown('#### Forecast Horizon')
            with col1:
                period_select = st.selectbox(
                    label="Select periods to predict",
                    options=['One month', 'Three months', 'Six months', 'One year']
                )
                # Holidays
                # st.subheader('Holidays')
                holidays = st.selectbox(
                    label="Add Holidays",
                    options=[True, False]
                )

            global period
            if period_select == 'One month':
                period = 30
            elif period_select == 'Three month':
                period = 91
            elif period_select == 'Six month':
                period = 182
            else:
                period =365

            with col2:
                #Growth rate
                # st.subheader('Growth Rate')
                growth = st.selectbox(
                    label="Select growth rate",
                    options=['linear', 'flat']
                )

                # Confidence Interval
                # st.subheader('Confidence Interval')
                conlevel_select = st.selectbox(
                    label="Select confidence level",
                    options=[0.8, 0.9, 0.95, 0.99]
                )

            with col3:
                # Seasonality
                # st.subheader('Seasonality')
                mode = st.selectbox(
                    label="Set seasonality mode",
                    options=['additive', 'multiplicative']
                )


            ##################################################################################
            # FB Prophet
            # Model
            try:
                m = Prophet(seasonality_mode=mode, growth=growth, interval_width=conlevel_select, daily_seasonality=False, holidays = holidays)

                # Holidays
                if holidays == True:
                    m.add_country_holidays(country_name='PH')
                else:
                   pass

                # st.markdown("### First 15 rows")
                st.write(df.head(15))
                # Model Fit

                try:
                    m.fit(df)
                except Exception as e:
                    print(e)

                # Create Forecast Horizon
                future = m.make_future_dataframe(periods=period)
                # Model Predict
                forecast = m.predict(future)

                # Result
                result = pd.concat([forecast[['ds','yhat_lower','yhat_upper','yhat']], df['y']], axis=1)
                result = result.set_index('ds')

                result_plot = result.tail(period*2)
                fig, ax = plt.subplots(figsize=(20,10))

                result_plot.loc[:,'yhat'].plot(lw=2, ax=ax, color='r', ls='-', label='forecast')
                result_plot.loc[:,'y'].plot(lw=2, ax=ax, color='steelblue', ls='-', label='actual')

                ax.fill_between(result_plot.index, result_plot['yhat_lower'], result_plot['yhat_upper'], alpha=0.3,color='coral')
                ax.set_title('Actual and Forecasted Value', fontsize=18)
                ax.set_xlabel('Date',fontsize=15)
                ax.legend(fontsize=15)

                # Visualization
                st.markdown('### __Predictions__')
                st.write(fig)

                st.markdown('### __Forecast__')
                st.write(plot_plotly(m, forecast))
                st.markdown('### __Seasonality__')
                st.write(plot_components_plotly(m, forecast))

                # Output button for downloading predicted values
                output_button = st.download_button(
                    label="Download Predicted Values",
                    data=forecast.to_csv(index=False).encode('utf-8'),
                    file_name='predicted_values.csv',
                )

                # Display the button only when the forecast is available
                if output_button and forecast is not None:
                    st.markdown('### __Download Predicted Values__')
                    st.write(output_button)

                # Cross Validation
                df_cv = cross_validation(m, initial='730 days', period='180 days', horizon='365 days')
                df_p = performance_metrics(df_cv)

                st.markdown('### __Metrics__')
                st.markdown('#### __MAE Plot__')
                st.write(plot_cross_validation_metric(df_cv, metric='mae'))
                st.markdown('#### __Model Scores__')
                st.write(pd.DataFrame(np.mean(df_p), columns=['Scores']))

            except:
                # st.write("Error in modeling!")
                st.empty()

# Run the app
if __name__ == '__main__':
    fbprophet()
