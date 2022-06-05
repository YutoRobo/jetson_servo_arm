#!/usr/bin/env python
# # license removed for brevity
import rospy
from sensor_msgs.msg import Joy

if __name__ == '__main__':
    pub = rospy.Publisher('my_joy', Joy, queue_size=10)
    rospy.init_node('pub_my_joy', anonymous=True)
    r = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        print("input joy data!")
        print("x")
        a = float(input())
        print("y")
        b = float(input())
        print("z")
        c = float(input())
        print(a,b,c)
        joy = Joy()
        joy.axes.append(a)
        joy.axes.append(b)
        joy.axes.append(c)
        pub.publish(joy)
        r.sleep()
    