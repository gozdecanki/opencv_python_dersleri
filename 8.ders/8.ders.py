# -*- coding: utf-8 -*-
"""
Created on Fri Jan 16 02:04:32 2026

@author: gozde
"""

# HSV renk uzayını OpenCV kütüphanesinde mavi değerini oluştururken 
# neden 240 derece değil de 120 derece kullandık?
#çünkü normalde H değeri 0 ile 360 derecesinde değişiyor ama 
#OpenCV kullanımında 0 ile 180 derece arasında değişiyor.
#Bu yüzden normalde olan değerini kullanırken 2'ye bölerek kullanıyoruz. yani 240/2=120 derece

import cv2
import numpy as np

camera= cv2.VideoCapture(0)

def nothing(x):
    pass

#RGB - HSV
cv2.namedWindow("frame")
cv2.createTrackbar("H1","frame", 0, 359, nothing)
cv2.createTrackbar("H2","frame", 0, 359, nothing)
cv2.createTrackbar("S1","frame", 0, 255, nothing)
cv2.createTrackbar("S2","frame", 0, 255, nothing)
cv2.createTrackbar("V1","frame", 0, 255, nothing)
cv2.createTrackbar("V2","frame", 0, 255, nothing)

while camera.isOpened():
    _, frame = camera.read()
    #rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
  
    H1 = int(cv2.getTrackbarPos("H1","frame")/2)
    H2 = int(cv2.getTrackbarPos("H2","frame")/2)
    S1 = cv2.getTrackbarPos("S1","frame")
    S2 = cv2.getTrackbarPos("S2","frame")
    V1 = cv2.getTrackbarPos("V1","frame")
    V2 = cv2.getTrackbarPos("V2","frame")
  
    
  
    lower = np.array([H1,S1,V1])
    upper = np.array([H2,S2,V2])
    
    mask = cv2.inRange(hsv,lower, upper)#maskemizi elde ettik
    
    res = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("frame", frame)
#    cv2.imshow("hsv",hsv)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)
   #cv2.imshow("rgb",rgb)

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()











#Kütüphanedeki renkler ile ilgili fonksiyonları bu şekilde görebiliriz
# for i in dir(cv2):
#     if "COLOR" in i:
#         print(i)


