import os
import numpy as np
import cv2 as cv
import random as r
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt 
from sklearn import svm


def main():
	"This function now takes in all the images in the Dataset and calculate the PCA and returns the only uncorrelated elements"

	os.chdir('/home/mohneesh/Desktop/ML/handwritten-character-recognition-ocr/Dataset/output') 

	# enter the path where the images are at.
	path = 'Z' 	

	temp=[]
	list_of_files=os.listdir(path)

	# randomize the images 
	r.shuffle(list_of_files)	

	for i in list_of_files:
		im = cv.imread(os.path.join(path,i),-1).flatten()
		temp.append(im)

	# # #plot 
	# plt.scatter(temp[0],temp[1])
	# plt.show()

	# Converting the List to a NumPy array		
	temp=np.array(temp,dtype='float64')

	# Giving it a matrix arrangement (just a visual affect nothing logically)
	temp=np.vstack(temp)

	# Standardizing the dataset ( can be individually done)
	X = StandardScaler().fit_transform(temp)
	print "The dimensions before PCA :",X.shape

	# #plot
	# plt.scatter(X[0],X[1])
	# plt.show()

	# Create a pca object retaining a variency of 99% and whiten it( whitening transformation is a linear transformation that transforms a vector of random variables with a known covariance matrix into a set of new variables whose covariance is the identity matrix, meaning that they are uncorrelated and each have variance 1.)
	pca = PCA(n_components=0.99,whiten=True)
	
	# first fit and then transform the pca object with the already scaled dataset
	x_=pca.fit_transform(X)
	print "The dimensions After PCA :",x_.shape
	print x_

	#plot
	# plt.scatter(x_[0],x_[1])
	# plt.show()

	# write the reduced dataset to a .csv file
	np.savetxt('Z.csv',x_[:100],delimiter=",",fmt="%.4f")

if __name__ == '__main__':
	# print main.__doc__
	main()
