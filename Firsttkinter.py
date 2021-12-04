import tkinter as tk
from datetime import date
from tkinter import Button

window=tk.Tk(screenName="Test",className="Tkinter First Program")
bt1=Button(window,text="Click here", width=20, height=5, bg="red")

bt1.place(x=50,y=40)
today = date.today()
bt2=Button(window,text=today, width=20, height=5, bg="yellow")
bt2.place(x=190,y=60)



window.mainloop()
