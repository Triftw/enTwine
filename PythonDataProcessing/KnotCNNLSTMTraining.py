# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:37:25 2020

@author: Trif
"""

import numpy as np
import os
import pandas as pd
import keras as kr
from keras.layers import Dropout
from keras.layers import LSTM
from keras.layers import Dense
from keras.layers import TimeDistributed
from keras.layers import *
from sklearn import preprocessing
from sklearn.utils import shuffle
from pickle import dump
version_name = '0428KnotverC1.8'
#1.2 500 1.3 1000 1.4 2000 1.5 300 1.6 200 1.7 250 1.8 280 1.9 230
#VER 1.2 batch5 epoch 200 2layer LSTM
batch = 5
epoch = 200
direction ='E:\\桌面N\\0426Knot_NT\\Data'
d2 = 'E:\\桌面N\\0428test\\'
#test_path = 'E:\桌面N\Data_cleantime\Test_Data'
feature = np.array([])
label= np.array([])
label_cnt = 4 
feature_cnt = 160
feature_length = 2000
#one hot encoding [Overhand Eight Slip Clove]

for folder in os.listdir(direction):
    folder = '\\'+folder+'\\'
    files = os.listdir(direction+folder)
    for f in files:
        rd = pd.read_csv(direction+folder+f)
        #print(rd.shape)
        feature = np.append(feature,rd)
        if f[0] == 'C':
            nl =[0,0,0,1]
        if f[0] == 'O':
            nl =[1,0,0,0]
        if f[0] == 'E':
            nl =[0,1,0,0]
        if f[0] == 'S':
            nl =[0,0,1,0]
        label = np.append(label,nl)

files = os.listdir(d2)
for f in files:
    rd = pd.read_csv(d2+f)
    #print(rd.shape)
    feature = np.append(feature,rd)
    if f[0] == 'C':
        nl =[0,0,0,1]
    if f[0] == 'O':
        nl =[1,0,0,0]
    if f[0] == 'E':
        nl =[0,1,0,0]
    if f[0] == 'S':
        nl =[0,0,1,0]
    label = np.append(label,nl)
#feature = np.array(feature)
'''
test_feature = np.array([])
for j in range(0,10):
    folder = '\\'+str(j)+'\\'
    files = os.listdir(test_path+folder)
    for f in files:
        rd = pd.read_csv(test_path+folder+f)
        test_feature = np.append(test_feature,rd)
np.savetxt('tf',test_feature)
'''

#test_feature = test_feature.reshape(50,511)
#feature = feature.reshape(feature_cnt,feature_length)
feature = feature.reshape(640,2000)
data_scaler_minmax = preprocessing.MinMaxScaler(feature_range=(0, 1))
feature = data_scaler_minmax.fit_transform(feature)
dump(data_scaler_minmax,  open(version_name+'_scaler.pkl', 'wb'))
#test_feature = data_scaler_minmax.fit_transform(test_feature)
#feature,label = shuffle(feature,label, random_state=0)
#test_feature = test_feature.reshape(50,511,1)
feature = feature.reshape(feature_cnt,feature_length,4)
#np.savetxt('f.csv',feature,delimiter=',')
label = label.reshape(feature_cnt,4)

#reshape to 5dimension
feature = feature.reshape(160,1,2000,4,1)

"""
label_scaler = preprocessing.MinMaxScaler(feature_range = (0,1))
label = label_scaler.fit_transform(label)
"""

model = kr.Sequential()
model.add(TimeDistributed(Conv2D(filters = 4,kernel_size = (3,3),data_format="channels_last",activation = 'relu'),input_shape =(1,2000,4,1)))
model.add(TimeDistributed(MaxPooling2D(pool_size=2)))
model.add(TimeDistributed(Flatten()))
model.add(LSTM(units = 100, return_sequences=True,))
model.add(Dropout(0.2))
model.add(LSTM(units=100))
model.add(Dropout(0.2))
#model.add(LSTM(units=50, return_sequences=True))
#model.add(Dropout(0.2))
#model.add(LSTM(units=100, return_sequences=True))
#model.add(Dropout(0.2))
#model.add(LSTM(units=100))
#model.add(Dropout(0.2))
model.add(Dense(units = 4,activation ='softmax'))
model.compile(metrics=['accuracy'],optimizer = 'adam', loss = 'categorical_crossentropy')
model.summary()

model.fit(feature, label ,epochs = epoch, batch_size = batch, validation_split=0.125)
model.save(version_name+'.h5')
print('finish')

'''
answer = model.predict(test_feature,verbose=0)
#print(answer)
for i in range(len(answer)):
    answer[i] = answer[i]*label_range
#answer.reshape(50,1)
#answer = label_scaler.inverse_transform(answer)
with open ('result200.txt','w') as f:
    f.write(str(answer))
'''