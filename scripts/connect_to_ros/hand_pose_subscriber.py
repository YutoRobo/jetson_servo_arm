#!/usr/bin/env python
# coding: utf-8

import rospy
import numpy as np
import math
from sensor_msgs.msg import Joy

class HandSubscrber:
    def listener(self, callback):
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber("my_joy", Joy, callback)  
        rospy.spin()    

if __name__ == '__main__':
    def callback(data):
        rospy.loginfo(data)  

    handSubscrber = HandSubscrber()
    handSubscrber.listener(callback)