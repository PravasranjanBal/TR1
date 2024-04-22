#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd
import numpy as np
#### Load source data
#s_data = pd.read_csv("F:\\oodata_python\\ant\\ant-1.3.csv")
#s_input = s_data.loc[:,'wmc':'avg_cc']

s_data = pd.read_csv("F:\\oodata_python\\AEEEM\\EQ.csv")
s_input = s_data.loc[:,'ck_oo_numberOfPrivateMethods':'LDHH_numberOfMethods']

s_output = s_data.loc[:,'bug']
#print(s_output)

# SMOTE balancing method
from collections import Counter
print('Original source dataset shape %s' % Counter(s_output))
from imblearn.over_sampling import SMOTE
sm = SMOTE()
s_input, s_output = sm.fit_resample(s_input, s_output)
print('Resampled source dataset shape %s' % Counter(s_output))

# Normalization
#from sklearn import preprocessing
#s_normalized_input = preprocessing.normalize(s_input,norm='l2')
s_normalized_input = s_input

#t_data = pd.read_csv("F:\\oodata_python\\jedit\\jedit-4.3.csv")
#t_input = t_data.loc[:,'wmc':'avg_cc']

t_data = pd.read_csv("F:\\oodata_python\\AEEEM\\PDE.csv")
t_input = t_data.loc[:,'ck_oo_numberOfPrivateMethods':'LDHH_numberOfMethods']

t_output = t_data.loc[:,'bug']
#print(Output)

# SMOTE balancing method
from collections import Counter
print('Original target dataset shape %s' % Counter(t_output))
from imblearn.over_sampling import SMOTE
sm = SMOTE()
t_input, t_output = sm.fit_resample(t_input, t_output)
print('Resampled target dataset shape %s' % Counter(t_output))

# Normalization
#from sklearn import preprocessing
#t_normalized_input = preprocessing.normalize(t_input,norm='l2')
t_normalized_input  = t_input

# splitting the testing data sets
from sklearn.model_selection import train_test_split
t_input_train, t_input_test, t_output_train, t_output_test = train_test_split(t_normalized_input, t_output, test_size=0.3)


# Length of target data
len_tdata = len(t_data)
print('Length of target data: \n',len_tdata)

new_source_input_data = np.concatenate((s_normalized_input, t_input_train), axis=0)

new_source_output_data = np.concatenate((s_output, t_output_train), axis=0)

new_input_test = t_input_test
new_output_test = t_output_test

# splitting the new_source_input and output data
from sklearn.model_selection import train_test_split
t1_input_train, t1_input_test, t1_output_train, t1_output_test = train_test_split(new_source_input_data, new_source_output_data, test_size=0.2)

new_input_val = t1_input_test
new_output_val = t1_output_test

import numpy as np 
mu, sigma = 0, 0.1 

l = len(t1_input_train)
# creating a noise with the same dimension as the dataset (2,2) 
noise = np.random.normal(mu, sigma, [l,61]) 
#print(noise)

new_input_train = (t1_input_train+noise)
new_output_train = t1_output_train


# Prediction using KNN
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(new_input_train,new_output_train)
y_pred = classifier.predict(new_input_test)


# Confusion matrix generation
from sklearn.metrics import confusion_matrix
cf = confusion_matrix(new_output_test, y_pred)
print('Confusion Matrix: \n',cf)

# Accuracy
from sklearn.metrics import accuracy_score
acc = accuracy_score(new_output_test, y_pred)
print('Accuracy: %f'%acc)

# Recall
from sklearn.metrics import recall_score
re = recall_score(new_output_test, y_pred)
print('Recall: %f' % re)

# Precision
from sklearn.metrics import precision_score
pr = precision_score(new_output_test, y_pred)
print('Precision: %f' % pr)

# F1 Score
from sklearn.metrics import f1_score
f1 = f1_score(new_output_test, y_pred)
print('F1 score: %f' % f1)

# ROC Curve and AUC
from sklearn.metrics import roc_auc_score
# ROC AUC
auc = roc_auc_score(new_output_test, y_pred)
print('ROC AUC: %f' % auc)

