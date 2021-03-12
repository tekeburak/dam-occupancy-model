import tensorflow as tf
from get_owm_data import get_open_weather_map_data

LSTM_model_name = 'LSTM_model.h5'
CNN_model_name = 'CNN_model.h5'

model_lstm = tf.keras.models.load_model(LSTM_model_name)
model_cnn = tf.keras.models.load_model(CNN_model_name)

input = get_open_weather_map_data()

prediction_lstm = model_lstm.predict(input) * 100
prediction_cnn = model_cnn.predict(input) * 100

prediction_lstm = prediction_lstm.ravel()
prediction_cnn = prediction_cnn.ravel()