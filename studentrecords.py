import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import ttk

root = tk.Tk()
root.geometry("500x500")
root.title("Student Records")

conn = mysql.connector.connect(
    user='root',
    password='password',
    host='127.0.0.1',
    database='student',
    auth_plugin='mysql_native_password')
cursor = conn.cursor()


def view():
    cursor.execute("SELECT * FROM student")

    rows = cursor.fetchall()
    for row in rows:
        print(row)
        tree.insert("", tk.END, values=row)

    conn.close()


tree = ttk.Treeview(root, column=(
    "c1", "c2", "c3", "c4", "c5"), show='headings')

tree.column("#1", anchor=tk.CENTER)

tree.heading("#1", text="Student Name")

tree.column("#2", anchor=tk.CENTER)

tree.heading("#2", text="Roll No")

tree.column("#3", anchor=tk.CENTER)

tree.heading("#4", text="Address")

tree.column("#4", anchor=tk.CENTER)

tree.heading("#5", text="Email")

tree.column("#5", anchor=tk.CENTER)

tree.heading("#3", text="Branch")

tree.pack()

button1 = tk.Button(text="Display data", command=view)

button1.pack(pady=10)
root.mainloop()
