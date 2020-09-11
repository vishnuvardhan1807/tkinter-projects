from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()

def click():
    global my_img
    root.filename = filedialog.askopenfilename(initialdir="tkinter/angel",title="select a file",filetypes=(("png files","*.png"),("all files","*.*")))
    Label(root,text=root.filename,bg="red").pack()
    my_img=ImageTk.PhotoImage(Image.open(root.filename))
    Label(root,image=my_img).pack()
def click1():
     global my_img1
     root.filename = filedialog.askopenfilename(initialdir="tkinter/angel",title="select a file",filetypes=(("png files","*.png"),("all files","*.*")))
     Label(root,text=root.filename1,bg="red").pack()
     my_img1=ImageTk.PhotoImage(Image.open(root.filename))
     Label(root,image=my_img).pack()
    
    
Button(root,text="press",fg="blue",command=click).pack()

Button(root,text="press1",fg="blue",command=click1).pack()

root.mainloop()