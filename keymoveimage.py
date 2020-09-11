from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("moving images")
root.iconbitmap("icons/superman.ico")
root.geometry("800x800")

my_canvas = Canvas(root,width=600,height=600,bg="pink")
my_canvas.pack()

image = Image.open("angel/vishnu2.png")
resize = image.resize((100,100),Image.ANTIALIAS)
pic = ImageTk.PhotoImage(resize)

vishnu = my_canvas.create_image(225,225,image=pic)

def click(event):
    if event.char == "w":
        my_canvas.move(vishnu,0,-10)
    elif event.char == "s":
        my_canvas.move(vishnu,0,10)
    elif event.char == "a":
        my_canvas.move(vishnu,-10,0)
    else:
 dd       my_canvas.move(vishnu,10,0)
        


root.bind("<Key>",click)




root.mainloop()