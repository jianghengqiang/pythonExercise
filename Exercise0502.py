# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 20:10:16 2023

@author: PC
"""

rate=eval(input("Enter the exchange rate from dollars to RMB:"))
flag=eval(input("Enter 0 to convert dollars to RMB and 1 vice versa:"))
if flag==0:
    amount=eval(input("Enter the dollar amount:"))
    number2=amount*rate
    print("$ {0:5.1f} is {1:5.1f} yuan".format(amount,number2))
elif flag==1:
    amount=eval(input("Enter the RMB amount:"))
    number2=amount/rate
    print("{0:5.1f} yuan is $ {1:5.1f}".format(amount,number2))
else:
    print("Incorrect input")