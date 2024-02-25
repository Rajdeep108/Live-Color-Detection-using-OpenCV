import cv2
import numpy as np

def mt(x):
    pass

#created a trackbar for hue, saturation and values
cv2.namedWindow('Color_Setter')
cv2.resizeWindow('Color_Setter',640,220)
cv2.createTrackbar('Upper_H','Color_Setter',0,255,mt)
cv2.createTrackbar('Lower_H','Color_Setter',0,255,mt)
cv2.createTrackbar('Upper_S','Color_Setter',0,255,mt)
cv2.createTrackbar('Lower_S','Color_Setter',0,255,mt)
cv2.createTrackbar('Upper_V','Color_Setter',0,255,mt)
cv2.createTrackbar('Lower_V','Color_Setter',0,255,mt)
#capturing live webcam video
cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)
    colSpace = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #getting the values from trackbar
    u_h = cv2.getTrackbarPos('Upper_H','Color_Setter')
    u_s = cv2.getTrackbarPos('Upper_S','Color_Setter')
    u_v = cv2.getTrackbarPos('Upper_V','Color_Setter')
    l_h = cv2.getTrackbarPos('Lower_H','Color_Setter')
    l_s = cv2.getTrackbarPos('Lower_S','Color_Setter')
    l_v = cv2.getTrackbarPos('Lower_V','Color_Setter')
    upper_hsv = np.array([u_h,u_s,u_v])
    lower_hsv = np.array([l_h,l_s,l_v])

    #created and optimised the mask
    krn = np.ones((5,5),dtype=np.uint8)
    mask = cv2.inRange(colSpace,lower_hsv,upper_hsv)
    mask = cv2.medianBlur(mask,5)
    mask = cv2.morphologyEx(mask,cv2.MORPH_OPEN,krn,iterations=3)
    mask = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,krn,iterations=3)
    new = cv2.bitwise_and(frame,frame,mask=mask)
    
    cv2.imshow('Feed',frame)
    cv2.imshow('Mask',mask)
    cv2.imshow('Result',new)
    if cv2.waitKey(5) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()