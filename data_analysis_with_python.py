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

# klasik yöntem
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
type(np.array([1, 2, 3, 4, 5]))  # class 'numpy.ndarray'

np.zeros(10, dtype=int)  # (adet,veri yapısı) | # 0 'dan oluşan ndarray oluşturmak istersem;
np.random.randint(0, 10,
                  size=10)  # (başlangıç aralık,bitiş aralık, adet) integer => randint() | # belirli bir aralık olacak şekilde;
# belirli bir istatiksel dağılıma göre sayı üretmek istersek normal() kullanırız
np.random.normal(10, 4, (3, 4))  # (normaldağılımlıkitleortalaması, argüman=> ör stand sapm = 4 , boyut)
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

a.ndim  # tek boyutlu [] olduğu icin 1 | kaç boyutlu? 1 mi 2 mi 3 mü
a.shape  # tek boyutlu ve içinde 5 eleman var | boyut bilgisi ver
a.size  # toplam eleman sayısı
a.dtype

##################
# Yeniden Şekillendirme - Reshaping
##################

# Numpy array’in boyutunu değiştirmek istediğimizde reshape( ) metodunu kullanırız.
# örneğin , 3'e 3'lük matris oluşturmak istersek,

import numpy as np

np.random.randint(1, 10, size=9)
np.random.randint(1, 10, size=9).reshape(3, 3)

# veya
ar = np.random.randint(1, 10, size=9)
ar.reshape(3, 3)
# atayarak da olur.
# ihtiyaçlara göre daha az sayıda veya daha fazla sayıda satır ya da sütun bilgisi girerek boyut değiştirme işlemleri yapılır.

# ama, 10 elemanlı olsaydı 3,3'e çeviremezdik. hata verir.

##################
# Index Seçimi - Index Selection
##################

import numpy as np

a = np.random.randint(10,
                      size=10)  # randint metodu kullanarak 0'dan 10'a kadar sayılardan oluşan 10 adet değer oluşturuldu.

# Örneğin, 0.elemanına gitmek için:

a[0]
a[0:5]

# 0. indexteki elemanı değiştirmek istersem

a[0] = 999

# 2 boyutlu arraylerde seçme işlemi nasıl olur?

# (3 satır,5 sütun)
m = np.random.randint(10, size=(3, 5))

# ilk eleman için

# satır,sütun / 0'ın 0'ı
m[0, 0]

m[1, 1]

# elemanı değiştirmek istersem

m[0, 4] = 5

m[1, 3] = 999

# float girersen onu int olarak yazar cünkü ndarray tek veri yapısı ile tutar.

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

# 0'dan 30'a kadar 3'er artacak şekilde array oluşturma
v = np.arange(0, 30, 3)
v[1]

# diyelim ki elimde birden fazla index bilgisi var. tek tek [0] , [5] gibi yazmaktan kolay olmalı.
# fancy index ne işe yarar? numpy arrayine bir liste girdiğinizde seçim işlemi sağlar.

catch = [1, 2, 3]  # list
v[catch]  # numpy array

##################
# NumPy'da Koşullu İşlemler ( Conditions on NumPy ) - Yapılması gereken şey ilgili array'in içerisine koşul ifadesi girmektir.
##################

import numpy as np

v = np.array([1, 2, 3, 4, 5])

# 3'ten küçük değerlere erişmek istiyorsak;

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

##################
# Matematiksel İşlemler - (Mathematical Operations)
##################

import numpy as np

v = np.array([1, 2, 3, 4, 5])

v / 5
v * 5 / 10
v ** 2
v - 1
v + 1

# metodlar ile de yapabiliriz;

np.subtract(v, 1)
np.add(v, 1)
np.mean(v)  # ortalama
np.sum(v)
np.min(v)
np.max(v)
np.var(v)  # varyans

# atamadık consoleda gözlemliyoruz. kalıcı olmasını istersen v 'ye tekrar atarsın.

# NumPy ile İki Bilinmeyenli Denklem Çözümü

# 5*x0 + x1 = 12
# x0 + 3*x1 = 10


# x0'ın katsayıları , x1 'in katsayıları
a = np.array([[5, 1], [1, 3]])
# sonuc ayrı bi array'de
b = np.array([12, 10])

np.linalg.solve(a, b)

# quiz
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('1. boyuttaki 2.eleman: ', arr[0, 1])

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1])

import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7])

filter_array = array % 2 == 0

new_array = array[filter_array]

print(new_array)

##########################
# Pandas
#########################
# - Konu Başlıkları -

# Pandas Series
# Veri Okuma (Reading Data)
# Veriye Hızlı Bakış (Quick Look at Data)
# Pandas’ta Seçim İşlemleri (Selection in Pandas)
# Toplulaştırma ve Gruplama (Aggregation & Grouping )
# Apply ve Lambda
# Birleştirme (Join) İşlemleri

###########
# Pandas Series
###########

import pandas as pd

s = pd.Series([10, 77, 12, 4, 5])
type(s)
s.index  # 0'dan 5' kadar 1'er artacak şekilde indexi vardır.
s.dtype  # verinin tip bilgisi
s.size  # eleman sayısı
s.ndim  # boyut bilgisi
s.values  # değerlerin kendilerine erişmek istersek
type(s.values)
s.head()  # ilk 5 örneği getirme
s.head(3)
s.tail()  # sondan 5 örneği getirme

###########
# Veri Okuma (Reading Data)
###########

import pandas as pd

df = pd.read_csv("datasets/advertising.csv")
df.head()

# pandas cheatseet

###########
# Veriye Hızlı Bakış (Quick Look at Data)
###########

import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()
df.shape
df.info()
df.columns
df.index
df.describe().T  # özel istatistiklerine erişmek için , T => transpose'unu almak icin  => adet, ortalama,std, min
df.isnull().values.any()  # Detaylarına girmeden sadece veri setinde en az bir tane dahi olsa bir eksiklik var mı?
df.isnull().sum()  # her değişkende kaç tane eksik değer olduğu bilgisi
df["sex"].head()
df["sex"].value_counts()  # kaç kadın kaç erkek

###########
# Pandas'ta Seçim İşlemleri (Selection in Pandas)
###########

import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()

df.index
df[0:3]
df.drop(0, axis=0).head()  # (hangi index silinecek, axis=0 => satırlardan silme),ilk 5i gör

# birden fazla index silme için,
delete_indexes = [1, 3, 5, 7]
df.drop(delete_indexes, axis=0).head()

# işlemin kalıcı olması için şunlar yapılır;
# df = df.drop(delete_indexes, axis=0)
# df.drop(delete_indexes, axis=0,inplacce=True)

###########################
# Değişkeni Indexe Çevirmek
###########################

# değişken seçimi için ikisi de olur,
df["age"].head()
df.age.head()

# değişkeni indexe çevirme
df.index = df["age"]

# biz bunu indexe çevirdik, değişken olarak ihtiyacımız olmadığını düşünürsek nasıl sileriz?
df.drop("age", axis=1, inplace=True)

###########################
# Indexi Değişkene Çevirmek
###########################

df.index  # bunu df'e atarsak, bunu değişken olarak eklemiş oluruz.

df["age"] = df.index

df.head()

# 2. yol
# tekrar oluşturulan değişkeni sil
df.drop("age", axis=1, inplace=True)
# reset_index() fonksiyonu kullanılacak.

df = df.reset_index().head()
