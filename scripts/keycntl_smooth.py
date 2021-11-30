#!/usr/bin/env python
import rospy, time
from geometry_msgs.msg import Twist

pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

def publish_vel_rate(vel, rate):
    vel1 = Twist()
    vel1.linear.x = vel.linear.x * rate
    vel1.angular.z = vel.angular.z * rate
    pub.publish(vel1)


while not rospy.is_shutdown():
    vel=Twist()
    direction = raw_input('w a s z, return:stop > ')
    if 'w' in direction: vel.linear.x = 0.20
    if 'z' in direction: vel.linear.x = -0.20
    if 'a' in direction: vel.angular.z = 3.14/8  #pi/4[rad/sec]
    if 'd' in direction: vel.angular.z = -3.14/8
    if 'q' in direction: break

    publish_vel_rate(vel,0.25)
    time.sleep(0.1)
    publish_vel_rate(vel,0.5)
    time.sleep(0.1)
    publish_vel_rate(vel,0.75)
    time.sleep(0.1)
    publish_vel_rate(vel,1)
    time.sleep(0.5)
    publish_vel_rate(vel,0.75)
    time.sleep(0.1)
    publish_vel_rate(vel,0.5)
    time.sleep(0.1)
    publish_vel_rate(vel,0.25)
    time.sleep(0.1)
    publish_vel_rate(vel,0.0)
