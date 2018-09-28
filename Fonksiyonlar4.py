# Kendini çağıran fonksiyonlar # özyinelemeli # recursion #


# sayi 2'den küçük kalana  kadar 2'ye bölen bir program yapalım #

def ikiyebol(x):
    x=x/2
    print(x)
    if(x<2):
        return 1
    else:
        return ikiyebol(x)

ikiyebol(43)
print("-------------")
ikiyebol(44)
print("-------------")
ikiyebol(2)
