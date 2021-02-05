# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 11:20:44 2021

@author: user
"""


from mcpi.minecraft import Minecraft
mc=Minecraft.create("35.229.251.147")
import time 
while True:
    mc.executeCommand("time add 50")
    time.sleep(0.2)
    