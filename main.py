import cv2
filepath= 'germanxbiancakes.jpg'
image = cv2.imread(filepath, 1)
cv2.imshow("german",image)
cv2.waitKey(0)
cv2.derstroyAllWindows()