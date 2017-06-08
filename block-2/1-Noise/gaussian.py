import cv2
import numpy as np
from matplotlib import pyplot as plt
#Gaussian function
def gaussian_noise(img , height , width , coef , mu , sigma):
    img_copy = img.copy()
    img_gaussian=np.random.normal(mu , sigma , (height, width))
    arr = np.random.random((height, width))
    for i in range(height):
        for j in range(width):
            if arr[i][j]>coef:
                pass
            elif arr[i][j]<coef and (coef)/2 > (arr[i][j]):
                img_copy[i][j]=img_gaussian[i][j]
            elif arr[i][j]<coef and (coef)/2 < (arr[i][j]):
                img_copy[i][j]=img_gaussian[i][j]
    return(img_copy)
def main():
    #Sourcing and operating the images
    img = cv2.imread('../moon.jpg' )
    height, width , sd= img.shape
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    noisy=gaussian_noise(img ,  height , width ,0.1, 126 , 30)
    cv2.randn(img,126,180);

    # Plotting the image
    plt.subplot(121),plt.imshow((255-img) ,cmap='Greys'),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow((255-(noisy)), cmap='Greys'),plt.title('Noise')
    plt.xticks([]), plt.yticks([])
    plt.show()
if __name__ == "__main__":
    main()
