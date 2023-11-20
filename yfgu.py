import tkinter
from tkinter import*

from PIL import Image, ImageTk

root = Tk()
canvas = Canvas(root, width=600, height=300)
canvas.pack()

# open and resize the image
image = Image.open(r"C:\Users\aditi\Downloads\PNGIMAGE.png")
resize_image = image.resize((100, 100))

# convert the image to a PhotoImage object
img = ImageTk.PhotoImage(resize_image)

# display the image on the canvas
canvas.create_image(0, 0, anchor=NW, image=img)


root.mainloop()
