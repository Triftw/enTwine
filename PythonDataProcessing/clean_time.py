# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 02:13:05 2020

@author: Trif
"""

import os
import numpy as np
import csv
path = 'C:\\Users\\Trif\\Desktop\\ToBeClean'
direction ='C:\\Users\\Trif\\Desktop\\Cleaned'
test = 'ground_truth2.csv'
folder =''
def clean_one(path,fname):
    with open(path+fname,'r') as f:
        file = csv.reader(f)
        file = list(file)
        with open(direction+folder+fname,'w') as fs:
            for i in range(18,len(file)):
                fs.write(((str(file[i]).split('\\t')))[1]+'\n')
                
with open (path+'\\'+test,'r') as f:
    file = csv.reader(f)
    file = list(file)
    with open(direction+folder+'\\'+test,'w') as fs:
            for i in range(18,len(file)):
                fs.write(file[i][1]+','+file[i][4]+','+file[i][7]+','+file[i][10]+'\n')
'''
for j in range(0,10):
    folder = '\\'+str(j)+'\\'
    files = os.listdir(path+folder)
    for ef in files:
        clean_one(path+folder,ef)
'''