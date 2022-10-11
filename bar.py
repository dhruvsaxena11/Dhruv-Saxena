# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 20:57:39 2021

@author: Atul Saxena
"""

import pandas as pd
import matplotlib.pyplot as pl
import numpy as np
d1=[[0,502,608,710],[232,612,102,321],[456,783,111,0],[872,902,484,416]]
fruitseller=pd.DataFrame(d1,index=["Apple","Orange","Mango","Pinapple"],columns=["Jan","Feb","Mar","Apr"])
print(fruitseller)
x=np.arange(1,5)
pl.bar(x,fruitseller["Jan"],width=0.1)
pl.bar(x+0.2,fruitseller["Feb"],width=0.1)
pl.bar(x+0.4,fruitseller["Mar"],width=0.1)
pl.bar(x+0.6,fruitseller["Apr"],width=0.1)
pl.xticks(x,["Jan","Feb","March","April"])
pl.show()