# -*- coding: utf-8 -*-
"""
Created on Fri Jan 16 00:49:33 2026

@author: gozde
"""

import cv2
import numpy as np


img1 = cv2.imread("cv2.png")
img2 = cv2.imread("r.jpg")

x,y,z= img1.shape # boyut bilgisi aldık
roi = img2[0:x,0:y] # 1. resimden bir parça kırpıyoruz img1 boyutu kadar

#renk uzayını değiştirmek için kullanıyoruz bu fonksiyonu
img1_gray= cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

#eşitleme işlemi yapıyoruz. renkli alanlar beyaz oldu. control için: cv2.imshow("resim", mask)
ret, mask = cv2.threshold(img1_gray, 10, 255, cv2.THRESH_BINARY)

# bu işlemle 1ler 0 , 0lar 1 e dönüşecek yani beyazlar siyah siyahlar beyaz olacak
mask_invert = cv2.bitwise_not(mask)

#biz beyaz olan kısma kırpma yaptığımız resmin rengini uygulamak istiyoruz o yüzden roi 
#parametre olarak verdik. mask_invert beyaza dönüştürdüğümüzdü bu değeri
#mask değişkenine vererek and yani çarpma işlemi yapmış olduk
img1_bg = cv2.bitwise_and(roi,roi,mask= mask_invert)


img2_fg= cv2.bitwise_and(img1,img1,mask=mask)

toplam = cv2.add(img1_bg, img2_fg)#ilk okuduğumuz img1 in renki kısımları roi işleminden sonra oluşan resimle birleştirdik

#toplam değerine denk gelen resmi img2 üzerine yerleştirdik: sol üst köşeden 
img2[0:x, 0:y] = toplam


cv2.imshow("resim", img1_bg)
cv2.imshow("resim2", img2_fg)
cv2.imshow("resim3", toplam)
cv2.imshow("resim4", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()







# img1 = cv2.imread("cv2.png")
# img2 = cv2.imread("d.jpg")
# toplam = cv2.addWeighted(img1, 0.3, img2, 0.7, 0)

# cv2.imshow("resim", toplam)
# cv2.waitKey(0)
# cv2.destroyAllWindows()




# x = np.uint8([250])
# y = np.uint8([10])


# sonuc1 = x+y # burada normal toplama yapıp 260 bulup 256 ile mod alma yaparak sonucu 4 olarak dönüyor
# sonuc2 = cv2.add(x,y) #