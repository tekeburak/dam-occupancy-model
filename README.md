# dam-occupancy-model
Udacity Bertelsmann AI Track Study Group Turkey GitHub project page.

### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [Dataset](#dataset)
4. [File Descriptions](#files)
5. [Analysis Process](#process)
6. [Results](#results)
7. [Licensing, Authors, and Acknowledgements](#licensing)


## Installation <a name="installation"></a>

There should be no necessary libraries to run the code here beyond the Anaconda distribution of Python. The code should run with no issues using Python versions 3.*.


## Project Motivation<a name="motivation"></a>

The aim of this project is to develop a Dam Occupancy Rate prediction model using machine learning techniques. It is a Side Project of Udacity Bertelsmann AI Track Study Group Turkey. 

The prediction of the dam occupancy rate of the reservoirs is critical in many cases (evaluating structural problems, water supply, resource availability, navigation management, disaster prevention). 

Questions to be answered:
- Is there enough data available to develop a Dam Occupancy Rate prediction model?
- How well can we predict the dam occupancy rate of reservoirs?

Performed analysis:
- For long term analysis we used time Sequential model and only considered data from the occupancy rate historic time series. 
- For short term analysis the dam occupancy rate was formulated as a (weekly time-horizon?) prediction problem.


## Dataset<a name="dataset"></a>

The dam occupancy rates were used as a dependent variable while reserved water, weather data were set up as the independent variables. To prevent over-fitting of the model, the data were divided into training and test dataset.
 
- Istanbul dam occpancy rate and dam reserved water dataset [here](https://data.ibb.gov.tr/tr/dataset/istanbul-dam-occupany-rates-data/resource/b68cbdb0-9bf5-474c-91c4-9256c07c4bdf)
- Istanbul weather dataset [here](https://www.kaggle.com/vonline9/weather-istanbul-data-20092019)

After pre-processing the data, there were ... data samples for the experiments. A seasonal approach was also considered as part of the experimental perfomance of the ML algorithms considered. The data were splitted into four seasons. Every regression technique was trained with each corresponding seasonal dataset. This way it was possible to assess how the different models perform on each season.


## File Descriptions <a name="files"></a>

- dam_occupancy csv file
- Istanbul_weather_data csv file
- Istanbul_5days_weather_forecast test xlsx file
- 1 jupyter notebook to showcase work related to prediction. Markdown cells were used to assist in walking through the thought process for individual steps.  
- 1 jupyter notebook for data visualization


# Analysis Process <a name="process"></a>

Our goal was to develop a model for predicting the future Dam Occupancy rate by using the weather and water level data obtained --> X days <--- prior to the day of interest. --> X days <--- ago data was found to have higher? relatedness than the data from --> Y days <-- ago. It has linear relationship ... <--- ???


## Results<a name="results"></a>

The main findings of the code can be found at the post available [here]()

The prediction performance by each model was evaluated using evaluation indicators, such as:
- correlation coefficient (CC) - it indicates the degree of linear relationship between simulated and observed data (-1:1),
- Nash-Sutcliffe efficiency (NSE) - it shows how well the plot of simulated and observed data fits on a 1:1 line (0:1),
- root mean square error (RMSE) - difference between the simulated and observed values, indicator of how much error the simulated results contain,
- persistence index (PI) - it measures the relative magnitude of the residual variance to the variance of the errors estimated from the model.

Weekly aggregation for both long and short term analysis was performed. This improved the representation of the differences in the changes of the level of the water stored in the reservoir, otherwise, the differences in a smaller scale of time (like daily) would be too small and unstable to properly train the model. On the precipitations and the output of the reservoir, the sum was calculated, while, for the variables average were obtained to convert them to weekly data.


Result of the long-term analysis with Sequential model:
....> MISSING <.....

Result of the short-time analysis:
The dam occupancy rate was formulated as a weekly time-horizon prediction problem. We considered a prediction problem with a time-horizon prediction of one week, thus the predictive variables were time delayed one week with respect to the objective variable.


--> ANN - Artificial Neural Network: The dependent and independent variables are standardized to values between 0 and 1 using the re-scaling method. 
--> Decision Tree - repeatedly dividing the data by finding branch points that minimize the mean squared error.
--> Overall Random Forest was the best method for simulating the occupancy rate among the machine learning methods. (PI value should be positive)

Data visualization shows the peak water level and the time delay between the observed and simulated results of the models.

The results indicate that the dam occupancy rate is ... (well?) predicted. The average CC value was 0..., which indicates that most of the machine learning models stimulates the trends of observed water levels appropriately. The average value of the NSE was ..., indicating that the overall simulation results simulate the overall performance of the observed water level well. The Mean value of the RMSE was 0..., this indicates that the error of the simulated value is lower than the observed value.


## Licensing, Authors, Acknowledgements<a name="licensing"></a>

Must give credit to IBB and Kaggle for the data. You can find the Licensing for the data and other descriptive information at the IBB page [here](https://data.ibb.gov.tr/en/license) and at the Kaggle link available [here](https://www.kaggle.com/vonline9/weather-istanbul-data-20092019).
 

