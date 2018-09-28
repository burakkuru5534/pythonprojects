# fonksiyon parametrelerinin kullanımı #
from __future__ import division # bölme işlemleri için

def kaydet(isim,soyisim,sicil_no,sinif,rutbe,garnizon):
    personel_listesi=[isim,soyisim,sicil_no,sinif,rutbe,garnizon]
    print(personel_listesi)
    

isim=input("İsim giriniz: ")
soyisim=input("Soyisim giriniz: ")
sicil_no=input("Sicil No giriniz: ")
sinif=input("Sınıf giriniz: ")
rutbe=input("Rütbe giriniz: ")
garnizon=input("Garnizon giriniz: ")

kaydet(isim,soyisim,sicil_no,sinif,rutbe,garnizon)

# parametrelerin içeriğini kullanıcıdan aldık.
# parametreleri kendimiz de yazabilirdik. yazarken sıra gözetmek zorunda değiliz.
#örnek olarak tersten başlayarak tanımlama yapalım:

kaydet(garnizon="Foça",rutbe="Üsteğmen",sinif="Piyade",sicil_no="5555",soyisim="Han",isim="Mete")

# parametreleri kullanırken sıra gözetmemize gerek yoktur. kullanım şekli budur.
