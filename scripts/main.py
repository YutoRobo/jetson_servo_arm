#!/usr/bin/env python
import rospy
import numpy as np
from actuator import servo
from robot import arm_robot

if __name__ == '__main__':
    servos = [
        servo.ServoMotor(), 
        servo.ServoMotor(), 
        servo.ServoMotor(), 
        servo.ServoMotor(), 
        servo.ServoMotor() ]
    robot = arm_robot.ArmRobot(*servos)
    robot.setHingeLength([1.0, 1.0])
    robot.calcServosDeg([0.1,0.0,0.0])
    robot.move()