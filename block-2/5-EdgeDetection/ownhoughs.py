# Manual implementation of the hougs figures
import matplotlib.pyplot as plt
import numpy as np
import math
from numpy import cos , sin
import cv2

d2r= math.pi/180


img = cv2.imread('../chess.jpg')

# smoothing
kernel = np.ones((3,3),np.float32)/9
img = cv2.filter2D(img,-1,kernel)

grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# apply the canny filter
dst = cv2.Canny(img,0,90)

#Arrays to transform to hough and to make the voting
angle=np.linspace(-math.pi/2, math.pi/2, num=100 )
canvas  =  np.zeros((100, 4*img.shape[1]) , dtype=float)
for i in range(dst.shape[0]):
    print(str(100*i/dst.shape[0])+"%")
    for j in range(dst.shape[1]):
        if dst[i][j] > 253:
            point=[i, j]
            b = (point[0]*cos(angle) + point[1]*sin(angle))
            for k in range(len(b)):
                element= int(b[k])
                element = element +2*img.shape[1]
                canvas [k , element] += 10
#Get a copy of the canvas
canvas_filtered = np.copy(canvas)
#Get the number that makes the 99.95 percentile
percentile = np.percentile(canvas_filtered, 99.995)
#Zero out all the results below the threshold
canvas_filtered[canvas_filtered < (percentile)]=0
#Reconvert the remaining results from hough to xy
for i in range(canvas_filtered.shape[0]):
    for j in range(canvas_filtered.shape[1]):
        if canvas_filtered[i , j]>0.0001:
            teta = angle[i]
            distance = j-2*img.shape[1]
            x1 = 0
            x2 = canvas_filtered.shape[1]
            y1 =int((distance-x1*cos(teta))/sin(teta))
            y2 =int((distance-x2*cos(teta))/sin(teta))
            cv2.line(grey,(y1,x1),(y2,x2),(0,0,255),2)#Careful, this has been transposed

#Plot the results
#Transposing everything to draw on the canvas
plt.subplot(221)
plt.title('Hough space results')
plt.imshow(canvas.T, interpolation='nearest', aspect='auto')
plt.subplot(222)
plt.title('Hough space filtered')
plt.imshow(canvas_filtered.T, interpolation='nearest', aspect='auto')
plt.subplot(223)
plt.title('Found lines'), plt.xticks([]), plt.yticks([])
plt.imshow(grey , cmap = 'gray' )
plt.show()
