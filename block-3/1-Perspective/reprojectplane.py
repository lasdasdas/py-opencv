
import sys
sys.path.append('../../')
import select_points
import cv2
import numpy as np
from matplotlib import pyplot as plt


# Follow the instructions in the terminal
rep = select_points.CorrespondencePoints('chess1.jpg', 'chess2.jpg' , 4)
rep.getCoord()

#Transform the list of tuples to a np array
rep1 = np.asarray(rep.correspondence1)
rep2 = np.asarray(rep.correspondence2)

#Find the homograpty given the two datasets of corresponding points
h, status = cv2.findHomography(rep1, rep2)

#Project image 1 into image 2
img_project = cv2.warpPerspective(rep.img1  , h, (rep.img2.shape[1],rep.img2.shape[0]))

# Display images
plt.subplot(221),plt.imshow(rep.img1),plt.title('Image 1 '),plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(rep.img2),plt.title('Image2'),plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(img_project),plt.title('Image 1 projected as image 2'),plt.xticks([]), plt.yticks([])
plt.show()
