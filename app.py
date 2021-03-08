import streamlit as st
import streamlit_theme as stt
from multiapp import MultiApp
from appss import home, arima, lstm, cnn, team, contact


app = MultiApp()


app.add_app("HOME", home.app)
app.add_app("ARIMA MODEL", arima.app)
app.add_app("LSTM MODEL", lstm.app)
app.add_app("CNN MODEL", cnn.app)
app.add_app("OUR TEAM", team.app)
app.add_app("CONTACT US", contact.app)
app.run()