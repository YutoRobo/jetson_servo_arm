#!/usr/bin/env python
# coding: utf-8
import numpy as np
import math
from actuator import servo

# サーボを5つ使う
class ArmRobot:
    def __init__(self, *servos):
        self.__servos = servos
    
    def setOffsetDegree(self, offsets_degree):
        #サーボの初期位置のずれの分補正をかけるoffset
        self.__offsets_degree = offsets_degree

    def setHingeLength(self, hinge_len):
        self.__hinge_len = hinge_len
        print("hinge length is ", hinge_len)

    def calcServosDeg(self, target_pose):
        print('target pose is ',target_pose)
        ## 各サーボの角度を計算する処理を記述
        self.__servos[0].setTargetDegree(
            math.degrees(math.atan2(target_pose[1], target_pose[0]))
        )
        xy_abs = np.linalg.norm(np.array([target_pose[0], target_pose[1]]))

        ## 2リンクモデルの逆運動学
        ## https://tajimarobotics.com/kinematics-two-link-model-2/
        try:    
            rad_theta1 = math.acos((xy_abs ** 2 + target_pose[2] ** 2 + self.__hinge_len[0] ** 2 - self.__hinge_len[1] ** 2) / (2 * self.__hinge_len[0] * math.sqrt( xy_abs ** 2 + target_pose[2] ** 2 ))) + math.atan2(target_pose[2], xy_abs)
            rad_theta2 = math.atan2((target_pose[2] - self.__hinge_len[0] * math.sin(rad_theta1)), (xy_abs - self.__hinge_len[0] * math.cos(rad_theta1))) - rad_theta1
            self.__servos[1].setTargetDegree(math.degrees(rad_theta1))
            self.__servos[2].setTargetDegree(math.degrees(rad_theta2))
        except Exception as e:
            print(e)

    def send(self):
        for servo in self.__servos:
            servo.send()

if __name__ == '__main__':
    servos = [
        servo.ServoMotor(), 
        servo.ServoMotor(), 
        servo.ServoMotor(), 
        servo.ServoMotor(), 
        servo.ServoMotor() ]
    robot = ArmRobot(*servos)
    robot.setHingeLength([1.0, 1.0])
    robot.calcServosDeg([0.1,0.0,0.0])
    robot.send()