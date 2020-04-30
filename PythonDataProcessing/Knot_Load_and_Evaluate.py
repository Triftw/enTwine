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
from pickle import load
#one hot encoding [Overhand Eight Slip Clove]
direction ='E:\\桌面N\\Data_cleantime'
test_path = 'E:\\桌面N\\0428test'
version_name = '0428KnotverC1.8'

test_feature = np.array([])
#order = np.array([0,1,2,3,4,5,6,7,8,9])
data_cnt = 20
feature_length = 2000
#folders = os.listdir(test_path)
'''
for i in range(len(order)):
    j = order[i]
    print(folders[j])
    folder = '\\'+str(folders[j])+'\\'
    files = os.listdir(test_path+folder)
'''
folder = '\\'
files = os.listdir(test_path)
fn =[]
for f in files:
    fn.append(f[0])
    rd = pd.read_csv(test_path+folder+f)
    test_feature = np.append(test_feature,rd)
        
#data_cnt = data_cnt*len(order)
test_feature = test_feature.reshape(4*data_cnt,feature_length,)
data_scaler_minmax = load(open(version_name+'_scaler.pkl', 'rb'))
test_feature = data_scaler_minmax.fit_transform(test_feature)
test_feature = test_feature.reshape(data_cnt,feature_length,4)
if 'C' in version_name:
    test_feature = test_feature.reshape(data_cnt,1,feature_length,4,1)
model = kr.models.load_model(version_name+'.h5')
model.summary()



answer = model.predict(test_feature,verbose=0)
anss=[]
ans = '?'
anst = -1
temp = 0.0
with open (version_name+'result1.txt','w') as f:
    for i in range(len(answer)):
        for j in range(len(answer[0])):
            if answer[i][j]> temp:
                temp = answer[i][j]
                anst = j
            if anst == 0:
                ans = 'Overhand'
            if anst == 1:
                ans = 'Eight'
            if anst == 2:
                ans = 'Slip'
            if anst == 3:
                ans = 'Clove'
        print(str(fn[i])+' '+str(ans))
            #anss.append(ans)
        f.write(str(fn[i])+' '+str(ans+'\n'))