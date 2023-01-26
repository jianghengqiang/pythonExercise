# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 19:50:46 2023

@author: PC
"""

from math import sqrt
for num in range(100,1000):
    j=2
    while j<int(sqrt(num)):
        if num%j==0:
            break
        j+=1
    else:
        hundred=num//100
        decimal=(num-hundred*100)//10
        digit=num%10
    #   print(hundred,decimal,digit)
        if (decimal+digit)%10==hundred:
            print(num,end='\n')