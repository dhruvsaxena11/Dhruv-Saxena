from tkinter import *
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
from PIL import Image, ImageTk
a=pd.read_csv("C:\Users\Atul Saxena\Downloads\Datasets\crop.csv")
a["target"]=pd.Categorical(a["label"]).codes
x=a.iloc[0:,:-4]
y=a.iloc[0:,-1:]
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
model=RandomForestClassifier()
model.fit(X_train,y_train)


root=Tk()

def predict():
    data=[[e1.get(),e2.get(),e3.get(),e4.get(),e5.get()]]
    ans=model.predict(data)
    anser=pd.Categorical(a["label"]).categories[ans[0]]
    anstotal="The Recommended Crop is :-"+"\n"+anser
    l10=Label(root,text=anstotal,font=("Arial",15,"bold"))
    l10.place(x=330,y=145)
def reset():
    e1.delete(0,10)
    e2.delete(0,10)
    e3.delete(0,10)
    e4.delete(0,10)
    e5.delete(0,10)
img=Image.open("gui bg 2.jpg")
img2=ImageTk.PhotoImage(img)
g1=root.geometry("650x360")
g2=root.title("ML BASED SMART SOIL ANALYZER")
l1=Label(root,image=img2)
l1.place(x=0,y=0)
l2=Label(root,text="ML BASED SMART SOIL ANALYZER",font=("Arial",18,"bold"))
l2.pack(pady=5)
l3=Label(root,text="Measured Soil Fertility :-",font=("Arial",10,"bold"))
l3.place(x=50,y=60)
l4=Label(root,text="Nitrogen :-",font=("Arial",11,"bold"))
l4.place(x=50,y=90)
e1=Entry(root,font=("Arial",10,"bold"))
e1.place(x=170,y=90)
l5=Label(root,text="Phosphorous :-",font=("Arial",11,"bold"))
l5.place(x=50,y=120)
e2=Entry(root,font=("Arial",10,"bold"))
e2.place(x=170,y=120)
l6=Label(root,text="Potassium :-",font=("Arial",11,"bold"))
l6.place(x=50,y=150)
e3=Entry(root,font=("Arial",10,"bold"))
e3.place(x=170,y=150)
l7=Label(root,text="Temperature :-",font=("Arial",11,"bold"))
l7.place(x=50,y=180)
e4=Entry(root,font=("Arial",10,"bold"))
e4.place(x=170,y=180)
l8=Label(root,text="Humidity :-",font=("Arial",11,"bold"))
l8.place(x=50,y=210)
e5=Entry(root,font=("Arial",10,"bold"))
e5.place(x=170,y=210)
b1=Button(root,text="Recommend Crop",font=("Arial",12,"bold"),command=predict)
b1.place(x=60,y=290)
b2=Button(root,text="  Reset  ",font=("Arial",12,"bold"),command=reset)
b2.place(x=250,y=290)
l11=Label(root,text="Team :- Dhruv Saxena, Arjun Kumar Soni")
l11.place(x=410,y=310)
root.mainloop()