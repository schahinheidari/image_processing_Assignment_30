import cv2 as cv

cam = cv.VideoCapture(0)

while(True):
    ret, frame = cam.read()
    if not ret:
        break
    
    frame_HSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    skinMask = cv.inRange(frame_HSV, (0 ,55 , 80), (20, 255, 255)) 
    skin = cv.bitwise_and(frame, frame, mask=skinMask)

    key = cv.waitKey(1)
    if key == 27: #Esc
        break

    cv.imshow('skinDetection', skin)

cam.release()
cv.destroyAllWindows()