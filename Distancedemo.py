import cv2 
import numpy as np
import os
import math as m
#os.remove('demo.jpg')
#os.remove('demo1.jpg')
pinover=False
snopdogg=False

try:
    os.remove('output.avi')
except:
    pass
#cv2.startWindowThread()
url = 'http://192.168.207.152:8080/video'

cap = cv2.VideoCapture(url)
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

out = cv2.VideoWriter(
    'output.avi',
    cv2.VideoWriter_fourcc(*'MJPG'),
    15.,
    (640,480))
def vision():
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == False or pinover == True:
            break
        #cv2.imwrite('demo.jpg',frame)
        #image = cv2.imread("demo.jpg")
        frame = cv2.resize(frame, (640, 480))
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        boxes, weights = hog.detectMultiScale(frame, winStride=(8,8) )
        boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
        #print(len(boxes))
        l1=[]
        #Loop for printing rectangle in cv2 and computing the centroids of the rectangle
        for (xA, yA, xB, yB) in boxes:
                # display the detected boxes in the colour picture
                cv2.rectangle(frame, (xA, yA), (xB, yB),
                                (0, 255, 0), 2)
                l2=[]
                l2.append((xA+xB)/2)
                l2.append((yA+yB)/2)
                l1.append(l2)
                
        if len(boxes) == 2:
            a=l1[0]
            b=l1[1]
            dist=m.pow(m.pow(a[0]-b[0],2)+m.pow(a[1]-b[1],2),(1/2))#Distance formula
            # print("the distance between two objects is",dist)
            global snopdogg
            snopdogg = True
            

        #print(l1)
        
                
        #cv2.imshow('frame',frame)
        out.write(frame.astype('uint8'))
        


    #xdg-open demo.jpg
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    
def snoop():
    return snopdogg

def over():
    global pinover
    pinover=True

def snoop2():
    global snopdogg
    snopdogg = False