
# # #Bluring of a image
import cv2
 import numpy as np

 selena_img = cv2.imread('C:\opencv\selena_gomez.jpg')

 # Smoothening of Image using kernel matrix
# #kernel = np.ones((5, 5), np.float32)/26
 kernel = np.ones((7, 7), np.float32)/49

 print(kernel)

# # #-1  depth of output image
 smoothed_img = cv2.filter2D(selena_img, -1, kernel)
 cv2.imshow("frame1", selena_img)
 cv2.imshow("frame2", smoothed_img)

# # wait for any key
 cv2.waitKey(0)
# # Close all frames
 cv2.destroyAllWindows()
