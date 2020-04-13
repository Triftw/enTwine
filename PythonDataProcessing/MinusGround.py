# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 02:13:05 2020

@author: Trif
"""

import os
import numpy as np
import csv
path = 'C:\\Users\\Trif\\Desktop\\Cleaned'
ground = 'ground_truth1.csv'
test = 'overhand2'
folder ='0411_1'
                
with open (path+'\\'+ground,'r') as g:
    groundf = csv.reader(g)
    groundf = list(groundf)
    #targets = os.listdir(path+'\\'+folder)
    targets =['ground_truth2.csv']
    if not os.path.exists(path+'\\'+'D'+folder):
        os.mkdir(path+'\\'+'D'+folder)
    for tf in targets:
        with open (path+'\\'+folder+'\\'+tf,'r') as f:
            file = csv.reader(f)
            file = list(file)
            
            with open(path+'\\'+'D'+folder+'\\'+'D'+tf,'w') as fw:
                fw.write('t1,t2,t3,t4\n')
                for i in range(2000):
                    t1 = float(file[i][0]) - float(groundf[i][0])
                    t2 = float(file[i][1]) - float(groundf[i][1])
                    t3 = float(file[i][2]) - float(groundf[i][2])
                    t4 = float(file[i][3]) - float(groundf[i][3])
                    fw.write(str(t1)+','+str(t2)+','+str(t3)+','+str(t4)+'\n')
 
'''
for j in range(0,10):
    folder = '\\'+str(j)+'\\'
    files = os.listdir(path+folder)
    for ef in files:
        clean_one(path+folder,ef)
'''