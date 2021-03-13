import streamlit as st
import tensorflow as tf
import pandas as pd
import numpy
from utils.get_owm_data import get_open_weather_map_data



def app():
	st.title("CNN Model")
	
	st.subheader('What does CNN model do?')
	st.markdown("""<p style='text-align: justify;'>Convolutional Neural Network, also known as CNN, is a subfield of deep learning which is mostly used for the analysis of visual imagery. CNN is a class of deep feedforward artificial neural networks (ANN). This Neural Network uses the already supplied dataset for training purposes and predicts the possible future labels to be assigned. Any kind of data This Neural Network uses its strengths against the curse of dimensionality. A portion of the territories where CNNs are broadly utilized are image recognition, image classification, image captioning and object detection etc.</p>""", unsafe_allow_html=True)
	
	st.subheader('Why we chose CNN?')
	st.markdown("""<p style='text-align: justify;'>A convolutional model makes predictions based on a fixed-width history, which may lead to better performance than the dense model since it can see how things are changing over time.</p>""", unsafe_allow_html=True)


	CNN_model_name = 'models/CNN_model.h5'

	model_cnn = tf.keras.models.load_model(CNN_model_name)

	features = get_open_weather_map_data()

	prediction_cnn = model_cnn.predict(features) * 100
	st.line_chart(prediction_cnn.reshape(-1))
