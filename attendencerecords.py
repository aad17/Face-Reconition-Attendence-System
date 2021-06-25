import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import *

root = tk.Tk()
root.geometry("500x500")
root.title("Attendence Records")

conn = mysql.connector.connect(
    user='root',
    password='password',
    host='127.0.0.1',
    database='student',
    auth_plugin='mysql_native_password')
cursor = conn.cursor()

# cursor.execute("SELECT * FROM attendence limit 0,10")
# i = 0
# for student in cursor:
#     for j in range(len(student)):
#         e = Entry(root, width=10, fg='blue')
#         e.grid(row=i, column=j)
#         e.insert(END, student[j])
#     i = i+1


def view():
    cursor.execute("select student.rollno, student.student_name, attendence.attend_date from student right join attendence on student.rollno=attendence.rollno order by attend_date asc;")

    rows = cursor.fetchall()
    for row in rows:
        print(row)
        tree.insert("", tk.END, values=row)

    conn.close()


tree = ttk.Treeview(root, column=(
    "c1", "c2", "c3"), show='headings')

tree.column("#1", anchor=tk.CENTER)

tree.heading("#1", text="Roll Number")

tree.column("#2", anchor=tk.CENTER)

tree.heading("#2", text="Student Name")

tree.column("#3", anchor=tk.CENTER)

tree.heading("#3", text="Attendence Date")


tree.pack()

button1 = tk.Button(text="Display data", command=view)
button1.pack(pady=10)
root.mainloop()
