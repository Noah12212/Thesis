#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PQRE Simulation

@author: noahmeyer
"""

import sys
import pandas as pd
import numpy as np
import pygambit as gam
import sympy
import time
import mpmath


#Set directory

PATH = '/Users/noahmeyer/Desktop/Masters/Thesis/new folder real/OKHERE/Python 2.0/'
sys.path.append(PATH)



def PQRE(B, Q, n):  
    """
    First it calculated the respective payoffs for a Tullock contest form 2-6 players. B is the payoff, Q is the endowment, n is number of players. 
    
    Then multiplies utilities depending on probability of getting there from other players, eg, for 1,1 multiply by q_1. for 1,1,2 multiply by q_1*q_2
    
    Solve equations using sympy nsolve. Guess of new solution of next lambda is based on previsous one, starting at lambda=0
    
    Final data shows in Data2, Data3, ect. where number represents n. This data is then exported and graphed in Glueviz
    
    Also records time spent for simulations
    
    """
    # NOTE: n=2 is well anotated, the others are the same as n=2 but with more players
    
    # Recording startimes
    STW = time.time()
    STP = time.process_time()
    
    
    global eq0
    global eq1
    global eq2
    global eq3
    global eq4
    global eq5
    global eq6
    global eq7
    
    global eq0s
    global eq1s
    global eq2s
    global eq3s
    global eq4s
    global eq5s
    global eq6s
    global eq7s
    
    global q0
    global q1
    global q2
    global q3
    global q4
    global q5
    global q6
    global q7

    global results2
    if n==2:
        global df_1
        df_1=pd.DataFrame(columns = ['Strat_1','Strat_2','Util_1', 'Util_2'])
        
        # This is to calculate payoffs in pure strategies
        
        for i in range(Q+1):
            for a in range(Q+1):
                if i<1 and a<1:
                    x=Q
                    y=Q
                else:
                    x = (Q-i+B*i/(i+a))
                    y = (Q-a+B*a/(i+a))
                P1 = x
                P2 = y
                df_1=df_1.append({'Strat_1': i ,'Strat_2': a ,'Util_1' : P1 , 'Util_2' : P2 }, ignore_index=True)
        df_1
        
        # Recording starttime once the payoffs have been calculated
        STW_ = time.time()
        STP_ = time.process_time()
        
        q0 = sympy.Symbol('q0')
        q1 = sympy.Symbol('q1')
        q2 = sympy.Symbol('q2')
        q3 = sympy.Symbol('q3')
        q4 = sympy.Symbol('q4')
        q5 = sympy.Symbol('q5')
        q6 = sympy.Symbol('q6')
        
        # Multiplies payoffs by probability of arriving there
        df_1.loc[df_1.Strat_2==0,'Util_1':]*=q0
        df_1.loc[df_1.Strat_2==1,'Util_1':]*=q1
        df_1.loc[df_1.Strat_2==2,'Util_1':]*=q2
        df_1.loc[df_1.Strat_2==3,'Util_1':]*=q3
        df_1.loc[df_1.Strat_2==4,'Util_1':]*=q4
        df_1.loc[df_1.Strat_2==5,'Util_1':]*=q5
        df_1.loc[df_1.Strat_2==6,'Util_1':]*=q6
        
        
        # Sums up by strategy to get expected payoffs for each strategy 
        eq0 = df_1.loc[df_1.Strat_1==0].sum()
        eq1 = df_1.loc[df_1.Strat_1==1].sum()
        eq2 = df_1.loc[df_1.Strat_1==2].sum()
        eq3 = df_1.loc[df_1.Strat_1==3].sum()
        eq4 = df_1.loc[df_1.Strat_1==4].sum()
        eq5 = df_1.loc[df_1.Strat_1==5].sum()
        eq6 = df_1.loc[df_1.Strat_1==6].sum()

        global Data2
        # I chose I want to solve for all these λ based on the data from the Gambit LQRE, I added λ=150 at the end as λ=100 was not large enough to properly show convergence in all cases
        fordata = pd.DataFrame({'λ': [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1.25,1.5,1.75,2,2.5,3,3.5,4,5,6,7,8,9,10,15,20,25,35,50,75,100,150]})
        Data2=pd.DataFrame(columns = [''])
        # I am now adding κ as a variable for the initial guess at lambda=0 for future guesses we use previous results of solve, we later use previous results as next guess
        κ = (1/7, 1/7, 1/7, 1/7, 1/7, 1/7, 1/7)
        for λ in [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1.25,1.5,1.75,2,2.5,3,3.5,4,5,6,7,8,9,10,15,20,25,35,50,75,100,150]:
            # This is just the formula for power quantal response equilibrium, seen in Equation (3) in Paper
            eqbase = ((eq0.loc[['Util_1']].iloc[0]**λ)+(eq1.loc[['Util_1']].iloc[0]**λ)+(eq2.loc[['Util_1']].iloc[0]**λ)+(eq3.loc[['Util_1']].iloc[0]**λ)++((eq4.loc[['Util_1']]).iloc[0]**λ)+(eq5.loc[['Util_1']].iloc[0]**λ)+(eq6.loc[['Util_1']].iloc[0]**λ))
            eq0s=(((eq0.loc[['Util_1']]**λ))/eqbase)-q0
            eq1s=(((eq1.loc[['Util_1']]**λ))/eqbase)-q1
            eq2s=(((eq2.loc[['Util_1']]**λ))/eqbase)-q2
            eq3s=(((eq3.loc[['Util_1']]**λ))/eqbase)-q3
            eq4s=(((eq4.loc[['Util_1']]**λ))/eqbase)-q4
            eq5s=(((eq5.loc[['Util_1']]**λ))/eqbase)-q5
            eq6s=(((eq6.loc[['Util_1']]**λ))/eqbase)-q6
            
            κ = sympy.nsolve((eq0s, eq1s, eq2s, eq3s, eq4s, eq5s,eq6s),(q0,q1,q2,q3,q4,q5,q6),(κ))
            
            Data2 = Data2.append({'Outputs': list(κ)}, ignore_index=True)
            
            
        Data2['λ'] = fordata
        
        Data2[['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6']] = pd.DataFrame(Data2.Outputs.tolist(), index = Data2.index)
        
        
        
        PRes = []
        # I add a loop to calculate expected investment by multiplying each strategy probability with the investment at that probability
        for abcd in range(33):
            efgh = ((Data2['q0'][abcd] * 0 + Data2['q1'][abcd] * 1 + Data2['q2'][abcd] * 2 + Data2['q3'][abcd] * 3 + Data2['q4'][abcd] * 4 + Data2['q5'][abcd] * 5 + Data2['q6'][abcd] * 6))
            
            PRes.append(efgh)

        Data2['2PRes'] = PRes
        
        Data2['2PResT'] = Data2['2PRes']*2
        
        # Get final time for the calculation of PQRE
        ETW = time.time()
        ETP = time.process_time()
        
        Data2['Wall time'] = ETW - STW
        
        Data2['Process time'] = ETP - STP
        
        Data2['Wall time sim'] = ETW - STW_
        
        Data2['Process time sim'] = ETP - STP_
        
        
        
    elif n==3:
        global df_2
        df_2=pd.DataFrame(columns = ['Strat_1','Strat_2', 'Strat_3', 'Util_1', 'Util_2', 'Util_3'])
        for i in range(Q+1):
            for a in range(Q+1):
                for j in range(Q+1):
                    if i<1 and a<1 and j<1:
                        x=Q
                        y=Q
                        z=Q
                    else:
                        x = (Q-i+B*i/(i+a+j))
                        y = (Q-a+B*a/(i+a+j))
                        z = (Q-j+B*j/(i+a+j))
                    P1 = x
                    P2 = y
                    P3 = z
                    df_2=df_2.append({'Strat_1': i ,'Strat_2': a , 'Strat_3' : j ,'Util_1' : P1 , 'Util_2' : P2 ,'Util_3' : P3}, ignore_index=True)
        df_2
        
        STW_ = time.time()
        STP_ = time.process_time()
        
        
        q0 = sympy.Symbol('q0')
        q1 = sympy.Symbol('q1')
        q2 = sympy.Symbol('q2')
        q3 = sympy.Symbol('q3')
        q4 = sympy.Symbol('q4')
        q5 = sympy.Symbol('q5')
        q6 = sympy.Symbol('q6')
        
        
        df_2.loc[df_2.Strat_2==0,'Util_1':]*=q0
        df_2.loc[df_2.Strat_2==1,'Util_1':]*=q1
        df_2.loc[df_2.Strat_2==2,'Util_1':]*=q2
        df_2.loc[df_2.Strat_2==3,'Util_1':]*=q3
        df_2.loc[df_2.Strat_2==4,'Util_1':]*=q4
        df_2.loc[df_2.Strat_2==5,'Util_1':]*=q5
        df_2.loc[df_2.Strat_2==6,'Util_1':]*=q6
        
        
        df_2.loc[df_2.Strat_3==0,'Util_1':]*=q0
        df_2.loc[df_2.Strat_3==1,'Util_1':]*=q1
        df_2.loc[df_2.Strat_3==2,'Util_1':]*=q2
        df_2.loc[df_2.Strat_3==3,'Util_1':]*=q3
        df_2.loc[df_2.Strat_3==4,'Util_1':]*=q4
        df_2.loc[df_2.Strat_3==5,'Util_1':]*=q5
        df_2.loc[df_2.Strat_3==6,'Util_1':]*=q6
        
        
        eq0 = df_2.loc[df_2.Strat_1==0].sum()
        eq1 = df_2.loc[df_2.Strat_1==1].sum()
        eq2 = df_2.loc[df_2.Strat_1==2].sum()
        eq3 = df_2.loc[df_2.Strat_1==3].sum()
        eq4 = df_2.loc[df_2.Strat_1==4].sum()
        eq5 = df_2.loc[df_2.Strat_1==5].sum()
        eq6 = df_2.loc[df_2.Strat_1==6].sum()
        eq7 = q0 + q1 + q2 + q3 + q4 + q5 +q6
        
        global Data3
        fordata = pd.DataFrame({'λ': [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1.25,1.5,1.75,2,2.5,3,3.5,4,5,6,7,8,9,10,15,20,25,35,50,75,100,150]})
        Data3=pd.DataFrame(columns = [''])
        # I am now adding κ as a variable for the initial guess at lambda=0 for future guesses we use previous results of solve
        κ = 1/7, 1/7, 1/7, 1/7, 1/7, 1/7, 1/7
        for λ in [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1.25,1.5,1.75,2,2.5,3,3.5,4,5,6,7,8,9,10,15,20,25,35,50,75,100,150]:
            eqbase = (eq0.loc[['Util_1']].iloc[0]**λ+eq1.loc[['Util_1']].iloc[0]**λ+eq2.loc[['Util_1']].iloc[0]**λ+eq3.loc[['Util_1']].iloc[0]**λ+eq4.loc[['Util_1']].iloc[0]**λ+eq5.loc[['Util_1']].iloc[0]**λ+eq6.loc[['Util_1']].iloc[0]**λ)
            eq0s=((eq0.loc[['Util_1']].iloc[0]**λ)/eqbase)-q0
            eq1s=((eq1.loc[['Util_1']].iloc[0]**λ)/eqbase)-q1
            eq2s=((eq2.loc[['Util_1']].iloc[0]**λ)/eqbase)-q2
            eq3s=((eq3.loc[['Util_1']].iloc[0]**λ)/eqbase)-q3
            eq4s=((eq4.loc[['Util_1']].iloc[0]**λ)/eqbase)-q4
            eq5s=((eq5.loc[['Util_1']].iloc[0]**λ)/eqbase)-q5
            eq6s=((eq6.loc[['Util_1']].iloc[0]**λ)/eqbase)-q6
            eq7s=eq7-1
            
            κ = sympy.nsolve((eq0s, eq1s, eq2s, eq3s, eq4s, eq5s,eq6s),(q0,q1,q2,q3,q4,q5,q6),(κ))
            
            Data3 = Data3.append({'Outputs': list(κ)}, ignore_index=True)
            
        Data3['λ'] = fordata
        
        
        Data3[['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6']] = pd.DataFrame(Data3.Outputs.tolist(), index = Data3.index)
        
        
        
        
        
        PRes = []
        
        for abcd in range(33):
            efgh = ((Data3['q0'][abcd] * 0 + Data3['q1'][abcd] * 1 + Data3['q2'][abcd] * 2 + Data3['q3'][abcd] * 3 + Data3['q4'][abcd] * 4 + Data3['q5'][abcd] * 5 + Data3['q6'][abcd] * 6))
            
            PRes.append(efgh)

        Data3['3PRes'] = PRes
        
        Data3['3PResT'] = Data3['3PRes']*3
        
        ETW = time.time()
        ETP = time.process_time()
        
        Data3['Wall time'] = ETW - STW
        
        Data3['Process time'] = ETP - STP
        
        Data3['Wall time sim'] = ETW - STW_
        
        Data3['Process time sim'] = ETP - STP_


    elif n==4:
        global df_3
        df_3=pd.DataFrame(columns = ['Strat_1','Strat_2', 'Strat_3', 'Strat_4', 'Util_1', 'Util_2', 'Util_3', 'Util_4'])
        for i in range(Q+1):
            for a in range(Q+1):
                for j in range(Q+1):
                    for jk in range(Q+1):
                        if i<1 and a<1 and j<1 and jk<1:
                            x=Q
                            y=Q
                            z=Q
                            uz=Q
                        else:
                            x = (Q-i+B*i/(i+a+j+jk))
                            y = (Q-a+B*a/(i+a+j+jk))
                            z = (Q-j+B*j/(i+a+j+jk))
                            uz = (Q-jk+B*jk/(i+a+j+jk))
                        P1 = x
                        P2 = y
                        P3 = z
                        P4 = uz
                        df_3=df_3.append({'Strat_1': i ,'Strat_2': a , 'Strat_3' : j , 'Strat_4' : jk , 'Util_1' : P1 , 'Util_2' : P2 ,'Util_3' : P3, 'Util_4' : P4}, ignore_index=True)
        df_3
        
        STW_ = time.time()
        STP_ = time.process_time()
        
                
        q0 = sympy.Symbol('q0')
        q1 = sympy.Symbol('q1')
        q2 = sympy.Symbol('q2')
        q3 = sympy.Symbol('q3')
        q4 = sympy.Symbol('q4')
        q5 = sympy.Symbol('q5')
        q6 = sympy.Symbol('q6')

        
        df_3.loc[df_3.Strat_2==0,'Util_1':]*=q0
        df_3.loc[df_3.Strat_2==1,'Util_1':]*=q1
        df_3.loc[df_3.Strat_2==2,'Util_1':]*=q2
        df_3.loc[df_3.Strat_2==3,'Util_1':]*=q3
        df_3.loc[df_3.Strat_2==4,'Util_1':]*=q4
        df_3.loc[df_3.Strat_2==5,'Util_1':]*=q5
        df_3.loc[df_3.Strat_2==6,'Util_1':]*=q6
        
        
        df_3.loc[df_3.Strat_3==0,'Util_1':]*=q0
        df_3.loc[df_3.Strat_3==1,'Util_1':]*=q1
        df_3.loc[df_3.Strat_3==2,'Util_1':]*=q2
        df_3.loc[df_3.Strat_3==3,'Util_1':]*=q3
        df_3.loc[df_3.Strat_3==4,'Util_1':]*=q4
        df_3.loc[df_3.Strat_3==5,'Util_1':]*=q5
        df_3.loc[df_3.Strat_3==6,'Util_1':]*=q6
        
        df_3.loc[df_3.Strat_4==0,'Util_1':]*=q0
        df_3.loc[df_3.Strat_4==1,'Util_1':]*=q1
        df_3.loc[df_3.Strat_4==2,'Util_1':]*=q2
        df_3.loc[df_3.Strat_4==3,'Util_1':]*=q3
        df_3.loc[df_3.Strat_4==4,'Util_1':]*=q4
        df_3.loc[df_3.Strat_4==5,'Util_1':]*=q5
        df_3.loc[df_3.Strat_4==6,'Util_1':]*=q6
        
        
        eq0 = df_3.loc[df_3.Strat_1==0].sum()
        eq1 = df_3.loc[df_3.Strat_1==1].sum()
        eq2 = df_3.loc[df_3.Strat_1==2].sum()
        eq3 = df_3.loc[df_3.Strat_1==3].sum()
        eq4 = df_3.loc[df_3.Strat_1==4].sum()
        eq5 = df_3.loc[df_3.Strat_1==5].sum()
        eq6 = df_3.loc[df_3.Strat_1==6].sum()
        eq7 = q0 + q1 + q2 + q3 + q4 + q5 +q6
        
        global Data4
        fordata = pd.DataFrame({'λ': [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1.25,1.5,1.75,2,2.5,3,3.5,4,5,6,7,8,9,10,15,20,25,35,50,75,100,150]})
        Data4=pd.DataFrame(columns = [''])
        # I am now adding κ as a variable for the initial guess at lambda=0 for future guesses we use previous results of solve
        κ = 1/7, 1/7, 1/7, 1/7, 1/7, 1/7, 1/7
        for λ in [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1.25,1.5,1.75,2,2.5,3,3.5,4,5,6,7,8,9,10,15,20,25,35,50,75,100,150]:
            eqbase = (eq0.loc[['Util_1']].iloc[0]**λ+eq1.loc[['Util_1']].iloc[0]**λ+eq2.loc[['Util_1']].iloc[0]**λ+eq3.loc[['Util_1']].iloc[0]**λ+eq4.loc[['Util_1']].iloc[0]**λ+eq5.loc[['Util_1']].iloc[0]**λ+eq6.loc[['Util_1']].iloc[0]**λ)
            eq0s=((eq0.loc[['Util_1']].iloc[0]**λ)/eqbase)-q0
            eq1s=((eq1.loc[['Util_1']].iloc[0]**λ)/eqbase)-q1
            eq2s=((eq2.loc[['Util_1']].iloc[0]**λ)/eqbase)-q2
            eq3s=((eq3.loc[['Util_1']].iloc[0]**λ)/eqbase)-q3
            eq4s=((eq4.loc[['Util_1']].iloc[0]**λ)/eqbase)-q4
            eq5s=((eq5.loc[['Util_1']].iloc[0]**λ)/eqbase)-q5
            eq6s=((eq6.loc[['Util_1']].iloc[0]**λ)/eqbase)-q6
            eq7s=eq7-1
            
            κ = sympy.nsolve((eq0s, eq1s, eq2s, eq3s, eq4s, eq5s,eq6s),(q0,q1,q2,q3,q4,q5,q6),(κ))
            
            Data4 = Data4.append({'Outputs': list(κ)}, ignore_index=True)
            
        Data4['λ'] = fordata
        
        Data4[['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6']] = pd.DataFrame(Data4.Outputs.tolist(), index = Data4.index)

        
        
        
        PRes = []
        
        for abcd in range(33):
            efgh = ((Data4['q0'][abcd] * 0 + Data4['q1'][abcd] * 1 + Data4['q2'][abcd] * 2 + Data4['q3'][abcd] * 3 + Data4['q4'][abcd] * 4 + Data4['q5'][abcd] * 5 + Data4['q6'][abcd] * 6))
            
            PRes.append(efgh)

        Data4['4PRes'] = PRes
        
        Data4['4PResT'] = Data4['4PRes']*4
                
        ETW = time.time()
        ETP = time.process_time()
        
        Data4['Wall time'] = ETW - STW
        
        Data4['Process time'] = ETP - STP
        
        Data4['Wall time sim'] = ETW - STW_
        
        Data4['Process time sim'] = ETP - STP_
        

    elif n==5:
        global df_4
        df_4=pd.DataFrame(columns = ['Strat_1','Strat_2', 'Strat_3', 'Strat_4', 'Strat_5' ,'Util_1', 'Util_2', 'Util_3', 'Util_4', 'Util_5'])
        for i in range(Q+1):
            for a in range(Q+1):
                for j in range(Q+1):
                    for jk in range(Q+1):
                        for fk in range(Q+1):
                            if i<1 and a<1 and j<1 and jk<1 and fk<Q+1:
                                x=Q
                                y=Q
                                z=Q
                                uz=Q
                                kz=Q
                            else:
                                x = (Q-i+B*i/(i+a+j+jk+fk))
                                y = (Q-a+B*a/(i+a+j+jk+fk))
                                z = (Q-j+B*j/(i+a+j+jk+fk))
                                uz = (Q-jk+B*jk/(i+a+j+jk+fk))
                                kz=(Q-fk+B*fk/(i+a+j+jk+fk))
                            P1 = x
                            P2 = y
                            P3 = z
                            P4 = uz
                            P5 = kz
                            df_4=df_4.append({'Strat_1': i ,'Strat_2': a , 'Strat_3' : j , 'Strat_4' : jk , 'Strat_5' : fk ,'Util_1' : P1 , 'Util_2' : P2 ,'Util_3' : P3, 'Util_4' : P4, 'Util_5' : P5}, ignore_index=True)
        df_4
        
        STW_ = time.time()
        STP_ = time.process_time()
        
        
        q0 = sympy.Symbol('q0')
        q1 = sympy.Symbol('q1')
        q2 = sympy.Symbol('q2')
        q3 = sympy.Symbol('q3')
        q4 = sympy.Symbol('q4')
        q5 = sympy.Symbol('q5')
        q6 = sympy.Symbol('q6')
        
        
        df_4.loc[df_4.Strat_2==0,'Util_1':]*=q0
        df_4.loc[df_4.Strat_2==1,'Util_1':]*=q1
        df_4.loc[df_4.Strat_2==2,'Util_1':]*=q2
        df_4.loc[df_4.Strat_2==3,'Util_1':]*=q3
        df_4.loc[df_4.Strat_2==4,'Util_1':]*=q4
        df_4.loc[df_4.Strat_2==5,'Util_1':]*=q5
        df_4.loc[df_4.Strat_2==6,'Util_1':]*=q6
        
        
        df_4.loc[df_4.Strat_3==0,'Util_1':]*=q0
        df_4.loc[df_4.Strat_3==1,'Util_1':]*=q1
        df_4.loc[df_4.Strat_3==2,'Util_1':]*=q2
        df_4.loc[df_4.Strat_3==3,'Util_1':]*=q3
        df_4.loc[df_4.Strat_3==4,'Util_1':]*=q4
        df_4.loc[df_4.Strat_3==5,'Util_1':]*=q5
        df_4.loc[df_4.Strat_3==6,'Util_1':]*=q6
        
        df_4.loc[df_4.Strat_4==0,'Util_1':]*=q0
        df_4.loc[df_4.Strat_4==1,'Util_1':]*=q1
        df_4.loc[df_4.Strat_4==2,'Util_1':]*=q2
        df_4.loc[df_4.Strat_4==3,'Util_1':]*=q3
        df_4.loc[df_4.Strat_4==4,'Util_1':]*=q4
        df_4.loc[df_4.Strat_4==5,'Util_1':]*=q5
        df_4.loc[df_4.Strat_4==6,'Util_1':]*=q6
        
        
        df_4.loc[df_4.Strat_5==0,'Util_1':]*=q0
        df_4.loc[df_4.Strat_5==1,'Util_1':]*=q1
        df_4.loc[df_4.Strat_5==2,'Util_1':]*=q2
        df_4.loc[df_4.Strat_5==3,'Util_1':]*=q3
        df_4.loc[df_4.Strat_5==4,'Util_1':]*=q4
        df_4.loc[df_4.Strat_5==5,'Util_1':]*=q5
        df_4.loc[df_4.Strat_5==6,'Util_1':]*=q6
        
        
        eq0 = df_4.loc[df_4.Strat_1==0].sum()
        eq1 = df_4.loc[df_4.Strat_1==1].sum()
        eq2 = df_4.loc[df_4.Strat_1==2].sum()
        eq3 = df_4.loc[df_4.Strat_1==3].sum()
        eq4 = df_4.loc[df_4.Strat_1==4].sum()
        eq5 = df_4.loc[df_4.Strat_1==5].sum()
        eq6 = df_4.loc[df_4.Strat_1==6].sum()
        eq7 = q0 + q1 + q2 + q3 + q4 + q5 +q6
        
        global Data5
        fordata = pd.DataFrame({'λ': [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1.25,1.5,1.75,2,2.5,3,3.5,4,5,6,7,8,9,10,15,20,25,35,50,75,100,150]})
        Data5=pd.DataFrame(columns = [''])
        # I am now adding κ as a variable for the initial guess at lambda=0 for future guesses we use previous results of solve
        κ = 1/7, 1/7, 1/7, 1/7, 1/7, 1/7, 1/7
        for λ in [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1.25,1.5,1.75,2,2.5,3,3.5,4,5,6,7,8,9,10,15,20,25,35,50,75,100,150]:
            eqbase = (eq0.loc[['Util_1']].iloc[0]**λ+eq1.loc[['Util_1']].iloc[0]**λ+eq2.loc[['Util_1']].iloc[0]**λ+eq3.loc[['Util_1']].iloc[0]**λ+eq4.loc[['Util_1']].iloc[0]**λ+eq5.loc[['Util_1']].iloc[0]**λ+eq6.loc[['Util_1']].iloc[0]**λ)
            eq0s=((eq0.loc[['Util_1']].iloc[0]**λ)/eqbase)-q0
            eq1s=((eq1.loc[['Util_1']].iloc[0]**λ)/eqbase)-q1
            eq2s=((eq2.loc[['Util_1']].iloc[0]**λ)/eqbase)-q2
            eq3s=((eq3.loc[['Util_1']].iloc[0]**λ)/eqbase)-q3
            eq4s=((eq4.loc[['Util_1']].iloc[0]**λ)/eqbase)-q4
            eq5s=((eq5.loc[['Util_1']].iloc[0]**λ)/eqbase)-q5
            eq6s=((eq6.loc[['Util_1']].iloc[0]**λ)/eqbase)-q6
            eq7s=eq7-1
            
            κ = sympy.nsolve((eq0s, eq1s, eq2s, eq3s, eq4s, eq5s,eq6s),(q0,q1,q2,q3,q4,q5,q6),(κ))
            
            Data5 = Data5.append({'Outputs': list(κ)}, ignore_index=True)
            
        Data5['λ'] = fordata
        
        Data5[['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6']] = pd.DataFrame(Data5.Outputs.tolist(), index = Data5.index)

       
        
        
        PRes = []
        
        for abcd in range(33):
            efgh = ((Data5['q0'][abcd] * 0 + Data5['q1'][abcd] * 1 + Data5['q2'][abcd] * 2 + Data5['q3'][abcd] * 3 + Data5['q4'][abcd] * 4 + Data5['q5'][abcd] * 5 + Data5['q6'][abcd] * 6))
            
            PRes.append(efgh)

        Data5['5PRes'] = PRes
        
        
        Data5['5PResT'] = Data5['5PRes']*5
        
                
        ETW = time.time()
        ETP = time.process_time()
        
        Data5['Wall time'] = ETW - STW
        
        Data5['Process time'] = ETP - STP
        
        Data5['Wall time sim'] = ETW - STW_
        
        Data5['Process time sim'] = ETP - STP_
        

    elif n==6:
        global df_5
        df_5=pd.DataFrame(columns = ['Strat_1','Strat_2', 'Strat_3', 'Strat_4', 'Strat_5' , 'Strat_6' ,'Util_1', 'Util_2', 'Util_3', 'Util_4', 'Util_5', 'Util_6'])
        for i in range(Q+1):
            for a in range(Q+1):
                for j in range(Q+1):
                    for jk in range(Q+1):
                        for fk in range(Q+1):
                            for gh in range(Q+1):
                                if i<1 and a<1 and j<1 and jk<1 and fk<1 and gh<1:
                                    x=Q
                                    y=Q
                                    z=Q
                                    uz=Q
                                    kz=Q
                                    gz=Q
                                else:
                                    x = (Q-i+B*i/(i+a+j+jk+fk+gh))
                                    y = (Q-a+B*a/(i+a+j+jk+fk+gh))
                                    z = (Q-j+B*j/(i+a+j+jk+fk+gh))
                                    uz = (Q-jk+B*jk/(i+a+j+jk+fk+gh))
                                    kz=(Q-fk+B*fk/(i+a+j+jk+fk+gh))
                                    gz=(Q-gh+B*gh/(i+a+j+jk+fk+gh))
                                P1 = x
                                P2 = y
                                P3 = z
                                P4 = uz
                                P5 = kz
                                P6 = gz
                                df_5=df_5.append({'Strat_1': i ,'Strat_2': a , 'Strat_3' : j , 'Strat_4' : jk , 'Strat_5' : fk , 'Strat_6' : gh , 'Util_1' : P1 , 'Util_2' : P2 ,'Util_3' : P3, 'Util_4' : P4, 'Util_5' : P5, 'Util_6' : P6}, ignore_index=True)
        df_5
                  
        
        STW_ = time.time()
        STP_ = time.process_time()
        
        q0 = sympy.Symbol('q0')
        q1 = sympy.Symbol('q1')
        q2 = sympy.Symbol('q2')
        q3 = sympy.Symbol('q3')
        q4 = sympy.Symbol('q4')
        q5 = sympy.Symbol('q5')
        q6 = sympy.Symbol('q6')
        
        
        df_5.loc[df_5.Strat_2==0,'Util_1':]*=q0
        df_5.loc[df_5.Strat_2==1,'Util_1':]*=q1
        df_5.loc[df_5.Strat_2==2,'Util_1':]*=q2
        df_5.loc[df_5.Strat_2==3,'Util_1':]*=q3
        df_5.loc[df_5.Strat_2==4,'Util_1':]*=q4
        df_5.loc[df_5.Strat_2==5,'Util_1':]*=q5
        df_5.loc[df_5.Strat_2==6,'Util_1':]*=q6
        
        
        df_5.loc[df_5.Strat_3==0,'Util_1':]*=q0
        df_5.loc[df_5.Strat_3==1,'Util_1':]*=q1
        df_5.loc[df_5.Strat_3==2,'Util_1':]*=q2
        df_5.loc[df_5.Strat_3==3,'Util_1':]*=q3
        df_5.loc[df_5.Strat_3==4,'Util_1':]*=q4
        df_5.loc[df_5.Strat_3==5,'Util_1':]*=q5
        df_5.loc[df_5.Strat_3==6,'Util_1':]*=q6
        
        df_5.loc[df_5.Strat_4==0,'Util_1':]*=q0
        df_5.loc[df_5.Strat_4==1,'Util_1':]*=q1
        df_5.loc[df_5.Strat_4==2,'Util_1':]*=q2
        df_5.loc[df_5.Strat_4==3,'Util_1':]*=q3
        df_5.loc[df_5.Strat_4==4,'Util_1':]*=q4
        df_5.loc[df_5.Strat_4==5,'Util_1':]*=q5
        df_5.loc[df_5.Strat_4==6,'Util_1':]*=q6
        
        
        df_5.loc[df_5.Strat_5==0,'Util_1':]*=q0
        df_5.loc[df_5.Strat_5==1,'Util_1':]*=q1
        df_5.loc[df_5.Strat_5==2,'Util_1':]*=q2
        df_5.loc[df_5.Strat_5==3,'Util_1':]*=q3
        df_5.loc[df_5.Strat_5==4,'Util_1':]*=q4
        df_5.loc[df_5.Strat_5==5,'Util_1':]*=q5
        df_5.loc[df_5.Strat_5==6,'Util_1':]*=q6
        
        df_5.loc[df_5.Strat_5==0,'Util_1':]*=q0
        df_5.loc[df_5.Strat_5==1,'Util_1':]*=q1
        df_5.loc[df_5.Strat_5==2,'Util_1':]*=q2
        df_5.loc[df_5.Strat_5==3,'Util_1':]*=q3
        df_5.loc[df_5.Strat_5==4,'Util_1':]*=q4
        df_5.loc[df_5.Strat_5==5,'Util_1':]*=q5
        df_5.loc[df_5.Strat_5==6,'Util_1':]*=q6
        
        
        eq0 = df_5.loc[df_5.Strat_1==0].sum()
        eq1 = df_5.loc[df_5.Strat_1==1].sum()
        eq2 = df_5.loc[df_5.Strat_1==2].sum()
        eq3 = df_5.loc[df_5.Strat_1==3].sum()
        eq4 = df_5.loc[df_5.Strat_1==4].sum()
        eq5 = df_5.loc[df_5.Strat_1==5].sum()
        eq6 = df_5.loc[df_5.Strat_1==6].sum()
        eq7 = q0 + q1 + q2 + q3 + q4 + q5 +q6
        
        global Data6
        fordata = pd.DataFrame({'λ': [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1.25,1.5,1.75,2,2.5,3,3.5,4,5,6,7,8,9,10,15,20,25,35,50,75,100,150]})
        Data6=pd.DataFrame(columns = [''])
        # I am now adding κ as a variable for the initial guess at lambda=0 for future guesses we use previous results of solve
        κ = 1/7, 1/7, 1/7, 1/7, 1/7, 1/7, 1/7
        for λ in [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1.25,1.5,1.75,2,2.5,3,3.5,4,5,6,7,8,9,10,15,20,25,35,50,75,100,150]:
            eqbase = (eq0.loc[['Util_1']].iloc[0]**λ+eq1.loc[['Util_1']].iloc[0]**λ+eq2.loc[['Util_1']].iloc[0]**λ+eq3.loc[['Util_1']].iloc[0]**λ+eq4.loc[['Util_1']].iloc[0]**λ+eq5.loc[['Util_1']].iloc[0]**λ+eq6.loc[['Util_1']].iloc[0]**λ)
            eq0s=((eq0.loc[['Util_1']].iloc[0]**λ)/eqbase)-q0
            eq1s=((eq1.loc[['Util_1']].iloc[0]**λ)/eqbase)-q1
            eq2s=((eq2.loc[['Util_1']].iloc[0]**λ)/eqbase)-q2
            eq3s=((eq3.loc[['Util_1']].iloc[0]**λ)/eqbase)-q3
            eq4s=((eq4.loc[['Util_1']].iloc[0]**λ)/eqbase)-q4
            eq5s=((eq5.loc[['Util_1']].iloc[0]**λ)/eqbase)-q5
            eq6s=((eq6.loc[['Util_1']].iloc[0]**λ)/eqbase)-q6
            eq7s=eq7-1
            
            κ = sympy.nsolve((eq0s, eq1s, eq2s, eq3s, eq4s, eq5s,eq6s),(q0,q1,q2,q3,q4,q5,q6),(κ))
            
            Data6 = Data6.append({'Outputs': list(κ)}, ignore_index=True)
            
        Data6['λ'] = fordata
        
        Data6[['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6']] = pd.DataFrame(Data6.Outputs.tolist(), index = Data6.index)

        
        
        PRes = []
        
        for abcd in range(33):
            efgh = ((Data6['q0'][abcd] * 0 + Data6['q1'][abcd] * 1 + Data6['q2'][abcd] * 2 + Data6['q3'][abcd] * 3 + Data6['q4'][abcd] * 4 + Data6['q5'][abcd] * 5 + Data6['q6'][abcd] * 6))
            
            PRes.append(efgh)

        Data6['6PRes'] = PRes


        Data6['6PResT'] = Data6['6PRes']*6
        
                
        ETW = time.time()
        ETP = time.process_time()
        
        Data6['Wall time'] = ETW - STW
        
        Data6['Process time'] = ETP - STP
        
        Data6['Wall time sim'] = ETW - STW_
        
        Data6['Process time sim'] = ETP - STP_

    else:
        print('n must be 1<n<7')
            

PQRE(16, 6, 2)

Data2.to_csv(PATH + '2 Players.csv', index = True)

PQRE(16, 6, 3)

Data3.to_csv(PATH + '3 Players.csv', index = True)

PQRE(16, 6, 4)

Data4.to_csv(PATH + '4 Players.csv', index = False)

PQRE(16, 6, 5)

Data5.to_csv(PATH + '5 Players.csv', index = False)

PQRE(16, 6, 6)

Data6.to_csv(PATH + '6 Players.csv', index = False)

PQRE(16, 6, 7)




