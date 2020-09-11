from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("images")


root.iconbitmap('images.png')
my_img=ImageTk.PhotoImage(Image.open('images/angel1.png'))
my_label=Label(image=my_img)
my_label.pack()

root.mainloop()

