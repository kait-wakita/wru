#!/usr/bin/env python
#######################################################################
# playing mp3 sound file in ROS
#    2021-11-30 T.Wakita 
#    2021-09-10 T.Wakita (mod for continuous sound) 
#######################################################################
#   installation:
#     sudo apt install mpg123
#     prepare mp3 file
#   usage:
#     rosrun wru sound_ppc.py
#   IN:
#      /sound_pp (mp3 file path)


import rospy
import time
import subprocess
from std_msgs.msg import String

def callback(data):
    global fname
    fname = data.data

    
def listener():
    rospy.spin()
        
if __name__ == '__main__':
    rospy.init_node('sound_ppc', anonymous=True)
    rospy.Subscriber('sound_pp', String, callback, queue_size=1)
    fname = ''
    
    while not rospy.is_shutdown():
        if fname != '':
            target='mpg123 -q '+ fname 
            rospy.loginfo("playing %s", fname)
            subprocess.call(target.split())