from tkinter import *

pencere = Tk()

class sinif():

    def __init__(self,pencere): # yapıcı fonk.
        frame= Frame(pencere) # frame'i pencere içine gömdük
        frame.pack() # frame'i çalıştırır

        self.buton1= Button(frame,text="Buton", bg= "blue", fg= "white")
        self.buton1.bind("<Button-1>",self.tikla)
        self.buton1.pack(side= LEFT)
        
        self.buton2= Button(frame,text= "Çıkış",command=pencere.destroy, bg="red",fg= "white")
        
        self.buton2.pack(side= LEFT)

    

    def tikla(self,pencere):
        print("butona tiklandi")


nesne = sinif(pencere)

pencere.mainloop()

        

    
