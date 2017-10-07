# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 08:28:55 2017

@author: bob
"""
import nSidedDie as nsd

class nSidedDice:
        def __init__(self,nSides,nDice):
            self.sides = nSides;
            self.N = nDice;
            self.dice = [nsd.nSidedDie(self.sides) for ii in range(self.N)];
        def roll(self):
            for ii in self.dice:
                ii.roll();
        def getValues(self):
            return([ii.readDie() for ii in self.dice])
        def getSum(self):
            f = lambda x,y: x+y
            return(reduce(f,self.getValues()))