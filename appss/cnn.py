import streamlit as st
import tensorflow as tf
from get_owm_data import get_open_weather_map_data

def app():
	st.title("CNN Model")
	
	st.subheader('What does CNN model do?')
	st.markdown("""<p style='text-align: justify;'>BLABLA</p>""", unsafe_allow_html=True)
	
	st.subheader('Why we chose CNN?')
	st.markdown("""<p style='text-align: justify;'>BLABLA</p>""", unsafe_allow_html=True)	
	
	CONV_WIDTH = 3
	LABEL_WIDTH = 30
	INPUT_WIDTH = 7

	st.write("before model reading")
	model = tf.keras.models.load_model('cnn_model.h5')
	st.write("after model reading")
	
	"""
	features = get_open_weather_map_data()
	st.wirte("after gettin features")
	prediction = model.predict(features)
	st.wirte("after gettin preds")
	st.write(prediction)
	"""
