import tkinter as tk
from tkinter import messagebox


win=tk.Tk()
win.title("Menu Example")
win.geometry("500x300")

menubar=tk.Menu(win)

def some_method():
    messagebox.showinfo(title="Python Say",message="You Click on Menu")

File=tk.Menu(menubar)
menubar.add_cascade(label="File",menu=File)
File.add_command(label="New Folder",command=some_method)
File.add_command(label="Save",command=some_method)

editmenu=tk.Menu(menubar)
menubar.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Cut",command=some_method)
editmenu.add_command(label="Copy",command=some_method)

win.config(menu=menubar)
win.mainloop()
