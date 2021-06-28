import cv2 
import numpy as np
import imutils
import os
os.remove('demo.jpg')
url = 'http://192.168.0.5:8080/video'
cap = cv2.VideoCapture(url)
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
while(cap.isOpened()):    
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imwrite('demo.jpg',frame)
    image = cv2.imread("demo.jpg")
    frame = cv2.resize(image, (640, 480))
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    boxes, weights = hog.detectMultiScale(frame, winStride=(8,8) )
    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
        #print(len(boxes))

    for (xA, yA, xB, yB) in boxes:
            # display the detected boxes in the colour picture
            cv2.rectangle(frame, (xA, yA), (xB, yB),
                              (0, 255, 0), 2)
    #cv2.imshow('frame',frame)
    cv2.imwrite('demo1.jpg',frame)

    


#xdg-open demo.jpg
cap.release()
cv2.destroyAllWindows()