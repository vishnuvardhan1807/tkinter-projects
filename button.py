from tkinter import *
root = Tk()
def clicked():
    mylabel=Label(root,text="I clicked",bg="blue")
    mylabel.pack()
myButton=Button(root,text="click me",command=clicked,padx=50,pady=25)
myButton.pack()