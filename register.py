from tkinter import *
import tkinter.messagebox
import mysql.connector
import mysql.connector.errors
import os

root = Tk()
root.geometry('500x500')
root.title("Registration Form")


Fullname = StringVar()
Email = StringVar()
RollNo = IntVar()
Address = StringVar()
Branch = StringVar()


def captureImg():
    os.system('python captureImg.py')


def database():
    name1 = Fullname.get()
    email = Email.get()
    rollno = RollNo.get()
    address = Address.get()
    branch = Branch.get()

    conn = mysql.connector.connect(
        user='root',
        password='password',
        host='127.0.0.1',
        database='student',
        auth_plugin='mysql_native_password')

    # with conn:
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO student (student_name,rollno,address,branch,email) VALUES(%s,%s,%s,%s,%s)',
                       (name1, rollno, address, branch, email))
        tkinter.messagebox.showinfo("Success", "Registered Successfully!")
        conn.commit()
    except:
        if (mysql.connector.errors.IntegrityError):
            tkinter.messagebox.showerror("Error", "Already Registered")
    # return rollno


label_0 = Label(root, text="Registration form", width=20, font=("bold", 20))
label_0.place(x=90, y=53)


label_1 = Label(root, text="FullName", width=20, font=("bold", 10))
label_1.place(x=80, y=130)

entry_1 = Entry(root, textvar=Fullname)
entry_1.place(x=240, y=130)

label_2 = Label(root, text="Email", width=20, font=("bold", 10))
label_2.place(x=68, y=180)

entry_2 = Entry(root, textvar=Email)
entry_2.place(x=240, y=180)

label_3 = Label(root, text="Branch", width=20, font=("bold", 10))
label_3.place(x=70, y=230)

entry_3 = Entry(root, textvar=Branch)
entry_3.place(x=240, y=230)

label_4 = Label(root, text="address", width=20, font=("bold", 10))
label_4.place(x=70, y=280)

entry_4 = Entry(root, textvar=Address)
entry_4.place(x=240, y=280)

label_5 = Label(root, text="Roll No", width=20, font=("bold", 10))
label_5.place(x=85, y=330)

entry_5 = Entry(root, textvar=RollNo)
entry_5.place(x=240, y=330)

f = Frame(root, height=1, width=400, bg="black")
f.pack()


# upload_btn = Button(
#     root, text="Capture Image", command=captureImg)
# upload_btn.pack()


Button(root, text='Submit', width=20, bg='brown',
       fg='white', command=database).place(x=180, y=380)

root.mainloop()
