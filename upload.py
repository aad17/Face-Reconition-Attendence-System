from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import os.path
import os
import face_recognition
import mysql.connector
import pickle
# from facerecognition import aai_face_encoding
# from captureImg import capture
# from register import RollNo


# face_pickled_data = pickle.dumps(amey_face_encoding)

# def captureImg():
#     os.system('python captureImg.py')


def insertImg(rollno):
    conn = mysql.connector.connect(
        user='root',
        password='password',
        host='127.0.0.1',
        database='student',
        auth_plugin='mysql_native_password')
    cursor = conn.cursor()
    sql = (
        "INSERT INTO faces(rollno, face_encoding)"
        "VALUES(%s, %s);"
    )

    try:
        # if os.path.isfile(rollno+'.jpg'):
        rollno = str(rollno)
        file = face_recognition.load_image_file(rollno+".jpg")
        encoding = face_recognition.face_encodings(file)
        faceEncoding = pickle.dumps(encoding)
        data = (rollno, faceEncoding)
        cursor.execute(sql, data)
        conn.commit()
        print("Encoding uploaded successfully")
        # else:
        #     print("File not found")
    except:
        conn.rollback()
        print("Failed to upload")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection Closed")


insertImg(69)
# ws = Tk()
# ws.title('PythonGuides')
# ws.geometry('400x200')

# def open_file():
#     file_path = askopenfile(mode='r', filetypes=[
#                             ('Image Files', '*jpeg *jpg')])
#     if file_path is not None:
#         pass

# # def save_file():
# #     filename = filedialog.asksaveasfile()

# def uploadFiles():
#     pb1 = Progressbar(
#         ws,
#         orient=HORIZONTAL,
#         length=300,
#         mode='determinate'
#     )
#     pb1.grid(row=4, columnspan=3, pady=20)
#     for i in range(5):
#         ws.update_idletasks()
#         pb1['value'] += 20
#         time.sleep(1)

#     pb1.destroy()
#     Label(ws, text='File Uploaded Successfully!',
#           foreground='green').grid(row=4, columnspan=3, pady=10)

# adhar = Label(
#     ws,
#     text='Upload Government id in jpg format '
# )
# adhar.grid(row=0, column=0, padx=10)

# adharbtn = Button(
#     ws,
#     text='Choose File',
#     command=lambda: open_file()
# )
# adharbtn.grid(row=0, column=1)

# upld = Button(
#     ws,
#     text='Upload Files',
#     command=uploadFiles
# )
# upld.grid(row=3, columnspan=3, pady=10)

# ws.mainloop()
