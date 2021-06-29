import cv2
import numpy as np
import imutils
import os
cv2.startWindowThread()
# os.remove('demo.jpg')
url = 'http://192.168.0.5:8080/video'
cap = cv2.VideoCapture(url)
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
out = cv2.VideoWriter(
    'output.avi',
    cv2.VideoWriter_fourcc(*'MJPG'),
    15.,
    (640,480))

while (cap.isOpened() and True):
    ret, frame = cap.read()
    if ret == False:
        break
    # cv2.imwrite('demo.jpg', frame)
    # image = cv2.imread("demo.jpg")
    frame = cv2.resize(frame, (640, 480))
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    boxes, weights = hog.detectMultiScale(frame, winStride=(8, 8))
    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
    # print(len(boxes))

    for (xA, yA, xB, yB) in boxes:
        # display the detected boxes in the colour picture
        cv2.rectangle(frame, (xA, yA), (xB, yB),
                      (0, 255, 0), 2)
    l1 = []
    for (xA, yA, xB, yB) in boxes:
            # display the detected boxes in the colour picture
            cv2.rectangle(frame, (xA, yA), (xB, yB),
                          (0, 255, 0), 2)
            if len(boxes) > 1:  # for computing centroids of rectangles
                l1.append([(xA + xB) / 2, (yA + yB) / 2])

    # l2=[]
    # l2=combinations(l1,2)
    # d1=[]
    # for i in l2:
    #     a=i[0]
    #     b=i[1]
    #     dist=(a[0]-b[0])^2 + (a[1]-b[1])^2
    #     dist.append(dist)
    
    # cv2.imshow('frame',frame)
    out.write(frame.astype('uint8'))
    # cv2.imwrite('demo1.jpg', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# xdg-open demo.jpg
cap.release()
out.release()
cv2.destroyAllWindows()
cv2.waitKey(1)
