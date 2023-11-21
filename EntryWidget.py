import tkinter
from tkinter import*
root=tkinter.Tk()
root.title=("login webpage")
root.geometry=("1500x1500")
root.configure(bg='#121212')
name=Label(root, text = "Name",bg='cyan2',fg='deeppink3').place(x = 30,y = 50) #backround of text promt and text colour add bg and fg here 
email=Label(root, text = "Email",bg='cyan2',fg='deeppink3').place(x = 30, y = 90) #NOTE- activebackground and active foreground doesnt work here only bga nd fg to be used
password=Label(root, text = "Password",bg='cyan2',fg='deeppink3').place(x = 30, y = 130) 
submitbtn=Button(root, text = "Submit",bg='chartreuse1',activebackground = "pink", activeforeground = "red").place(x = 30, y = 170) 
entry1=Entry(root,bg='lightpink2',fg='indianred3').place(x = 80, y = 50)  #for the textbox colour and text colour add bg and fg here
entry2=Entry(root,bg='lightpink2',fg='indianred3').place(x = 80, y = 90) #NOTE- activebackground and active foreground doesnt work here only bga nd fg to be used 
entry3=Entry(root,bg='lightpink2',fg='indianred3').place(x = 95, y = 130) 
root.mainloop()