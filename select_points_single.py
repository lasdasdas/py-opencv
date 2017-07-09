import cv2
import matplotlib.pyplot as plt
import time
import numpy
import random
class CorrespondencePoints( ):
    def __init__(self , path1 , points):

        #Read the originals in rgb
        self.img1 = cv2.cvtColor(cv2.imread(path1), cv2.COLOR_BGR2RGB)
        #Make a copy to "mark the dots"
        self.img1_copy = self.img1.copy()


        self.corresponding_points = points
        self.iterator = 0

        self.close = False # To block exiting fn
        self.point = ()  #For each individual point
        self.correspondence1 = [] #Correspondence vector in img1
        self.fig = plt.figure()
        self.color =  (random.randrange(256),random.randrange(256),random.randrange(256))
    def getCoord(self):
        #Show the images
        self.ax1 = self.fig.add_subplot(111)
        plt.imshow(self.img1)

        #Link the click event to the onclick fn
        cid = self.fig.canvas.mpl_connect('button_press_event', self.onclick)
        print("Click on the 1st image")
        plt.show()

        #Wait for the points to be clicked
        while not self.close:
            pass
        return

    def onclick(self,click):
    #A bit messy, every event requests the information for the next one.
        self.point = (click.xdata,click.ydata)
        #Clicked outside
        if click.inaxes == None:
            print("What you clicked was not an image")
            return self.point
        #correspondence points
        else:
            self.correspondence1.append(self.point)
            print("Input the corresponding point "+str(len(self.correspondence1))+" on img 2 " )
            self.ax1 = self.fig.add_subplot(111)
            self.ax1.clear()
            # The radius of the circle is 5/1000 of the width
            self.img1_copy  = cv2.circle(self.img1_copy,(int(click.xdata) , int(click.ydata)), int(5*self.img1_copy.shape[0]/1000), self.color, -1)
            plt.imshow(self.img1_copy )

        self.color =  (random.randrange(256),random.randrange(256),random.randrange(256)) #Change the color
        #Iterating till the desired points are reached
        self.iterator=self.iterator+1
        self.fig.canvas.draw()
        #If reached, close the canvas and finish the funcion
        if (self.iterator+1) > self.corresponding_points:
            self.close = True
            plt.close()

#Usage
if __name__ == '__main__':
    rep = CorrespondencePoints('block-2/chess.jpg'  , 4)
    rep.getCoord()
    print(rep.correspondence1)
