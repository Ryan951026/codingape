# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 16:35:28 2021

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
mc.setBlock(x,y,z,56)
mc.setBlock(x+1,y+10,z,56)
mc.setBlock(x+2,y+10,z,56)
mc.setBlock(x+1,y+10,z+1,56)
mc.setBlock(x+2,y+10,z+2,56)
mc.setBlock(x+2,y+10,z,56)
mc.setBlock(x+1,y+10,z+2,56)
mc.setBlock(x,y+10,z+2,56)
mc.setBlock(x,y+10,z+1,56)
mc.setBlock(x+2,y+10,z+1,56)
mc.setBlock(x,y+10,z,56)