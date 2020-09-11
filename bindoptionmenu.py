from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk

root = Tk()
root.title("binding dropdownbox")
root.iconbitmap("icons/superman.ico")
root.geometry("500x500")

def click(event):
    Label(root,text="you selectes"+" "+var.get()).pack()
    
items = ["pizza","burger","idly","dosa","vada","Biriyani"]
var = StringVar()
var.set(items[0])
#creating a list of option menu items


drop = OptionMenu(root,var,*items,command=click)
drop.pack(pady=20)

'''button = Button(root,text="select",font=("arial",20),command=click)
button.pack(pady=20)'''

#craeting a combo box

combo = ttk.Combobox(root,value=items)
combo.current(2)
combo.bind("<<ComboboxSelected>>",click)
combo.pack()




root.mainloop()
