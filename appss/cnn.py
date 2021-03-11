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


	model = tf.keras.models.load_model('cnn_model.h5')

	features = get_open_weather_map_data()

	prediction = model.predict(features)
	
	st.line_chart(prediction[0, :, 0].reshape(-1))
