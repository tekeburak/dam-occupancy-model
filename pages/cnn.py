import streamlit as st
import tensorflow as tf
import pandas as pd
import numpy
from utils.get_owm_data import get_open_weather_map_data



def app():
	st.title("CNN Model")
	
	st.subheader('What does CNN model do?')
	st.markdown("""<p style='text-align: justify;'>A Convolutional Neural Network (ConvNet/CNN) is a Deep Learning algorithm which can take in an input image, assign importance (learnable weights and biases) to various aspects/objects in the image and be able to differentiate one from the other.</p>""", unsafe_allow_html=True)
	
	#st.subheader('Why we chose CNN?')
	#st.markdown("""<p style='text-align: justify;'>BLABLA</p>""", unsafe_allow_html=True)


	CNN_model_name = 'models/CNN_model.h5'

	model_cnn = tf.keras.models.load_model(CNN_model_name)

	features = get_open_weather_map_data()

	prediction_cnn = model_cnn.predict(features) * 100
	st.line_chart(prediction_cnn.reshape(-1))
