# -*- coding: utf-8 -*-
"""
Created on Tue May 19 13:29:23 2015

@author: Thomas
"""

import csv
import numpy as np

csv_file_object = csv.reader(open('C:\Users\Thomas\Documents\GitHub\Kaggle\train.csv', 'rb'))
header = csv_file_object.next()

# Import data in 'data' as numpy array
data = []
for row in csv_file_object:
    data.append(row)
data = np.array(data)

# Find number of passengers and survivors
number_passengers = np.size(data[0::,1].astype(np.float))
number_survived = np.sum(data[0::,1].astype(np.float))
proportion_survivors = number_survived / number_passengers

# Find mean of age of passengers
age_sum = []
for a in data[0::,5]:
    if a != '0':
        a = a.astype(np.float)
        age_sum.append(a)
        
mean = np.mean(age_sum)

# Get only women and only men data
above_mean = data[0::,5].astype(np.float) > mean
under_mean = data[0::,5].astype(np.float) < mean

abovemean_onboard = data[above_mean,1].astype(np.float)     
undermean_onboard = data[under_mean,1].astype(np.float)

# Find out survival percentage men/women
proportion_above_mean_survived = np.sum(abovemean_onboard) / np.size(abovemean_onboard)
proportion_under_mean_survived = np.sum(undermean_onboard) / np.size(undermean_onboard) 

test_file = open('test.csv', 'rb')
test_file_object = csv.reader(test_file)
test_file_object.next()

for row in test_file_object:
    print float(row[4])
    #if int(row[4]) < mean:
        #print 'hoi'

def save_prediction(mean):
    test_file = open('test.csv', 'rb')
    test_file_object = csv.reader(test_file)
    test_file_object.next()

    prediction_file = open("agebasedmodel.csv", "wb")
    prediction_file_object = csv.writer(prediction_file)


    prediction_file_object.writerow(["PassengerId", "Survived"])
    for row in test_file_object:       # For each row in test.csv
        if row[5] < mean:         # is it a female, if yes then                                       
            prediction_file_object.writerow([row[0],'1'])    # predict 1
        else:                              # or else if male,       
            prediction_file_object.writerow([row[0],'0'])    # predict 0
        test_file.close()
        prediction_file.close()

#save_prediction(mean)