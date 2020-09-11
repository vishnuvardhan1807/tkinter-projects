from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("adding frames")
root.iconbitmap("image.ico")
frame = LabelFrame(root,padx=40,pady=40)
frame.pack(padx=100,pady=100)

Button(frame,text="click").pack()
Button(frame,text="here").pack()



root.mainloop()