from tkinter import *
from tkinter import colorchooser

root = Tk()
root.title("color chooser")

def clicked():
    color = colorchooser.askcolor()[1]
    Label(root,text=color).pack(pady=20)
    Label(root,text="hello vishnu",font=("Helvetica",30),bg=color).pack(pady=25)

button = Button(root,text="click",font="arial,20,bold",command=clicked)
button.pack()


root.mainloop()