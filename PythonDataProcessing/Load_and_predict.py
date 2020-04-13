# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 11:43:06 2020

@author: Trif
"""

import os
import pandas as pd
import numpy as np
import keras as kr
from keras.layers import Dropout
from keras.layers import LSTM
from keras.layers import Dense
from sklearn import preprocessing

direction ='E:\\桌面N\\Data_cleantime'
test_path = 'E:\桌面N\Data_cleantime\Test_Data'


test_feature = np.array([])
for j in range(0,10):
    folder = '\\'+str(j)+'\\'
    files = os.listdir(test_path+folder)
    for f in files:
        rd = pd.read_csv(test_path+folder+f)
        test_feature = np.append(test_feature,rd)
        

test_feature = test_feature.reshape(50,511)
data_scaler_minmax = preprocessing.MinMaxScaler(feature_range=(0, 1))
test_feature = data_scaler_minmax.fit_transform(test_feature)
test_feature = test_feature.reshape(50,511,1)

model = kr.models.load_model('ver7.h5')
model.summary()



answer = model.predict(test_feature,verbose=0)
#print(answer)
for i in range(len(answer)):
    answer[i] = answer[i]*10
#answer.reshape(50,1)
#answer = label_scaler.inverse_transform(answer)
with open ('resultL.txt','w') as f:
    f.write(str(answer))