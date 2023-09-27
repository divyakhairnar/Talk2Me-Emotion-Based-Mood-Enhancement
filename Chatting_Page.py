from tkinter import *
import time
from pygame import mixer

window = Tk()
frame = Frame(window, width=450, height=600)
frame.configure(background="#ffff8f")

input_user = StringVar()
input_field = Entry(window, text=input_user)
input_field.pack(side=BOTTOM, fill=X)

global msg_num
msg_num = 0
global name
name = 'LAdkat'
def enter_pressed(event):
    global msg_num
    if(msg_num==0):
        input_get = input_field.get()
        print(input_get)
        label = Label(frame, text=input_get)
        label.config(fg="#0000ff")
        label.config(bg="#ffff8f")
        input_user.set('')
        label.pack()    #organizes widgets
        frame.update()
        time.sleep(1)
        input_get = input_field.get()
        print(input_get)
        label = Label(frame, text="Just Relax..!! I am Having Coffee..!! Would you like to have it..!!")
        label.config(fg="#ff0000")
        label.config(bg="#ffff8f")
        input_user.set('')
        label.pack()

    if(msg_num==1):
        input_get = input_field.get()
        print(input_get)
        label = Label(frame, text=input_get)
        label.config(fg="#0000ff")
        label.config(bg="#ffff8f")
        input_user.set('')
        label.pack()
        frame.update()
        time.sleep(1)
        input_get = input_field.get()
        print(input_get)
        label = Label(frame, text="Lets listen one of my favorite Song while talking..")
        label.config(fg="#ff0000")
        label.config(bg="#ffff8f")
        input_user.set('')
        label.pack()
        frame.update()
        mixer.init()
        mixer.music.load('A.mp3')
        mixer.music.play()


    if(msg_num==2):
        input_get = input_field.get()
        print(input_get)
        label = Label(frame, text=input_get)
        label.config(fg="#0000ff")
        label.config(bg="#ffff8f")
        input_user.set('')
        label.pack()
        frame.update()
        time.sleep(1)
        input_get = input_field.get()
        print(input_get)
        label = Label(frame, text="I Really like songs of this mood..!!")
        label.config(fg="#ff0000")
        label.config(bg="#ffff8f")
        input_user.set('')
        label.pack()

    if(msg_num==3):
        input_get = input_field.get()
        print(input_get)
        label = Label(frame, text=input_get)
        label.config(fg="#0000ff")
        label.config(bg="#ffff8f")
        input_user.set('')
        label.pack()
        frame.update()
        time.sleep(1)
        input_get = input_field.get()
        print(input_get)
        label = Label(frame, text="Which type of songs you like the most..??")
        label.config(fg="#ff0000")
        label.config(bg="#ffff8f")
        input_user.set('')
        label.pack()
        

    if(msg_num==4):
        input_get = input_field.get()
        print(input_get)
        label = Label(frame, text=input_get)
        label.config(fg="#0000ff")
        label.config(bg="#ffff8f")
        input_user.set('')
        label.pack()
        frame.update()
        time.sleep(1)
        input_get = input_field.get()
        print(input_get)
        label = Label(frame, text="Okay .. ! Okay .. !! That's cool..!!!")
        label.config(fg="#ff0000")
        label.config(bg="#ffff8f")
        input_user.set('')
        label.pack()


    if(msg_num==5):
        input_get = input_field.get()
        print(input_get)
        label = Label(frame, text=input_get)
        label.config(fg="#0000ff")
        label.config(bg="#ffff8f")
        input_user.set('')
        label.pack()
        frame.update()
        time.sleep(1)
        input_get = input_field.get()
        print(input_get)
        label = Label(frame, text="I remember one joke, let me tell you that..")
        label.config(fg="#ff0000")
        label.config(bg="#ffff8f")
        input_user.set('')
        label.pack()
        frame.update()
        time.sleep(2)
        label = Label(frame, text="A teacher is talking to a student.")
        label.config(fg="#ff0000")
        label.config(bg="#ffff8f")
        input_user.set('')
        label.pack()
        frame.update()
        time.sleep(1)
        label = Label(frame, text="Teacher: Did your father help your with your homework? ")
        label.config(fg="#ff0000")
        label.config(bg="#ffff8f")
        input_user.set('')
        label.pack()
        frame.update()
        time.sleep(1)
        label = Label(frame, text="Student: No, he did it all by himself.")
        label.config(fg="#ff0000")
        label.config(bg="#ffff8f")
        input_user.set('')
        label.pack()

    if(msg_num==6):
        input_get = input_field.get()
        print(input_get)
        label = Label(frame, text=input_get)
        label.config(fg="#0000ff")
        label.config(bg="#ffff8f")
        input_user.set('')
        label.pack()
        frame.update()
        time.sleep(1)
        input_get = input_field.get()
        print(input_get)
        label = Label(frame, text="Ha haa.. Seems like your mood has been changed..")
        label.config(fg="#ff0000")
        label.config(bg="#ffff8f")
        input_user.set('')
        label.pack()

    if(msg_num==7):
        input_get = input_field.get()
        print(input_get)
        label = Label(frame, text=input_get)
        label.config(fg="#0000ff")
        label.config(bg="#ffff8f")
        input_user.set('')
        label.pack()
        frame.update()
        time.sleep(1)
        input_get = input_field.get()
        print(input_get)
        label = Label(frame, text="So let's start work again.. I have also too much work to do..!!")
        label.config(fg="#ff0000")
        label.config(bg="#ffff8f")
        input_user.set('')
        label.pack()
        label = Label(frame, text="Ba Bye.. !!")
        label.config(fg="#ff0000")
        label.config(bg="#ffff8f")
        input_user.set('')
        label.pack()

    msg_num = msg_num + 1
    return "break"


def chatting():
    global name
    name = "Ladkat"

    kk = "ajay" + name + "corret"
    frame.pack_propagate(False) # prevent frame to resize to the labels size
    input_field.bind("<Return>", enter_pressed)
    frame.pack()
    name = ""
    input_get = input_field.get()
    print(input_get)
    label = Label(frame, text=kk)
    label.config(fg="#ff0000")
    label.config(bg="#ffff8f")
    input_user.set('')
    label.pack()
    window.mainloop()




chatting()
