import cv2
import matplotlib.pyplot as plt
import time
import numpy
import random
class CorrespondencePoints( ):
    def __init__(self , path1 , path2 , points):

        #Read the originals in rgb
        self.img1 = cv2.cvtColor(cv2.imread(path1), cv2.COLOR_BGR2RGB)
        self.img2 = cv2.cvtColor(cv2.imread(path2), cv2.COLOR_BGR2RGB)
        #Make a copy to "mark the dots"
        self.img1_copy = self.img1.copy()
        self.img2_copy = self.img2.copy()

        self.corresponding_points = points
        self.iterator = 0

        self.close = False # To block exiting fn
        self.point = ()  #For each individual point
        self.correspondence1 = [] #Correspondence vector in img1
        self.correspondence2 = [] #Correspondence vector in img2
        self.fig = plt.figure()
        self.color =  (random.randrange(256),random.randrange(256),random.randrange(256))
    def getCoord(self):
        #Show the images

        self.ax1 = self.fig.add_subplot(121)
        plt.imshow(self.img1)

        self.ax2 = self.fig.add_subplot(122)
        plt.imshow(self.img2 )

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
        #Determine the first img
        elif self.iterator == 0:
            self.imgaxis1 = click.inaxes
            print("Click on the 2nd image")
        #Determine the second image
        elif self.iterator == 1:
            self.imgaxis2 = click.inaxes
            print("Input the corresponding point "+str(len(self.correspondence1)+1)+" on img 1 " )

        #1st image correspondence points
        elif len(self.correspondence1) == len (self.correspondence2):
            if click.inaxes != self.imgaxis1:
                print("Wrong image!")
                return
            self.correspondence1.append(self.point)
            print("Input the corresponding point "+str(len(self.correspondence1))+" on img 2 " )
            self.ax1 = self.fig.add_subplot(121)
            self.ax1.clear()
            # The radius of the circle is 5/1000 of the width
            self.img1_copy  = cv2.circle(self.img1_copy,(int(click.xdata) , int(click.ydata)), int(5*self.img2_copy.shape[0]/1000), self.color, -1)
            plt.imshow(self.img1_copy )
        #2nd image correspondence points
        elif len(self.correspondence1) != len (self.correspondence2):
            if click.inaxes != self.imgaxis2:
                print("Wrong image!")
                return
            self.correspondence2.append(self.point)
            if not (self.iterator)/2 > self.corresponding_points:
                print("Input the corresponding point "+str(len(self.correspondence2)+1)+" on img 1 " )
            self.ax2.clear()
            self.ax2 = self.fig.add_subplot(122)
            self.img2_copy  = cv2.circle(self.img2_copy,(int(click.xdata) , int(click.ydata)), int(5*self.img2_copy.shape[0]/1000),  self.color, -1)
            self.color =  (random.randrange(256),random.randrange(256),random.randrange(256)) #Change the color

            plt.imshow(self.img2_copy)
        #Iterating till the desired points are reached
        self.iterator=self.iterator+1
        self.fig.canvas.draw()
        #If reached, close the canvas and finish the funcion
        if (self.iterator-1)/2 > self.corresponding_points:
            self.close = True
            plt.close()

#Usage
if __name__ == '__main__':
    rep = CorrespondencePoints('block-2/chess.jpg' , 'block-2/chess.jpg' , 4)
    rep.getCoord()
    print(rep.correspondence1)
    print(rep.correspondence2)
