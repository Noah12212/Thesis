#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: noahmeyer
"""
#Set directory

import sys
import pandas as pd
import matplotlib.pyplot as plt


#Set directory
PATH = '/Users/noahmeyer/Desktop/Masters/Thesis/new folder real/OKHERE/Python/Game files 2.0/'
sys.path.append(PATH)


# Import all the data from the gambit sofware
df_1 = pd.read_csv(PATH + 'Gambit QRE Output/G1 Data')

df_2 = pd.read_csv(PATH + 'Gambit QRE Output/G2 Data')

df_3 = pd.read_csv(PATH + 'Gambit QRE Output/G3 Data')

df_4 = pd.read_csv(PATH + 'Gambit QRE Output/G4 Data')

df_5 = pd.read_csv(PATH + 'Gambit QRE Output/G5 Data')

# The QRE data is symetric as the players are symetric, so it is sufficinet to only look at 1 players strategies
# First row in data represents the Lambda, then the represent strategies of players going in ascending order one after the other

#add back in the row that was intepreted as titles of rows

new_row = {'0.000000': 0, '0.142857':0.142857, '0.142857.1':0.142857, '0.142857.2':0.142857, '0.142857.3':0.142857, '0.142857.4':0.142857, '0.142857.5':0.142857}


df_1n=df_1.append(new_row, ignore_index=True)

df_2n=df_2.append(new_row, ignore_index=True)

df_3n=df_3.append(new_row, ignore_index=True)

df_4n=df_4.append(new_row, ignore_index=True)

df_5n=df_5.append(new_row, ignore_index=True)

# Get avg invested for each player

#2 Player case

df_1n['res1'] = df_1n['0.142857'] * 0 + df_1n['0.142857.1'] * 1 + df_1n['0.142857.2'] * 2 + df_1n['0.142857.3'] * 3 + df_1n['0.142857.4'] * 4 + df_1n['0.142857.5'] * 5 + df_1n['0.142857.6']*6 

ndf_1 = df_1n[['0.000000', 'res1']].copy()

#3 Player case

df_2n['res2'] = df_2n['0.142857'] * 0 + df_2n['0.142857.1'] * 1 + df_2n['0.142857.2'] * 2 + df_2n['0.142857.3'] * 3 + df_2n['0.142857.4'] * 4 + df_2n['0.142857.5'] * 5 + df_2n['0.142857.6']*6

ndf_2 = df_2n[['0.000000', 'res2']].copy()

#4 Player case

df_3n['res3'] = df_3n['0.142857'] * 0 + df_3n['0.142857.1'] * 1 + df_3n['0.142857.2'] * 2 + df_3n['0.142857.3'] * 3 + df_3n['0.142857.4'] * 4 + df_3n['0.142857.5'] * 5 + df_3n['0.142857.6']*6

ndf_3 = df_3n[['0.000000', 'res3']].copy()


#5 Player case

df_4n['res4'] = df_4n['0.142857'] * 0 + df_4n['0.142857.1'] * 1 + df_4n['0.142857.2'] * 2 + df_4n['0.142857.3'] * 3 + df_4n['0.142857.4'] * 4 + df_4n['0.142857.5'] * 5 + df_4n['0.142857.6']*6

ndf_4 = df_4n[['0.000000', 'res4']].copy()


#6 Player case

df_5n['res5'] = df_5n['0.142857'] * 0 + df_5n['0.142857.1'] * 1 + df_5n['0.142857.2'] * 2 + df_5n['0.142857.3'] * 3 + df_5n['0.142857.4'] * 4 + df_5n['0.142857.5'] * 5 + df_5n['0.142857.6']*6

ndf_5 = df_5n[['0.000000', 'res5']].copy()

# Get avg invested for each game (Just multiply avg per player by number of players)

ndf_1['sumRes1'] = ndf_1['res1']*2

ndf_2['sumRes2'] = ndf_2['res2']*3

ndf_3['sumRes3'] = ndf_3['res3']*4

ndf_4['sumRes4'] = ndf_4['res4']*5

ndf_5['sumRes5'] = ndf_5['res5']*6

final = pd.concat([ndf_1, ndf_2, ndf_3, ndf_4, ndf_5], axis = 0)


# I want csv files as I make graphs using Glueviz

final.to_csv(PATH + 'Final csv files for graphing/final.csv', index = False)

ndf_1.to_csv(PATH +'Final csv files for graphing/2 Players.csv', index = False)

ndf_2.to_csv(PATH +'Final csv files for graphing/3 Players.csv', index = False)

ndf_3.to_csv(PATH +'Final csv files for graphing/4 Players.csv', index = False)

ndf_4.to_csv(PATH +'Final csv files for graphing/5 Players.csv', index = False)

ndf_5.to_csv(PATH +'Final csv files for graphing/6 Players.csv', index = False)










