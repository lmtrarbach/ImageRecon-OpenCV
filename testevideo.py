import numpy as np
import cv2
armas = cv2.CascadeClassifier('/opt/miniconda2/envs/projetoimagem/projeto/projetoimagem/mycascades/wasponcacade.xml')

cap = cv2.VideoCapture('videoarmas.mp4')


while(cap.isOpened()):
    ret, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    armasDetect = armas.detectMultiScale(gray,1.05,30)
    for (x, y, w, h) in armasDetect:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
