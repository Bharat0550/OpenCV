
import cv2
import numpy as np

selena_img = cv2.imread('C:\opencv\selena_gomez.jpg')

# Smoothening of Image using kernel matrix
kernel = np.ones((5, 5), np.float32)/25
#kernel1 = np.ones((9, 9), np.float32)/81

print(kernel)
#print(kernel1)

# # #-1  depth of output image
smoothed_img = cv2.filter2D(selena_img, -1, kernel)
#smoothed_img1 = cv2.filter2D(selena_img, -1, kernel1)
cv2.imshow("original image", selena_img)
cv2.imshow("frame2", smoothed_img)
#cv2.imshow("frame3", smoothed_img1)

# Gaussian Blur - kernel must be odd positive
# It normalize the image pixel 
g_blur = cv2.GaussianBlur(selena_img, (7,7), 0) 
cv2.imshow("frame3", g_blur)

# Median Blur - Median of pixel values under selected region
m_blur = cv2.medianBlur(selena_img, 5) 
cv2.imshow("median Blur", m_blur)

# # Average Blur
# avg_blur = cv2.blur(selena_img, (5,5)) 
# cv2.imshow("average Blur", avg_blur)

# wait for any key
cv2.waitKey(0)
# Close all frames
cv2.destroyAllWindows()
