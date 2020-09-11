from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import time
import os
import sys

root = Tk()
root.title("my tabs")
root.iconbitmap("icons/superman.ico")
root.geometry("720x720")

#creating a notebook
my_tabs = ttk.Notebook(root)
my_tabs.grid(row=0,column=0)

#creating frames to be placed in notebook
frame1 = Frame(my_tabs,bg="pink",width=720,height=720)
frame1.grid(row=1,column=1)

frame2 = Frame(my_tabs,bg="blue",width=720,height=720)
frame2.grid(row=1,column=1)

#adding frames to notebook
my_tabs.add(frame1,text="digital block")
my_tabs.add(frame2,text="tab2")

#adding widgets to frame1 that is tab1

#calling time function
def times():
    clock = time.strftime("%H:%M:%S")
    label3.config(text=clock)
    label3.after(200,times)

#creating a widget to show title and display image

image1 = Image.open("angel/clock.png")
resize1 = image1.resize((200,200),Image.ANTIALIAS)
pic1 = ImageTk.PhotoImage(resize1)
image_label1=Label(frame1,image=pic1,bg="pink")
image_label1.grid(row=0,column=1,padx=150,pady=15)

#label to show title
label2 = Label(frame1,text="digital clock by vishnu",font=("times",30,"bold"),bg="pink",fg="red")
label2.grid(row=1,column=1,pady=20,padx=100)

#label to display time

label3 = Label(frame1,text=" ",font=("times",50,"bold"),fg="blue",bg="pink")
label3.grid(row=2,column=1,padx=80,pady=20)
times()

#label to show hours minutes seconds
label4 = Label(frame1,text="hours   minutes   seconds",font=("arial",35,"bold"),bg="pink",fg="yellow")
label4.grid(row=3,column=1,padx=80,pady=10)




root.mainloop()