# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 12:14:48 2017

@author: bob
"""
import twoSixSiDiceRoll as tssdr

def playCraps():
    x = tssdr.twoSixSiDiceRoll();
    x.roll()
    s = x.getTotal();
    print x.toString()
    if (s == 7) or (s == 11):
        print "WINNER"
        return
    if (s==2) or (s==3) or (s==12):
        print "LOSER"
        return
    point = s
    keepRollin = True;
    while keepRollin:
        x.roll()
        s = x.getTotal();
        print "Point = ",
        print point,
        print x.toString()
        if s == point:
            print "Winner"
            return
        if s == 7:
            print "Out"
            break
if __name__ == '__main__':
    playCraps()
              