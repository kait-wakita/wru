#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist


rospy.init_node('keyboard_cmd_vel')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
while not rospy.is_shutdown():
    str = " "
    str = input("v (km/h, default=1.0)>>>")
    if str.isdecimal():
        v = int(str)
    else:
        v = 1.0

    str = input("w (deg/s, default=45.0)>>>")
    if str.isdecimal():
        wd = int(str)
    else:
        wd = 45.0

    str = input("dt (s, default=1.0)>>>")
    if str.isdecimal():
        dt = int(str)
    else:
        dt = 1.0

    vel=Twist()
    vel.linear.x = v
    vel.angular.z = 3.14 * wd / 180
    print(vel)
    pub.publish(vel)

    time.sleep(dt)    
