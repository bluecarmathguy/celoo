# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 12:25:06 2017

@author: apluser
"""

import ceeLoRoll as clr
class clrPlayer:
    def __init__(self):
        self.ceeLo = clr.ceeLoRoll();
    def go(self):
        self.ceeLo = clr.ceeLoRoll();
        while self.ceeLo.decision == clr.ceeLoRoll.ROLL:
             self.ceeLo.roll();
             print self.ceeLo.toString()