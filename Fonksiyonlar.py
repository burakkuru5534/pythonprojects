# fonksiyonlar #
# bir işlemi birden fazla kez yapacaksak fonksiyonları kullanırız. #
from __future__ import division

def aciklama():
    print("parametresiz fonk.")

def arttir(x):
    return x+1

def azalt(x):
    return x-1

def karesini_al(x):
    return x*x

def ikiye_bol(x):
    return x/2

def topla(x,y):
    return x+y

def cikar(x,y):
    print("x-y: ")
    return x-y

def carp(x,y):
    return x*y

def bol(x,y):
    if(y==0):
        print("0'a bölünme hatası")
        return -1
    else:
        return x/y

a=10
b=0
print("a: ",a,"b: ",b)
print("arttır a: ",arttir(a))

print("karesini al a: ",karesini_al(a))

print("azalt a: ",azalt(a))

print("azalt b: ",azalt(b))

print("arttir b: ",arttir(b))

print("karesini al b:",karesini_al(b))

print("ikiye bol b: ",ikiye_bol(b))

print("ikiye bol a: ",ikiye_bol(a))

print("topla: ",topla(a,b))

print("carp: ",carp(a,b))

print("bol: ",bol(a,b))

print("cikar: ",cikar(a,b))





