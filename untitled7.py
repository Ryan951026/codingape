# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 11:39:28 2021

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import random
import time
flower=38
count=0
while count<50:
     color=random.randint(0,8)
     x,y,z=mc.player.getTilePos() 
     mc.setBlock(x,y,z,flower,color)
     time.sleep(0.2)
     count=count+1