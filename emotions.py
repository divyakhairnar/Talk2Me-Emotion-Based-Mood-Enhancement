import cv2
import numpy as np
from keras.models import load_model
from statistics import mode
from utils.inference import detect_faces
from utils.inference import draw_text
from utils.inference import draw_bounding_box
from utils.inference import apply_offsets
from utils.inference import load_detection_model
from utils.preprocessor import preprocess_input

import time

from tkinter import *

top = Tk()

global get_name
get_name = 5

time.sleep(1)

def Register():
    def Update():
        get_name = 1
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
    top.mainloop()

Register()
    
while True:
    if(get_name==5):
#        print('ZAL ki mg')
        break

#print('Zalay')
    




# parameters for loading data and images
emotion_model_path = './models/emotion_model.hdf5'
emotion_labels = {0:'angry',1:'disgust',2:'fear',3:'happy',4:'sad',5:'surprise',6:'neutral'}

# hyper-parameters for bounding boxes shape
frame_window = 10
emotion_offsets = (20, 40)

# loading models
face_cascade = cv2.CascadeClassifier('./models/haarcascade_frontalface_default.xml')
emotion_classifier = load_model(emotion_model_path)

# getting input model shapes for inference
emotion_target_size = emotion_classifier.input_shape[1:3]

# starting lists for calculating modes
emotion_window = []

# starting video streaming

cv2.namedWindow('Emotion Detection')
video_capture = cv2.VideoCapture(0)

cap = cv2.VideoCapture(0) # Webcam source


emotion_mode = []
while cap.isOpened(): # True:
    ret, bgr_image = cap.read()

    #bgr_image = video_capture.read()[1]

    gray_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)
    rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)

    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5,
			minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

    for face_coordinates in faces:

        x1, x2, y1, y2 = apply_offsets(face_coordinates, emotion_offsets)
        gray_face = gray_image[y1:y2, x1:x2]
        try:
            gray_face = cv2.resize(gray_face, (emotion_target_size))
        except:
            continue

        gray_face = preprocess_input(gray_face, True)
        gray_face = np.expand_dims(gray_face, 0)
        gray_face = np.expand_dims(gray_face, -1)
        emotion_prediction = emotion_classifier.predict(gray_face)
        emotion_probability = np.max(emotion_prediction)
        emotion_label_arg = np.argmax(emotion_prediction)
        emotion_text = emotion_labels[emotion_label_arg]
        emotion_window.append(emotion_text)

        
        if len(emotion_window) > frame_window:
            emotion_window.pop(0)
        try:
            emotion_mode = mode(emotion_window)
        except:

            continue

        color = np.asarray((255, 255, 255))
        
        color = color.astype(int)
        color = color.tolist()

        draw_bounding_box(face_coordinates, rgb_image, color)
        draw_text(face_coordinates, rgb_image, emotion_mode,
                  color, 0, -45, 1, 1)
        print(emotion_mode)
        
    bgr_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR)
    cv2.imshow('Emotion Detection', bgr_image)
    if(emotion_mode=='angry' or emotion_mode == 'sad'):
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


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

def enter_pressed(event):
    global msg_num
    if(msg_num==0):
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
   
    first_text = "Hello ..  Whatsup. . . ! ! !"
    frame.pack_propagate(False) # prevent frame to resize to the labels size
    input_field.bind("<Return>", enter_pressed)
    frame.pack()
    name = ""
    input_get = input_field.get()
    print(input_get)
    label = Label(frame, text=first_text)
    label.config(fg="#ff0000")
    label.config(bg="#ffff8f")
    input_user.set('')
    label.pack()
    window.mainloop()

chatting()

