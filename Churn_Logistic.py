# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 18:18:48 2018

@author: sparachi
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import pylab as pt

import os
import sys
print (os.getcwd())
os.chdir('D:\Koushik\AP\ML_AP')
print (os.getcwd())

Test_Churn= pd.read_csv('Churn_MV.csv')

Test_Churn.dropna(how='all',inplace=True)


Test_Churn['Daily Charges MV']=Test_Churn['Daily Charges MV'].fillna(Test_Churn['Daily Charges MV'].mean())


Test_Churn.dtypes
Test_Churn['Account Length'].astype('int64')

Test_Churn['Area Code'].astype('int64')


Test_Churn.describe()

y=Test_Churn['Churn']
ColToDrop=['VMail Message','Day Mins','Eve Mins','Night Mins','Intl Mins','Area Code']
Test_Churn.drop(ColToDrop,inplace=True,axis=1)

Test_Churn.keys()
Test_Churn.drop('Churn',inplace=True,axis=1)
X=Test_Churn
