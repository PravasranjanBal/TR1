#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np
#### Load source data
s_data = pd.read_csv("F:\\oodata_python\\jedit\\jedit-4.0.csv")
s_input = s_data.loc[:,'wmc':'avg_cc']


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


t_data = pd.read_csv("F:\\oodata_python\\ant\\ant-1.3.csv")
t_input = t_data.loc[:,'wmc':'avg_cc']

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
noise = np.random.normal(mu, sigma, [l,20]) 
#print(noise)

new_input_train = (t1_input_train+noise)
new_output_train = t1_output_train

# Normalization
from sklearn import preprocessing
new_input_train = preprocessing.normalize(new_input_train,norm='l2')
new_input_test = preprocessing.normalize(new_input_test,norm='l2')

# One Hot Encoding
from keras.utils import to_categorical
source_output = to_categorical(new_output_train)
target_output = to_categorical(new_output_test)


# Define model
from keras.models import Sequential
from keras.layers import Dense
#from keras.optimizers import SGD
from matplotlib import pyplot
#from keras.layers import Dropout
#from keras import regularizers
from keras.layers import Dropout
from keras.layers import Activation
model = Sequential()
model.add(Dense(150, input_dim=20, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(150, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(150, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(2, activation='softmax'))

from keras import optimizers
adam = optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False)
model.compile(loss='binary_crossentropy', optimizer=adam, metrics=['accuracy'])
model.summary()
# fit model
history = model.fit(new_input_train, source_output, validation_data=(new_input_test, target_output), batch_size=32, epochs=300)

# evaluate the model
train_ac = model.evaluate(new_input_train, source_output, verbose=0)
test_ac = model.evaluate(new_input_test, target_output, verbose=0)
_,train_acc = model.evaluate(new_input_train, source_output, verbose=0)
_,test_acc = model.evaluate(new_input_test, target_output, verbose=0)
# Probability prediction of classes
y_predict = model.predict(new_input_test, verbose=0)
# Prediction of classes
#y_class = model.predict_classes(new_input_test)

y_class = np.argmax(y_predict,axis=1)
#print('Probability prediction Results:\n', y_predict)
#print('prediction Results:\n', y_class)

#print('Actual Value:\n', output_test)
#print('Predicted Value:\n', y_class)
print('Train Accuracy:\n',train_ac)
print('Test Accuracy:\n', test_ac)
#print('Train: %.3f, Test: %.3f' % (train_acc, test_acc))

# plot history
# summarize history for accuracy
#from matplotlib import pyplot
#pyplot.plot(history.history['acc'], label='train')
#pyplot.plot(history.history['val_acc'], label='test')
#pyplot.legend()
#pyplot.xlabel('Number of epochs')
#pyplot.ylabel('Accuracy')
#pyplot.savefig('figg.png')
#pyplot.savefig('figg.pdf')
#pyplot.show()

#print('Actual Value:\n', output_test)
#print('Predicted Value:\n', y_class)
print('Train Accuracy:\n',train_ac)
print('Test Accuracy:\n', test_ac)
print('Train: %.3f, Test: %.3f' % (train_acc, test_acc))


# Confusion matrix generation
from sklearn.metrics import confusion_matrix
cf = confusion_matrix(new_output_test, y_class)
print('Confusion Matrix: \n',cf)

# Accuracy
from sklearn.metrics import accuracy_score
acc = accuracy_score(new_output_test, y_class)
print('Accuracy: %f'%acc)

# Recall
from sklearn.metrics import recall_score
re = recall_score(new_output_test, y_class)
print('Recall: %f' % re)

# Precision
from sklearn.metrics import precision_score
pr = precision_score(new_output_test, y_class)
print('Precision: %f' % pr)

# F1 Score
from sklearn.metrics import f1_score
f1 = f1_score(new_output_test, y_class)
print('F1 score: %f' % f1)

# ROC Curve and AUC
from sklearn.metrics import roc_auc_score
# ROC AUC
auc = roc_auc_score(new_output_test, y_class)
print('ROC AUC: %f' % auc)

