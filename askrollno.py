import os
from tkinter import *
import tkinter.messagebox
# from captureImg import capture
# import captureImg

# def captureImg():
#     os.system("python captureImg.py")


# RollNo = IntVar()
# root = Tk()
# root.geometry('500x500')
# root.title("Registration Form")
# rollno = RollNo.get()
# label = Label(root, text="Roll No", width=20, font=("bold", 10))
# label.place(x=85, y=330)
# entry = Entry(root, textvar=RollNo)
# entry.place(x=240, y=330)
# Button(root, text='Submit', width=20, bg='brown',
#        fg='white', command=captureImg).place(x=180, y=380)

root = Tk()
root.geometry('500x250')
root.title("Registration Form")

RollNo = IntVar()


def askRollno():
    rollno = RollNo.get()
    # captureImg.capture(str(rollno))
    # os.system("python captureImg.py")
    tkinter.messagebox.showinfo(
        "Success", "OK, Please press close button to capture image")
    return rollno


label = Label(root, text="Roll No", width=20, font=("bold", 10))
label.place(x=85, y=130)

entry = Entry(root, textvar=RollNo)
entry.place(x=240, y=130)

Button(root, text='Submit', width=20, bg='brown',
       fg='white', command=askRollno).place(x=180, y=200)


root.mainloop()
