import streamlit as st
import streamlit_theme as stt
from utils.multiapp import MultiApp
from pages import home, arima, lstm, cnn, team, contact


app = MultiApp()
CONV_WIDTH = 3
LABEL_WIDTH = 30
INPUT_WIDTH = 7



app.add_app("HOME", home.app)
app.add_app("ARIMA MODEL", arima.app)
app.add_app("LSTM MODEL", lstm.app)
app.add_app("CNN MODEL", cnn.app)
app.add_app("OUR TEAM", team.app)
app.add_app("CONTACT US", contact.app)
app.run()
