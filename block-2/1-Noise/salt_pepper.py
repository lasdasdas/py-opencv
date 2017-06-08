import cv2
import numpy as np
from matplotlib import pyplot as plt
#Salt and pepper function
def salt_and_pepper_noise(img , coef , height , width ):
    arr = np.random.random((height, width))
    img_copy = img.copy()
    for i in range(height):
        for j in range(width):
            if arr[i][j]>coef:
                pass
            elif arr[i][j]<coef and (coef)/2 > (arr[i][j]):
                img_copy[i][j]=255
            elif arr[i][j]<coef and (coef)/2 < (arr[i][j]):
                img_copy[i][j]=0
    return(img_copy)

def main():
    #Sourcing and operating the images
    img = cv2.imread('../moon.jpg' )
    height, width , sd= img.shape
    print(img.shape)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    noisy=salt_and_pepper_noise(img ,0.08,  height , width)

    # Plotting the imagea
    plt.subplot(121),plt.imshow((255-img) ,cmap='Greys'),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow((255-(noisy)), cmap='Greys'),plt.title('Noise')
    plt.xticks([]), plt.yticks([])
    plt.show()
if __name__ == "__main__":
    main()
