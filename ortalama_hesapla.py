from tkinter import *
from tkinter import messagebox
def hesapla():
    v1=int(vize1.get())
    v2=int(vize2.get())
    fn=int(fnotu.get())
    if(v2==0):
        ort=((v1*40)/100)+((fn*60)/100)
        yazi.config(text="Not:%d"%ort)
        
    else:
        ort=((v1*20)/100)+((v2*20)/100)+((fn*60)/100)
        yazi.config(text="Not:%d"%ort)
    
anapencere=Tk()
anapencere.geometry("300x200")
ilkyazi=Label(anapencere)
ilkyazi.config(text="Tek vize ise vize 2 sıfır girilmelidir.!")
ilkyazi.pack()
yazi=Label(anapencere)
yazi.config(text="Not:")
yazi.pack()


L1 = Label(anapencere, text="Vize 1")
L1.pack()
vize1=Entry(anapencere)

vize1.pack()
L2 = Label(anapencere, text="Vize 2")
L2.pack()
vize2=Entry(anapencere)

vize2.pack()

L3 = Label(anapencere, text="Final")
L3.pack()



fnotu=Entry(anapencere)

fnotu.pack()

buton=Button(anapencere)
buton.config(text="Hesapla")
buton.config(command=hesapla)
buton.pack()
anapencere.mainloop() 
