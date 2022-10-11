# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 21:43:57 2021

@author: Atul Saxena
"""

import pandas as pd
d=[[1,"pencil",12,11],[2,"eraser",23,12],[3,"paper",34,14],[4,"cardboard",56,16],[5,"sharpner",22,23],[6,"cloth",39,50]]
sell=pd.DataFrame(d,columns=["item no","Item name","item sell","item cost"])
print(sell.loc[:,"item no":"item sell"])