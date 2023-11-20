import tkinter
from tkinter import*
root=tkinter.Tk()
root.title=("candy store login page")
root.geometry=("1500x1500")
root.configure(bg='#121212')
username=Label(root, text = "username",background="Pink",foreground="black").place(x = 10,y = 50) 
password=Label(root, text = "Password",background="Pink",foreground="black").place(x = 10, y =90)

submitbutton=Button(root, text = "Submit",activebackground = "green", activeforeground = "white").place(x = 30, y = 120) 
e1=Entry(root,width = 20).place(x = 100, y = 50) 
e2=Entry(root, width = 20).place(x = 100, y = 90) 

root.mainloop()