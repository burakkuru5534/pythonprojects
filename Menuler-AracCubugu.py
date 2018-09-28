from tkinter import *


def islem1():
    print("islem1 yapıldı")

def islem2():
    print("islem2 yapıldı")


def islem3():
    print("islem3 yapıldı")


def islem4():
    print("islem4 yapıldı")


def islem5():
    print("islem5 yapıldı")


def islem6():
    print("islem6 yapıldı")

def klasorAc():
    print("Klasör Açılamadı")
def yeniKlasor():
    print("Klasör Oluşturulamadı")

pencere= Tk()


menu = Menu(pencere)

pencere.config(menu= menu)

altMenu= Menu(menu)
altMenu2=Menu(menu
              )
menu.add_cascade(label= "Menu-1", menu=altMenu)
altMenu.add_command(label= "islem-1", command= islem1)
altMenu.add_command(label= "islem-2", command= islem2)
altMenu.add_command(label= "islem-3", command= islem3)
altMenu.add_separator()
altMenu.add_command(label= "Çıkış",command= pencere.destroy)

menu.add_cascade(label= "Menu-2", menu=altMenu2)
altMenu2.add_command(label= "islem-4", command= islem4)
altMenu2.add_command(label= "islem-5", command= islem5)
altMenu2.add_command(label= "islem-6", command= islem6)
altMenu2.add_separator()
altMenu2.add_command(label= "Çıkış",command= pencere.destroy)



# araç çubuğu #

AracCubugu= Frame(pencere,bg= "black")
YeniKlasor= Button(AracCubugu, text="Yeni Klasör Oluştur", command=yeniKlasor)
KlasorAc= Button(AracCubugu, text="Klasör Aç", command= klasorAc)
AracCubugu.pack(side= TOP, fill=X)
YeniKlasor.pack(side=LEFT, padx=2,pady=2)
KlasorAc.pack(side=LEFT, padx=2,pady=2)
# araç çubuğu #







pencere.mainloop()
