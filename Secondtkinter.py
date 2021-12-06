import tkinter as tk

win=tk.Tk()
win.title("Second App By Tkinter")

txt=win.title()
print(txt)
#for print title of app

win.geometry("500x250+500+100")
#set geometry width*height+left+bottom

#win.resizable(False,False)
#set resizable enable or not

win.minsize(100,100)
win.maxsize(600,600)
#set min and max size

#win.attributes('-alpha',0.5)
win.attributes('-topmost',0.5)
#for transperent effect to window
win.mainloop()
