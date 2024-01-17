##################
# FONKSİYONLAR, KOŞULLAR, DÖNGÜLER, COMPREHENSIONS
##################
# Functions
# Koşullar (Conditions)
# Döngüler (Loops)
# Comprehesions

#################
# Functions
#################

#################
# Fonksiyon Okuryazarlığı
#################

print("a", "b")
print("a","b", sep="__")

#################
# Fonksiyon Tanımlama
#################


def calculate(x):
    print(x*2)

calculate(4)

## İki argümanlı/parametreli bir fonksiyon tanımlayalım.
# sırası önemli

def summer(arg1,arg2):
    print(arg1 + arg2)

summer(4,5)

def summer(arg1,arg2):
    """
    sum of 2 numbers

    :param arg1: int,float
    :param arg2: int,float
    :return: int,float
    """
    print(arg1 + arg2)

summer()

#######################
# Fonksiyonların Statement/Body Bölümü
#######################

# def function_name(parameters/arguments):
#       statements (function body)

def say_hi():   ##argümansız da olur
    print("meloş")
    print("hi")
    print("hello")

say_hi("Melisa")


def multiplication(a,b):

   c = (a * b)
   print(c)

multiplication(4,5)

## girilen 2 sayıyı çarpsın ve sonucu bir liste içinde saklayacak fonksiyon

list_store = []               # global scope

def add_element(a,b):
    c = a * b                  # local scope
    list_store.append(c)
    print(list_store)

add_element(1,2)
add_element(3,4)
add_element(5,7)

#######################
# Ön Tanımlı Argümanlar/Parametreler (Default Arguments/Parameters):
# Teknik olarak parametre, fonksiyon tanımlanması esnasında kullanılan ifadelerdir.
#######################

def divide(a,b):
    print(a / b)

def divide(a,b=1):
    print(a / b)

divide(80)

#######################
# Ne zaman fonksiyon yazma ihtiyacımız olur?
#######################

# Don't repeat yourself

def calculate(varm, moisture, charge):
    print((varm + moisture) / charge)

calculate(96,12,78)
calculate(33,44,55)

#######################
# Return : Fonksiyon Çıktılarını Girdi Olarak Kullanmak
#######################

def calculate(varm, moisture, charge):
    print((varm + moisture) / charge)

# calculate(96,12,78) * 10

def calculate(varm, moisture, charge):
    return (varm + moisture) / charge

calculate(96,12,78) * 10

##birden fazla işlem girdiğinde tuple olarak çıktı veriyor!!

#######################
# Fonksiyon İçerisinden Fonksiyon Çağırmak
#######################

def calculate(varm, moisture, charge):
    return int((varm + moisture) / charge)

calculate(90,12,12) * 10

def standardization(a, p):
    return a * 10 / 100 * p * p

standardization(45,1)

def all_calculation(varm, moisture,charge, p):
    a = calculate(varm, moisture, charge)
    b = standardization(a, p)
    print(b * 10)

all_calculation(1,3,5,12)

############################
# Local & Global Variables
############################

list_store = [1,2]

def add_element(a,b):
    c = a * b                  # local scope
    list_store.append(c)
    print(list_store)

############################
# KOŞULLAR (CONDITIONS)
############################

1 == 1
1 == 2

#####################
#if
#####################

if 1 == 1:
    print("smth")

number = 11

if number == 10:
    print("number is 10")

def number_check(number):
    if number == 10:
        print("number is 10")

number_check(12)

#####################
#else
#####################

def number_check(number):
    if number == 10:
        print("number is 10")
    else:
        print("print is not 10")

number_check(12)

#####################
#elif
#####################

def number_check(number):
    if number > 10:
        print("number is greater than 10 ")
    elif number < 10:
        print("number is less than 10")
    else:
        print("invalid number")

number_check(11)

#####################
# LOOPS (Döngüler)
#####################
#for loop

students = ["portakal", "çitos", "osman", "süslü"]

## her öğrenciyi gezmek için for i in students diyoruz
for student in students:
    print(student)

## isimlerini büyütmek istersek

for student in students:
    print(student.upper())

salaries = [ 1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    print(salary)

# herkese %20 zam

for salary in salaries:
    print(int(salary * (20/100) + salary))

## maaşları %20 , %30, %50 olarak tek tek yazmam kendimi tekrar etmeme yol açar o yüzden fonksiyon yazıyorum.

def new_salary(salary, rate):
    return int(salary * rate/100 + salary)

new_salary(1500,10)
new_salary(2000,20)

for salary in salaries:
    print(new_salary(salary, 10))

#maaşı 3000'den yukarısı olanlara farklı zam uygulasın

for salary in salaries:
    if salary >= 3000:
        print(new_salary(salary,10))
    else:
        print(new_salary(salary,20))

## maaşı tek tek gez
## her bir maaş için 3000den büyük mü kontrol et, new_salary fonks. çalıştır
## er bir maaş için 3000den büyük değilse %20 zam yap.

#############################
# Alternating ( MÜLAKAT SORUSU )
#############################

# Amaç aşağıdaki string değiştiren fonksiyon yazmak istiyoruz.

# before : "hi my name is john and i am learning python"
# after : "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"

def alternating(string):
    new_string =""
                        # stringin indexlerinde gezme => range()
    for string_index in range(len(string)):
        #index çift ise büyük harfe çevir
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
        # index tek ise küçük harfe çevir
        else:
            new_string += string[string_index].lower()
    print(new_string)

alternating("hi my name is john and i am learning python")

#########################
# break & continue & while
#########################
# break : akışı kesmek, durdurmak için
# continue : ilgili şart gözlemlendiğinde o şartı atlamak için ( pas geçmek için )
# while(-dığı sürece) : bir koşul sağlandığı sürece çalışmayı sürdürür.

salaries = [ 1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    if salary == 3000:
        break
    print(salary)

for salary in salaries:
    if salary == 3000:
        continue
    print(salary)

number = 1

while number < 5:
    print(number)
    number += 1

################
# Enumerate : Otomatik Counter/Indexer ile for loop
# Bir interatif nesne içinde elemanları gezip aynı zamanda index bilgisini de takip etmemizi sağlar.
################

## örnek => çift indexlileri A listesine , tek indexlileri B listesine alma

students = ["portakal", "çitos", "osman", "süslü"]

for student in students:
    print(student)     #burada index bilgisini output olarak alamadık


for index,student in enumerate(students):
    print(index,student)  # burada index bilgisini de alabildik

A = []
B = []
for index,student in enumerate(students):
    if index % 2 == 0:
        A.append(student)
    else:
        B.append(student)
print(students)
print(A)
print(B)

################
# Uygulama - Mülakat Sorusu
################
#divide_students fonksiyonu yazınız.
#Çift indexte yer alan öğrencileri bir listeye alınız.
#Tek indexte yer alan öğrencileri bir listeye alınız.
#Fakat bu iki liste tek bir liste olarak return olsun.

students = ['John', 'Mark', 'Vanessa', 'Mariam']

def divide_students(students):
    groups = [[],[]]
    for index,student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    print(groups)
    return groups

st = divide_students(students)
st[0]
st[1]

#################
# Alternating Fonksiyonunun Enumerate ile Yazılması
#################

def alternating_with_enumerate(string):
    new_string = ""
    for i,letter in enumerate(string):
        if i % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
    print(new_string)

alternating_with_enumerate("hi mY naMe is MeliSa")