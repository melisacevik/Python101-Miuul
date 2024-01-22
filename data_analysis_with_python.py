##################
# PYTHON İLE VERİ ANALİZİ ( DATA ANALYSIS WITH PYTHON )
##################

# - NumPy
# - Pandas
# - Veri Görselleştirme: Matplotlib & Seaborn
# - Gelişmiş Fonksiyonel Keşifçi Veri Analizi ( Advanced Functional Exploratory Data Analysis )

##################
# NUMPY
##################

# Neden NumPy?
# NumPy Array'i oluşturmak
# Numpy Array Özellikleri
# Yeniden Şekillendirme
# Index Seçimi
# Slicing
# Fancy Index
# NumPy'da Koşullu İşlemler Conditions on NumPy
# Matematiksel İşlemler

##################
# Neden NumPy?
##################

import numpy as np

# örnek: listedeki elemanları birbiriyle çarpacağız. ( elemanlar içinde gezme/çarpma/boş listeye ekleme/ sonuç görme)

a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

#klasik yöntem
ab = []
for i in range(0, len(a)):
    ab.append(a[i] * b[i])

# numPy çözümü

a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])
a * b

##################
# NumPy Array'i oluşturma - creating numpy arrays
##################

import numpy as np

np.array([1, 2, 3, 4, 5])
type(np.array([1, 2, 3, 4, 5])) # class 'numpy.ndarray'


np.zeros(10, dtype=int) #(adet,veri yapısı) | # 0 'dan oluşan ndarray oluşturmak istersem;
np.random.randint(0, 10, size=10) #(başlangıç aralık,bitiş aralık, adet) integer => randint() | # belirli bir aralık olacak şekilde;
# belirli bir istatiksel dağılıma göre sayı üretmek istersek normal() kullanırız
np.random.normal(10, 4,(3,4)) #(normaldağılımlıkitleortalaması, argüman=> ör stand sapm = 4 , boyut)
# 3 satır 4 sütundan oluşan ortalaması 10 standart sapması 4 olacak şekilde normal dağılımlı sayılar oluşturuldu.


##################
# NumPy Array Özellikleri ( Attributes of NumPy Arrays )
##################

import numpy as np

# ndim : boyut sayısı
# shape : boyut bilgisi
# size : toplam eleman sayısı
# dtype : array veri tipi

a = np.random.randint(10, size=5)

a.ndim #tek boyutlu [] olduğu icin 1 | kaç boyutlu? 1 mi 2 mi 3 mü
a.shape #tek boyutlu ve içinde 5 eleman var | boyut bilgisi ver
a.size # toplam eleman sayısı
a.dtype

##################
# Yeniden Şekillendirme - Reshaping
##################

# Numpy array’in boyutunu değiştirmek istediğimizde reshape( ) metodunu kullanırız.
# örneğin , 3'e 3'lük matris oluşturmak istersek,

import numpy as np
np.random.randint(1, 10, size=9)
np.random.randint(1, 10, size=9).reshape(3,3)

#veya
ar = np.random.randint(1, 10, size=9)
ar.reshape(3,3)
#atayarak da olur.
#ihtiyaçlara göre daha az sayıda veya daha fazla sayıda satır ya da sütun bilgisi girerek boyut değiştirme işlemleri yapılır.

#ama, 10 elemanlı olsaydı 3,3'e çeviremezdik. hata verir.

##################
# Index Seçimi - Index Selection
##################

import numpy as np

a = np.random.randint(10, size=10) #randint metodu kullanarak 0'dan 10'a kadar sayılardan oluşan 10 adet değer oluşturuldu.

# Örneğin, 0.elemanına gitmek için:

a[0]
a[0:5]

# 0. indexteki elemanı değiştirmek istersem

a[0] = 999


# 2 boyutlu arraylerde seçme işlemi nasıl olur?

                    # (3 satır,5 sütun)
m = np.random.randint(10,size=(3,5))

#ilk eleman için

#satır,sütun / 0'ın 0'ı
m[0, 0]

m[1, 1]

# elemanı değiştirmek istersem

m[0, 4] = 5

m[1, 3] = 999

#float girersen onu int olarak yazar cünkü ndarray tek veri yapısı ile tutar.

# bütün satırların 0. elemanını almak istersem

m[:, 0]

# 1.satırın bütün sütunlarını seçmek istersek

m[1, :]

# hem satırlardan belli bir aralık hem sütunlardan belli bir aralık verebilir miyiz?

m[0:2, 0:3]

##################
# Fancy Index
##################

import numpy as np

            #0'dan 30'a kadar 3'er artacak şekilde array oluşturma
v = np.arange(0, 30, 3)
v[1]

# diyelim ki elimde birden fazla index bilgisi var. tek tek [0] , [5] gibi yazmaktan kolay olmalı.
#fancy index ne işe yarar? numpy arrayine bir liste girdiğinizde seçim işlemi sağlar.

catch = [1,2,3] # list
v[catch] # numpy array

##################
# NumPy'da Koşullu İşlemler ( Conditions on NumPy ) - Yapılması gereken şey ilgili array'in içerisine koşul ifadesi girmektir.
##################

import numpy as np
v = np.array([1,2,3,4,5])

#3'ten küçük değerlere erişmek istiyorsak;

# klasik çözüm

ab = []

# for i in v:
#   print(i)

for i in v:
    if i < 3:
        ab.append(i)

# NumPy çözümü

v < 3

v[v < 3]
v[v > 3]
v[v == 3]
v[v != 3]
v[v >= 3]

