import os
import time
import sys
from tkinter import *
from PIL import ImageTk,Image

def times():
   
    clock=time.strftime("%H:%M:%S")
    top.config(text=clock)
    top.after(200,times)


root = Tk()
root.title("digital clock")
root.iconbitmap("icons/clock.ico")
root.geometry("800x800")
root.config(bg="pink")

#label to show time
top = Label(root,text=" ",font=("arial",50,"bold"),bg="pink")
top.grid(row=2,column=1,pady=20,padx=100)
times()

#label to show clock image

image = Image.open("angel/clock.png")
resize = image.resize((200,200),Image.ANTIALIAS)
pic = ImageTk.PhotoImage(resize)
image_label=Label(root,image=pic,bd=0,bg="pink")
image_label.grid(row=0,column=1)
#label to show title
digital = Label(root,text="Digital clock by Vishnu",font=("arial",30,"bold"),relief=RIDGE,fg="red",bg="pink")
digital.grid(row=1,column=1,pady=30,padx=110)

#label to show abbrevations
bottom = Label(root,text="hours     minutes    seconds",font=("arial",25,"bold"),fg="blue",bg="pink")
bottom.grid(row=3,column=1,padx=80,pady=30)

#bottom imagelabel
image1 = Image.open("angel/watch.png")
resize1 = image1.resize((200,200),Image.ANTIALIAS)
pic1 = ImageTk.PhotoImage(resize1)
image_label1=Label(root,image=pic1,bg="pink")
image_label1.grid(row=4,column=1)







root.mainloop()