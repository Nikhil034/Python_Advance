import tkinter as tk
from tkinter import Button
from tkinter import messagebox

win=tk.Tk()
win.title("Butto Example")
win.geometry('500x400')

def btn_tap():
    msg=messagebox.showinfo("Button App","Clicked")


bt1=Button(win,text="Click here!",command=btn_tap)
bt1.pack()

win.mainloop()
