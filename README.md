# dam-occupancy-model
Udacity Bertelsmann AI Track Study Group Turkey GitHub project page.

![image](https://github.com/tekeburak/dam-occupancy-model/blob/update_docs/Home.PNG)

### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [Dataset](#dataset)
4. [File Descriptions](#files)
5. [Analysis Process](#process)
6. [Deployment](#deployment)
7. [Licensing, Authors, and Acknowledgements](#licensing)


## Installation <a name="installation"></a>

There should be no necessary libraries to run the code here beyond the Anaconda distribution of Python. The code should run with no issues using Python versions 3.*.


## Project Motivation<a name="motivation"></a>

The aim of this project is to develop an Istanbul Dam Occupancy Rate prediction model using machine learning techniques. It is a Side Project of Udacity Bertelsmann AI Track Study Group Turkey. 

The prediction of the dam occupancy rate of the reservoirs is critical in many cases (evaluating structural problems, water supply, resource availability, navigation management, disaster prevention). 


## Dataset<a name="dataset"></a>

The dam occupancy rates were used as a dependent variable while reserved water, weather data were set up as the independent variables.
 
- Istanbul dam occpancy rate and dam reserved water dataset [here](https://data.ibb.gov.tr/tr/dataset/istanbul-dam-occupany-rates-data/resource/b68cbdb0-9bf5-474c-91c4-9256c07c4bdf)
- Istanbul weather dataset [here](https://www.kaggle.com/vonline9/weather-istanbul-data-20092019)


## File Descriptions <a name="files"></a>

- dam_occupancy csv file
- Istanbul_weather_data csv file
- Istanbul_5days_weather_forecast test xlsx file
- train model branch files
- streamlit branch files
- README doc


## Analysis Process <a name="process"></a>

Selected Models:
- ARIMA MODEL - Auto Regressive Integrated Moving Average algorithm
- LSTM MODEL - Long Short Term Memory algorithm
- CNN MODEL - Convolutional Neural Network, Deep learning algorithm


## Deployment<a name="deployment"></a>

This is a interactive web applications with Streamlit. Check out the app [here](https://share.streamlit.io/tekeburak/dam-occupancy-model/streamlit/app.py)

![image](https://github.com/tekeburak/dam-occupancy-model/blob/update_docs/Project%20AI%20Turkey.gif)


## Licensing, Authors, Acknowledgements<a name="licensing"></a>

Must give credit to IBB and Kaggle for the data. You can find the Licensing for the data and other descriptive information at the IBB page [here](https://data.ibb.gov.tr/en/license) and at the Kaggle link available [here](https://www.kaggle.com/vonline9/weather-istanbul-data-20092019).
 
