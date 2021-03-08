import streamlit as st
import numpy as np
import pandas as pd
import pickle
import streamlit.components.v1 as components
from PIL import Image

def app():
	st.title('Contact Us')
	st.markdown("""<p style='text-align: justify;'></p>""", unsafe_allow_html=True)
	
	image = Image.open('BurakTeke.jpg')
	st.image(image, width=350)
	st.subheader('Burak Teke')
	link = '[LinkedIn](https://www.linkedin.com/in/burakteke)'
	st.markdown(link, unsafe_allow_html=True)

	image = Image.open('MerveDin.jpg')
	st.image(image,width=350)
	st.subheader('Merve Din')
	link = '[LinkedIn](https://www.linkedin.com/in/mervedin16/)'
	st.markdown(link, unsafe_allow_html=True)

	image = Image.open('HaticeKoc.jpg')
	st.image(image,width=350)
	st.subheader('Hatice Koç')
	link = '[LinkedIn](https://www.linkedin.com/in/haticekoc/)'
	st.markdown(link, unsafe_allow_html=True)

	image = Image.open('BernadettKepenyesGokcay.jpg')
	st.image(image,width=350)
	st.subheader('Bernedett Kepenyes Gökçay')
	link = '[LinkedIn](https://www.linkedin.com/in/bernadett-kepenyes/)'
	st.markdown(link, unsafe_allow_html=True)

	image = Image.open('MertIzcan.jpg')
	st.image(image,width=350)
	st.subheader('Mert İzcan')
	link = '[LinkedIn](https://www.linkedin.com/in/mert-halit-izcan-834180b1/)'
	st.markdown(link, unsafe_allow_html=True)

	image = Image.open('SametAydin.jpg')
	st.image(image,width=350)
	st.subheader('Samet Aydın')
	link = '[LinkedIn](https://www.linkedin.com/in/samet-aydin/)'
	st.markdown(link, unsafe_allow_html=True)
	
	image = Image.open('OsmanKirci.jpg')
	st.image(image,width=350)
	st.subheader('Osman Kırcı')
	link = '[LinkedIn](https://www.linkedin.com/in/osmank%C4%B1rc%C4%B1)'
	st.markdown(link, unsafe_allow_html=True)

	image = Image.open('HandenurGurpinar.jpeg')
	st.image(image,width=300)
	st.subheader('Handenur Gürpınar')
	link = '[LinkedIn](https://www.linkedin.com/in/handenurgurpinar)'
	st.markdown(link, unsafe_allow_html=True)