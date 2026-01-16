# -*- coding: utf-8 -*-
"""
Created on Fri Jan 16 03:17:04 2026

@author: gozde
"""

import cv2
import numpy as np


img = cv2.imread("1.jpeg")
print(img.shape)
rows,cols = img.shape[:2]

#koordinatları kullanıcı çift tıklama ile 4 köşesini seçecek ve kırpma yapılacak
click_count=0
a=[]

dst_points= np.float32([
    [0,0],
    [cols-1,0],
    [0,rows-1],
    [cols-1,rows-1]
    ])

cv2.namedWindow("img",cv2.WINDOW_NORMAL)

def draw(event,x,y,flags,param):
    global click_count, a
    if click_count<4:
        if event ==cv2.EVENT_LBUTTONDBLCLK:
            click_count +=1
            a.append((x,y))
        pass
    else:
      
        
        src_points= np.float32([ 
            [a[0][0], a[0][1]],
            [a[1][0], a[1][1]],
            [a[2][0], a[2][1]],
            [a[3][0], a[3][1]]])
        
        click_count=0
        a=[]
        
        M = cv2.getPerspectiveTransform(src_points,dst_points)
        img_output=cv2.warpPerspective(img,M,(cols,rows))
        cv2.imshow("img_output", img_output)
    pass
    
cv2.setMouseCallback("img", draw)

while(1):
    cv2.imshow("img", img)
   # cv2.imshow("img_output", img_output)
    if cv2.waitKey(1) == ord("q"):
       break
cv2.destroyAllWindows()




# #projective ile kırpma yaptık
# src_points= np.float32([ #resmin köşe koordinatlarını vermiş olduk
#     [80,100],
#     [400,90],
#     [50,400],
#     [400,400]
#     ])

# dst_points= np.float32([
#     [0,0],
#     [cols-1,0],
#     [0,rows-1],
#     [cols-1,rows-1]
#     ])

# projective_matrix= cv2.getPerspectiveTransform(src_points,dst_points)

# img_output=cv2.warpPerspective(img,projective_matrix,(cols,rows))

# cv2.imshow("img", img)
# cv2.imshow("img_output", img_output)
# cv2.waitKey()
# cv2.destroyAllWindows()





# src_points= np.float32([ #resmin köşe koordinatlarını vermiş olduk
#     [0,0],
#     [cols-1,0],
#     [0,rows-1],
#     [cols-1,rows-1]
#     ])

# dst_points= np.float32([
#     [0,0],
#     [cols-1,0],
#     [int(0.33*(cols-1)),rows-1],
#     [int(0.66*(cols-1)),rows-1]
#     ])

# projective_matrix= cv2.getPerspectiveTransform(src_points,dst_points)

# img_output=cv2.warpPerspective(img,projective_matrix,(cols,rows))

# cv2.imshow("img", img)
# cv2.imshow("img_output", img_output)
# cv2.waitKey()
# cv2.destroyAllWindows()




# #noktaları kaydırma
# src_points= np.float32([
#     [0,0],
#     [cols-1,0],
#     [0,rows-1]
#     ])

# dst_points= np.float32([
#     [0,0],
#     [int(0.6*(cols-1)),0],
#     [int(0.4*(cols-1)),rows-1]
#     ])

# affine_matrix = cv2.getAffineTransform(src_points, dst_points)

# img_output=cv2.warpAffine(img,affine_matrix,(cols,rows))

# cv2.imshow("img", img)
# cv2.imshow("img_output", img_output)
# cv2.waitKey()
# cv2.destroyAllWindows()


# #translation
# #resmi kaydırmış olduk
# # translation_matrix= np.float32([
# #     [1,0,50], #tx =50
# #     [0,1,50]  #ty=50
# #     ]) 
# #img_translation= cv2.warpAffine(img,translation_matrix,(cols,rows))
# #img_translation= cv2.warpAffine(img,translation_matrix,(cols+50,rows+50))

# #döndürme
# #30 derece sola çevirmiş olduk. -50 yazarsak sağa 50 derece çevirmiş oluruz
# rotation_matrix = cv2.getRotationMatrix2D((cols/2,rows/2), 30, 1)
# img_rotation= cv2.warpAffine(img,rotation_matrix,(cols,rows))


# #res = cv2.resize(img, (300,300))
# #res = cv2.resize(img,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_CUBIC)

# cv2.imshow("img", img)
# cv2.imshow("img_rotation", img_rotation)
# #cv2.imshow("img_translation", img_translation)
# #cv2.imshow("res", res)
# cv2.waitKey()
# cv2.destroyAllWindows()