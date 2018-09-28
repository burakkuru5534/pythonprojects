from tkinter import *
from tkinter import messagebox

pencere=Tk()


# kullanıcıya bilgi verme #
def bilgi():
    messagebox.showinfo("Python seviyor mu?.","Seviyor.")



cevap=messagebox.askquestion("Question","Do you like python?")

if(cevap=="yes"):
    bilgiButonu = Button(pencere,text="Sonuç",command=bilgi)
    bilgiButonu.pack(side=TOP)
else:
    print("yapma")
pencere.mainloop()

