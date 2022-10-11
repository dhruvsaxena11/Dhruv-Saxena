# -*- coding: utf-8 -*-
"""
Created on Tue May 19 11:11:17 2020

@author: Atul Saxena
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
    print(d1.iloc[int(input("select your pizza"))])
    print(qty)
elif size=="M":
    print(d2)
    print(d2.iloc[int(input("select your pizza"))])
    print(qty)
elif size=="L":
    print(d3)
    print(d3.iloc[int(input("select your pizza"))])
    print(qty)
elif size=="A":
    print(d4)
    print(d4.iloc[int(input("select your pizza"))])
    print(qty)
qty=int(input("enter quantity"))
d1ad=[["cold drink",20],["chips",20],["extra cheese",30]]
pizzad=pd.DataFrame(d1ad,columns=["Item","rate"])
ad=str(input("want addon Yes:Y/No:N"))
if ad=="Y":
    print(pizzad)
    print(pizzad.iloc[int(input("select addon"))
