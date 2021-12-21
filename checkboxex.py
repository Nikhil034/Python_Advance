import tkinter as tk
from tkinter import messagebox,Checkbutton
from tkinter import *

win=tk.Tk()
win.title("CheckButton Example")
win.geometry("400x400")

veb1=IntVar()
veb2=IntVar()



def btn_click():
              
    o_var=''
    if veb1.get()==1:
        o_var='bca checked'
    else:
        o_var='bca unchecked'

    if veb2.get()==1:
        o_var+='bscit checked'
    else:
        o_var+='bscit unchecked'

    messagebox.showinfo(message=o_var)        

cb1=Checkbutton(win,text="Bca",variable=veb1)
cb2=Checkbutton(win,text="Bscit",variable=veb2)

btn=Button(win,command=btn_click,text="Show Result")
cb1.grid(row=0,column=0)
cb2.grid(row=1,column=0)

btn.grid(row=3,column=0)
win.mainloop()
