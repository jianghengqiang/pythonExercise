# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 19:43:35 2023

@author: PC
"""
from math import sqrt
a,b,c=eval(input("Please enter the number(a,b,c):"))
longest=max((a,b,c))
if a+b+c>2*longest:
    Perimeter=a+b+c
    print("The Perimeter of triangle is {:5.2f}".format(Perimeter))
    p=Perimeter/2
    Area=sqrt(p*(p-a)*(p-b)*(p-c))
    print("The Area of triangle is {:5.2f}".format(Area))
else:
    print("The three lines can't form a triangle")