""" Like a boss: By Thomas van der Wardt and Eric Dignum """

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Import data in a Pandas DataFrame
train_df = pd.read_csv("C:/Users/Eric/SkyDrive/Kaggle/train.csv")
test_df = pd.read_csv("C:/Users/Eric/SkyDrive/Kaggle/test.csv")

# Clean the data

# Set male to 1 and female to 0
train_df['Gender'] = train_df['Sex'].map({'female': 0, 'male': 1}).astype(int)
test_df['Gender'] = test_df['Sex'].map({'female': 0, 'male': 1}).astype(int)

# Fill all missing embarked with the most common place to embark
train_df.Embarked.fillna(train_df.Embarked.mode()[0], inplace = True)
test_df.Embarked.fillna(test_df.Embarked.mode()[0], inplace = True)

# Give persons with a missing age the value of the mode of all ages
#train_df.Age.fillna(train_df.Age.mode()[0], inplace = True)
test_df.Age.fillna(test_df.Age.mode()[0], inplace = True)