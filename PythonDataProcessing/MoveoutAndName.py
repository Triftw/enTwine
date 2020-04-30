# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 14:44:44 2020

@author: Trif
"""

import os
path ='E:\\桌面N\\0426Knot_NT\\slip'
def moveout(MainFolder):
    for sfolder in os.listdir(MainFolder):
        #print(sfolder)
        if sfolder == '正北':
            fix = 'NP'
        if sfolder == '負北':
            fix = 'NN'
        if sfolder == '正東':
            fix = 'EP'
        if sfolder == '負東':
            fix = 'EN'
        if sfolder == '正南':
            fix = 'SP'
        if sfolder == '負南':
            fix = 'SN'
        if sfolder == '正西':
            fix = 'WP'
        if sfolder == '負西':
            fix = 'WN'
        fpath = MainFolder+'\\'+sfolder+'\\'
        nfpath = MainFolder+'\\'
        #os.mkdir(nfpath)
        for file in os.listdir(fpath):
            os.rename(fpath+file,nfpath+fix+file)
moveout(path)