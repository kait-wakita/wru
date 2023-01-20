#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist
import time
import numpy as np

rospy.init_node('keyboard_cmd_vel')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)


def move_diagonal(vx,vy,duration):
    vel.linear.x = vx
    vel.linear.y = vy
    vel.angular.z = 0
    pub.publish(vel)
    time.sleep(duration)
    vel.linear.x = 0
    vel.linear.y = 0
    vel.angular.z = 0
    pub.publish(vel)


def rotate_excenter(h, vxy, omega):
    # 90度回転
    #    # h: 車両回転中心から実際の回転中心までの距離
    # vxy: 平行移動時の速度
    # omega: 回転時の速度
    vel = Twist()
    real_time_factor = 1.00  #  シミュレータ用の速度、実機の場合1.0

    vel.linear.x = vxy
    if omega < 0:
        vel.linear.y = vxy
    else:
        vel.linear.y = -vxy
    vel.angular.z = 0
    pub.publish(vel)
    time.sleep(h / vxy / real_time_factor)

    vel.linear.x = 0
    vel.linear.y = 0
    vel.angular.z = omega
    pub.publish(vel)
    time.sleep(abs((np.pi / 2) / omega) / real_time_factor)

    vel.angular.z = 0
    pub.publish(vel)   


def rotate_excenter_fine(h, omega):
    # 90度回転
    # 　h: 車両回転中心から実際の回転中心までの距離
    # 　omega: 回転時の速度
    vel = Twist()

    real_time_factor = 1.00  #  シミュレータ用の速度、実機の場合1.0

    duration =  abs(np.pi / 2 / omega) / real_time_factor
    vel.angular.z = omega
    vel.linear.x =  0
    vel.linear.y =  - h * omega
    pub.publish(vel)   
    time.sleep(duration)

    vel.linear.x = 0
    vel.linear.y = 0
    vel.angular.z = 0
    pub.publish(vel)   



while not rospy.is_shutdown():
    vel=Twist()
    direction = raw_input('w:前 z:後 a:左 d:右 e:反時計 r:時計 Enter:停止 q:quit> ')
    v_std = 0.3
    if 'w' in direction: vel.linear.x = v_std
    if 'z' in direction: vel.linear.x = -v_std
    if 'a' in direction: vel.linear.y = v_std
    if 'd' in direction: vel.linear.y = -v_std
    if 'e' in direction: vel.angular.z = np.pi / 8
    if 'r' in direction: vel.angular.z = -np.pi / 8
    if 'E' in direction: rotate_excenter_fine(1.0, np.pi / 4)
    if 'R' in direction: rotate_excenter_fine(1.0, -np.pi / 4)
    if '1' in direction: move_diagonal(v_std, v_std, 1.0)
    if '3' in direction: move_diagonal(v_std,-v_std, 1.0)
    if 'q' in direction: break
    print vel
    pub.publish(vel)
    

