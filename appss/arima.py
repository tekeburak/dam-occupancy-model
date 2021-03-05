import streamlit as st
import datetime
import matplotlib.pyplot as plt
import pickle
import os


def app():
	st.title("ARIMA Model")
	
	st.subheader('What does ARIMA model do?')
	st.markdown("""<p style='text-align: justify;'>Arima is a popular and widely used statistical method for time series forecasting. ARIMA is an acronym that stands for AutoRegressive Integrated Moving Average. It is a class of model that captures a suite of different standard temporal structures in time series data.</p>""", unsafe_allow_html=True)
	
	st.subheader('Why we chose ARIMA?')
	st.markdown("""<p style='text-align: justify;'>ARIMA is very popular statistical method and it is an answer to an important question that we need a more complex model or not. You can access our process of modeling from the link below.</p>""", unsafe_allow_html=True)	

	link = '[Process of ARIMA Modeling](https://github.com/tekeburak/dam-occupancy-model/blob/train_model/arima.ipynb)'
	st.markdown(link, unsafe_allow_html=True)

	st.subheader("Try out ARIMA Model")
	st.markdown("""<p style='text-align: justify;'>Train data 2005-01 -> 2018-08. Min date to forecast 2018-09</p>""", unsafe_allow_html=True)

	selected_date = st.date_input("Please, select a date.", min_value=datetime.date(2018, 9, 1))
	
	last_date = datetime.date(2018, 8, 1)

	subtract, add = 0, 0
	if selected_date.month < 8:
   		subtract = 8 - selected_date.month
	elif selected_date.month == 8:
		subtract  = 0
	else:
		add = selected_date.month - 8
	steps = (selected_date.year - last_date.year)*12+add-subtract
	
	
	
	
	load_model = pickle.load(open('./appss/arima_model.pkl', 'rb'))
	
	predictions = load_model.forecast(steps)[0]
	#st.write(predictions)
	
	fig, ax = plt.subplots()
	ax.plot(predictions)
	#add date to the x-axes
	#add data before the forecast with different color
	#add title
	st.pyplot(fig)