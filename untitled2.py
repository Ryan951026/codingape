# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 09:01:57 2021

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getPos()
mc.spawnEntity(x,y,z,93)