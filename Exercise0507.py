# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 19:34:48 2023

@author: PC
"""
num1=eval(input('Please input a number between 2 and 1000: '))
num2=num1
lst=[]
i=2
while i<=num2:
    if num2%i==0:
        lst.append(str(i))
        num2/=i
        continue
    i+=1
right='*'.join(lst)
print('{0}={1}'.format(num1,right))