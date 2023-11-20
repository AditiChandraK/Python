# GUI PROGRAMING TKINTER

import tkinter
from tkinter.ttk import Button
root=tkinter.Tk()#creats a window
'''root.mainloop() '''#loops continuosly until we close the window

#adding title and geometry to the window made
root.title("AC-TESTING") #Title
root.geometry("1500x1500")  #Dimension
root.configure(bg='#121212')# cause dark mode is seggsy

#BUTTON WIDGET

b=Button(root, text='Enter the Webpage') #creating a button
'''b.pack()'''#this thingy needs to be used to display the button


from tkinter import messagebox
def click():
    messagebox.showinfo("Message", "Green Button clicked")
a=Button(root, text="yellow",activeforeground="yellow", activebackground="orange", pady=10)
b.pack()



root.mainloop()



