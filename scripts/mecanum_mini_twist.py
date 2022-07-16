#!/usr/bin/env python

import rospy
import socket

from geometry_msgs.msg import Twist


class VelTwist(object):
    def __init__(self):
        self._image_sub = rospy.Subscriber('/cmd_vel', Twist, self.callback)
        self._vel = Twist()

    def callback(self, data):
        # rospy.loginfo("x:%.2f y:%.2f th:%.2f", data.linear.x, data.linear.y, data.angular.z)
        print("%5.2f   %5.2f   %5.2f" %(data.linear.x, data.linear.y, data.angular.z))
        message = "%d %d %d" % (data.linear.x*100, data.linear.y*100, data.angular.z)
        send_len = sock.sendto(message.encode('utf-8'), serv_address)
        

if __name__ == '__main__':
    rospy.init_node('mecanum_mini_twist')
    serv_address = ('192.168.1.4', 8888) # change IP address to proper address
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    color = VelTwist()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        pass

