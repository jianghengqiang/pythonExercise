# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 19:44:03 2023

@author: PC
"""

n=eval(input("Please enter a number between 1 and 10: "))  # 需要输入的数字
j=1  # 起始数字
count=0  # 让每行打印5个数字的办法
convert_certain_number=str(n)
while j<=100:
    convert_num=str(j)     
    if j%n!=0 and convert_certain_number not in convert_num:       
        count+=1
        if count%10==0:
            print(j,end='\n')
        else:
            print(j,end=' ')
    j+=1

  