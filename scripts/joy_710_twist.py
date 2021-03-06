#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

class JoyTwist(object):
    def __init__(self):
        self._joy_sub = rospy.Subscriber('joy', Joy, self.joy_callback, queue_size=1)
        self._twist_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)

    def joy_callback(self, joy_msg):
        twist = Twist()
        twist.linear.x = joy_msg.axes[4] * 0.5
        twist.angular.z = joy_msg.axes[3] * 0.5
        self._twist_pub.publish(twist)
        # rospy.loginfo("vx:%f, w:%f", twist.linear.x, twist.angular.z)
        
if __name__ == '__main__':
    rospy.init_node('joy_twist')
    joy_twist = JoyTwist()
    rospy.spin()
