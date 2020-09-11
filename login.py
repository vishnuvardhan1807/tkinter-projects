from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.geometry("720x720")
root.title("login to instagram")


my_image = Image.open("angel/insta.png")
resize = my_image.resize((80,80),Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(resize)

my_label=Label(root,image=new_pic)
my_label.grid(row=5,column=10,columnspan=3,padx=200,pady=50)

login = Label(root,text="userid")
login.grid(row=10,column=10,ipady=20)

password = Label(root,text="password")
password.grid(row=12,column=10,ipady=20)

e1 = Entry(root,width=30)
e1.grid(row=10,column=11)

e2 = Entry(root,width=30)
e2.grid(row=12,column=11)

def click():
    
    global insta
    global resize1
    global my_page
    if e1.get()=="vishnu" and e2.get()=="rapid":
        top = Toplevel()
        insta = Image.open("angel/login.png")
        resize1 =insta.resize((720,720),Image.ANTIALIAS)
        my_page = ImageTk.PhotoImage(resize1)
        
        Label(top,image=my_page).pack()
    else:
      messagebox.showerror("invalid","invalid password")
    

#creating login button

button = Button(root,text="login",bg="blue",fg="yellow",command=click)
button.grid(row=13,column=11)







root.mainloop()