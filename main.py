import random
import pyperclip
import tkinter
from tkinter import *
from tkinter.ttk import *



def low():
    entry.delete(0,END)
    length = var1.get()

    lower ='abcdefghijklmnopqrstuvwxyz'
    medium = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    hard = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()_-+=~`,./'
    password =''


    if var.get() == 1:
        for i in range(0,length):
            password = password + random.choice(lower)
        return password
    
    elif var.get() == 0:
        for i in range(0,length):
            password = password + random.choice(medium)
        return password
    elif var.get() == 3:

        for i in range(0,length):
            password = password + random.choice(hard)
        return password
    else:
        print("plase choice an option")

    

def generate():
    password1= low()
    entry.insert(10,password1)


def copyclip():
    random_password =entry.get()
    pyperclip.copy(random_password)



root=Tk()
var = IntVar()
var1 = IntVar()


root.title("RANDOM PASSWORD GENERATOR")
root.geometry('500x500')


random_password = Label(root,text="PASSWORD")
random_password.grid(row=0,padx=20)
entry=Entry(root,width=25)
entry.grid(row=0,column=1,padx=10,pady=10)


len =Label(root,text="LENGTH",padding=20)
len.grid(row=1)


copy_button =Button(root,text= "COPY" ,command=copyclip)
copy_button.grid(row=0 ,column=2)


copy_button =Button(root,text= "GENERATE" ,command=generate)
copy_button.grid(row=0 ,column=3 ,padx=10,pady=10)

radio_low = Radiobutton(root,text="LOW",variable=var,value=1)
radio_low.grid(row=3,column =1,sticky ='E' ,padx=20)

radio_mid = Radiobutton(root,text="MEDIUM",variable=var,value=0)
radio_mid.grid(row=3,column =2,sticky ='E',padx=20)

radio_hard = Radiobutton(root,text="HIGH",variable=var,value=3)
radio_hard.grid(row=3,column =3,sticky ='E',padx=20)

Combo= Combobox(root,textvariable=var1)

Combo['values']=(8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,"Length")

Combo.current(0)

Combo.bind('<<ComboboxSelected>>')
Combo.grid(row=1,column=1)

root.mainloop()

