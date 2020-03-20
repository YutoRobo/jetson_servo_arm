#!/usr/bin/env python

class ServoMotor:
    def __init__(self):
        self.__now_deg = 0.0

    def setNowDegree(self, now_deg):
        self.__now_deg = now_deg

    def setTargetDegree(self, tar_deg):
        self.__target_deg  = tar_deg
        print("set target degree: ", tar_deg)
        
    