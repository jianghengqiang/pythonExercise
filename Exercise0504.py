# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 20:28:24 2023

@author: PC
"""
count=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):            
            newNumber=i*100+j*10+k
            print(newNumber,end=' ')
            count+=1
print("\n The total number of these integers is : {:d}".format(count))