import numpy as np
import cv2 as cv

# generate some random data
data = np.random.sample(128)
# print data
for x in xrange(63): data = np.vstack((data, np.random.sample(128)))
# print data
print data.shape # (64, 128) i.e. 64 arrays of 128 dimensions

# train the PCA
mean, eigenvectors = cv.PCACompute(data, maxComponents=32)
print mean.shape # (1, 128)
print eigenvectors.shape # (32, 128)
print mean,eigenvectors