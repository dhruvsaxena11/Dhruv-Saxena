# -*- coding: utf-8 -*
from tkinter import *
root=Tk()
a=root.geometry("144x124")
Label(root,text="WELCOME TO SMART WASTE MANAGEMENT SYSTEM",font=("Arial",15,"bold")).grid(row=1,column=20)
Label(root,text="UserName",font=("Arial",15,"bold")).grid(row=1000)
Label(root,text="Password",font=("Arial",15,"bold")).pack(row=2000)
uname=Entry(root,font=("Arial",15,"bold"))
pas=Entry(root,font=("Arial",15,"bold"),show="*")
uname.grid(row=1000,column=40)
pas.grid(row=2000,column=40)
#uname.pack()
#pas.pack()
root.mainloop()
