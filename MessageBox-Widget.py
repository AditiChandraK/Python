#Name of the function            Significance
#showinfo()                      To display some important information
#showwarning()                   To display some type of Warning
#showerror()                     To display some Error Message
#askquestion()                   To display a dialog box that asks with two options YES or NO
#askokcancel()                   To display a dialog box that asks with two options OK or CANCEL
#askretrycancel()                To display a dialog box that asks with two options RETRY or CANCEL
#askyesnocancel()                To display a dialog box that asks with three options YES or NO or CANCEL

import tkinter
from tkinter import*
from tkinter import messagebox
root=tkinter.Tk()
root.title=("so it goes")
root.dimensions=("1500x1500")
root.configure(bg='#171717')
# function to use the askquestion() function
def Submit(): 
    messagebox.askquestion("so it goes", "are you sure all eyes are on us?")
root.geometry("300x300")
root.geometry("300x300")
# creating Submit Button
b=Button(root,activebackground='pink', text = "are you my magician", command = Submit) 
b.pack() 
root.mainloop()



