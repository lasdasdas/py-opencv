#box filter --> it doesent work very well


import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../chess.jpg', 0)

kernel = 1/36*np.ones((6 , 6))
dst = cv2.filter2D(img, -1, kernel)

plt.subplot(121),plt.imshow(img,cmap = 'gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst,cmap = 'gray'),plt.title('Sharp filter')
plt.xticks([]), plt.yticks([])
plt.show()
