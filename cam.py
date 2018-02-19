import cv2
import sys
'''Testando outras coisas'''
armas = cv2.CascadeClassifier('/opt/miniconda2/envs/projetoimagem/projeto/projetoimagem/mycascades/wasponcacade.xml')

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    video_capture.isOpened()
    ret == True  
    

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    armasDetect = armas.detectMultiScale(gray,1.05,30)

    # Draw a rectangle around the faces
    for (x, y, w, h) in armasDetect:
    	cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
