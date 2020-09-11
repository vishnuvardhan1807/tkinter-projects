from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("menu Bar")
root.iconbitmap("icons/superman.ico")
root.geometry("500x500")

#creating menubar
my_menu = Menu(root)
root.config(menu=my_menu)

def new():
    clear_all()
    newframe.pack(fill='both',expand=1)
    Label(newframe,text="you clicked").pack()

def cut():
    clear_all()
    newframe1.pack(fill='both',expand=1)
    Label(newframe1,text="you clicked").pack()

def search():
    clear_all()
    newframe2.pack(fill='both',expand=1)
    Label(newframe2,text="you clicked").pack()
def clear_all():
    newframe.pack_forget()
    newframe1.pack_forget()
    newframe2.pack_forget()

#creating submnenus
file_menu = Menu(my_menu)
my_menu.add_cascade(label="file",menu=file_menu)

file_menu.add_command(label="New",command=new)

edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit",menu=edit_menu)

edit_menu.add_command(label="cut",command=cut)


option_menu = Menu(my_menu)
my_menu.add_cascade(label="Search",menu=option_menu)

option_menu.add_command(label="name",command=search)

newframe = Frame(root,bg="red")
newframe1 = Frame(root,bg="black")
newframe2 = Frame(root,bg="green")



root.mainloop()