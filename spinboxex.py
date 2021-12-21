from tkinter import *

win=Tk()
win.geometry("500x400")

v_spin=StringVar()

s_box=Spinbox(win,from_=11,to=20,textvariable=v_spin)

Label(win,textvariable=v_spin).pack()
s_box.pack()
win.mainloop()
