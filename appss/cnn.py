import streamlit as st
import tensorflow as tf
import pandas as pd
from get_owm_data import get_open_weather_map_data



def app():
	st.title("CNN Model")
	
	st.subheader('What does CNN model do?')
	st.markdown("""<p style='text-align: justify;'>BLABLA</p>""", unsafe_allow_html=True)
	
	st.subheader('Why we chose CNN?')
	st.markdown("""<p style='text-align: justify;'>BLABLA</p>""", unsafe_allow_html=True)


	CNN_model_name = 'CNN_model.h5'

	model_cnn = tf.keras.models.load_model(CNN_model_name)

	features = get_open_weather_map_data()


	prediction_cnn = model_cnn.predict(features) * 100
