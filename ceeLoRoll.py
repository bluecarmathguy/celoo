# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 08:43:52 2017

@author: bob
"""
import nSidedDice as nsd
class ceeLoRoll:
    WINNER = 2;
    POINT  = 1;
    ROLL   = 0;
    LOSER  = -1; 
    NO_VALUE = -999;
    def __init__(self): 
        self.sides = 6;
        self.nDice = 3;
        self.dice =nsd.nSidedDice(self.sides,self.nDice);
        self.Point = -999;
        self.v = [-999,-999,-999]
        self.decision = ceeLoRoll.ROLL;
        self.isTriple = False;
    def roll(self):
        self.Point = -999;
        self.decision = ceeLoRoll.ROLL;
        self.isTriple = False; 
        self.dice.roll();
        self.v = self.dice.getValues();
        x = [0 for ii in range(self.sides)];
        for ii in self.v:
            x[ii-1] +=1;
        if (x[0] == 1 & x[1] == 1 & x[2] ==1):
            self.decision = ceeLoRoll.LOSER;
            return
        if (x[3] == 1 & x[4] == 1 & x[5] ==1):
            self.decision = ceeLoRoll.WINNER;
            return
        if  3 in x:
            self.isTriple = True;
            self.decision = ceeLoRoll.POINT;
            self.Point = x.index(3)+1;
            return
        if 2 in x:
            self.decision = ceeLoRoll.POINT;
            self.Point = x.index(1)+1;
            return
    def toString(self):
        if self.decision == ceeLoRoll.LOSER:
            outString = 'LOSER: [%d,%d,%d]'%(self.v[0],self.v[1],self.v[2])
        if self.decision == ceeLoRoll.WINNER:
            outString = 'WINNER: [%d,%d,%d]' % (self.v[0],self.v[1],self.v[2])            
        if self.decision == ceeLoRoll.POINT:            
            if self.isTriple:
                outString = 'Trips %d: [%d,%d,%d]' % (self.Point,self.v[0],self.v[1],self.v[2])                            
            else:
                outString = 'Point %d: [%d,%d,%d]' % (self.Point,self.v[0],self.v[1],self.v[2])            
        if self.decision == ceeLoRoll.ROLL:    
            outString = 'ROLL: [%d,%d,%d]' % (self.v[0],self.v[1],self.v[2])            
        return(outString)