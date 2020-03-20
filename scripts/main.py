#!/usr/bin/env python
# coding: utf-8
import rospy
import numpy as np
from robot.actuator import servo
from robot import arm_robot
from connect_to_ros import hand_pose_subscriber

if __name__ == '__main__':
    LINK1_LENGTH = 0.1
    LINK2_LENGTH = 0.1

    ## ロボットモデルの作成
    servos = [
        servo.ServoMotor(), 
        servo.ServoMotor(), 
        servo.ServoMotor(), 
        servo.ServoMotor(), 
        servo.ServoMotor() ]
    robot = arm_robot.ArmRobot(*servos)
    # 2リンク関節の各長さ[m]を代入
    robot.setHingeLength([LINK1_LENGTH, LINK2_LENGTH])

    ## ここに受信したUnityデータに対するcallback処理を記述
    def callback(data):
        rospy.loginfo(data) 
        robot.calcServosDeg([data.axes[0],data.axes[0],data.axes[0]])
        robot.move() 

    handSubscrber = hand_pose_subscriber.HandSubscrber()
    handSubscrber.listener(callback)