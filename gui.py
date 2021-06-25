from tkinter import *
import os

root = Tk(className='face_recognition_gui')
root.title('Face Recognizer')
root.geometry("500x500")
# svalue = StringVar()  # defines the widget state as string

# l = Label(root, text="Add new person")
# l.config(font=("Courier", 30))
# l.pack()

# w = Entry(root, textvariable=svalue)  # adds a textarea widget
# w.pack()


def captureImg():
    os.system('python captureImg.py')


def recog_dlib():
    os.system('python facerecognition.py')


def register():
    os.system('python register.py')


def add_person():
    # name = svalue.get()
    os.system('python add_person.py')


def studentRecords():
    os.system('python studentrecords.py')


def attendenceRecords():
    os.system('python attendencerecords.py')


# add_btn = Button(root, text="Add", command=add_person)
# add_btn.pack()

f = Frame(root, height=1, width=400, bg="black")
f.pack()

# l = Label(root, text="Train")
# l.config(font=("Courier", 30))
# l.pack()

f = Frame(root, height=1, width=400, bg="black")
f.pack()

l = Label(root, text="Register")
l.config(font=("Arial", 30))
l.pack()

register_btn = Button(
    root, text="Register", command=register)
register_btn.pack()

f = Frame(root, height=1, width=400, bg="black")
f.pack()


l = Label(root, text="Recognize")
l.config(font=("Arial", 30))
l.pack()


recogDL_btn = Button(
    root, text="Recognize (dlib - Deep Learning)", command=recog_dlib)
recogDL_btn.pack()

f = Frame(root, height=1, width=400, bg="black")
f.pack()

l = Label(root, text="Student Records")
l.config(font=("Courier", 30))
l.pack()

studRec_btn = Button(
    root, text="Student Records", command=studentRecords)
studRec_btn.pack()

f = Frame(root, height=1, width=400, bg="black")
f.pack()

l = Label(root, text="Attendence Records")
l.config(font=("Courier", 30))
l.pack()

attdRec_btn = Button(
    root, text="Attendence Records", command=attendenceRecords)
attdRec_btn.pack()

f = Frame(root, height=1, width=400, bg="black")
f.pack()

l = Label(root, text="Capture Image")
l.config(font=("Courier", 30))
l.pack()

upload_btn = Button(
    root, text="Capture Image", command=captureImg)
upload_btn.pack()


root.mainloop()
