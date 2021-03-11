import tensorflow as tf
from get_owm_data import get_open_weather_map_data

CONV_WIDTH = 3
LABEL_WIDTH = 30
INPUT_WIDTH = 7

model = tf.keras.models.load_model('cnn_model.h5')

input = get_open_weather_map_data()

prediction = model.predict(input)