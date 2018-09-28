from tkinter import *

pencere = Tk()

foto= PhotoImage(file="giphy.gif")

etiket=Label(pencere,image=foto)
etiket.pack()

pencere.mainloop()
