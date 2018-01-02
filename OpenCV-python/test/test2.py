import cv2
	
import numpy as np
l=[]
j1=[]
k=[]
img=cv2.imread('235.jpg',-1).flatten()
img1=cv2.imread('3.jpg',-1).flatten()
img2=cv2.imread('4.jpg',-1).flatten()

# print img1
# print img1
# cv2.imshow('image',img)
# cv2.waitKey(0)
# print img.shape
# print img.dtype
# print img.size
# for i in range(34):
# 	for j in range(34):
# 		 l.append(img1[i,j])
# print l 
# for i in range(34):
# 	for j in range(34):
# 		 j1.append(img1[i,j])
# for i in range(34):
# 	for j in range(34):
# 		 k.append(img2[i,j])
# # print l
# a1=np.array(l)
# print a1
l1=[img,img1,img2]
# print l1
l1=np.vstack((img,img1,img2))
m,a=cv2.PCACompute(l1)
# print a,len(a),"\n"
# print m
# a2=np.reshape(a,(1,-1))
# cv2.imshow('image2',a2)
# cv2.waitKey(0)
