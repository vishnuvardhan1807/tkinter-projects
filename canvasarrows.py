from tkinter import *

root = Tk()
root.title("moving with arrows")
root.iconbitmap("icons/superman.ico")
root.geometry("700x700")

my_canvas = Canvas(root,width=500,height=500,bg="pink")
my_canvas.pack()

circle=my_canvas.create_oval(250,250,280,220,fill="red")

#calling functions
def up(event):
    x=0
    y=-30
    my_canvas.move(circle,x,y)
    
def down(event):
    my_canvas.move(circle,0,30)
    
def right(event):
    my_canvas.move(circle,30,0)
    
def left(event):
    my_canvas.move(circle,-30,0)
    
def press(event):
    if event.char == "w":
         x=0
         y=-30
         my_canvas.move(circle,x,y)
    elif event.char == "s":
        my_canvas.move(circle,0,30)
        
        


root.bind("<Key>",press)
root.bind("<a>",up)
root.bind("<b>",down)
root.bind("<c>",right)
root.bind("<d>",left)




root.mainloop()