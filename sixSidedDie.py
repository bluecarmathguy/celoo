# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 08:06:29 2017

@author: bob
"""
import random as rn
class sixSidedDie:
    def __init__(self):
        self.value = -999;
        self.sides = 6;
        self.isRolled = False;
    def roll(self):
        self.value = rn.randint(1,self.sides)
    def readDie(self):
        return(self.value);