import streamlit as st
import tensorflow as tf
import pandas as pd
import numpy as np
from utils.get_owm_data import get_open_weather_map_data
from utils.get_date import get_date_list_for_gmt

import plotly.graph_objects as go
from plotly import tools
import plotly.offline as py
import plotly.express as px


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
	prediction_cnn = prediction_cnn.ravel()
	date_list = get_date_list_for_gmt()

	data = []

	layout = go.Layout(
	
	title= "<b>CNN Dam Occupancy Forecasting Plot</b>",paper_bgcolor = 'rgb(248, 248, 255)',plot_bgcolor = 'rgb(248, 248, 255)',barmode = "stack",
	xaxis = dict(title="Time", linecolor="#BCCCDC",showspikes=True,spikethickness=2,spikedash="dot",spikecolor= "#ffffff",spikemode="across",),
	yaxis= dict(title="Dam Occupancy Rate (%)",linecolor="#021C1E"))


	line_chart= go.Scatter(x=date_list, y=prediction_cnn, marker_color='rgb(0, 200, 200)' )
	data.append(line_chart)
	fig= go.Figure(data=data, layout=layout)
	st.plotly_chart(fig)