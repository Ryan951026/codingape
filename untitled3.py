# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 09:01:58 2021

@author: user
"""

from mcpi.minecraft import Minecraft
import random
import time
mc=Minecraft.create()
while True:
    x,y,z=mc.player.getPos()
    x=x+random.uniform(-20,20)
    z=z+random.uniform(-20,20)
    y=y+30
    mc.spawnEntity(x,y,z,90)
    time.sleep(0.2)
    
 Minecraft.create("35.229.251.147")   