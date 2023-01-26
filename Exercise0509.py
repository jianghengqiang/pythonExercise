# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 19:51:17 2023

@author: PC
"""

inNum=1432
strList=list(str(inNum))
numList=[int(x) for x in strList]
biggestList=sorted(numList,reverse=True)
smallestList=sorted(numList)
biggestNumList=[str(x) for x in biggestList]
smallestNumList=[str(x) for x in smallestList]
biggestNum=int(''.join(biggestNumList))
smallestNum=int(''.join(smallestNumList))

newNum=biggestNum-smallestNum
while newNum!=6174:
    print("{0:0>4d}-{1:0>4d}={2:0>4d}".format(biggestNum,smallestNum,newNum))
    strList=list(str(newNum))
    numList=[int(x) for x in strList]
    biggestList=sorted(numList,reverse=True)
    smallestList=sorted(numList)
    biggestNumList=[str(x) for x in biggestList]
    smallestNumList=[str(x) for x in smallestList]
    biggestNum=int(''.join(biggestNumList))
    smallestNum=int(''.join(smallestNumList))
    newNum=biggestNum-smallestNum
print("{0:0>4d}-{1:0>4d}={2:0>4d}".format(biggestNum,smallestNum,newNum))

    