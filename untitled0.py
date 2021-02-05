# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 10:07:33 2021

@author: user
"""
from mcpi.minecraft import Minecraft
mc=Minecraft.create("35.229.251.147")
import time

for i in range(28):
    myID=mc.getPlayerEntityId("APE_43")
    mc.executeCommand("tp APE_43 1052 68 974")
    mc.postToTitle(myID,"過了第"+str(i//2+1)+"天")
    mc.executeCommand("time add 14000")
    time.sleep(1)
mc.postToTitle(myID,"你已隔離結束")


    

