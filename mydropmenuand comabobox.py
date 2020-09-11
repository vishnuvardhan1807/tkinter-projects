from tkinter import *
from tkinter import ttk

root = Tk()
root.title("option menu")
root.geometry("500x500")

items = [1,3,5,7]
var = IntVar()
var.set(items[0])

def click(event):
    
    Label(root,text="you selected").pack()
     

drop = OptionMenu(root,var,*items,command=click)
drop.pack()

combo = ttk.Combobox(root,value=items)
combo.bind("<<ComboboxSelected>>",click)
combo.pack()










root.mainloop()
