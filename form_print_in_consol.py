from tkinter import *
import sqlite3
import tkinter.messagebox
from PIL import Image,ImageTk

#geometry of form
root=Tk()
root.geometry("500x600")
root.title("Registration Form")

#image loading part
imge=Image.open('lena.jpg')
photo=ImageTk.PhotoImage(imge)

lab=Label(image=photo)
lab.pack()




#creating menu bar
menu=Menu(root)
root.config(menu=menu)

def exit1():
    exit()

def abt():
    tkinter.messagebox.showinfo("welcome to authors","this is demo for menu fields")


subm1=Menu(menu)
menu.add_cascade(label="file",menu=subm1)
subm1.add_command(label="Exit",command=exit1)

subm2=Menu(menu)
menu.add_cascade(label="Option",menu=subm2)
subm2.add_command(label="about",command=abt)

#variable declaration part
fn=StringVar()
ln=StringVar()
dob=StringVar()
var=StringVar()
var_c1="java"
var_c2="python"
radio_var=StringVar()


#print and exit function part
def printt():
    first=fn.get()
    sec=ln.get()
    dobut_signup=dob.get()
    var1=var.get()
    var3=var_c1
    var3=var_c2
    var4=radio_var.get()
    print(f"your full name is {first}{sec}")
    print(f"your age is {dobut_signup}")
    print(f"your country is {var1}")
    print(f"your prog lang is {var3}")
    print(f"your gender is {var4}")
    tkinter.messagebox.showinfo("welcome",'user is successfully signed up !!') #messagebox popup

#opening second window from a button
def second_win():
    window=Tk()
    window.title("welcome to second window")
    window.geometry('250x200')
    label_02= Label(window, text="registration completed", relief="solid", width=20, font=("arial", 15, "bold")).place(x=30, y=70)
    b_02=Button(window,text="ok",width=12,bg='brown',fg='white',command=abt).place(x=80,y=110)


#form name
label1=Label(root,text="registration form",relief="solid",width=20,font=("arial",19,"bold"))
label1.place(x=90,y=150)

#first name
label2=Label(root,text="first name :",width=20,font=("arial",10,"bold"))
label2.place(x=80,y=240)

entry_1=Entry(root,textvar=fn)
entry_1.place(x=240,y=242)

#last name
label3=Label(root,text="last name :",width=20,font=("arial",10,"bold"))
label3.place(x=80,y=280)

entry_2=Entry(root,textvar=ln)
entry_2.place(x=240,y=282)

#date of birth
label4=Label(root,text="dob :",width=20,font=("arial",10,"bold"))
label4.place(x=65,y=320)

entry_4=Entry(root,textvar=dob)
entry_4.place(x=240,y=320)

#country using droplist
label5=Label(root,text="country :",width=20,font=("arial",10,"bold"))
label5.place(x=75,y=370)



list1=['nepal', 'india', 'japan']
droplist=OptionMenu(root,var,*list1)
var.set("select country")
droplist.config(width=15)
droplist.place(x=230,y=370)


#programming language using check button
label6=Label(root,text="prog lang :",width=20,font=("arial",10,"bold"))
label6.place(x=80,y=420)

c1=Checkbutton(root,text="java",variable=var_c1).place(x=235,y=420)
c1=Checkbutton(root,text="python",variable=var_c2).place(x=290,y=420)


#gender using radio button
label7=Label(root,text="gender :",width=20,font=("arial",10,"bold"))
label7.place(x=73,y=459)

r1=Radiobutton(root,text='male',variable=radio_var,value="male").place(x=230,y=460)
r2=Radiobutton(root,text='female',variable=radio_var,value="female").place(x=290,y=460)

#signup and quit button
but_signup=Button(root,text="signup",width=12,bg='brown',fg='white',command=printt).place(x=130,y=515)
but_quit=Button(root,text="quit",width=12,bg='brown',fg='white',command=exit1).place(x=280,y=515)
but_login=Button(root,text="login",width=12,bg='brown',fg='white',command=second_win).place(x=208,y=560)

root.mainloop()