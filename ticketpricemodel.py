# -*- coding: utf-8 -*-
"""
Created on Tue May 19 13:29:23 2015

@author: Thomas
"""

import csv
import numpy as np

csv_file_object = csv.reader(open('train.csv', 'rb'))
header = csv_file_object.next()

# Import data in 'data' as numpy array

data = []
for row in csv_file_object:
    data.append(row)
data = np.array(data)

# Start creating array gender, class, price paid

print data[0::,9]
#print data[0::,9].astype(np.float)

# Price-ceiling
#fare_ceiling = 40
#data[ data[0::,9].astype(np.float) >= fare_ceiling, 9] = fare_ceiling - 1.0

