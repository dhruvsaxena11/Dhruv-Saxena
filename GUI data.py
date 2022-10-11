import pandas as pd
import matplotlib.pyplot as pl
from Tkinter import *
from PIL import Image, ImageTk
a1={"Roll No":[101,101,101,101],"Maths":[20,100,80,60],"Science":[100,68,40,55],"Name":["Dhruv","Dhruv","Dhruv","Dhruv"]}
df1=pd.DataFrame(a1,index=[2018,2019,2020,2021])
print(df1)
a2={"Maths":[20,55,90,68],"Science":[10,58,80,39],"Name":["Appy","Appy","Appy","Appy"],"Roll No":[102,102,102,102]}
df2=pd.DataFrame(a2,index=[2018,2019,2020,2021])
print(df1)
stu={"Name":["Dhruv","Appy"]}
st1=pd.DataFrame(stu,index=[101,102])
print(st1)
pl.plot([2018,2019,2020,2021],df1["Maths"],marker="*")
pl.show()
pl.plot([2018,2019,2020,2021],df1["Science"],marker="*")
pl.show()
pl.bar([2018,2019,2020,2021],df1["Maths"],color="red")
pl.show()
pl.bar([2018,2019,2020,2021],df1["Science"])
pl.show()

root=Tk()
def d1():
    m1=int(entry1.get())
    m2=menue.get()
    
    name.insert(0,st1.get_value(m1,"Name"))
    if m1==df1.get_value(m2,"Roll No"):
        maths.insert(0,df1.get_value(m2,"Maths"))
        science.insert(0,df1.get_value(m2,"Science"))
    elif m1==df2.get_value(m2,"Roll No"):
        maths.insert(0,df2.get_value(m2,"Maths"))
        science.insert(0,df2.get_value(m2,"Science"))

geo=root.geometry("400x400")
label0=Label(text="Data Feching and Analysis System")
label0.grid(row=4,column=4,pady=8)
label1=Label(text="Enter Roll No")
label1.grid(row=7,column=2)
entry1=Entry(root)

entry1.grid(row=7,column=3)
lis=[2018,2019,2020,2021]
label2=Label(root,text="Name of the Student")
label2.grid(row=9,column=2)
name=Entry(root)
name.grid(row=9,column=3)
label3=Label(root,text="Maths Marks")
label3.grid(row=11,column=2)
maths=Entry(root)
maths.grid(row=11,column=3)
label3=Label(root,text="Science Marks")
label3.grid(row=14,column=2)
science=Entry(root)
science.grid(row=14,column=3)
menue=IntVar()

b1=Button(text="Fetch Data",command=d1)
b1.grid(row=18,column=3)
label4=Label(text="Select Year :")
label4.grid(row=6,column=4)
dp1=Radiobutton(root,text=2018,variable=menue,value=2018)
dp1.grid(row=7,column=4)
dp2=Radiobutton(root,text=2019,variable=menue,value=2019)
dp2.grid(row=9,column=4)
dp3=Radiobutton(root,text=2020,variable=menue,value=2020)
dp3.grid(row=11,column=4)
dp4=Radiobutton(root,text=2021,variable=menue,value=2021)
dp4.grid(row=14,column=4)
root.mainloop()
