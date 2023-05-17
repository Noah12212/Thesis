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


#6 players

B=16
df_5=pd.DataFrame(columns = ['Util_1', 'Util_2', 'Util_3', 'Util_4', 'Util_5', 'Util_6'])


for i in range(7):
    for a in range(7):
        for j in range(7):
            for jk in range(7):
                for fk in range(7):
                    for gh in range(7):
                        if i<1 and a<1 and j<1 and jk<1 and fk<1 and gh<1:
                            x=6
                            y=6
                            z=6
                            uz=6
                            kz=6
                            gz=6
                        else:
                            x = (6-i+B*i/(i+a+j+jk+fk+gh))
                            y = (6-a+B*a/(i+a+j+jk+fk+gh))
                            z = (6-j+B*j/(i+a+j+jk+fk+gh))
                            uz = (6-jk+B*jk/(i+a+j+jk+fk+gh))
                            kz=(6-fk+B*fk/(i+a+j+jk+fk+gh))
                            gz=(6-gh+B*gh/(i+a+j+jk+fk+gh))
                        P1 = x
                        P2 = y
                        P3 = z
                        P4 = uz
                        P5 = kz
                        P6 = gz
                        df_5=df_5.append({'Util_1' : P1 , 'Util_2' : P2 ,'Util_3' : P3, 'Util_4' : P4, 'Util_5' : P5, 'Util_6' : P6}, ignore_index=True)
df_5
       

array_1 = df_5['Util_1'].to_numpy()
array_2 = df_5['Util_2'].to_numpy()
array_3 = df_5['Util_3'].to_numpy()
array_4 = df_5['Util_4'].to_numpy()
array_5 = df_5['Util_5'].to_numpy()
array_6 = df_5['Util_6'].to_numpy()

a_1= array_1.reshape(7,7,7,7,7,7)
a_2= array_2.reshape(7,7,7,7,7,7)
a_3= array_3.reshape(7,7,7,7,7,7)
a_4= array_4.reshape(7,7,7,7,7,7)
a_5= array_5.reshape(7,7,7,7,7,7)
a_6= array_6.reshape(7,7,7,7,7,7)

a_1 = a_1.astype(gam.Decimal)
a_2 = a_2.astype(gam.Decimal)
a_3 = a_3.astype(gam.Decimal)
a_4 = a_4.astype(gam.Decimal)
a_5 = a_5.astype(gam.Decimal)
a_6 = a_6.astype(gam.Decimal)


# Code addapted from https://github.com/gambitproject/gambit/issues/267
an_1 = np.zeros((7,7,7,7,7,7), dtype=gam.Decimal)
for r in range(7):
    for c in range(7):
        for k in range(7):
            for we in range(7):
                for tk in range (7):
                    for sd in range(7):
                        an_1[r][c][k][we][tk][sd] = gam.Decimal(a_1[r][c][k][we][tk][sd])

an_2 = np.zeros((7,7,7,7,7,7), dtype=gam.Decimal)
for r in range(7):
    for c in range(7):
        for k in range(7):
            for we in range(7):
                for tk in range (7):
                    for sd in range(7):
                        an_2[r][c][k][we][tk][sd] = gam.Decimal(a_2[r][c][k][we][tk][sd])

an_3 = np.zeros((7,7,7,7,7,7), dtype=gam.Decimal)
for r in range(7):
    for c in range(7):
        for k in range(7):
            for we in range(7):
                for tk in range (7):
                    for sd in range(7):
                        an_3[r][c][k][we][tk][sd] = gam.Decimal(a_3[r][c][k][we][tk][sd])

an_4 = np.zeros((7,7,7,7,7,7), dtype=gam.Decimal)
for r in range(7):
    for c in range(7):
        for k in range(7):
            for we in range(7):
                for tk in range (7):
                    for sd in range(7):
                        an_4[r][c][k][we][tk][sd] = gam.Decimal(a_4[r][c][k][we][tk][sd])

an_5 = np.zeros((7,7,7,7,7,7), dtype=gam.Decimal)
for r in range(7):
    for c in range(7):
        for k in range(7):
            for we in range(7):
                for tk in range (7):
                    for sd in range(7):
                        an_5[r][c][k][we][tk][sd] = gam.Decimal(a_5[r][c][k][we][tk][sd])

an_6 = np.zeros((7,7,7,7,7,7), dtype=gam.Decimal)
for r in range(7):
    for c in range(7):
        for k in range(7):
            for we in range(7):
                for tk in range (7):
                    for sd in range(7):
                        an_6[r][c][k][we][tk][sd] = gam.Decimal(a_6[r][c][k][we][tk][sd])

# Code addaption ends here


game_2 = gam.Game.from_arrays(an_1, an_2, an_3, an_4, an_5, an_6)
game_2.write()


#open text file
text_file = open(PATH + "Game Creation Outputs/G5", "w")
 
#write string to file
text_file.write(game_2.write())
 
#close file
text_file.close()




  
