from tkinter import *

pencere= Tk()

user= Label(pencere, text="Kullanıcı Adı:")
password= Label(pencere, text="Şifre:")

entry_1= Entry(pencere)
entry_2= Entry(pencere)


user.grid(row= 0,column= 0)
password.grid(row= 1,column= 0,sticky=E)
entry_1.grid(row= 0,column= 1)
entry_2.grid(row= 1,column= 1)

tik = Checkbutton(pencere,text= "Remember Me...")
tik.grid(columnspan=2)
pencere.mainloop()
