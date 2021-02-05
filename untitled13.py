# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 10:01:31 2021

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create("35.229.251.147")
import time
nuber=1
for i in range(8):
    x,y,z=mc.player.getPos()
    for a in range(nuber):
        mc.spawnEntity(x,y,z,120)
    
    nuber=nuber*2
    mc.postToChat("這次生成了"+str(nuber)+"隻村民")
    time.sleep(1)