# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 20:39:53 2020

@author: Atul Saxena
"""

import pandas as pd
a={"Jan":{"Apple":0,"Orange":232,"Mango":456,"Pinapple":872},"Feb":{"Apple":502,"Orange":612,"Mango":783,"Pinapple":902},"March":{"Apple":608,"Orange":102,"Mango":111,"Pinapple":484},"April":{"Apple":710,"Orange":321,"Mango":0,"Pinapple":416}}
df=pd.DataFrame(a)
print(df)
df.to_csv("fruitseller.csv",sep=";")
pd.read_csv("fruitseller.csv")