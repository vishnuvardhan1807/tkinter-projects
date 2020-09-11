from tkinter import *
from PIL import ImageTk,Image

root = Tk()

var=IntVar()


c = Checkbutton(root,text="check",variable=var,onvalue=1,offvalue=2)
c.deselect()
c.pack()


def click():
    my_label = Label(root,text=var.get())
    my_label.pack()
    
    
def clicked():
    global my_img
    global pic
    top = Toplevel()
    my_img =ImageTk.PhotoImage(Image.open("angel/angel1.png"))
    pic = Label(top,image=my_img).pack()
    




my_button = Button(root,text="click",command=click)
my_button.pack()
my_button2 = Button(root,text="click here to go to new window",command=clicked)
my_button2.pack()

root.mainloop()