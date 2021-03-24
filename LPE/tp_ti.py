import numpy as np
import cv2
from matplotlib import pyplot as plt

I = cv2.imread('smarties.png', 0)
ret,I1 = cv2.threshold(I,245,255,cv2.THRESH_BINARY)

Idist = cv2.distanceTransform(255-I1, cv2.DIST_L2, 5)
ret,I2 = cv2.threshold(Idist,10,255,cv2.THRESH_BINARY)
kernel = np.ones((2,17),np.uint8)
I2=cv2.erode(I2,kernel)

num_labels, Ilabels = cv2.connectedComponents(I2.astype(np.uint8))
I3 = Ilabels + (I1)*((num_labels+1)/255);

plt.figure() # ouvre une nouvelle figure
plt.subplot(221) # Image 1
plt.imshow(I1, 'binary') # colormap 'binary'
plt.title('Thresholded Image')
plt.subplot(222) # Image 2
plt.imshow(Idist, 'gray') # colormap 'gray'
plt.title('Distance Transform')
plt.subplot(223) # Image 3
plt.imshow(I2, 'gray') # colormap 'gray'
plt.title('Distance Transform + threshold')
plt.subplot(224) # Image 4
plt.imshow(I3, 'jet') # colormap 'jet'
plt.title('Labels')
plt.show()

# print(I2[150::170][30::50])
print(num_labels)