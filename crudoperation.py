import tkinter as tk
import mysql.connector
from tkinter import Button
from tkinter import messagebox
from tkinter import Label


win=tk.Tk()
win.title("CRUD opration of Database")
win.geometry('500x500')
#win.resizable(False,False)

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="company"
)    



tv1=tk.StringVar()
tv2=tk.StringVar()
tv3=tk.StringVar()
tvdel=tk.StringVar()

def add_data():
    val=tv1.get()
    val2=tv2.get()
    val3=tv3.get()
    mycursor=mydb.cursor()
    args=(val,val2,val3)
    mycursor.execute("insert into studdt(sid,sname,scity)values(%s,%s,%s)",args)
    mydb.commit()
    msg=messagebox.showinfo("System Message","Dear "+val2+" Succesfully Add")


def fetch_data():
    mycursor=mydb.cursor()
    mycursor.execute("select * from studdt")
    records=mycursor.fetchall()
    print("Total rows are:  ", len(records))
    lblline=Label(win,text="-----------------------------------")
    lblline.place(x=200,y=370)
    for x in records:
        lblstid=Label(win,text=x)
        lblstid.place(x=220,y=400)

def del_data():
    val=tv1.get()
    mycursor=mydb.cursor()  
    mycursor.execute("delete from studdt where sid="+val)
    print(val)
    mydb.commit()
    msg=messagebox.showinfo("System Message","Remove student Done"+val)

def edit_data():
    val=tv1.get()
    val2=tv2.get()
    val3=tv3.get()
    args=(val2,val3,val)
    mycursor=mydb.cursor()
    mycursor.execute("update studdt set sname=%s,scity=%s where sid=%s",args)
    mydb.commit()
    msg=messagebox.showinfo("System Message","Update student Done"+val)
    
    
    
       
    
               

def exit_win():
    exit()

lblid=Label(win,text="Student_id")
tx1=tk.Entry(win,textvariable=tv1)
lblid.place(x=150,y=150)
tx1.place(x=220,y=150)

lblnm=Label(win,text="Student_name")
tx2=tk.Entry(win,textvariable=tv2)
lblnm.place(x=150,y=210)
tx2.place(x=230,y=210)

lblct=Label(win,text="Student_city")
tx3=tk.Entry(win,textvariable=tv3)
lblct.place(x=152,y=260)
tx3.place(x=230,y=260)

btadd=Button(win,text="+Add",bg="green",command=add_data)
btadd.place(x=200,y=300)

btexit=Button(win,text="Remove",bg="red",command=del_data)
btexit.place(x=250,y=300)

btup=Button(win,text="Update",bg="Pink",command=edit_data)
btup.place(x=320,y=300)

btfetch=Button(win,text="Fetch",bg="Blue",command=fetch_data)
btfetch.place(x=200,y=350)

btdel=Button(win,text="Exit",bg="Orange",command=exit_win)
btdel.place(x=250,y=350)



win.mainloop()
