# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 20:07:39 2020

@author: Trif
"""

from tensorflow.python.client import device_lib
from keras import backend as K
import keras
import tensorflow as tf
config = tf.ConfigProto( device_count = {'GPU': 1 , 'CPU': 56} ) 
sess = tf.Session(config=config) 
keras.backend.set_session(sess)
#print(device_lib.list_local_devices())
#K.tensorflow_backend._get_available_gpus()