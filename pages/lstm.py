import streamlit as st
import tensorflow as tf
import numpy
from utils.get_owm_data import get_open_weather_map_data
from utils.get_date import get_date_list_for_gmt

import plotly.graph_objects as go
from plotly import tools
import plotly.offline as py
import plotly.express as px


def app():
	st.title("LSTM Model")
	
	st.subheader('What does LSTM model do?')
	st.markdown("""<p style='text-align: justify;'>LSTM networks are an extension of recurrent neural networks (RNNs) mainly introduced to handle situations where RNNs fail. It has been so designed that thevanishing gradient problem is almost completely removed, while the training model is left unaltered. Long-time lags in certain problems are bridged using LSTMs where they also handle noise, distributed representations, and continuous values.</p>""", unsafe_allow_html=True)
	
	st.subheader('Why we chose LSTM?')
	st.markdown("""<p style='text-align: justify;'>LSTM is well-suited to classify, process and predict time series given time lags of unknown duration. Relative insensitivity to gap length gives an advantage to LSTM over alternative RNNs, hidden Markov models and other sequence learningmethods. In addition, LSTM works great because LSTM cells have a memory that can store previous timestep information and this is how it learns.</p>""", unsafe_allow_html=True)	
	
	st.subheader('LSTM model input and output')
	st.markdown("Model input is 7 days daily weather data from [OpenWeatherAPI](https://openweathermap.org/api). Model input features are *Rain*, *MaxTemp*, *MinTemp*, *AvgWind*, *AvgHumidity* and *AvgPressure*. Model predicts 7 days dam occupancy rate of İstanbul using these features.", unsafe_allow_html=True)

	
	LSTM_model_name = 'models/LSTM_model.h5'

	model_lstm = tf.keras.models.load_model(LSTM_model_name)

	features = get_open_weather_map_data()


	prediction_lstm = model_lstm.predict(features) * 100
	prediction_lstm = prediction_lstm.ravel()
	date_list = get_date_list_for_gmt()

	data = []

	layout = go.Layout(
	
	title= "<b>LSTM Dam Occupancy Forecasting Plot</b>",paper_bgcolor = 'rgb(248, 248, 255)',plot_bgcolor = 'rgb(248, 248, 255)',barmode = "stack",
	xaxis = dict(title="Time", linecolor="#BCCCDC",showspikes=True,spikethickness=2,spikedash="dot",spikecolor= "#ffffff",spikemode="across",),
	yaxis= dict(title="Dam Occupancy Rate (%)",linecolor="#021C1E"))


	line_chart= go.Scatter(x=date_list, y=prediction_lstm, marker_color='rgb(0, 200, 200)' )
	data.append(line_chart)
	fig= go.Figure(data=data, layout=layout)
	st.plotly_chart(fig)
