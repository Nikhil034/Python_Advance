import tkinter as tk
from tkinter import messagebox,Entry,StringVar,Button

win=tk.Tk()
win.title("MessageBox Widget")
win.geometry("400x400")

v1=StringVar()

def click_me():
    #messagebox.showwarning("System Tell",message="This is warning")

    #res=messagebox.askyesno("Confirmation From System",message="Are You Sure")
    #res=messagebox.askretrycancel("Confirmation From System",message="Are You Sure")
    #res=messagebox.askokcancel("Confirmation From System",message="Are You Sure")
    #res=messagebox.askyesnocancel("Confirmation From System",message="Are You Sure")

    res=messagebox.askquestion("Confirmation From System",message="Are You Sure")
    print(res)

    if res=='yes':
        messagebox.showinfo("System Tell",message="Yes Return")
    else:
        messagebox.showinfo("System Tell",message="No Return")
        
    '''if res==True:
        messagebox.showinfo("System Tell",message="Yes")
    else:
         messagebox.showinfo("System Tell",message="No")'''
        

tx1=Entry(win,textvariable=v1)
tx1.place(x=200,y=100)

bt1=Button(win,text="Here!",bg="cyan",command=click_me)
bt1.place(x=230,y=150)

win.mainloop()

