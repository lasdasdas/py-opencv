import sys
sys.path.append('../../')
import select_points
import cv2
import numpy as np
from matplotlib import pyplot as plt

rep = select_points.CorrespondencePoints('desk1.jpg' , 'desk2.jpg' ,15)
print("Please mark 15 corresponding points on each picture")
rep.getCoord()
rep1 = np.asarray(rep.correspondence1)
rep2 = np.asarray(rep.correspondence2)
fundamental_matrix =cv2.findFundamentalMat(rep1, rep2, cv2.FM_RANSAC, 3, 0.99);
print(fundamental_matrix)
