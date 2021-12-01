#!/usr/bin/env python
#######################################################################
# playing mp3 sound file in ROS
#    2021-11-30 T.Wakita  
#######################################################################
#   installation:
#     sudo apt install mpg123
#     prepare mp3 file
#   usage:
#     rosrun wru sound_pp.py
#   IN:
#      /sound_pp (mp3 file path)


import rospy
import time
import subprocess
from std_msgs.msg import String

def callback(data):
    global last_time
    target='mpg123 -q '+data.data
    if rospy.get_time() > last_time+1:
      rospy.loginfo("playing %s",data.data)
      subprocess.call(target.split())
      last_time = rospy.get_time()
    
def listener():
    rospy.spin()
        
if __name__ == '__main__':
    rospy.init_node('sound_pp', anonymous=True)
    last_time = rospy.get_time()
    rospy.Subscriber('sound_pp', String, callback, queue_size=1)
    
    listener()
