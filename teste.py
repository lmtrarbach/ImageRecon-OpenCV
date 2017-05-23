import numpy as np
import cv2
cao= cv2.CascadeClassifier('./mycascades/huskyCascade.xml')
img = cv2.imread('siberian-husky-dog-breed-pictures-1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
caes = cao.detectMultiScale(gray, 1.5, 400)
print "Encontrados {0} Caes!".format(len(caes))
for (x, y, w, h) in caes:
	cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
	
	


cv2.imshow("Encontrados {0} Caes!".format(len(caes)) ,img)
cv2.waitKey(0)
cv2.destroyAllWindows()
