# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 15:30:40 2021

@author: user
"""
from mcpi.minecraft import Minecraft
from time import time

mc = Minecraft.create()
def linearSearch():
    sTime=time()
    for i in range(1,10000001):
        if i==number:
            print("找到答案了!是"+str(i))
            print("線性搜尋法:花了"+str(time()-sTime)+"秒")
            break
number=randrange(1,10000001)
linearSearch()        
        
            