#!/usr/bin/env python
# coding: utf-8
import rospy
import numpy as np
from robot.actuator import servo
from robot import arm_robot
from connect_to_ros import hand_pose_subscriber
from geometry_msgs.msg import Twist

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

    pub = rospy.Publisher('degrees', Twist, queue_size=10)

    ## ここに受信したUnityデータに対するcallback処理を記述
    def callback(data):
        rospy.loginfo(data) 
        robot.calcServosDeg([data.axes[0],data.axes[0],data.axes[0]])
        pub_data = Twist()
        pub_data.linear.x = servos[0].getDegree()
        pub_data.linear.y = servos[1].getDegree()
        pub_data.linear.z = servos[2].getDegree()
        pub_data.angular.x = servos[3].getDegree()
        pub_data.angular.y = servos[4].getDegree()
        pub.publish(pub_data)

    handSubscrber = hand_pose_subscriber.HandSubscrber()
    handSubscrber.listener(callback)