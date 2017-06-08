import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('../chess.jpg',0)
# smoothing
kernel = np.ones((3,3),np.float32)/9
img = cv2.filter2D(img,-1,kernel)
# apply the canny filter
edges = cv2.Canny(img,0,40)
# ploting the imagess
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()
