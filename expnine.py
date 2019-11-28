# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 21:33:09 2019

@author: asus
"""
import pandas as pd

Math= {'Student':['Ice Bear','Panda','Grizzly'],'Math':[80,95,79]}
Elec= {'Student':['Ice Bear','Panda','Grizzly'],'Electronics':[85,81,83]}
GEAS= {'Student':['Ice Bear','Panda','Grizzly'],'GEAS':[90,79,93]}
ESAT= {'Student':['Ice Bear','Panda','Grizzly'],'ESAT':[93,89,88]}

m=pd.DataFrame(Math,columns=['Student','Math'])
el=pd.DataFrame(Elec,columns=['Student','Electronics'])
g=pd.DataFrame(GEAS,columns=['Student','GEAS'])
es=pd.DataFrame(ESAT,columns=['Student','ESAT'])
Gr = pd.merge(m, el ,how='left',on='Student')
Gra = pd.merge(g, es ,how='left',on='Student')
Grades = pd.merge(Gr, Gra ,how='left',on='Student')

long=pd.melt(Grades,id_vars='Student',value_vars=['Math','Electronics','GEAS','ESAT'])
