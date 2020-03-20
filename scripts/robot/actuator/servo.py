#!/usr/bin/env python
# coding: utf-8

import Jetson.GPIO as GPIO

MIN_DEGREE = -90.0
MAX_DEGREE = 90.0

class ServoMotor:
    def __init__(self, pin):
        print("pin: ", pin)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        self.__motor = GPIO.PWM(pin, 50)
        self.__motor.start(0.0)

        self.__now_deg = 0.0
        self.__target_deg = 0.0
        self.__min_deg = MIN_DEGREE
        self.__max_deg = MAX_DEGREE

    def setNowDegree(self, now_deg):
        self.__now_deg = now_deg

    def setTargetDegree(self, tar_deg):
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
        
    def move(self):
        print("move start to ", self.__target_deg)
        
        ## 角度を出力に補正
        out = (1.0 + self.__target_deg/180.0)/20.0*100.0 
        self.__motor.ChangeDutyCycle(out)
        ## 以下にjetson nanoでのGPIOの処理を記述

    