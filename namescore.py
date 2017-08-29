# -*- coding: utf-8 -*-
"""
Read text file with strings separated by commas and compute a "namescore" for each string:

Read file objects into a list
sort list A-Z
sum positions of characters for each name and multiply by it's position in list
sum these values
"""
SUM = 0

TOTAL = 0

c = 0

TEXT = open('C:/Python27/p022_names.txt', 'r')

myString = TEXT.read()

TEXT.close()

newString = myString.replace("\"","").lower()

nameList = newString.split(',')

newList = sorted(nameList)  
    
for x in newList:
    c += 1
    for i in x:
        SUM += c*(ord(i)-96)
    print x, SUM
    TOTAL += SUM
    SUM = 0
print 'TOTAL:', TOTAL