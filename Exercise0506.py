# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 20:01:18 2023

@author: PC
"""

s=input('Please input a setence: ')
s=s.lower()
sList=list(s)
# for item in sList:
#    if item[-1] in ',.\'
alphabet='abcdefghijklmnopqrstuvwxyz'
alphabetList=list(alphabet)
gInfo={}.fromkeys(tuple(alphabetList),0)
for item in sList:
    gInfo[item]=gInfo.get(item,0)+1
print(list(gInfo.values()))