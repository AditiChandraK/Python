from tkinter import *
win=Tk() 
win.geometry("1500x15000") 
win.configure(bg='#121212')
w=Label(win, text ='frame my life', font = "50") 
w.pack() 
frame=Frame(win) 
frame.pack()
bottomframe=Frame(win)
bottomframe.pack( side = TOP)
b1= Button(frame, text ="depression", fg ="red") 
b1.pack( side = LEFT) 
b2 = Button(frame, text ="suicidal", fg ="brown") 
b2.pack( side = LEFT ) 
b3 = Button(frame, text ="melanchony", fg ="blue") 
b3.pack( side = LEFT )
b4 = Button(bottomframe, text ="happy", fg ="green") 
b4.pack( side = TOP) 
b5 = Button(bottomframe, text ="negetivity", fg ="green") 
b5.pack( side = TOP) 
b6 = Button(bottomframe, text ="snake", fg ="green") 
b6.pack( side =TOP) 
win.mainloop()