from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("deleting labels")
root.iconbitmap("icons/superman.ico")

e1 = Entry(root,width=20,font=("arial",20,"bold"))
e1.grid(row=0,column=0)

my_label = Label(root)
my_label.grid()
def click():
    global my_label
    room = e1.get()
    my_label.grid_forget()

    my_label=Label(root,text=room,fg="green")
    my_label.grid(row=3,column=0)
    e1.delete(0,END)
   # button['state'] = DISABLED
    
'''def erase():
    my_label.grid_forget()
    button['state'] =NORMAL
    print(button.winfo_exists())'''

button = Button(root,text="submit",bg="yellow",command=click)
button.grid(row=1,column=0)

'''delete = Button(root,text="refresh",bg="green",command=erase)
delete.grid(row=2,column=0)'''




root.mainloop()