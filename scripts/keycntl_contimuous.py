#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist


rospy.init_node('keyboard_cmd_vel')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
vel=Twist()

def callback(msg):
    global vel
    pub.publish(vel)
rospy.Timer(rospy.Duration(0.2), callback)

while not rospy.is_shutdown():
    direction = raw_input('w: forward z:backward a:left d:right Enter:stop q:quit> ')
    vel.linear.x = 0
    vel.angular.z = 0
    if 'w' in direction: vel.linear.x = 1.5
    if 'z' in direction: vel.linear.x = -1.5
    if 'a' in direction: vel.angular.z = 3.14/8  #pi/4[rad/sec]
    if 'd' in direction: vel.angular.z = -3.14/8
    if 'q' in direction: break
    print vel
