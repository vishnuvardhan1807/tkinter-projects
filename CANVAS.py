from tkinter import *

root = Tk()
root.title("canvas in tkinter")
root.iconbitmap("icons/superman.ico")
root.geometry("800x800")

#creating a canvas area
my_canvas = Canvas(root,width=500,height=500,bg="white")
my_canvas.pack(pady=20)

my_canvas.create_rectangle(50,450,450,25,fill="pink")

my_canvas.create_oval(50,450,450,50,fill="cyan")

my_canvas.create_line(0,250,500,250,fill="red")
my_canvas.create_line(250,500,250,0,fill="red")





root.mainloop()