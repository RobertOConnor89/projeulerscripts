# -*- coding: utf-8 -*-
"""
Find the sum of all the positive integers  which can not be written as the sum 
of two abundant numbers.

An abundant number is a number that is greater than the sum of its divisors.

Find all abundant numbers, perfect numbers, and deficient numbers.

Find all sums of two abundant numbers less than 28123.

Subtract these numbers from range(28123).

Sum the remaining values.
"""
def divisors(x):
    div_list = []
    for i in range(1,int(x**0.5)+1):
        if x % i == 0:
            if (i == 1) or (x/i == i):
               div_list.append(i)
            elif (i != 1) and (x/i != i):
                div_list.append(i)
                div_list.append(x/i)
    return div_list

def list_sum(x):
    total = 0
    for i in x:
        total += i
    return total

mySum = 0
myList = []
deficient = []
perfect = []
abundant = []
TOTAL = 0
ab_sums = []

for j in range(1,28124):
    myList = divisors(j)
    mySum = list_sum(myList)
    if j < mySum:
        abundant.append(j)
    elif j == mySum:
        perfect.append(j)
    else:
        deficient.append(j)
    mySum = 0
    myList = []
    
abundant = sorted(set(abundant))

for i in range(len(abundant)):
    for j in range(len(abundant)):
        ab_sums.append(abundant[i]+abundant[j])
        
ab_sums = sorted(set(ab_sums))

ab_sums = [x for x in ab_sums if x < 28123]

TOTAL = 28123*28122/2 - sum(ab_sums)

print TOTAL

    

