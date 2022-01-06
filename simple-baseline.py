import numpy as np
import pandas as pd 
from sklearn.metrics import accuracy_score, mean_squared_error, f1_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import random

#load datasets
train_data = pd.read_csv('data/train_data.csv', sep=',')
test_data = pd.read_csv('data/test_data.csv', sep=',')
dev_data = pd.read_csv('data/dev_data.csv', sep=',')

#get rid of review id column
test_data = test_data.iloc[:, 1:]
dev_data = dev_data.iloc[:,1:]
train_data = train_data.iloc[:,1:]


# Simple baseline 1: Use the average star rating of all the reviews in the training set 
train_true_labels =  train_data['star_rating'].to_numpy()
avg_value = np.mean(train_true_labels)

avg_class = [avg_value for x in range(len(test_data))]

#write out the csv file for predictions using the average review baseline
with open('avg_baseline_output.csv', 'w') as f:
    for pred in avg_class:
        f.write(str(pred))
        f.write('\n')


# Simple baseline 2: Randomly assign a rating from 1 to 5 to the predictions
random.seed(5)
random_class = [random.randint(1,5) for x in range(len(test_data))]
random_class = np.asarray(random_class)

#write out the csv file for the predictions using the random baseline 
with open('random_baseline_output.csv', 'w') as f:
    for pred in random_class:
        f.write(str(pred))
        f.write('\n')