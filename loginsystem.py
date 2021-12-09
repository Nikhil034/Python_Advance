import tkinter as tk
from tkinter import StringVar,messagebox,Entry,Button
import login_call as lg
from tkinter import Label

win=tk.Tk()
win.title("Login System ")
win.geometry("500x400")

v_em=StringVar()
v_pw=StringVar()

def btn_login():
    v1=v_em.get()
    v2=v_pw.get()
    lg.check_user(v1,v2)
   

lblem=Label(win,text="Enter Email")
lblem.grid(row=1,column=1)
lblpw=Label(win,text="Enter Password")
lblpw.grid(row=2,column=1)

txem=Entry(win,textvariable=v_em)
txem.grid(row=1,column=2)
txpw=Entry(win,textvariable=v_pw,show="*")
txpw.grid(row=2,column=2)

btnlg=Button(text="Login" ,command=btn_login,bg="green")
btnlg.grid(row=3,column=2)




win.mainloop()
