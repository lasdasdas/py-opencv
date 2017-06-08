# Manual implementation of the hougs figures
import matplotlib.pyplot as plt
import numpy as np
import math
from numpy import cos , sin
import cv2


def gridbelong(grid , point):
    pass


d2r= math.pi/180


img = cv2.imread('../chess.jpg',0)
# smoothing
kernel = np.ones((3,3),np.float32)/9
img = cv2.filter2D(img,-1,kernel)
# apply the canny filter
dst = cv2.Canny(img,0,40)
angle=np.linspace(-math.pi/2, math.pi/2, num=1000   )
print(dst.shape)
col =300*"rbgkm"
for i in range(dst.shape[0]):
    print("line ",i )
    for j in range(200):
        if dst[i][j] > 150:
            point=[i, j]
            b = (point[0]*cos(angle) + point[1]*sin(angle))
            plt.plot(angle, b, color= col[j])
# plt.axis([0, 6, 0, 20])
plt.show()
