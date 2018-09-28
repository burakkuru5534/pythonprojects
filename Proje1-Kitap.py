""" kitap adlı bir class oluşturalım. bu class'tan bir kitaplar nesne listesi
oluşturalım. bu liste birnevi kitaplık vazifesi yapsın. okunanları
okundu listesine ekleyelim. bu ekleme işlemlerini yaparken nesne tabanlı
özellikleri kullanalım.
"""
import math # math kütüphanesini import ettik.
kitapListesi=["Şu Çılgın Türkler"]
kitap_adeti=1
okunanlarListesi=[""]
class Kitap():
    
    def __init__(self,ad,yazar,tur,konu,sayfa_sayisi,okundu_mu):

        self.Ad=ad
        self.Yazar=yazar
        self.Tur=tur
        self.Konu=konu
        self.Sayfa_Sayisi=sayfa_sayisi
        self.Okundu_mu=okundu_mu

    def kitap_oku(self,adi):
        if(adi in kitapListesi):
            self.Okundu_mu=True
            okunanlarListesi.append(adi)
            
                      
        
        

    
                

"""
kitap1=Kitap("Şu Çılgın Türkler","Turgut Özakman","Roman","Türk Kurtuluş Savaşı","743",False)
print(kitap1.Okundu_mu)
kitap1.kitap_oku("Şu Çılgın Türkler")
print(kitap1.Okundu_mu)
"""
while(True):
    girdi=input("Kitap Listesini görmek için 1'e basınız.\nListeye Kitap Eklemek için 2'ye basınız.\nListeden kitap silmek için 3'e basınız.\nSeçenek: ")
    if(girdi=="1"):
        print(kitapListesi)
        girdi2=input("Kitap okumak için Kitap ismini giriniz. Anasayfaya dönmek için q'ya basınız.")
        if(girdi2=="q"):
            continue
        else:
            kitap1.kitap_oku(girdi2)
        
    elif(girdi=="2"):
        girdi3=input("Eklemek istediğiniz Kitap bilgilerini giriniz.\nKitap adı:")
        girdi4=input("\nYazar adı:")
        girdi5=input("\nTür adı:")
        girdi6=input("\nKonu adı:")
        girdi7=input("\nSayfa sayısı:")
        girdiListesi=[girdi3,girdi4,girdi5,girdi6,girdi7]
        kitap2=Kitap(girdi3,girdi4,girdi5,girdi6,girdi7,False)
        kitapListesi.append(girdi3)
        print("Kitap Listeye başarıyla eklendi.")
        continue
    elif(girdi=="3"):
        girdi8=input("Listeden silmek istediğiniz kitap adını giriniz.")
        kitapListesi.remove(girdi8)
        continue
    else:
        print("yanlış girdi.")
        continue







        
        
    
