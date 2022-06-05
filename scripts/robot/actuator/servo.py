#!/usr/bin/env python
# coding: utf-8

MIN_DEGREE = -90.0
MAX_DEGREE = 90.0

class ServoMotor:
    def __init__(self):
        self.__now_deg = 0.0
        self.__target_deg = 0.0
        self.__min_deg = MIN_DEGREE
        self.__max_deg = MAX_DEGREE
        self.__offset_deg = 0.0

    def setNowDegree(self, now_deg):
        self.__now_deg = now_deg

    def setOffsetDegree(self, offset_deg):
        self.__offset_deg = offset_deg

    def setTargetDegree(self, tar_deg):
        tar_deg = tar_deg + self.__offset_deg
        if tar_deg <= self.__min_deg:
            self.__target_deg  = self.__min_deg
        elif tar_deg >= self.__max_deg:
            self.__target_deg  = self.__max_deg
        else:
            self.__target_deg  = tar_deg
        print("set target degree: ", self.__target_deg)
    
    def setDegreeRange(self, min_deg, max_deg):
        self.__min_deg = min_deg
        self.__max_deg = max_deg

    def getDegree(self):
        return self.__target_deg
        
    def send(self):
        print("move start to ", self.__target_deg)
        ## 以下にmbedへの送信の処理を記述


    