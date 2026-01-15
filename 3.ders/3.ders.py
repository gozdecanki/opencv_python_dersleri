# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 00:07:55 2026

@author: gozde
"""

import cv2
import numpy as np

# siyah bir esim oluşturur zeros/ pozitif integer sayı için uint8
img = np.zeros((512,512,3),np.uint8)


#Lıne Çizimi
# #sol üst köşeden sağ alt köşeye olacak şekilde köşeden köşeye line çizdik
cv2.line(img, (0,0),(511,511),(255,0,0),5)
# #başka bir line çizimi yaptık
cv2.line(img, (50,400),(400,50),(0,255,0),10)

#Rectangle Çizimi
cv2.rectangle(img, (50,50),(300,300), (0,0,255),5)#kenarı kırmızı olan dikdörtgen
cv2.rectangle(img, (300,300),(511,511), (0,0,255),-1)#içi dolu dikdörtgen

#Circle çizimi
cv2.circle(img,(255,255),60,(120,120,120),2)#kenarı gri renk olan yarı çapı 60 olan bir daire
cv2.circle(img,(100,100),90,(255,50,50),-1)#içi dolu pembe renkli daire

#Ellipse çizimi
cv2.ellipse(img,(256,256),(100,50),0,0,180,(255,100,0),3)
cv2.ellipse(img,(100,100),(100,50),0,0,180,(255,100,0),-1)

#Polygon çizimi
pts= np.array([[20,30],[100,120],[255,255],[10,400]],np.int32)
pts2= pts.reshape(-1,1,2)
cv2.polylines(img, [pts], True, (255,255,255),3)#kapalı line çizer
#cv2.polylines(img, [pts], False, (255,255,255),3)# kapalı olmaz 

#Text yazma
font= cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, "OpenCV", (10,400), font, 3, (0,155,255),2,cv2.LINE_AA)


cv2.imshow("resim",img)
cv2.waitKey(0)
cv2.destroyAllWindows()