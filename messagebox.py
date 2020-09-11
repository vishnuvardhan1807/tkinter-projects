from tkinter import *
from PIL import ImageTk,ImageTk
from tkinter import messagebox

root = Tk()
root.title("popup box")

#showinfo,showwarning,showerror,askokcancel,askquestion,askyesno

def msg1():
    
    response=messagebox.showinfo("message is", "get out of here")
    Label(root,text=response).pack()
def msg2():
     response=messagebox.showwarning("message is", "get out of here")
     Label(root,text=response).pack()
def msg3():
    response=messagebox.showerror("message is", "get out of here")
    Label(root,text=response).pack()
def msg4():
    response=messagebox.askokcancel("message is", "get out of here")
    Label(root,text=response).pack()
def msg5():
    response=messagebox.askquestion("message is", "get out of here")
    Label(root,text=response).pack()
def msg6():
    response=messagebox.askyesno("message is", "get out of here")
    Label(root,text=response).pack()
    



button_1=Button(root,text="popup",command=msg1).pack()
button_1=Button(root,text="warning",command=msg2).pack()
button_1=Button(root,text="error",command=msg3).pack()
button_1=Button(root,text="asok",command=msg4).pack()
button_1=Button(root,text="askquestion",command=msg5).pack()
button_1=Button(root,text="askyesno",command=msg6).pack()

root.mainloop()