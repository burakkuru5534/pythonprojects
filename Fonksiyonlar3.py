#Fonksiyonlar ve global, pass deyimleri kullanımı #

def kisilistele():
         
    kisi_listesi= []
    while(True):
        kisi=input("Eklenecek kişinin ismini giriniz. (çıkmam için q): ")
        if(len(kisi)<3 and kisi!="q"):
            print("İsim 3 harften az olamaz.")
            pass
        
        if(kisi=="q"):
            print("programdan çıkıldı.")
            return
        else:
            kisi_listesi.append(kisi)
            print(kisi_listesi)
            continue
    
kisilistele()
