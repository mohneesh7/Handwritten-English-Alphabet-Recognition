import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('235.jpg')
img_mean=cv2.mean(img)
print img_mean[:3][::-1]
