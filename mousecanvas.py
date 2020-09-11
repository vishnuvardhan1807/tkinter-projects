from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("mouse motion")
root.iconbitmap("icons/superman.ico")
root.geometry("600x600")

#creating canvas
my_canvas = Canvas(root,height=500,width=500,bg="pink")
my_canvas.pack()

def click(e):
    global image
    global resize
    global pic
    image = Image.open("angel/vishnu2.png")
    resize = image.resize((100,100),Image.ANTIALIAS)
    pic = ImageTk.PhotoImage(resize)

    vishnu = my_canvas.create_image(e.x,e.y,image=pic)






root.bind("<B1-Motion>",click)

root.mainloop()