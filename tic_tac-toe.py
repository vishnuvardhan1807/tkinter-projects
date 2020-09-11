from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("tic tac toe game")
root.iconbitmap("D:/tkinter/tic tac toe/game.ico")
root.geometry("1350x750")
root.config(background="skyblue")

#frame for showing title of game
frame1 = Frame(root,bg="cadet blue",width=1350,height=100,pady=2,relief=RIDGE)
frame1.grid(row=0,column=0)

#frame for body of game
frame2 = Frame(root,bg="powder blue",width=1350,height=600,pady=2,relief=RIDGE)
frame2.grid(row=1,column=0)

#label to show title
gametitle = Label(frame1,font=("arial",50,"bold"),text="GUI Tic toc toe game",padx=20,pady=10,fg="red")
gametitle.grid(row=0,column=0)

#inserting right and left side frames
rightframe = Frame(frame2,bd=10,width=560,height=500,padx=10,pady=2,relief=RIDGE,bg="cadet blue")
rightframe.pack(side="right")

leftframe = Frame(frame2,bd=10,width=750,height=500,padx=10,pady=2,relief=RIDGE,bg="cadet blue")
leftframe.pack(side="left")

#partitioning right frame
rightframe1 = Frame(rightframe,bd=10,width=600,height=230,padx=10,pady=2,relief=RIDGE,bg="green")
rightframe1.grid(row=0,column=0)

rightframe2 = Frame(rightframe,bd=10,width=600,height=230,padx=10,pady=2,relief=RIDGE,bg="green")
rightframe2.grid(row=1,column=0)

#declaring player variables
playerx=IntVar()
player0=IntVar()
playerx.set(0)
player0.set(0)
buttons = StringVar()
click = True
def check(buttons):
    global click
    if buttons['text'] == " " and click == True:
        buttons['text'] = 'X'
        click = False
        score()
    if buttons['text'] == " " and click == False:
        buttons['text'] = 'O'
        click = True
        score()
        
def score():
    if button1['text']=="X" and button2['text'] == "X" and button3["text"] == "X":
         button1.configure(background="red")
         button2.configure(background="red")
         button3.configure(background="red")
         n = float(playerx.get())
         value = n+1
         playerx.set(value)
         messagebox.showinfo("status","player x won")
         
    if button4['text']=="X" and button5['text'] == "X" and button6["text"] == "X":
        
        button4.configure(background="red")
        button5.configure(background="red")
        button6.configure(background="red")
        n = float(playerx.get())
        value = n+1
        playerx.set(value)
        messagebox.showinfo("status","player x won")
        
    if button7['text']=="X" and button8['text'] == "X" and button9["text"] == "X":
        button7.configure(background="red")
        button8.configure(background="red")
        button9.configure(background="red")
        n = float(playerx.get())
        value = n+1
        playerx.set(value)
        messagebox.showinfo("status","player x won")
        
    if button1['text']=="X" and button5['text'] == "X" and button9["text"] == "X":
        button1.configure(background="red")
        button5.configure(background="red")
        button9.configure(background="red")
        n = float(playerx.get())
        value = n+1
        playerx.set(value)
        messagebox.showinfo("status","player x won")
        
    if button3['text']=="X" and button5['text'] == "X" and button7["text"] == "X":
        button3.configure(background="red")
        button5.configure(background="red")
        button7.configure(background="red")
        n = float(playerx.get())
        value = n+1
        playerx.set(value)
        messagebox.showinfo("status","player x won")
    
    if button1['text']=="X" and button4['text'] == "X" and button7["text"] == "X":
        
        button1.configure(background="red")
        button4.configure(background="red")
        button7.configure(background="red")
        n = float(playerx.get())
        value = n+1
        playerx.set(value)
        messagebox.showinfo("status","player x won")
    
    if button3['text']=="X" and button6['text'] == "X" and button9["text"] == "X":
        button3.configure(background="red")
        button6.configure(background="red")
        button9.configure(background="red")
        n = float(playerx.get())
        value = n+1
        playerx.set(value)
        messagebox.showinfo("status","player x won")
        
    if button2['text']=="X" and button5['text'] == "X" and button8["text"] == "X":
        button2.configure(background="red")
        button5.configure(background="red")
        button8.configure(background="red")
        n = float(playerx.get())
        value = n+1
        playerx.set(value)
        messagebox.showinfo("status","player x won")
        
    #checking for player 0
    if button1['text']=="O" and button2['text'] == "O" and button3["text"] == "O":
         button1.configure(background="red")
         button2.configure(background="red")
         button3.configure(background="red")
         n = float(player0.get())
         value = n+1
         player0.set(value)
         messagebox.showinfo("status","player 0 won")
         
    if button4['text']=="O" and button5['text'] == "O" and button6["text"] == "O":
        
        button4.configure(background="red")
        button5.configure(background="red")
        button6.configure(background="red")
        n = float(player0.get())
        value = n+1
        player0.set(value)
        messagebox.showinfo("status","player 0 won")
        
    if button7['text']=="O" and button8['text'] == "O" and button9["text"] == "O":
        button7.configure(background="red")
        button8.configure(background="red")
        button9.configure(background="red")
        n = float(player0.get())
        value = n+1
        player0.set(value)
        messagebox.showinfo("status","player 0 won")
        
    if button1['text']=="O" and button5['text'] == "O" and button9["text"] == "O":
        button1.configure(background="red")
        button5.configure(background="red")
        button9.configure(background="red")
        n = float(player0.get())
        value = n+1
        player0.set(value)
        messagebox.showinfo("status","player 0 won")
        
    if button3['text']=="O" and button5['text'] == "O" and button7["text"] == "O":
        button3.configure(background="red")
        button5.configure(background="red")
        button7.configure(background="red")
        n = float(player0.get())
        value = n+1
        player0.set(value)
        messagebox.showinfo("status","player 0 won")
        
    if button1['text']=="O" and button4['text'] == "O" and button7["text"] == "O":
        
        button1.configure(background="red")
        button4.configure(background="red")
        button7.configure(background="red")
        n = float(player0.get())
        value = n+1
        player0.set(value)
        messagebox.showinfo("status","player x won")
    
    if button3['text']=="O" and button6['text'] == "O" and button9["text"] == "O":
        button3.configure(background="red")
        button6.configure(background="red")
        button9.configure(background="red")
        n = float(player0.get())
        value = n+1
        player0.set(value)
        messagebox.showinfo("status","player x won")
        
    if button2['text']=="O" and button5['text'] == "O" and button8["text"] == "O":
        button2.configure(background="red")
        button5.configure(background="red")
        button8.configure(background="red")
        n = float(player0.get())
        value = n+1
        player0.set(value)
        messagebox.showinfo("status","player x won")
        
   
    

def reset():
    button1['text']=" "
    button2['text']=" "
    button3['text']=" "
    button4['text']=" "
    button5['text']=" "
    button6['text']=" "
    button7['text']=" "
    button8['text']=" "
    button9['text']=" "
    click = True
    
    
    #changing color
    button1.configure(background="powder blue")
    button2.configure(background="powder blue")
    button3.configure(background="powder blue")
    button4.configure(background="powder blue")
    button5.configure(background="powder blue")
    button6.configure(background="powder blue")
    button7.configure(background="powder blue")
    button8.configure(background="powder blue")
    button9.configure(background="powder blue")
    
def new():
    reset()
    playerx.set(0)
    player0.set(0)
        
        
#adding player names in rightframe1
label1 = Label(rightframe1,text="playerx:",font="arial,40,bold")
label1.grid(row=0,column=0,pady=10)

e1 = Entry(rightframe1,width=20,textvariable=playerx,font="arial,40,bold")
e1.grid(row=0,column=1,padx=10)

label2 = Label(rightframe1,text="playerx:",font="arial,40,bold")
label2.grid(row=1,column=0,pady=10)

e2 = Entry(rightframe1,width=20,textvariable=player0,font="arial,40,bold")
e2.grid(row=1,column=1,padx=10)

#declaring reset and new game button
buttonreset = Button(rightframe2,text="reset",bg="blue",font=("arial",20,"bold"),height=3,width=20,command=reset)
buttonreset.grid(row=0,column=0)

buttonnewgame = Button(rightframe2,text="new game",bg="blue",font=("arial",20,"bold"),height=3,width=20,command=new)
buttonnewgame.grid(row=1,column=0)

#declaring buttons in right frame for playing game
button1 = Button(leftframe,text=" ",bg="powder blue",font=("arial",20,"bold"),height=3,width=8,command=lambda:check(button1))
button1.grid(row=0,column=0,sticky=S+N+W+E)

button2 = Button(leftframe,text=" ",bg="powder blue",font=("arial",20,"bold"),height=3,width=8,command=lambda:check(button2))
button2.grid(row=0,column=1,sticky=S+N+W+E)

button3 = Button(leftframe,text=" ",bg="powder blue",font=("arial",20,"bold"),height=3,width=8,command=lambda:check(button3))
button3.grid(row=0,column=2,sticky=S+N+W+E)

button4 = Button(leftframe,text=" ",bg="powder blue",font=("arial",20,"bold"),height=3,width=8,command=lambda:check(button4))
button4.grid(row=1,column=0,sticky=S+N+W+E)

button5 = Button(leftframe,text=" ",bg="powder blue",font=("arial",20,"bold"),height=3,width=8,command=lambda:check(button5))
button5.grid(row=1,column=1,sticky=S+N+W+E)

button6 = Button(leftframe,text=" ",bg="powder blue",font=("arial",20,"bold"),height=3,width=8,command=lambda:check(button6))
button6.grid(row=1,column=2,sticky=S+N+W+E)

button7 = Button(leftframe,text=" ",bg="powder blue",font=("arial",20,"bold"),height=3,width=8,command=lambda:check(button7))
button7.grid(row=2,column=0,sticky=S+N+W+E)

button8 = Button(leftframe,text=" ",bg="powder blue",font=("arial",20,"bold"),height=3,width=8,command=lambda:check(button8))
button8.grid(row=2,column=1,sticky=S+N+W+E)

button9 = Button(leftframe,text=" ",bg="powder blue",font=("arial",20,"bold"),height=3,width=8,command=lambda:check(button9))
button9.grid(row=2,column=2,sticky=S+N+W+E)


root.mainloop()