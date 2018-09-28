# araba class'ı yaratalım. __init(self) fonksiyonu kullanımını gösterelim
# araba class'ından oluşturulan nesnelere araba class'ından özellikleri nasıl
# kulandığına bakalım.

class araba():
    
    def __init__(self,Marka,Model,Vites_Tipi,Fiyat):
        self.marka=Marka
        self.model=Model
        self.vites_tipi=Vites_Tipi
        self.fiyat=Fiyat

araba1=araba("Renault","2013","Düz","32.000 TL")
araba2=araba("Ford","2016","Otomatik","44.000 TL")


print(araba1.marka,araba1.model,araba1.vites_tipi,araba1.fiyat)
print("\n-------------------------------------------------------\n")
print(araba2.marka,araba2.model,araba2.vites_tipi,araba2.fiyat)

""" __init__(self) fonksiyonunu kullanmazsak
değişkenlere doğrudan nesneadı.değişken şeklinde erişebiliriz.
fakat değişkenler nesnelere aynı değer olarak atanır.
def __init__(self,değişken1,değişken2...) şeklinde her nesne için
farklı değer atama yapabiliriz. init fonksiyonu birnevi yapıcı fonksiyondur.
##değişkenleri self.değişkenadı şeklinde tanımlamamız gerekir.##
"""
