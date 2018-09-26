# Continue ve Break #

a=0
while(True):
    
    if(a<2):
        print("a<2")
        a=a+1
        continue # kodun akışını while döngüsüne tekrar geri döndürüyor 
    if(a<4):
        print("a<4")
        
        a=a+1
        continue # kodun akışını while döngüsüne tekrar geri döndürüyor 
    print("iflere girmedi")
    break # while döngüsünü kırıyor ve döngüden çıkıyor.

print("while dan çıktı")

x=input("")
