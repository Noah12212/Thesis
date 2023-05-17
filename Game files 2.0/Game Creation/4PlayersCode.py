#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: noahmeyer
"""

import pandas as pd
import numpy as np
import pygambit as gam
import sys

# Set Path
PATH = '/Users/noahmeyer/Desktop/Masters/Thesis/new folder real/OKHERE/Python/Game files 2.0/'
sys.path.append(PATH)


#4 players

B=16
df_3=pd.DataFrame(columns = ['Util_1', 'Util_2', 'Util_3', 'Util_4'])


for i in range(7):
    for a in range(7):
        for j in range(7):
            for jk in range(7):
                if i<1 and a<1 and j<1 and jk<1:
                    x=6
                    y=6
                    z=6
                    uz=6
                else:
                    x = (6-i+B*i/(i+a+j+jk))
                    y = (6-a+B*a/(i+a+j+jk))
                    z = (6-j+B*j/(i+a+j+jk))
                    uz = (6-jk+B*jk/(i+a+j+jk))
                P1 = x
                P2 = y
                P3 = z
                P4 = uz
                df_3=df_3.append({'Util_1' : P1 , 'Util_2' : P2 ,'Util_3' : P3, 'Util_4' : P4}, ignore_index=True)
df_3
       

array_1 = df_3['Util_1'].to_numpy()
array_2 = df_3['Util_2'].to_numpy()
array_3 = df_3['Util_3'].to_numpy()
array_4 = df_3['Util_4'].to_numpy()

a_1= array_1.reshape(7,7,7,7)
a_2= array_2.reshape(7,7,7,7)
a_3= array_3.reshape(7,7,7,7)
a_4= array_4.reshape(7,7,7,7)

a_1 = a_1.astype(gam.Decimal)
a_2 = a_2.astype(gam.Decimal)
a_3 = a_3.astype(gam.Decimal)
a_4 = a_4.astype(gam.Decimal)


# Code addapted from https://github.com/gambitproject/gambit/issues/267
an_1 = np.zeros((7,7,7,7), dtype=gam.Decimal)
for r in range(7):
    for c in range(7):
        for k in range(7):
            for we in range(7):
                an_1[r][c][k][we] = gam.Decimal(a_1[r][c][k][we])

an_2 = np.zeros((7,7,7,7), dtype=gam.Decimal)
for r in range(7):
    for c in range(7):
        for k in range(7):
            for we in range(7):
                an_2[r][c][k][we] = gam.Decimal(a_2[r][c][k][we])
            
an_3 = np.zeros((7,7,7,7), dtype=gam.Decimal)
for r in range(7):
    for c in range(7):
        for k in range(7):
            for we in range(7):
                an_3[r][c][k][we] = gam.Decimal(a_3[r][c][k][we])

an_4 = np.zeros((7,7,7,7), dtype=gam.Decimal)
for r in range(7):
    for c in range(7):
        for k in range(7):
            for we in range(7):
                an_4[r][c][k][we] = gam.Decimal(a_4[r][c][k][we])
# Code addaption ends here


game_2 = gam.Game.from_arrays(an_1, an_2, an_3, an_4)
game_2.write()


#open text file
text_file = open(PATH + "Game Creation Outputs/G3", "w")
 
#write string to file
text_file.write(game_2.write())
 
#close file
text_file.close()



  
