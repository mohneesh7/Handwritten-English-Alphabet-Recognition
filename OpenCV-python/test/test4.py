	# An aapproach to calculate the PCA of different features of the image
#Beta_1
# resolution in each image : 34*34

import os
import numpy as np
import cv2 as cv
import random as r


os.chdir('/home/mohneesh/Desktop/ML/handwritten-character-recognition-ocr/Dataset/output')
path = 'A'
temp=[]
list_of_files=os.listdir(path)
r.shuffle(list_of_files)
for i in list_of_files:
	im = cv.imread(os.path.join(path,i),-1).flatten()
	temp.append(im)		
temp=np.array(temp)
temp=np.vstack(temp)
print temp
print temp.shape		# the dimension of the  NumPy Array

mean1, eigenvectors = cv.PCACompute(temp,np.mean(temp),maxComponents=(100))

print mean1.shape        # the dimensions of mean

print eigenvectors.shape	## the dimensions of eigenvectors
eigenvector=lambda x : [x[:50] for x in eigenvectors]
e=eigenvector(eigenvectors)
e=np.array(e)
print e
np.savetxt('A.csv',e,delimiter=",",fmt="%.4f")
