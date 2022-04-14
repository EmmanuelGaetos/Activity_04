import cv2
import os

while True:
	Filename = input("File name [Add'.jpg' at the end of the File name: ")

	if os.path.exists(Filename):
		img= cv2.imread(Filename, 1)
		cv2.imshow(Filename, img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		break

	else:
		print("File name doesn't exist...")