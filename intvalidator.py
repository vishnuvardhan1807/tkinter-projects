from tkinter import *

root = Tk()
root.title("integer validator")
root.iconbitmap("icons/superman.ico")
root.geometry("500x500")

list1 = []

#calling click function
def click():
    result = ""
    for items in list1:
        result = result + items.get() + "\n"
        Label(root,text=result).grid(row=3,column=1)

#adding a label
label1 = Label(root,text="phone number:",font="arial,10")
label1.grid(row=0,column=0,padx=10,pady=10)


label2 = Label(root,text="Roll no:",font="arial,10")
label2.grid(row=1,column=0,padx=10,pady=10)

#creating entry boxes
e1 = Entry(root,width=25)
e1.grid(row=0,column=1,padx=5)
list1.append(e1)

e2 = Entry(root,width=25)
e2.grid(row=1,column=1,padx=5)
list1.append(e2)

#creating buttons

button = Button(root,text="get",command=click)
button.grid(row=2,column=1)











root.mainloop()