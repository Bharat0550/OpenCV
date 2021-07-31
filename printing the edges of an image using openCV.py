import cv2

img=cv2.imread("C:\opencv\selena_gomez.jpg")# the given path should be simple and clear
print(img)
cv2.imshow("frame1", img)
import cv2

#Getting Contour of Image using Canny Filter
mg = cv2.imread("C:\opencv\selena_gomez.jpg")
#Convert Image into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Computing edges with Canny using thresholds 
#Using canny filter to Contours
edges = cv2.Canny(gray, 90, 50)

high_threshold = cv2.Canny(gray, 190, 150)

cv2.imshow("Original", img)
cv2.imshow("Edges", edges)
cv2.imshow("High Edges", high_threshold)

#wait for any key
cv2.waitKey(0)
#Close all frames
cv2.destroyAllWindows()
