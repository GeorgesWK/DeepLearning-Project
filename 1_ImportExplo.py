# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 18:45:53 2020

@author: Georges
"""


# -*- coding: utf-8 -*-
"""
Importing the data and exploring it
"""
import numpy as np
import pandas as pd
import os
import re
import matplotlib.pyplot as plt

#import seaborn as sns

#import difflib


# Set working directory
path = os.getcwd()

# Import
train = pd.read_csv("anno_train.csv", header = None)
print(train.shape)

test = pd.read_csv("anno_test.csv", header = None)
print(test.shape)

names = pd.read_csv("names.csv", header = None)
print(names.shape)

################################# Exploration #################################
print(train.head())

# Train - set column names
train.columns = ['Image', 'Box 1', 'Box 2', 'Box 3', 'Box 4', 'Y']
print(train.head())

# Names - Extract Maker
names.columns = ['Key']
names['Maker'] = names['Key'].str.split().str[0]

# Names - Extract Year
names['Year'] = names['Key'].str.extract('(\d{4})', expand=True)

# Names - Extract Model
info = names['Key']
info = info.to_frame()
info.columns = ['Year']



# Outer Join
#names.Key = names.Key.astype(str)
#names.Year = names.Key.astype(str)
#names.Maker = names.Key.astype(str)
#info.Year = info.Year.astype(str)

# a = names.join(info, on = 'Year', how = 'outer')


print(names.head())
print(info.head())
