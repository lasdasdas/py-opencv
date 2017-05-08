import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../park.jpg', 0)



kernel_sharpen_2 = 1/9*np.array([[-1,-1,-1], [-1,18,-1], [-1,-1,-1]])
dst = cv2.filter2D(img, -1, kernel_sharpen_2)

plt.subplot(121),plt.imshow(img,cmap = 'gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst,cmap = 'gray'),plt.title('Sharp filter')
plt.xticks([]), plt.yticks([])
plt.show()
