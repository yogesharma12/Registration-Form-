from tkinter import *
import sqlite3
import tkinter.messagebox
from PIL import Image, ImageTk

# geometry of form
root = Tk()
root.geometry("500x600")
root.title("Registration Form")

# image loading part
imge = Image.open('index1.png')
photo = ImageTk.PhotoImage(imge)

lab = Label(image=photo)
lab.pack()

#connecting to database
def database():
    name1 = fn.get()
    last1 = ln.get()
    date = dob.get()
    country = var.get()
    prog = var_c2
    gender = radio_var.get()
    conn = sqlite3.connect("Form.db")
    with conn:
        cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Student (Name TEXT,Last TEXT,DOB TEXT,country TEXT,Programming TEXT,Gender TEXT)')
    cursor.execute('INSERT INTO Student(Name,Last,DOB,country,Programming,Gender) VALUES(?,?,?,?,?,?)',(name1, last1, date, country, prog, gender))
    conn.commit()


# creating menu bar
menu = Menu(root)
root.config(menu=menu)


def exit1():
    exit()


def abt():
    tkinter.messagebox.showinfo("Welcome to authors", "This is demo for Menu Fields")


subm1 = Menu(menu)
menu.add_cascade(label="File", menu=subm1)
subm1.add_command(label="Exit", command=exit1)

subm2 = Menu(menu)
menu.add_cascade(label="Option", menu=subm2)
subm2.add_command(label="About", command=abt)

# variable declaration part
fn = StringVar()
ln = StringVar()
dob = StringVar()
var = StringVar()
var_c1 = "Java"
var_c2 = "Python"
radio_var = StringVar()


# print and exit function part
def printt():
    First = fn.get()
    sec = ln.get()
    dobut_signup = dob.get()
    var1 = var.get()
    var3 = var_c1
    var3 = var_c2
    var4 = radio_var.get()
    print(f"Your Full name is {First}{sec}")
    print(f"Your age is {dobut_signup}")
    print(f"Your country is {var1}")
    print(f"Your prog lang is {var3}")
    print(f"Your gender is {var4}")
    tkinter.messagebox.showinfo("Welcome", 'user is successfully signed up !!')  # messagebox popup


# opening second window from a button
def second_win():
    window = Tk()
    window.title("Welcome to second window")
    window.geometry('250x200')
    label_02 = Label(window, text="Registration completed", relief="solid", width=20, font=("arial", 15, "bold")).place(
        x=30, y=70)
    b_02 = Button(window, text="ok", width=12, bg='brown', fg='white', command=abt).place(x=80, y=110)


# form name
label1 = Label(root, text="Registration form", relief="solid", width=20, font=("arial", 19, "bold"))
label1.place(x=90, y=150)

# First name
label2 = Label(root, text="First name :", width=20, font=("arial", 10, "bold"))
label2.place(x=80, y=240)

entry_1 = Entry(root, textvar=fn)
entry_1.place(x=240, y=242)

# last name
label3 = Label(root, text="Last name :", width=20, font=("arial", 10, "bold"))
label3.place(x=80, y=280)

entry_2 = Entry(root, textvar=ln)
entry_2.place(x=240, y=282)

# date of birth
label4 = Label(root, text="DOB :", width=20, font=("arial", 10, "bold"))
label4.place(x=65, y=320)

entry_4 = Entry(root, textvar=dob)
entry_4.place(x=240, y=320)

# country using droplist
label5 = Label(root, text="Country :", width=20, font=("arial", 10, "bold"))
label5.place(x=75, y=370)

list1 = ['Nepal', 'India', 'Japan']
droplist = OptionMenu(root, var, *list1)
var.set("Select Country")
droplist.config(width=15)
droplist.place(x=230, y=370)

# programming language using check button
label6 = Label(root, text="Programming Lang :", width=20, font=("arial", 10, "bold"))
label6.place(x=80, y=420)

c1 = Checkbutton(root, text="Java", variable=var_c1).place(x=235, y=420)
c1 = Checkbutton(root, text="Python", variable=var_c2).place(x=290, y=420)


# gender using radio button
label7 = Label(root, text="Gender :", width=20, font=("arial", 10, "bold"))
label7.place(x=73, y=459)

r1 = Radiobutton(root, text='Male', variable=radio_var, value="Male").place(x=230, y=460)
r2 = Radiobutton(root, text='Female', variable=radio_var, value="Female").place(x=290, y=460)

# signup and quit button
but_signup = Button(root, text="Signup", width=12, bg='brown', fg='white', command=database).place(x=130, y=515)
root.bind("<Return>",database)
but_quit = Button(root, text="Quit", width=12, bg='brown', fg='white', command=exit1).place(x=280, y=515)
but_login = Button(root, text="Login", width=12, bg='brown', fg='white', command=second_win).place(x=208, y=560)

root.mainloop()