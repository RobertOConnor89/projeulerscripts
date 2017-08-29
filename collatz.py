# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 18:01:29 2016

@author: Jeff and Ashley
"""

def collatz(number):
    if number%2 == 0:
        print number//2
        return number//2
    else:
        print number*3 + 1
        return number*3 + 1
     
print 'Please enter an integer: '

myNum = input()
try:
    myNum = int(myNum)    
            
    while(myNum != 1):
        myNum = collatz(myNum)
        
except NameError:
    print 'You did not enter an integer, dummy.'