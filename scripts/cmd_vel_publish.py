#!/usr/bin/env python
import rospy
import time
from geometry_msgs.msg import Twist


rospy.init_node('cmd_vel_publish')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
while not rospy.is_shutdown():
    v = input("v (km/h, default=1.0)>>>")
    wd = input("w (deg/s, default=45.0)>>>")
    dt = input("dt (s, default=1.0)>>>")

    vel=Twist()
    vel.linear.x = v
    vel.angular.z = 3.14 * wd / 180
    print(vel)

    nt = int(round(dt / 0.5))

    for i in range(nt):
        pub.publish(vel)
        rospy.sleep(0.5)

