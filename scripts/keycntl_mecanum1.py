#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist


rospy.init_node('keyboard_cmd_vel')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
while not rospy.is_shutdown():
    vel=Twist()
    direction = raw_input('w:fwd z:bwd a:left d:right e:c-clock r:clock Enter:stop q:quit> ')
    if 'w' in direction: vel.linear.x = 0.3
    if 'z' in direction: vel.linear.x = -0.35
    if 'a' in direction: vel.linear.y = 0.3
    if 'd' in direction: vel.linear.y = -0.3
    if 'e' in direction: vel.angular.z = 3.14/2
    if 'r' in direction: vel.angular.z = -3.14/2
    if 'q' in direction: break
    print vel
    pub.publish(vel)
    
