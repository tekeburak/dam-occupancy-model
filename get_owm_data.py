import requests
import json
import numpy as np

API_KEY = "d36220c2741c4f7076ad680282de5d68"
LAT = "41.0082"
LON = "28.9784"
URL = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&exclude=current,minutely,hourly,alerts&appid=%s&units=metric" % (LAT, LON, API_KEY)

data_size = 7



def get_open_weather_map_data():
    response = requests.get(URL)
    data = json.loads(response.text)
    
    owm_list = []

    for i in range(data_size):
        if 'rain' in data['daily'][i]:
            Rain = data['daily'][i]['rain']
        else:
            Rain = 0.0
        MaxTemp = data['daily'][i]['temp']['max']
        MinTemp = data['daily'][i]['temp']['min']
        AvgWind = data['daily'][i]['wind_speed']
        AvgHumidity = data['daily'][i]['humidity']
        AvgPressure = data['daily'][i]['pressure']
        
        owm_data = [Rain, MaxTemp, MinTemp, AvgWind, AvgHumidity, AvgPressure]
        owm_list.append(owm_data)
        out = np.transpose(np.array(owm_list))
        out = np.expand_dims(out, axis=0)
        

    return out
