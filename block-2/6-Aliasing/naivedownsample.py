import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../park.jpg', 0)
img_gaussian=cv2.GaussianBlur(img,(3,3),0)

#Own implementation
img_down_nofilter=np.zeros((int(img.shape[0]/2),int(img.shape[1]/2)))
img_down_gaussian=np.zeros((int(img.shape[0]/2),int(img.shape[1]/2)))
for i in range(int(img.shape[0]/2)):
     for j in range(int(img.shape[1]/2)):
         img_down_nofilter[i][j]=img[2*i][2*j]
         img_down_gaussian[i][j]=img_gaussian[2*i][2*j]

#Opencv implementation
img_down_cv = cv2.pyrDown(img)

plt.subplot(221),plt.imshow(img,cmap = 'gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(img_down_nofilter,cmap = 'gray'),plt.title('Downsampled')
plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(img_down_gaussian,cmap = 'gray'),plt.title('Gaussian + Downsampled')
plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(img_down_cv,cmap = 'gray'),plt.title('OpenCV downsampled')
plt.xticks([]), plt.yticks([])
plt.show()
