# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 12:20:40 2017

@author: apluser
"""
import nSidedDice as nsd

class twoSixSiDiceRoll:
    def __init__(self):
        self.dice = nsd.nSidedDice(6,2);
        self.call = "";
        self.values = None;
    def roll(self):
        self.dice.roll()
        self.values = self.dice.getValues();
        self.values.sort()
        self.getCall();
    def getTotal(self):
        return(self.dice.getSum())
    def getCall(self):
        self.call = "Ooops";        
        if self.values is not None:
            if ((self.values[0] == 1) and (self.values[1] == 1)):
                self.call = "Snake Eyes";
            if ((self.values[0] == 1) and (self.values[1] == 2)):
                self.call = "Ace Duece";
            if ((self.values[0] == 1) and (self.values[1] == 3)):
                self.call = "Easy Four";
            if ((self.values[0] == 1) and (self.values[1] == 4)):
                self.call = "Fever Five";
            if ((self.values[0] == 1) and (self.values[1] == 5)):
                self.call = "Easy Six";
            if ((self.values[0] == 1) and (self.values[1] == 6)):
                self.call = "Seven Out";
            if ((self.values[0] == 2) and (self.values[1] == 2)):
                self.call = "Hard Four";
            if ((self.values[0] == 2) and (self.values[1] == 3)):
                self.call = "Fever Five";
            if ((self.values[0] == 2) and (self.values[1] == 4)):
                self.call = "Easy Six";
            if ((self.values[0] == 2) and (self.values[1] == 5)):
                self.call = "Seven Out";
            if ((self.values[0] == 2) and (self.values[1] == 6)):
                self.call = "Easy Eight";
            if ((self.values[0] == 3) and (self.values[1] == 3)):
                self.call = "Hard Six";
            if ((self.values[0] == 3) and (self.values[1] == 4)):
                self.call = "Seven Out";
            if ((self.values[0] == 3) and (self.values[1] == 5)):
                self.call = "Easy Eight";
            if ((self.values[0] == 3) and (self.values[1] == 6)):
                self.call = "Nina";
            if ((self.values[0] == 4) and (self.values[1] == 4)):
                self.call = "Hard Eight";
            if ((self.values[0] == 4) and (self.values[1] == 5)):
                self.call = "Nina";
            if ((self.values[0] == 4) and (self.values[1] == 6)):
                self.call = "Easy Ten";
            if ((self.values[0] == 5) and (self.values[1] == 5)):
                self.call = "Hard Ten";
            if ((self.values[0] == 5) and (self.values[1] == 6)):
                self.call = "Yo-leven";
            if ((self.values[0] == 6) and (self.values[1] == 6)):
                self.call = "Boxcars";
        else:
            self.call = "no roll";   
        return(self.call)              
    def toString(self):
        return('(%d,%d) %s'%(self.values[0],self.values[1],self.getCall()) )                 