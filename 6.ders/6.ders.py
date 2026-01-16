# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 23:31:16 2026

@author: gozde
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

#burada mavi olsun dedik ama; opencv BGR formatını kullanırken Matplotlib RGB formatını kullanıyor
#plt.imshow ile gösterirken maviler kırmızı, kırmızılar mavi olarak gösterilir => constant adlı çizimde kırmızı kenarlık oluşur
BLUE = [255,0,0] 

img1 = cv2.imread('cv2.png')

replicate = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)
reflect101= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)

plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

plt.show()



#Resim kırpma ve yerleştirme
# resim = cv2.imread("r.jpg",0)# 0 değerini resmi siyah beyaz göremk için ekledik

# #x koordinatında 500 den 800'e kadar, y koordinatında 500 den 800'e kadar olan bölgeyi kırp dedik
# #300x300 lük bir resim
# kirp= resim[500:800,500:800]

# #kırpılan resmi asıl ana resimde belirlediğimiz bir  bölgeye ekleme işlemi için
# resim[100:400,1400:1700]= kirp

# plt.subplot(121)# 1: satır 2: sütun 1: 1.resim
# plt.imshow(resim,"gray")#resmi siyah beyaz göremk için
# plt.subplot(122)# 1: satır 2: sütun 2: 2.resim şeklinde çerçeveye yerleştirecek
# plt.imshow(kirp,"gray")
# plt.show()



#console resim işlevleri

# px = resim[100,100]

# px_blue= resim[100,100,0]

# resim[100,100,0]=255

# px_blue
# Out[5]: np.uint8(146)

# px_blue=resim[100,100,0]

# px_blue
# Out[7]: np.uint8(255)

# resim[100,100]=[255,255,255]

# resim[100,100]
# Out[9]: array([255, 255, 255], dtype=uint8)

# resim.item(100,100,0)
# Out[10]: 255

# resim.itemset((100,100,0),100)

# resim[100,100]
# Out[12]: array([255, 255, 255], dtype=uint8)

# resim.shape
# Out[13]: (1080, 1920, 3)

# resim.size
# Out[14]: 6220800

# resim.dtype
# Out[15]: dtype('uint8')

#ROI=Region Of Image
#resmin belirli bir alanın alınması, kırpılması
#başka bir pencereye alınması vs başka yere yerleştirilmesi
#bu işlem ile önce yüz tespiti yapıp sonra yüz üzerinde
# göz aramak aynı zamanda doğruluğu arttırır

#resim =cv2.imread("r.jpg)
# b,g,r = cv2.split(resim)# bu fonksiyon renk kanallarını ayırmaya yarıyor. daha yavaş çalışıyor
# resim2= cv2.merge((b,g,r))# bu fonksiyon renk kanallarını birleştirmeye yarıyor
# b= resim[:,:,0] # bu kısayolu renkleri ayırmanın, resimdeki tüm piksellerin mavi olanını ayır demiş oluyoruz
# resim[:,:,2]= 0 # kırmızı pikselleri mavi yap demiş olduk
# cv2.imshow("resim",resim) # yazıp görebiliriz
