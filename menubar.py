from tkinter import *
from PIL import ImageTk,Image

root = Tk()

var = StringVar()
var.set("monday")

def click():
    Label(root,text="today is" + " " +var.get(),bd=1).pack()

drop = OptionMenu(root,var,"monday","tuesday","wednesday","thursday","friday")
drop.pack()


button1 = Button(root,text="click",command=click).pack()
root.mainloop()