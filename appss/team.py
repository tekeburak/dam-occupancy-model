import streamlit as st
import numpy as np
import pandas as pd
import pickle
import streamlit.components.v1 as components
from PIL import Image

def app():
	st.title('Our Team')
	st.subheader('Who we are?')
	st.markdown("""<p style='text-align: justify;'>Our team consists of NUMBER classmates that are members of Turkey Study Group (#sg_turkey) of AI - Bertelsmann Scholarship Program.</p>""", unsafe_allow_html=True)
	st.markdown("""<p style='text-align: justify;'>We have completed our work on our project by having meetings every week during the scholarship program.</p>""", unsafe_allow_html=True)
	
	image = Image.open('team.jpg')
	st.image(image,width=600,caption="Our Team Meeting")

	st.subheader('\nContact Us')
	
	image = Image.open('cv.jpg')
	st.image(image,width=250,caption="FirstName LastName")

	image = Image.open('cv2.jpg')
	st.image(image,width=250,caption="FirstName2 LastName2")

	
