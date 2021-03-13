import streamlit as st
import numpy as np
import pandas as pd
import pickle
import streamlit.components.v1 as components
from PIL import Image

def app():
	st.title('Contact Us')
	st.markdown("""<p style='text-align: justify;'></p>""", unsafe_allow_html=True)
	newsize = (300, 300) 
	
	
	row1 = st.beta_columns(4)
	
	
	image = Image.open('images/burak.jpg').resize(newsize)
	alt="Avatar"
	row1[0].image(image)
	row1[0].subheader('Burak Teke')
	link = '[LinkedIn](https://www.linkedin.com/in/burakteke)'
	row1[0].markdown(link, unsafe_allow_html=True)


	image = Image.open('images/merve.jpg').resize(newsize)
	row1[1].image(image)
	row1[1].subheader('Merve Din')
	link = '[LinkedIn](https://www.linkedin.com/in/mervedin16/)'
	row1[1].markdown(link, unsafe_allow_html=True)

	image = Image.open('images/hatice.jpg').resize(newsize)
	row1[2].image(image)
	row1[2].subheader('Hatice Koç')
	link = '[LinkedIn](https://www.linkedin.com/in/haticekoc/)'
	row1[2].markdown(link, unsafe_allow_html=True)

	image = Image.open('images/bernadett.jpg').resize(newsize)
	row1[3].image(image)
	row1[3].subheader('Bernedett Kepenyes Gökçay')
	link = '[LinkedIn](https://www.linkedin.com/in/bernadett-kepenyes/)'
	row1[3].markdown(link, unsafe_allow_html=True)


	row2 = st.beta_columns(4)
	
	
	image = Image.open('images/mert.jpg').resize(newsize)
	row2[0].image(image)
	row2[0].subheader('Mert İzcan')
	link = '[LinkedIn](https://www.linkedin.com/in/mert-halit-izcan-834180b1/)'
	row2[0].markdown(link, unsafe_allow_html=True)

	image = Image.open('images/samet.jpg').resize(newsize)
	row2[1].image(image)
	row2[1].subheader('Samet Aydın')
	link = '[LinkedIn](https://www.linkedin.com/in/samet-aydin/)'
	row2[1].markdown(link, unsafe_allow_html=True)
	
	image = Image.open('images/osman.jpg').resize(newsize)
	row2[2].image(image)
	row2[2].subheader('Osman Kırcı')
	link = '[LinkedIn](https://www.linkedin.com/in/osmank%C4%B1rc%C4%B1)'
	row2[2].markdown(link, unsafe_allow_html=True)

	image = Image.open('images/handenur.jpg').resize(newsize)
	row2[3].image(image)
	row2[3].subheader('Handenur Gürpınar')
	link = '[LinkedIn](https://www.linkedin.com/in/handenurgurpinar)'
	row2[3].markdown(link, unsafe_allow_html=True)
