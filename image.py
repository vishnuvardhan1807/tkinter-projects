from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("welcome")

button=Button(root,text="exitbutton",command=root.quit)
button.pack()