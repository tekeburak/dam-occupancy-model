import numpy as np
import pandas as pd
import pickle
from statsmodels.tsa.arima_model import ARIMA
import warnings
warnings.filterwarnings("ignore")

#loading data
df = pd.read_csv("dam_occupancy.csv").drop("GENERAL_DAM_RESERVED_WATER", axis=1)
df.columns = ["date", "occupancy_rate"]
df["date"] = pd.to_datetime(df["date"])

#converting data to monthly basis 
df = df.resample("M", on="date").mean().reset_index()
df['date'] = df['date'].apply(lambda x: x.strftime('%Y-%m'))
df.set_index('date', inplace=True)

#dividing data into train and test
train = df.occupancy_rate[:160]
test = df.occupancy_rate[160:]



#arima model with best parameters and its forecast for the test data
arima = ARIMA(train, order=(2, 1, 4))
arima_fit = arima.fit()

pickle.dump(arima_fit, open("arima_model.pkl", "wb"))





