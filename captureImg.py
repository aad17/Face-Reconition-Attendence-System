import cv2
# from register import RollNo
# import tkinter
# from tkinter import *
# from register import database
import upload
# from askrollno import askRollno
import askrollno
# rollno = database()


def capture(rollno):
    key = cv2. waitKey(1)
    webcam = cv2.VideoCapture(0)
    while True:
        try:
            check, frame = webcam.read()
            print(check)  # prints true as long as the webcam is running
            print(frame)  # prints matrix values of each framecd
            cv2.imshow("Capturing", frame)
            key = cv2.waitKey(1)
            if key == ord('s'):
                cv2.imwrite(filename='photo/'+rollno+".jpg", img=frame)
                # print(saved_img)
                webcam.release()
                print("Image saved!")

                break
            elif key == ord('q'):
                print("Turning off camera.")
                webcam.release()
                print("Camera off.")
                print("Program ended.")
                cv2.destroyAllWindows()
                break

        except(KeyboardInterrupt):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break


# RollNo = IntVar()


# def askRollno():
#     root = Tk()
#     root.geometry('500x500')
#     root.title("Registration Form")
#     rollno = RollNo.get()
#     label = Label(root, text="Roll No", width=20, font=("bold", 10))
#     label.place(x=85, y=330)
#     entry = Entry(root, textvar=RollNo)
#     entry.place(x=240, y=330)
#     Button(root, text='Submit', width=20, bg='brown',
#            fg='white', command=capture).place(x=180, y=380)
#     return rollno


# capture(RollNo)
# rollno = askRollno()
# rollno = str(rollno)
Rollno = askrollno.askRollno()
capture(str(Rollno))
# upload.insertImg(1)
