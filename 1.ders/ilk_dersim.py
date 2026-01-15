# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 23:07:35 2026

@author: gozde
"""

import cv2
from matplotlib import pyplot as plt

resim = cv2.imread("kizkulesi.jpg")# resmin orjinali bu şekilde görülür
#resim = cv2.imread("kizkulesi.jpg",0)#resim siyah beyaz olarak okunacak

#cv2.namedWindow("resim",cv2.WINDOW_AUTOSIZE)#boş bir çerçeve oluşturduk.pencere boyutunu büyütüp küçültemiyoruz
cv2.namedWindow("resim",cv2.WINDOW_NORMAL)#boş bir çerçeve oluşturduk.pencere boyutunu büyütüp küçültebiliyoruz

cv2.imshow("resim", resim)

#OpenCV tarafından yüklenen renkli görüntü BGR modunda. Ancak Matplotlib, RGB modunda görüntülenir. Dolayısıyla,
#görüntü OpenCV ile okunduğunda renkli görüntüler Matplotlib'de doğru görüntülenmeyecektir.
#örneğin Kırmızı ile mavi renkleri birbirinin tersi olarak görüntülenir.

plt.imshow(resim,cmap="gray")#resim üzerinde manuel işlem yapabilmek için yeni bir pencere açıyor
plt.show()

k = cv2.waitKey(0)#gösterilenin ekranda kalması için yazıyoruz

if k== 27:
    print("Esc tuşuna basıldı")

elif k== ord("q"):
    print("q tuşuna basıldı, resim kayıt edildi")
    cv2.imwrite("kizkulesigri.jpg",resim)



#cv2.destroyWindow("resim penceresi")--- kapatılacak pencere ismini bu şekilde de yazabiliriz
cv2.destroyAllWindows()