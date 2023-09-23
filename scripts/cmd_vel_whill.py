#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

class GetVel(object):
    def __init__(self):
        self._twist_sub = rospy.Subscriber('/cmd_vel', Twist, self.callback)
        self._vel = Twist()

    def callback(self, data):
        self._vel = data
        

if __name__ == '__main__':
    rospy.init_node('cmd_vel_whill')
    getvel = GetVel()
    pub = rospy.Publisher('/whill/controller/cmd_vel', Twist, queue_size=10)

    rate = rospy.Rate(5)
    while not rospy.is_shutdown():
        pub.publish(getvel._vel)
        data = getvel._vel
        print("%5.2f   %5.2f   %5.2f" %(data.linear.x, data.linear.y, data.angular.z))

        rate.sleep()
    