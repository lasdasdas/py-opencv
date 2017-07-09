
import sys
sys.path.append('../../')
import select_points_single
import cv2
import numpy as np
from matplotlib import pyplot as plt


# Follow the instructions in the terminal
rep = select_points_single.CorrespondencePoints('chess1.jpg' , 4)
print("Click on the 4 corners of the square to unwarp the prespective: ")
print("For correct reconstruction: bot right first and then couterclockwise order")
rep.getCoord()

#Transform the list of tuples to a np array
rep1 = np.asarray(rep.correspondence1)
print(rep1)
rep2 = 4000*np.array([[1, 1] , [1 , 0],[0, 0] , [0, 1]])

#Find the homograpty given the two datasets of corresponding points
h, status = cv2.findHomography(rep1, rep2)

#Project image 1 into image 2
img_project = cv2.warpPerspective(rep.img1  , h, (rep.img1.shape[0],rep.img1.shape[0]))

# Display images
plt.subplot(221),plt.imshow(rep.img1),plt.title('Image 1 '),plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(img_project),plt.title('Image 1 projected square image 2'),plt.xticks([]), plt.yticks([])
plt.show()
