# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 21:44:37 2019

@author: andy3
"""
import numpy as np
import keras 

num_validation_samples=10000

np.random.shuffle(data)

validation_data=data[:num_validation_samples]

data=data[num_validation_samples:]

train_data=tada[:]

model=get_model()

model.train(train_data)

validation_score=model.evaluate(validation_data)




