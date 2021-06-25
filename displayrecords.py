import mysql.connector
import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry("500x500")
root.title("Records")

conn = mysql.connector.connect(
    user='root',
    password='password',
    host='127.0.0.1',
    database='student',
    auth_plugin='mysql_native_password')
cursor = conn.cursor()


def studentRecords():
    cursor.execute("SELECT * FROM student limit 0,10")
    i = 0
    for student in cursor:
        for j in range(len(student)):
            e = Entry(root, width=10, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, student[j])
        i = i+1
    # root.mainloop()


def attendenceRecords():
    cursor.execute("SELECT * FROM attendence limit 0,10")
    i = 0
    for student in cursor:
        for j in range(len(student)):
            e = Entry(root, width=10, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, student[j])
        i = i+1
    # root.mainloop()


attendeceBtn = Button(
    root, text="Attendence Records", command=attendenceRecords)
attendeceBtn.pack()

f = Frame(root, height=1, width=400, bg="black")
f.pack()

studentsBtn = Button(
    root, text="Student Records", command=studentRecords)
studentsBtn.pack()
root.mainloop()
