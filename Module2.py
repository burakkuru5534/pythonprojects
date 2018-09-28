# Module1 is going to import in this module #
import Module1
# also we can use this : from module1 import *
# we don have to use module name when we use this type of import
a=6
b=8
c=10
# module1'de tanımlı olan fonk1 kare alır.
#ilk 3 printte kullanılan değişkenler module2'nin a,b,c değişkeni

print(Module1.fonk1(a))  
print(Module1.fonk1(b))
print(Module1.fonk1(c))

#bu üç printte kullanılan ise module1'de tanımlanmış olan a,b,c değerleri
print(Module1.fonk1(Module1.a))
print(Module1.fonk1(Module1.b))
print(Module1.fonk1(Module1.c))

