# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 21:37:33 2019

@author: asus
"""

import pandas as pd
new= {'Box':['Box1','Box1','Box1','Box2','Box2','Box2',],'Dimension':['Length','Width','Height','Length','Width','Height'],'Value':[6,4,2,5,3,4]}
messy=pd.DataFrame(new,columns=['Box','Dimension','Value'])
tidy=messy.pivot_table(index=['Box'],columns='Dimension',values='Value').reset_index()
tidy['Volume'] = tidy.Length*tidy.Height*tidy.Width