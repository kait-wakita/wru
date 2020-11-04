#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

class VelDisp(object):
    def __init__(self):
        self._image_sub = rospy.Subscriber('/cmd_vel', Twist, self.callback)
        self._vel = Twist()

    def callback(self, data):
        # rospy.loginfo("x:%.2f y:%.2f th:%.2f", data.linear.x, data.linear.y, data.angular.z)
        print("%5.2f   %5.2f   %5.2f" %(data.linear.x, data.linear.y, data.angular.z))
        

if __name__ == '__main__':
    rospy.init_node('cmd_vel_disp')
    color = VelDisp()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        pass

