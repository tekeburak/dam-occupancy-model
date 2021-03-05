import streamlit as st
import streamlit_theme as stt
from multiapp import MultiApp
from appss import home, arima, lstm, team


stt.set_theme({'primary': '#881b1d'})

app = MultiApp()


app.add_app("HOME", home.app)
app.add_app("ARIMA MODEL", arima.app)
app.add_app("LSTM", lstm.app)
app.add_app("OUR TEAM", team.app)
app.run()