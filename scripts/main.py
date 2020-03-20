#!/usr/bin/env python
import rospy
from actuator import servo

if __name__ == '__main__':
    servo = servo.ServoMotor()
    
    servo.setTargetDegree(60)
    