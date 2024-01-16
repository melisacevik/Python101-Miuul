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

