from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("calculator")
root.geometry("165x165")

#creating a enrty box
e1 = Entry(root,width=20)
e1.grid(row=0,column=0,columnspan=3)


def number(digit):
    current=e1.get()
    e1.delete(0,END)
    e1.insert(0,str(current)+str(digit))
    
def addition():
    global firstnum
    global secondnum
    global math
    math = "addition"
    firstnum = e1.get()
    secondnum = int(firstnum)
    e1.delete(0,END)
   
    
def equal():
    nxtnum = e1.get()
    e1.delete(0,END)
    if math == "addition":
        e1.insert(0,secondnum+int(nxtnum))
    if math == "subraction":
        e1.insert(0,secondnum-int(nxtnum))
    if math == "multiplication":
        e1.insert(0,secondnum*int(nxtnum))
    if math == "division":
        e1.insert(0,secondnum/int(nxtnum))
    

def sub():
    global firstnum
    global secondnum
    global math
    math = "subraction"
    firstnum = e1.get()
    secondnum = int(firstnum)
    e1.delete(0,END)
   

def mul():
    global firstnum
    global secondnum
    global math
    math = "multiplication"
    firstnum = e1.get()
    secondnum = int(firstnum)
    e1.delete(0,END)

def div():
    global firstnum
    global secondnum
    global math
    math = "division"
    firstnum = e1.get()
    secondnum = int(firstnum)
    e1.delete(0,END)

def delete():
    e1.delete(0,END)
    
    

#creating buttons
button1 = Button(root,text="1",command=lambda:number(1))
button1.grid(row=3,column=0,ipadx=18)

button2 = Button(root,text="2",command=lambda:number(2))
button2.grid(row=3,column=1,ipadx=18)

button3 = Button(root,text="3",command=lambda:number(3))
button3.grid(row=3,column=2,ipadx=18)

button4 = Button(root,text="4",command=lambda:number(4))
button4.grid(row=2,column=0,ipadx=18)

button5 = Button(root,text="5",command=lambda:number(5))
button5.grid(row=2,column=1,ipadx=18)

button6 = Button(root,text="6",command=lambda:number(6))
button6.grid(row=2,column=2,ipadx=18)

button7 = Button(root,text="7",command=lambda:number(7))
button7.grid(row=1,column=0,ipadx=18)

button8 = Button(root,text="8",command=lambda:number(8))
button8.grid(row=1,column=1,ipadx=18)

button9 = Button(root,text="9",command=lambda:number(9))
button9.grid(row=1,column=2,ipadx=18)

button0 = Button(root,text="0",command=lambda:number(0))
button0.grid(row=4,column=0,ipadx=18)

buttonadd = Button(root,text="+",command=addition)
buttonadd.grid(row=4,column=1,ipadx=18)

buttonsub = Button(root,text="-",command=sub)
buttonsub.grid(row=4,column=2,ipadx=18)

buttonmul = Button(root,text="*",command=mul)
buttonmul.grid(row=5,column=0,ipadx=18)

buttondiv = Button(root,text="/",command=div)
buttondiv.grid(row=5,column=1,ipadx=18)

buttonequal = Button(root,text="=",command=equal)
buttonequal.grid(row=5,column=2,ipadx=18)

buttondel = Button(root,text="AC",command=delete)
buttondel.grid(row=6,column=0,ipadx=18)







root.mainloop()