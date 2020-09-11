from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("deleting widgets")
root.iconbitmap("icons/superman.ico")
root.geometry("500x500")

my_menu = Menu(root)
root.config(menu = my_menu)

def new():
    destroy()
    frame1.pack(fill=BOTH,expand=1)
    Label(frame1,text='42' + u'\u0039',font="arial,20,bold").pack()

def cut():
    destroy()
    frame2.pack(fill=BOTH,expand=1)
    Label(frame2,text="u selexted a option",font="arial,20,bold").pack()
    Label(frame2,text="rara erri pushpha",font="arial,20,bold").pack(pady=10)
    Label(frame2,text=frame2.winfo_children()[0],font="arial,20,bold").pack(pady=10)
    print(frame2.winfo_children())
    
    
def destroy():
    for i in frame1.winfo_children():
        i.destroy()
        
    for i in frame2.winfo_children():
        
        i.destroy()
    frame1.pack_forget()
    frame2.pack_forget()
    

file_menu = Menu(my_menu)
my_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="new",command=new)

edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="cut",command=cut)

frame1 = Frame(root,bg="red",bd=2)
frame2 = Frame(root,bg="green",bd=2)
root.mainloop()