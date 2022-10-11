import pandas as pd
from tkinter import *
data={"Roll":[1,2,3,4],"Name":["a","b","c","dd"]}
df=pd.DataFrame(data,index=[1,2,3,4])
root=Tk()
def dft():
    myr=int(c.get())
    e.insert(0,df.get_value(myr,"Name"))
    
    
a=root.geometry("200x200")
b=Label(text="Enter Roll")
b.pack()
c=Entry()
c.pack()
f=Button(text="Fetch",command=dft)
f.pack()
d=Label(text="Name")
d.pack()
e=Entry()
e.pack()



root.mainloop()