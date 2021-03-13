import streamlit as st
import tensorflow as tf
import numpy
from utils.get_owm_data import get_open_weather_map_data


def app():
	st.title("LSTM Model")
	
	st.subheader('What does LSTM model do?')
	st.markdown("""<p style='text-align: justify;'>Long Short-Term Memory (LSTM) networks are a type of recurrent neural network capable of learning order dependence in sequence prediction problems. An LSTM has a similar control flow as a recurrent neural network. It processes data passing on information as it propagates forward. The differences are the operations within the LSTM's cells. These operations are used to allow the LSTM to keep or forget information.</p>""", unsafe_allow_html=True)
	
	#st.subheader('Why we chose LSTM?')
	#st.markdown("""<p style='text-align: justify;'>BLABLA</p>""", unsafe_allow_html=True)	
	
	
	LSTM_model_name = 'models/LSTM_model.h5'

	model_lstm = tf.keras.models.load_model(LSTM_model_name)

	features = get_open_weather_map_data()


	prediction_lstm = model_lstm.predict(features) * 100
	st.line_chart(prediction_lstm.reshape(-1))
