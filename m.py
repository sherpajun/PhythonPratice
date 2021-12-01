import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns   
from datetime import datetime
import keras
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
from keras.models import Sequential
from keras.layers import Dense, LSTM
from keras.utils import np_utils
plt.rcParams['font.family']='Malgun Gothic'

df = pd.read_csv('북구.csv')

df = df.set_index('측정일시')

x = df[['CO', 'NO2', 'O3', 'SO2', '기온(°C)', '강수량(mm)',
'풍속(m/s)', '풍향(16방위)', '습도(%)', '일조(hr)', '일사(MJ/m2)', '중하층운량(10분위)',]]
y=df[['PM10']]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=156)

x_train = x_train.values
x_test = x_test.values
y_train = y_train.values
y_test = y_test.values
x_train_t = x_train.reshape(x_train.shape[0], x_train.shape[1], 1)
x_test = x_test.reshape(x_test.shape[0], x_test.shape[1], 1)

model = Sequential()
model.add(LSTM(340, activation='relu', input_shape=(x_train.shape[1],1)))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')

dust = model.fit(x_train_t, y_train, epochs=100, batch_size=10, verbose = 1)

model.save('북구.h5')