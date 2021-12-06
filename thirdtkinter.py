import tkinter as tk
from tkinter import Button

win=tk.Tk()
win.title("Third Tkinter")

win.iconbitmap("user.ico")
#it is used to change the icon

bt1=Button(win,text="click1")
bt2=Button(win,text="click2")
bt3=Button(win,text="click3")

'''bt1.pack()
bt2.pack()
bt3.pack()'''

'''bt1.grid(column=1,row=1)
bt2.grid(column=2,row=2)
bt3.grid(column=3,row=3)'''

bt1.place(x=50,y=100)
bt2.place(x=100,y=100)




win.mainloop()
