import streamlit as st
import numpy as np
import pandas as pd
import pickle
import streamlit.components.v1 as components
from PIL import Image

def app():
	st.title('Our Team')
	st.subheader('Who we are?')
	st.markdown("""<p style='text-align: justify;'>Our project team consists of 8 classmates that are members of Turkey Study Group (#sg_turkey) of AI - Bertelsmann Scholarship Program.</p>""", unsafe_allow_html=True)
	st.markdown("""<p style='text-align: justify;'>We have completed our work on our project by having meetings every week during the scholarship program.</p>""", unsafe_allow_html=True)
	
	image = Image.open('images/TeamMeeting.png')
	st.image(image,width=600)
	
	st.markdown("""<p style='text-align: justify;'>Moreover, we have shared information about the course requirements, challenges, events and resources in our weekly meetings.</p>""", unsafe_allow_html=True)
	st.markdown("""<p style='text-align: justify;'>We keep communicating with each other to motivate and improve our technical and social skills. If you want to join our group, you can reach the link below.</p>""", unsafe_allow_html=True)
	link = '[#sg_turkey - Study Group](https://app.slack.com/client/T01E9ECEM0D/C01HD5FGLNM)'
	st.markdown(link, unsafe_allow_html=True)

	st.markdown("""<p style='text-align: justify;'>As you know, our slack workspace will be closed when Phase 1 is over. Therefore, we can stay in touch at Phase 2 via the link below.</p>""", unsafe_allow_html=True)
	link = '[Bertelsmann AI Track - Discord](https://discord.com/invite/T3qhsXkEKB)'
	st.markdown(link, unsafe_allow_html=True)




	
	


	
