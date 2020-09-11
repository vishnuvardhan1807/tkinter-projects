from tkinter import *
from PIL import ImageTk,Image
from random import randint
import random

root = Tk()
root.title("flashcards")
root.iconbitmap("icons/superman.ico")
root.geometry("600x600")

#creating a menubar
my_menu = Menu(root)
root.config(menu=my_menu)

result=0

#create randpm chnage function
def change():
    
    global list1
    global rando
    #creating a list
    list1 = ['ntr_np','ntr_tem','ntr_jlk','prabhas','mahesh_sri',
            'mahesh_ban','mahesh_maha']
    
    #creating a random int
    rando = randint(0,len(list1)-1)
    states = "angel/" + list1[rando] + ".png"
    
    #inserting our images
    global my_label
    global my_pic
    my_pic = ImageTk.PhotoImage(Image.open(states))
    my_label.config(image=my_pic,bg="white")
     
    
#calling submitt button

def submit():
    global answer
    answer = e1.get().lower()
    if answer == list1[rando]:
        
        result = "correct it is" +" " + list1[rando]
    else:
        result = "incorrect it is not correct answer"
    my_label1 = Label(hero_frame,text=result,font="arial,25")
    my_label1.pack(pady=15)
    e1.delete(0,END)
#calling functions
def heroes():
    global my_label
    removeall()
    hero_frame.pack(fill=BOTH,expand=1)
    my_label = Label(hero_frame)
    my_label.pack(pady=15)
    change()
    
    #creating a entrybox
    global e1
    e1 = Entry(hero_frame,width=30)
    e1.pack()
    #creating a next button
    button1 = Button(hero_frame,text="next",command=heroes)
    button1.pack(pady=15)
    
    #button to show mwssage
    button2 = Button(hero_frame,text="submit",command=submit)
    button2.pack()
    
#calling select function
def select():
    if radio_cap.get()==names[answer]:
        result="correct"
    answerlabel.config(text=result)

def movies():
    removeall()
    state_frame_movies.pack(fill=BOTH,expand=1)
    my_label = Label(state_frame_movies)
    my_label.pack()
    global list1
    global rando
    global names
    global answer
    list1 = ['ntr_np','ntr_tem','ntr_jlk','prabhas','mahesh_sri',
            'mahesh_ban','mahesh_maha']
    
    names = {"ntr_np":'nanakuprematho',"ntr_tem":'temper',"ntr_jlk":'jailavakusa',
             "prabhas":'saaho',"mahesh_sri":'srimanthudu',"mahesh_ban":'bharath ane nenu',"mahesh_maha":'maharshi'}
        
        #creating a random int
    
    count=1
    answer_list = []
    while count<4:
        
        rando = randint(0,len(list1)-1)
        
        if count == 1:
            
            
            answer = list1[rando]
            global my_pic
            states = "angel/" + list1[rando] + ".png"
            my_pic = ImageTk.PhotoImage(Image.open(states))
            my_label.config(image=my_pic)
            
       
        answer_list.append(list1[rando])
        list1.remove(list1[rando])
        random.shuffle(list1)
        count+=1
        
    global radio_cap
    radio_cap=StringVar()
    radio_cap.set(names[answer_list[0]])
    
    radio_button1 = Radiobutton(state_frame_movies,text=names[answer_list[0]],variable=radio_cap,value=names[answer_list[0]]).pack()
    radio_button2 = Radiobutton(state_frame_movies,text=names[answer_list[1]],variable=radio_cap,value=names[answer_list[1]]).pack()
    radio_button3 = Radiobutton(state_frame_movies,text=names[answer_list[2]],variable=radio_cap,value=names[answer_list[2]]).pack()
    
    #creating a next button
    
    nxt_button = Button(state_frame_movies,text="next",command=movies)
    nxt_button.pack()
    
    #creating a select button
    
    btselect = Button(state_frame_movies,text="select",font="arial,20",command=select)
    btselect.pack(pady=15)
    
    #creating answer label
    global answerlabel
    answerlabel = Label(state_frame_movies,text=" ",font="arial,20")
    answerlabel.pack(pady=15)
    

#removing framses and deleting childrens    
def removeall():
    #looping through for deleting frame children
    for widget in hero_frame.winfo_children():
        widget.destroy()
    for widget in state_frame_movies.winfo_children():
        widget.destroy()
        
    hero_frame.pack_forget()
    state_frame_movies.pack_forget()
    
#creating submenu titles
tollywood_menu = Menu(my_menu)
my_menu.add_separator()
my_menu.add_cascade(label="tollywood",menu=tollywood_menu)
tollywood_menu.add_command(label="heroes",command=heroes)
tollywood_menu.add_command(label="movies",command=movies)
tollywood_menu.add_command(label="exit",command=root.destroy)

hero_frame = Frame(root,width=500,height=500,bg="white")
state_frame_movies = Frame(root,width=500,height=500,bg="yellow")



root.mainloop()


