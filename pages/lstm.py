import streamlit as st
import tensorflow as tf
import numpy
from utils.get_owm_data import get_open_weather_map_data


def app():
	st.title("LSTM Model")
	
	st.subheader('What does LSTM model do?')
	st.markdown("""<p style='text-align: justify;'>LSTM networks are an extension of recurrent neural networks (RNNs) mainly introduced to handle situations where RNNs fail. It has been so designed that thevanishing gradient problem is almost completely removed, while the training model is left unaltered. Long-time lags in certain problems are bridged using LSTMs where they also handle noise, distributed representations, and continuous values.</p>""", unsafe_allow_html=True)
	
	st.subheader('Why we chose LSTM?')
	st.markdown("""<p style='text-align: justify;'>LSTM is well-suited to classify, process and predict time series given time lags of unknown duration. Relative insensitivity to gap length gives an advantage to LSTM over alternative RNNs, hidden Markov models and other sequence learningmethods. In addition, LSTM works great because LSTM cells have a memory that can store previous timestep information and this is how it learns.</p>""", unsafe_allow_html=True)	
	
	
	LSTM_model_name = 'models/LSTM_model.h5'

	model_lstm = tf.keras.models.load_model(LSTM_model_name)

	features = get_open_weather_map_data()


	prediction_lstm = model_lstm.predict(features) * 100
	st.line_chart(prediction_lstm.reshape(-1))
