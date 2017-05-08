import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('../chess.jpg')
# smoothing
kernel = np.ones((3,3),np.float32)/9
img = cv2.filter2D(img,-1,kernel)
# apply the canny filter
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150)

#High level hough implementation
lines = cv2.HoughLines(edges,1, np.pi/180,150)
for val in lines:
    rho= val[0][0]
    theta = val[0][1]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
for plot in lines:
    print(plot)
# ploting the imagess
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
