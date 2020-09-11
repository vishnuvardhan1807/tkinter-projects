from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("my menu bars")
root.iconbitmap("icons/superman.ico")
root.geometry("600x600")

my_menu = Menu(root)
root.config(menu=my_menu)

def click():
    top = Toplevel()
    top.geometry("720x720")
    top.title("new file")
def edit():
    return

file_menu = Menu(my_menu)
my_menu.add_cascade(label="file",menu=file_menu)
file_menu.add_separator()
file_menu.add_command(label="new..",command=click)
file_menu.add_command(label="exit..",command=root.destroy)

edit_menu = Menu(my_menu)
my_menu.add_cascade(label="edit",menu=edit_menu)
edit_menu.add_separator()
edit_menu.add_command(label="cut",command=edit)
edit_menu.add_command(label="copy",command=edit)


option_menu = Menu(my_menu)
my_menu.add_cascade(label="options",menu=option_menu)
option_menu.add_separator()
option_menu.add_command(label="cut",command=edit)
option_menu.add_command(label="copy",command=edit)

root.mainloop()