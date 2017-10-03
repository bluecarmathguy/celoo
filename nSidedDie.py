# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 08:26:54 2017

@author: bob
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 08:06:29 2017

@author: bob
"""
import random as rn
class nSidedDie:
    def __init__(self,s):
        self.value = -999;
        self.sides = s;
        self.isRolled = False;
    def roll(self):
        self.value = rn.randint(1,self.sides)
    def readDie(self):
        return(self.value);
    def getIsRolled(self):
        return(self.isRolled)