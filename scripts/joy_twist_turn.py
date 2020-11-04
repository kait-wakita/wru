#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
import time

class JoyTwist(object):
    def __init__(self):
        self._joy_sub = rospy.Subscriber('joy', Joy, self.joy_callback, queue_size=1)
        self._twist_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)

    def joy_callback(self, joy_msg):
        twist = Twist()
        if joy_msg.buttons[0] == 1:
            twist.linear.x = 0
            twist.angular.z = 6.28
            self._twist_pub.publish(twist)
            time.sleep(1) 
        elif joy_msg.buttons[1] == 1:
            twist.linear.x = 0
            twist.angular.z = -6.28
            self._twist_pub.publish(twist)
            time.sleep(1) 
        else:
            twist.linear.x = joy_msg.axes[1] * 0.5
            twist.angular.z = joy_msg.axes[0] * 0.5
            self._twist_pub.publish(twist)


if __name__ == '__main__':
    rospy.init_node('joy_twist')
    joy_twist = JoyTwist()
    rospy.spin()
