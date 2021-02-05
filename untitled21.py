# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 16:41:50 2021

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
myID=mc.getPlayerEntityId("APE_43")
mc.postToTitle(myID,"hello")