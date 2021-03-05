import requests
import json

API_KEY = "d36220c2741c4f7076ad680282de5d68"
LAT = "41.0082"
LON = "28.9784"
URL = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&exclude=current,minutely,hourly,alerts&appid=%s&units=metric" % (LAT, LON, API_KEY)

response = requests.get(URL)
data = json.loads(response.text)

# DateTime, Rain, MaxTemp, MinTemp, Humidity, Pressure, Wind

# if data['daily'][4]['rain'] == None:
#     print("Rain is Nan")

if 'rain' not in data['daily'][5]:
    print("Rain is Nan")
else:
    print(data['daily'][5]['rain'])

print(data)