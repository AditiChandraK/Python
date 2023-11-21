import tkinter
from tkinter import*
root=tkinter.Tk()
root.title=("LOVE STORY- TS")
root.geometry=("1500x1500")
root.configure(bg='#121212')
w=Label(root, text ='ARE YOU JULIET?', foreground="Black",background="Red",font = "100",width=100) 
w.pack() 

Checkbutton1 = IntVar() # holds integer data passed to the checkbutton widget
Checkbutton2 = IntVar() 
Checkbutton3 = IntVar()

cb1=Checkbutton(root, text="yes",variable = Checkbutton1, onvalue = 1, offvalue = 0, height = 2, width = 100,background="green",foreground="white")
cb2=Checkbutton(root, text = "YES, BUT DID YOU ASK MY DAD", variable = Checkbutton2, onvalue = 1, offvalue = 0, height = 2, width = 100,background="pink",foreground="white")
cb3=Checkbutton(root, text = "SO CAN GO PICK OUT A WHITE DRESS", variable = Checkbutton3, onvalue = 1, offvalue =0, height = 2, width = 100,background="Purple",foreground="white") 
cb1.pack() 
cb2.pack() 
cb3.pack()


root.mainloop()
