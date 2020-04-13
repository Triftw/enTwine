# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:37:25 2020

@author: Trif
"""

import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd
import keras as kr
from keras.layers import Dropout
from keras.layers import LSTM
from keras.layers import Dense
from sklearn import preprocessing

direction ='E:\\桌面N\\Data_cleantime'
test_path = 'E:\桌面N\Data_cleantime\Test_Data'
feature = np.array([])
label= np.array([])
for j in range(0,10):
    folder = '\\'+str(j)+'\\'
    files = os.listdir(direction+folder)
    for f in files:
        rd = pd.read_csv(direction+folder+f)
        feature = np.append(feature,rd)
        nj = float(j)/10.0
        label = np.append(label,nj)
#feature = np.array(feature)
test_feature = np.array([])
for j in range(0,10):
    folder = '\\'+str(j)+'\\'
    files = os.listdir(test_path+folder)
    for f in files:
        rd = pd.read_csv(test_path+folder+f)
        test_feature = np.append(test_feature,rd)
np.savetxt('tf',test_feature)
np.savetxt('f',feature)

test_feature = test_feature.reshape(50,511)
feature = feature.reshape(950,511)

data_scaler_minmax = preprocessing.MinMaxScaler(feature_range=(0, 1))
feature = data_scaler_minmax.fit_transform(feature)
test_feature = data_scaler_minmax.fit_transform(test_feature)

test_feature = test_feature.reshape(50,511,1)
feature = feature.reshape(950,511,1)

label = label.reshape(950,1)
"""
label_scaler = preprocessing.MinMaxScaler(feature_range = (0,1))
label = label_scaler.fit_transform(label)
"""

model = kr.Sequential()
model.add(LSTM(units = 100, return_sequences=True,input_shape=(511,1)))
model.add(Dropout(0.2))
model.add(LSTM(units=100, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=100, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=100))
model.add(Dropout(0.2))
model.add(Dense(units = 1))
model.compile(optimizer = 'adam', loss = 'mean_squared_error')
model.summary()

model.fit(feature, label, epochs = 100, batch_size = 64)
model.save('ver7.h5')
print('finish')
answer = model.predict(test_feature,verbose=0)
#print(answer)
for i in range(len(answer)):
    answer[i] = answer[i]*10
#answer.reshape(50,1)
#answer = label_scaler.inverse_transform(answer)
with open ('result.txt','w') as f:
    f.write(str(answer))