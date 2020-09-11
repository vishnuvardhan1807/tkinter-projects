from tkinter import *
root = Tk()
root.title("simple calculator")
e = Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
    
def addition():
    first_number=e.get()
    global nxtnum
    global math
    math="addition"
    nxtnum=int(first_number)
    e.delete(0,END)

def equal():
    second_num=e.get()
    e.delete(0,END)
    if math=="addition":
        e.insert(0,nxtnum + int(second_num))
    elif math=="subraction":
        e.insert(0,nxtnum - int(second_num))
    elif math=="multiplication":
        e.insert(0,nxtnum * int(second_num))
    else:
        e.insert(0,nxtnum / int(second_num))
        
def delete():
    e.delete(0,END)

def subract():
     first_number=e.get()
     global nxtnum
     global math
     math="subraction"
     nxtnum=int(first_number)
     e.delete(0,END)
 
def multiply():
     first_number=e.get()
     global nxtnum
     global math
     math="multiplication"
     nxtnum=int(first_number)
     e.delete(0,END)
    

def divison():
     first_number=e.get()
     global nxtnum
     global math
     math="division"
     nxtnum=int(first_number)
     e.delete(0,END)
    
    
button_1=Button(root,text="1",padx=40,pady=40,command=lambda: click(1))
button_2=Button(root,text="2",padx=40,pady=40,command=lambda: click(2))
button_3=Button(root,text="3",padx=40,pady=40,command=lambda: click(3))
button_4=Button(root,text="4",padx=40,pady=40,command=lambda: click(4))
button_5=Button(root,text="5",padx=40,pady=40,command=lambda: click(5))
button_6=Button(root,text="6",padx=40,pady=40,command=lambda: click(6))
button_7=Button(root,text="7",padx=40,pady=40,command=lambda: click(7))
button_8=Button(root,text="8",padx=40,pady=40,command=lambda: click(8))
button_9=Button(root,text="9",padx=40,pady=40,command=lambda: click(9))
button_0=Button(root,text="0",padx=40,pady=40,command=lambda: click(0))
button_add=Button(root,text="+",padx=40,pady=40,command=addition)
button_clear=Button(root,text="refresh",padx=40,pady=40,command=delete)
button_equal=Button(root,text="=",padx=70,pady=40,command=equal)

button_subraction=Button(root,text="-",padx=40,pady=40,command=subract)
button_multiplication=Button(root,text="*",padx=40,pady=40,command=multiply)
button_divide=Button(root,text="/",padx=40,pady=40,command=divison)


button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)


button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)


button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_0.grid(row=4,column=0)
button_add.grid(row=4,column=1)
button_clear.grid(row=4,column=2)

button_equal.grid(row=5,column=1,columnspan=3)

button_subraction.grid(row=6,column=0)
button_multiplication.grid(row=6,column=1)
button_divide.grid(row=6,column=2)




root.mainloop()
