from tkinter import *

root = Tk()
root.title("multiple entry boxes")
root.geometry("720x720")
root.config(bg="yellow")
list1 = []

#calling click function
def click():
    result = ""
    for items in list1:
        result = result + str(items.get())+"\n"
        my_label.config(text=result)
        
    

for i in range(5):
    for j in range(5):
        e1 = Entry(root,width=15)
        e1.grid(row=i,column=j,padx=5,pady=10)
        list1.append(e1)
print(list1)
    
#creating a buttom
button = Button(root,text="select",command=click)
button.grid(row=6,column=1)

#creating a label
my_label = Label(root,text="")
my_label.grid(row=7,column=1,pady=15)
    
    
root.mainloop()