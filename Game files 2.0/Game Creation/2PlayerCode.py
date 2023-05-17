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


#2 players
# I set Payoff to be 16, and endowment = 6
B=16
df_1=pd.DataFrame(columns = ['Util_1', 'Util_2'])


print(df_1)
# Calculate Payoffs
for i in range(7):
    for a in range(7):
        if i<1 and a<1:
            x=6
            y=6
        else:
            x = (6-i+B*i/(i+a))
            y = (6-a+B*a/(i+a))
        P1 = x
        P2 = y
        df_1=df_1.append({'Util_1' : P1 , 'Util_2' : P2 }, ignore_index=True)
df_1
# Make arrays from dataframes and then make proper matrixes
array_1 = df_1['Util_1'].to_numpy()
array_2 = df_1['Util_2'].to_numpy()

a_1= array_1.reshape(7,7)
a_2= array_2.reshape(7,7)

a_1 = a_1.astype(gam.Decimal)
a_2 = a_2.astype(gam.Decimal)

# The Gambit software wasn't accepted the answers due to too many decimal points, so I found this fix
# Code addapted from https://github.com/gambitproject/gambit/issues/257
an_1 = np.zeros((7,7), dtype=gam.Decimal)
for r in range(7):
    for c in range(7):
        an_1[r][c] = gam.Decimal(a_1[r][c])

an_2 = np.zeros((7,7), dtype=gam.Decimal)
for r in range(7):
    for c in range(7):
        an_2[r][c] = gam.Decimal(a_2[r][c])
# Code addaption ends here

# Create Gambit files
game_1 = gam.Game.from_arrays(an_1, an_2)
game_1.write()


#open text file
text_file = open(PATH + "Game Creation Outputs/G1", "w")
 
#write string to file
text_file.write(game_1.write())
 
#close file
text_file.close()



  