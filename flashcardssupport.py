from random import randint
import random

answer_list = []

 
global list1
global rando

list1 = ['ntr_np','ntr_tem','ntr_jlk','prabhas','mahesh_sri',
            'mahesh_ban','mahesh_maha']

names = {"ntr_np":'nanakuprematho',"ntr_tem":'temper',"ntr_jlk":'jailavakusa',
         "prabhas":'saaho',"mahesh_sri":'srimanthudu',"mahesh_ban":'bharath ane nenu',"mahesh_maha":'maharshi'}
    
    #creating a random int

count=1

while count<4:
    rando = randint(0,len(list1)-1)
    answer = list1[rando]
    print(answer,"is selected")
    list1.remove(list1[rando])
    answer_list.append(list1[rando])
    count+=1
   
print(answer_list)