import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../park.jpg', 0)


dst=cv2.GaussianBlur(img,(15,15),0)

plt.subplot(121),plt.imshow(img,cmap = 'gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst,cmap = 'gray'),plt.title('Gaussian filter')
plt.xticks([]), plt.yticks([])
plt.show()
