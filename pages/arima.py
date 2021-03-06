import streamlit as st
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import os

import matplotlib.dates as mdates
import plotly.graph_objects as go
from plotly import tools
import plotly.offline as py
import plotly.express as px

def app():
	st.title("ARIMA Model")
	
	st.subheader('What does ARIMA model do?')
	st.markdown("""<p style='text-align: justify;'>Arima is a popular and widely used statistical method for time series forecasting. ARIMA is an acronym that stands for AutoRegressive Integrated Moving Average. It is a class of model that captures a suite of different standard temporal structures in time series data.</p>""", unsafe_allow_html=True)
	
	st.subheader('Why we chose ARIMA?')
	st.markdown("""<p style='text-align: justify;'>ARIMA is very popular statistical method and it is an answer to an important question that we need a more complex model or not. You can access our process of modeling from the link below.</p>""", unsafe_allow_html=True)	

	link = '[Process of ARIMA Modeling](https://github.com/tekeburak/dam-occupancy-model/blob/train_model/notebooks/arima.ipynb)'
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
	
	
	load_model = pickle.load(open('models/arima_model.pkl', 'rb'))
	
	predictions = load_model.forecast(steps)[0]

	end_date = ""
	if selected_date.month <= 11:
		end_date = str(selected_date.year)+"-"+str(selected_date.month+1)
	else:
		end_date = str(selected_date.year+1)+"-"+"01"
	dates = pd.date_range(start="2018-09",end=end_date, freq='M').values
	dates = dates.astype('datetime64[M]')

	data = []

	layout = go.Layout(
	
	title= "<b>ARIMA Model Dam Occupancy Forecasting Plot</b>",paper_bgcolor = 'rgb(248, 248, 255)',plot_bgcolor = 'rgb(248, 248, 255)',barmode = "stack",
	xaxis = dict(title="Time", linecolor="#BCCCDC",showspikes=True,spikethickness=2,spikedash="dot",spikecolor= "#ffffff",spikemode="across",),
	yaxis= dict(title="Dam Occupancy Rate (%)",linecolor="#021C1E"))


	line_chart= go.Scatter(x=dates, y=predictions, marker_color='rgb(0, 200, 200)' )
	data.append(line_chart)
	fig= go.Figure(data=data, layout=layout)
	st.plotly_chart(fig)
	
