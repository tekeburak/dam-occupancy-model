import requests
import json
import numpy as np

API_KEY = "d36220c2741c4f7076ad680282de5d68"
LAT = "41.0082"
LON = "28.9784"
URL = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&exclude=current,minutely,hourly,alerts&appid=%s&units=metric" % (LAT, LON, API_KEY)

data_size = 7

train_min_values = [0.0, -3.0, -4.0, 2.0, 42.0, 992.0]
train_max_values = [41.45, 37.0, 26.0, 56.0, 97.0, 1038.0]

owm_list = []

def get_open_weather_map_data():
    response = requests.get(URL)
    data = json.loads(response.text)

    for i in range(data_size):
        if 'rain' in data['daily'][i]:
            Rain = data['daily'][i]['rain']
            Rain = (Rain - train_min_values[0]) / (train_max_values[0] - train_min_values[0])
        else:
            Rain = 0.0
        MaxTemp = data['daily'][i]['temp']['max']
        MinTemp = data['daily'][i]['temp']['min']
        AvgWind = data['daily'][i]['wind_speed']
        AvgHumidity = data['daily'][i]['humidity']
        AvgPressure = data['daily'][i]['pressure']

        MaxTemp = (MaxTemp - train_min_values[1]) / (train_max_values[1] - train_min_values[1])
        MinTemp = (MinTemp - train_min_values[2]) / (train_max_values[2] - train_min_values[2])
        AvgWind = (AvgWind - train_min_values[3]) / (train_max_values[3] - train_min_values[3])
        AvgHumidity = (AvgHumidity - train_min_values[4]) / (train_max_values[4] - train_min_values[4])
        AvgPressure = (AvgPressure - train_min_values[5]) / (train_max_values[5] - train_min_values[5])
        
        owm_data = [Rain, MaxTemp, MinTemp, AvgWind, AvgHumidity, AvgPressure]
        owm_list.append(owm_data)
        out = np.transpose(np.array(owm_list))
        out = np.expand_dims(out, axis=0)

    return out