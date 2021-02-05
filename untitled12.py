# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 16:08:21 2021

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getPos()
mc.setSigh(x,y,z,0,63,")