# project.py
import tkinter as tk
 
root = tk.Tk()

display1 = tk.StringVar()
entry1 = tk.Entry(root,
    relief=tk.FLAT,
    textvariable=display1,
    justify='right',
    bg='orange')
entry1.pack()
entry1["font"] = "arial 30 bold"
    
b1 = tk.Button(root,
            #relief=tk.FLAT,
            compound=tk.LEFT,
            text="new",
            #command=None,
            #image=tk.PhotoImage("img.png")
            )
b1.pack()

display2 = tk.StringVar()
entry2 = tk.Entry(root,
    relief=tk.FLAT,
    textvariable=display2,
    justify='right',
    bg='orange')
entry2.pack()
entry2["font"] = "arial 30 bold"
    
b2 = tk.Button(root,
            #relief=tk.FLAT,
            compound=tk.LEFT,
            text="new",
            #command=None,
            #image=tk.PhotoImage("img.png")
            )
b2.pack()
root.mainloop()
