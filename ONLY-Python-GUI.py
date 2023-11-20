import tkinter
from tkinter import*
from tkinter import messagebox
root=tkinter.Tk()
root.title("ONlY Python") 
root.geometry("1500x1500")  
root.configure(bg='#121212')
b=Button(root, text='Click to sell feet pics') 



def click():
    messagebox.showinfo("Message","do you have an invisible string tieing u to me eeee")

a=Button(root, text="click to get purple pink skies",command=click, activeforeground="pink", activebackground="purple", pady=20, width=40,bg='grey')

def click():
    messagebox.showinfo("Message","importing python...")
b=Button(root, text="click if u wanna get a python from amazon", command=click, activeforeground="green", activebackground="yellow", pady=20,width=40,bg='grey')
# adding click function to the below button
def click():
   messagebox.showinfo("Message","U are NOT the real slim shady") # when green button clicked it shows a message 
c=Button(root, text="click if u are slim shady", command=click, activeforeground = "white",activebackground="pink", pady=20,width=40, bg='grey')#shows message when this is clicked

def click():
    messagebox.showinfo("Message","u are burdened with glorious purpose")
d=Button(root, text="click if u like loki",command=click, activeforeground="white", activebackground="green", pady=20,width=40,bg='grey')
a.pack()
b.pack()
c.pack()
d.pack()
w=Canvas(root,bg='#C67DE3',height='300')


filename=PhotoImage(file=r"C:\Users\aditi\Downloads\PNGIMAGE.png")
image=w.create_image(20, 20, anchor=NW, image=filename)


w.pack()
root.mainloop()

