import streamlit as st
import numpy as np
import pandas as pd
import pickle
import streamlit.components.v1 as components
from PIL import Image

def app():
	
	st.title('Dam Occupancy Rate Forecasting')
	image = Image.open('images/istanbul.jpg')
	st.image(image,width=600)
	st.subheader('Our Project Purpose')
	st.markdown("""<p style='text-align: justify;'>Unconsciously use of water resources have being affected the world.\nWith climate change, our water resources are running out rapidly.\nAddition to these, dam occupancy rates become more significant for countries such as Turkey.</p>""", unsafe_allow_html=True)
	st.markdown("""<p style='text-align: justify;'>Our project aims to forecast dam occupancy rate of İstanbul. Also we aimed for this project to accurately estimate the future dam occupancy rate.</p>""", unsafe_allow_html=True)

	st.subheader('\nThe Data We Used in The Project')
	st.markdown("""<p style='text-align: justify;'>Open Source culture has started to get more attention in Turkey and some of the  municipalities started to share their data with the community. Istanbul Metropolitan Municipality is one of them. We have gotten dam occupancy rate data from their website. For additional features, we use the weather dataset for Istanbul on Kaggle.</p>""", unsafe_allow_html=True)

	st.markdown("""<p style='text-align: justify;'></p>""", unsafe_allow_html=True)
	
	
	st.subheader('\nThe Links for The Data')
	st.markdown("""<p style='text-align: justify;'>If you are interested, you can access the data from the links below.</p>""", unsafe_allow_html=True)

	link = '[Istanbul Metropolitan Municipality - Data](https://data.ibb.gov.tr/dataset/istanbul-dam-occupany-rates-data)'
	st.markdown(link, unsafe_allow_html=True)
	link = '[Istanbul Weather Data - Kaggle](https://www.kaggle.com/vonline9/weather-istanbul-data-20092019)'
	st.markdown(link, unsafe_allow_html=True)

	


	
	


