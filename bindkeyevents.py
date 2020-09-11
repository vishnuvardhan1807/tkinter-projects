from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("binding events")
root.iconbitmap("icons/superman.ico")
root.geometry("400x400")

def clicked(event):
    Label(root,text="button clicked"+" "+str(event.x)+" "+str(event.y)+" "+event.char+" ",font=("arial",20)).pack()
    


button = Button(root,text="click",bg="green",fg="cyan",font=("Helvetica",25)    
                )
button.bind("<Button-3>",clicked)
button.bind("<Button-1>",clicked)
button.bind("<Enter>",clicked)
button.bind("<Leave>",clicked)
button.bind("<FocusIn>",clicked)        
button.bind("Return",clicked)
button.bind("<Key>",clicked)
button.pack()
Button(root,text="Exit").pack()






root.mainloop()