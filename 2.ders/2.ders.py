# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 23:29:24 2026

@author: gozde
"""
import cv2


cam = cv2.VideoCapture(0)# harici kameramız varsa 0 yerine 2 yazıyoruz

fourrc = cv2.VideoWriter_fourcc(*'XVID')# .avi uzantısında video oluşturur

out = cv2.VideoWriter("video.avi",fourrc, 30.0,(640,480))

while cam.isOpened():
    
    ret, frame = cam.read()
    
    if not ret:
        print("kameradan görüntü alınamadı")
        break
    
    out.write(frame)
    
    cv2.imshow("kamera",frame)
    
    if cv2.waitKey(33) == ord("q"):
        print("videodan ayrıldınız.")
        break


cam.release()
out.release()
cv2.destroyAllWindows()





# cam = cv2.VideoCapture("dron.mp4")


# while cam.isOpened():
    
#     ret, frame = cam.read()
    
#     #frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     frame = cv2.cvtColor(frame,cv2.COLOR_RGB2RGBA)
   
#     if not ret:
#         print("kameradan görüntü okunamıyor")
#         break
    
#     cv2.imshow("görüntü",frame)
    
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         print("video kapatıldı.")
#         break
    
# cam.release()
# cv2.destroyAllWindows()




# cam = cv2.VideoCapture(0)

# print(cam.get(3))
# print(cam.get(4))

# cam.set(3,320)
# cam.set(4,240)

# print(cam.get(3))
# print(cam.get(4))


# if not cam.isOpened():
#     print("kamera tanınmadı")
#     exit()

# while True:
#     ret, frame = cam.read()

#     frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

#     if not ret:
#         print("kameradan görüntü okunamıyor")
#         break
    
#     cv2.imshow("kamera",frame)
    
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         print("görüntü sonlandırıldı.")
#         break
    
# cam.release()
# cv2.destroyAllWindows()