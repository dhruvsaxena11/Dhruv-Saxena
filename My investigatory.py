# -*- coding: utf-8 -*-
"""
Created on Tue May 19 11:11:17 2020

@author: Dhruv Saxena
"""
import pandas as pd
import matplotlib.pyplot as pl
name=str(input("Customer Name"))
phone=int(input("Enter customer Phone no"))
d1s=[["Margherita",150,"cheese only"],["Fresh Veggie",200,"Tomato,Capsicum,Onion,cheese"],["Paneer Pizza",250,"Paneer and Cheese"],["Onion Pizza",100,"Onion and Cheese"],["Paneer Veggie",300,"onion,Capsicum,Paneer,Tomato And Cheese"]]
d1=pd.DataFrame(d1s,columns=["Type Of Pizza","Rate","Ingredients"])
d1m=[["Margherita",300,"cheese only"],["Fresh Veggie",400,"Tomato,Capsicum,Onion,cheese"],["Paneer Pizza",500,"Paneer and Cheese"],["Onion Pizza",200,"Onion and Cheese"],["Paneer Veggie",600,"onion,Capsicum,Paneer,Tomato And Cheese"]]
d2=pd.DataFrame(d1m,columns=["Type Of Pizza","Rate","Ingredients"])
d1l=[["Margherita",350,"cheese only"],["Fresh Veggie",450,"Tomato,Capsicum,Onion,cheese"],["Paneer Pizza",300,"Paneer and Cheese"],["Onion Pizza",250,"Onion and Cheese"],["Paneer Veggie",650,"onion,Capsicum,Paneer,Tomato And Cheese"]]
d3=pd.DataFrame(d1l,columns=["Type Of Pizza","Rate","Ingredients"])
d1a=[["Margherita",150,"cheese only","S"],["Fresh Veggie",200,"Tomato,Capsicum,Onion,cheese","S"],["Paneer Pizza",250,"Paneer and Cheese","S"],["Onion Pizza",100,"Onion and Cheese","S"],["Paneer Veggie",300,"onion,Capsicum,Paneer,Tomato And Cheese","S"],["Margherita",300,"cheese only","M"],["Fresh Veggie",400,"Tomato,Capsicum,Onion,cheese","M"],["Paneer Pizza",500,"Paneer and Cheese","M"],["Onion Pizza",200,"Onion and Cheese","M"],["Paneer Veggie",600,"onion,Capsicum,Paneer,Tomato And Cheese","M"],["Margherita",350,"cheese only","L"],["Fresh Veggie",450,"Tomato,Capsicum,Onion,cheese","L"],["Paneer Pizza",300,"Paneer and Cheese","L"],["Onion Pizza",250,"Onion and Cheese","L"],["Paneer Veggie",650,"onion,Capsicum,Paneer,Tomato And Cheese","L"]]
d4=pd.DataFrame(d1a,columns=["Type Of Pizza","Rate","Ingredients","Size"])
size=str(input("enter size of Pizza Small:S/Medium:M/Large:L/All:A"))
if size=="S":
    print(d1)
    select1=d1.iloc[int(input("select your pizza"))]
    #print(qty)
elif size=="M":
    print(d2)
    select2=d2.iloc[int(input("select your pizza"))]
    #print(qty)
elif size=="L":
    print(d3)
    select3=d3.iloc[int(input("select your pizza"))]
    #print(qty)
elif size=="A":
    print(d4)
    select4=d4.iloc[int(input("select your pizza"))]
    #print(qty)
#qty=int(input("enter quantity"))
d1ad=[["cold drink",20],["chips",20],["extra cheese",30]]
pizzad=pd.DataFrame(d1ad,columns=["Item","rate"])
a1=str(input("want addon Yes:Y/No:N"))
if a1=="Y":
    print(pizzad)
    add1=pizzad.iloc[int(input("select addon"))]
bils=[name,phone]
bills=pd.Series(bils,index=["Name","Phone No"])
b1=str(input("Do you want to print bill Yes:Y/No:N"))
if b1=="Y" and size=="S" and a1=="Y":
    print(bills)
    print(select1)
    print("Addon:")
    print(add1)
    print("GST 5% included already")
elif b1=="Y" and size=="S" and a1=="N":
    print(bills)
    print(select1)
    print("GST 5% included already")
elif b1=="Y" and size=="M" and a1=="Y":
    print(bills)
    print(select2)
    print("Addon:")
    print(add1)
    print("GST 5% included already")
elif b1=="Y" and size=="M" and a1=="N":
    print(bills)
    print(select2)
    print("GST 5% included already")
elif b1=="Y" and size=="L" and a1=="Y":
    print(bills)
    print(select3)
    print("Addon:")
    print(add1)
    print("GST 5% included already")
elif b1=="Y" and size=="L" and a1=="N":
    print(bills)
    print(select3)
    print("GST 5% included already")
elif b1=="Y" and size=="A" and a1=="Y":
    print(bills)
    print(select4)
    print("Addon:")
    print(add1)
    print("GST 5% included already")
elif b1=="Y" and size=="A" and a1=="N":
    print(bills)
    print(select4)
    print("GST 5% included already")
dsr=[["Margherita",15,"cheese only","S"],["Fresh Veggie",20,"Tomato,Capsicum,Onion,cheese","S"],["Paneer Pizza",25,"Paneer and Cheese","S"],["Onion Pizza",10,"Onion and Cheese","S"],["Paneer Veggie",30,"onion,Capsicum,Paneer,Tomato And Cheese","S"],["Margherita",30,"cheese only","M"],["Fresh Veggie",40,"Tomato,Capsicum,Onion,cheese","M"],["Paneer Pizza",50,"Paneer and Cheese","M"],["Onion Pizza",20,"Onion and Cheese","M"],["Paneer Veggie",60,"onion,Capsicum,Paneer,Tomato And Cheese","M"],["Margherita",30,"cheese only","L"],["Fresh Veggie",45,"Tomato,Capsicum,Onion,cheese","L"],["Paneer Pizza",30,"Paneer and Cheese","L"],["Onion Pizza",20,"Onion and Cheese","L"],["Paneer Veggie",60,"onion,Capsicum,Paneer,Tomato And Cheese","L"]] 
ds1=pd.DataFrame(dsr,columns=["Type Of Pizza","daily sell","Ingredients","Size"])
ds=str(input("Print Daily Sell Report Yes:Y/No:N :-"))
if ds=="Y":
    print(ds1)
    pl.bar(ds1["Type Of Pizza"],ds1["daily sell"],color=["red","green","blue","black","yellow"])
    pl.show()
    ds1.to_csv("Daily Sell Report")
    print("Database Saved successfully")