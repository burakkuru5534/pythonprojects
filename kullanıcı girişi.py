# Continue ve Break #

# Kullanıcı adı şifre girişi için 3 hakkı olan bir giriş sistemi yapalım. #

while(True):
    secenek=int(input("1: Kaydol\n2:Giriş yap\nSeçenek: "))
    if(secenek==1):
        username=input("Kullanıcı Adınızı giriniz: ")
        parola=input("Parolanızı giriniz: ")
        print("Tebrikler",username,"Başarıyla kayıt oldunuz!")
        continue
    else:
        a=0
        while(a<3):
            if(secenek==2):
                usr=input("Kullanıcı adınızı giriniz: ")
                prl=input("Parolanızı giriniz: ")
                if(usr==username and prl==parola):
                    print("Hoşgeldin",username)
                    break
                else:
                    if(a!=2):
                        print("tekrar dene")
                    a=a+1
                    continue
                    
        if(a==3):
            print("3 hatalı giriş")
        
    break       
print("Program sonlandı.")

