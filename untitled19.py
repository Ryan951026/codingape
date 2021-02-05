# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 16:08:45 2021

@author: user
"""

from random import randrange
from time import time

def binarySearch():
    sTime=time()
    low=0
    top=10000000
    
    while low<= top:
        mid=(low+top)//2
        
        if mid<number:
            low=mid+1
            
        elif mid>number:
            top=mid-1
        
        else:
            print("找到答案了!是"+str(mid))
            print("二元搜尋法:花了"+str(time()-sTime)+"秒")
            break
        
number=randrange(10000000)
binarySearch()