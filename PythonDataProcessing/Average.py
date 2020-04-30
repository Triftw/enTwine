# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 13:26:40 2020

@author: Trif
"""

import os
import numpy as np
import csv
path = 'E:\\桌面N\\0426ground\\'
avgfname = 'average.csv'
channel = 4
length = 10
a = [0.0,0.0,0.0,0.0]*length
cnt = 0
dcnt=0
#print(a[543][1])
for file in os.listdir(path):
    cnt +=1
    with open(path+file,'r') as f:
        print(file)
        f = csv.reader(f)
        f = list(f)
        for i in range(length):
            for j in range(channel):
                print(str(i)+' '+str(j))
                a[i][j] = float(a[i][j])+ float(f[i][j])
                print(str(a[9][3]))
#print(a[300][3])
with open(path+avgfname,'w') as af:
    for i in range(length):
        for j in range(channel):
            a[i][j] /=float(cnt)
    for i in range(length):
        af.write(str(a[i][0])+','+str(a[i][1])+','+str(a[i][2])+','+str(a[i][3])+'\n')