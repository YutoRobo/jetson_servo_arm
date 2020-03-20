#!/usr/bin/env python
# coding: utf-8

class ServoMotor:
    def __init__(self):
        self.__now_deg = 0.0
        self.__target_deg = 0.0

    def setNowDegree(self, now_deg):
        self.__now_deg = now_deg

    def setTargetDegree(self, tar_deg):
        self.__target_deg  = tar_deg
        print("set target degree: ", tar_deg)
        
    def move(self):
        print("move start to ", self.__target_deg)
        ## 以下にjetson nanoでのGPIOの処理を記述

    