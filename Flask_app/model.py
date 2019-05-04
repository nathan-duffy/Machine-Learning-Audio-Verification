#Imports
import pandas as pd
import numpy as np
from skimage.io import imread
import skimage
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pickle
import requests
import json

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
scalar = StandardScaler()

from sklearn.svm import SVC

def main():

	#filepath = input()

	#Finding Features of new Spectogram

	#Training the Algorithm
	df = pd.read_csv('SCORE_v1.csv', header = None)

	#Finding and converting raw data
	Y = df.iloc[:, 0].values.astype(str)
	X = df.iloc[:, 1:].values.astype(float)
	scalar.fit(X)
	X = scalar.transform(X)

	#Finding and converting test data
	Y_test = df.iloc[800:, 0].values
	X_test = df.iloc[800:, 1:].values.astype(float)

	scalar.fit(X_test)
	X_test = scalar.transform(X_test)


	classifier = SVC(probability = True, random_state = 123)

	classifier.fit(X,Y)
	print('fitted')


	#Serializing our model to a file called model.pkl
	filename = 'model.pkl'
	outfile = open(filename,'wb')
	pickle.dump(classifier,outfile)
	outfile.close()


if __name__ == '__main__':
	main()
