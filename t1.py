from tkinter import *

root = Tk()
photo = PhotoImage(file="coffee.png")
Button(root,image=photo,borderwidth=0).pack(side=LEFT,padx =20,pady=15)

root.mainloop()
