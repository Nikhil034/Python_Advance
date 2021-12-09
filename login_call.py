import mysql.connector
import tkinter as tk
from tkinter import messagebox

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="helthtocare"
    )


def check_user(val1,val2):
              mycursor=mydb.cursor()
              args=(val1,val2)
              mycursor.execute("select * from datadoctor where Email=%s and Password=%s",args)
              user=mycursor.fetchone()
              print(user)

              if user is None:
                  messagebox.showerror(title="System Message",message="Invalid User")
              else:
                   messagebox.showinfo(title="System Message",message="Welcome User")
                  
                  
    
