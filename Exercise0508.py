# -*- coding: gb2312 -*-
"""
Created on Wed Jan 25 19:51:24 2023

@author: PC
"""
for basicNum in range(111,1000,37):
    hundred=basicNum//100
    ten=basicNum//10-hundred*10
    digit=basicNum%10
    firstNum=digit*100+hundred*10+ten
    secondNum=ten*100+digit*10+hundred
    flag=0
    if firstNum%37!=0 or secondNum%37!=0:
        flag=1
        print("这是个假命题。")
        break
if flag==0:
    print("这是个真命题。")
        
    
    