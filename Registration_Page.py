from tkinter import *

top = Tk()

def Register():
    def Update():
        p = username.get()
        print(p)
        top.destroy()
        
    top.geometry("400x300")
    top.configure(background="#ffff8f")

    label2 = Label(top, text="Register your name")
    label2.configure(background="#ffff8f")
    label2.config(font=("Courier", 15))
    label2.place(x = 55,y=50,height=70, width=300)

    username = StringVar() 
    passEntry = Entry(top, textvariable=username)
    passEntry.place(x =145,y=150,height=40, width=120)

    B7 = Button(top, text = "Register", command = Update)
    B7.place(x = 145,y = 220,height=40, width=120)
    B7.configure(background="#ffff8f")    

Register()


