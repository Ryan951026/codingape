# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import random
import time
x,y,z=mc.player.getTilePos()
while True:
    color=random.randint(0,16)
    time.sleep(0.5)
    x,y,z=mc.player.getTilePos()
    mc.setBlocks(x+5,y-1,z+5,x-5,y-1,z-5,95,color)
    