from tkinter import *
root = Tk()
e = Entry(root,width=50)
e.insert(0,"enter here")
e.pack()
def clicked():
    hello="hello"+" "+e.get()
    mylabel=Label(root,text=hello,fg="blue")
    mylabel.pack()

button=Button(root,text="click here",command=clicked)
button.pack()
root.mainloop()