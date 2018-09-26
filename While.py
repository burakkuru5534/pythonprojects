# While Döngüsü #

# Hesap Makinesi #

# basit türev işlemi #

print("x^n in Türevi için:1'e bas\nSabitin Türevi için:2'ye bas.\nToplamın Türevi için 3'e bas.\nÇarpmanın Türevi için 4'e bas\nBölmenin Türevi")

while(True):
    islem=int(input("İşlem için Seçim yapın: "))
    if(islem==1):
        n=int(input("x'in derecesini giriniz"))
        print(n,"*","x^",n-1)

    elif(islem==2):
        sabit=input("değeri giriniz:")
        print("Sabitin Türevi 0'dır")
    elif(islem==3):
        print("fonksiyonlar sadece x ve xin kuvvetleri olabilir(x,x^2 gibi)")
        fx=input("fx fonksiyonunu giriniz:")
        gx=input("gx fonksiyonunu giriniz:")
        if(fx=="x"):
            if(gx=="x"):
                print("fx + gx in türevi: 1")
            else:
                n=int(gx[2])
                print("1+",n,"*","x^",n-1)
        else:
            n=int(fx[2])
            m=int(gx[2])
            if(n==m):
                print(n+m,"*x^",n-1)
            else:
                print(n,"*","x^",n-1,"+",m,"* x^",m-1)
            
    if(islem==4):
        print("Fx ve Gx x ve kuvvetleri olabilir.(x,x^2 gibi)")
        Fx=input("Fx fonksiyonunu giriniz: ")
        Gx=input("Gx fonksiyonunu giriniz: ")
        if(len(Fx)>=3):
            Fn=int(Fx[2])
            Gn=int(Gx[2])
        
        if(Fx=="x"):
            if(Gx=="x"):
                print("2x")
            else:
                print(Gx,"+",Gn,"*x^",Gn-1,"*x")
        else:
            print(Fn,"*x^",Fn-1,"*",Gx,"+",Gn,"*x^",Gn-1,"*",Fx)
            





            
