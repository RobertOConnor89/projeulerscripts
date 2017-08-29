# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 17:09:29 2016

@author: Jeff and Ashley

A program designed to find the integer below a certain value with the longest
repeating decimal expansion
"""

winner = 1 #place holder for the integer with greatest repeating reciprocal
max_count = 1 #place holder for the largest number of digits in the reciprocal
cycle = False
for i in range(1,1000): #loops through the desired range of integers
    count = 1 #counts length of decimal cycles
    rem = 10%i #remainder of division 10/i
    while cycle == True: #cycles through the first 20 digits in the reciprocal
        
    if (count > max_count):
        max_count = count
        winner = i

print "The winner is: ", i," with a cycle of length ", max_count

        