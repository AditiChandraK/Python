import tkinter
from tkinter import*
root=tkinter.Tk()
root.title=("BABY JUST SAY YES")
root.geometry=("1500x1500")
root.configure(bg='#121212')
w=Label(root, text ='Do you love me?', foreground="Black",background="Red",font = "100",width=100) 
w.pack() 

Checkbutton1 = IntVar() # holds integer data passed to the checkbutton widget
Checkbutton2 = IntVar() 
Checkbutton3 = IntVar()

cb1=Checkbutton(root, text="yes",variable = Checkbutton1, onvalue = 1, offvalue = 0, height = 2, width = 100,background="green",foreground="white")
cb2=Checkbutton(root, text = "YES, MARRY ME", variable = Checkbutton2, onvalue = 1, offvalue = 0, height = 2, width = 100,background="pink",foreground="white")
cb3=Checkbutton(root, text = "NO BISH GO DIE", variable = Checkbutton3, onvalue = 1, offvalue =0, height = 2, width = 100,background="Purple",foreground="white") 
cb1.pack() 
cb2.pack() 
cb3.pack()


root.mainloop()
