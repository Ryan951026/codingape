# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 11:20:19 2021

@author: user
"""
from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
time.sleep(5)

x=-16
y=80
z=15

mc.player.setTilePos(x,y,z)
time.sleep(0.5)
y =y+1
mc.player.setTilePos(x,y,z)
time.sleep(0.5)
y=y+1
mc.player.setTilePos(x,y,z)
time.sleep(0.5)
y=y+1
mc.player.setTilePos(x,y,z)
while True:
        mc.postToChat("hello")
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
t=0
while True:
    t=t+1
    mc.postToChat()第