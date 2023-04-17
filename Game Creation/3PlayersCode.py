#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: noahmeyer
"""

import pandas as pd
import numpy as np
import pygambit as gam


#3 players

B=16
df_2=pd.DataFrame(columns = ['Util_1', 'Util_2', 'Util_3'])


for i in range(7):
    for a in range(7):
        for j in range(7):
            if i<1 and a<1 and j<1:
                x=6
                y=6
                z=6
            else:
                x = (6-i+B*i/(i+a+j))
                y = (6-a+B*a/(i+a+j))
                z = (6-j+B*j/(i+a+j))
            P1 = x
            P2 = y
            P3 = z
            df_2=df_2.append({'Util_1' : P1 , 'Util_2' : P2 ,'Util_3' : P3}, ignore_index=True)
df_2
       

array_1 = df_2['Util_1'].to_numpy()
array_2 = df_2['Util_2'].to_numpy()
array_3 = df_2['Util_3'].to_numpy()

a_1= array_1.reshape(7,7,7)
a_2= array_2.reshape(7,7,7)
a_3= array_3.reshape(7,7,7)

a_1 = a_1.astype(gam.Decimal)
a_2 = a_2.astype(gam.Decimal)
a_3 = a_3.astype(gam.Decimal)


# Code addapted from https://github.com/gambitproject/gambit/issues/267
an_1 = np.zeros((7,7,7), dtype=gam.Decimal)
for r in range(7):
    for c in range(7):
        for k in range(7):
            an_1[r][c][k] = gam.Decimal(a_1[r][c][k])

an_2 = np.zeros((7,7,7), dtype=gam.Decimal)
for r in range(7):
    for c in range(7):
        for k in range(7):
            an_2[r][c][k] = gam.Decimal(a_2[r][c][k])
            
an_3 = np.zeros((7,7,7), dtype=gam.Decimal)
for r in range(7):
    for c in range(7):
        for k in range(7):
            an_3[r][c][k] = gam.Decimal(a_3[r][c][k])
# Code addaption ends here


game_2 = gam.Game.from_arrays(an_1, an_2, an_3)
game_2.write()


#open text file
text_file = open("/Users/noahmeyer/Desktop/Masters/Thesis/new folder real/OKHERE/Python/G2", "w")
 
#write string to file
text_file.write(game_2.write())
 
#close file
text_file.close()


# Game is complete, from here I copy it onto the an empty gambit file and do QRE on app

  