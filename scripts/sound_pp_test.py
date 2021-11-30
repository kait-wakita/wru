#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('sound_pp', String, queue_size=10)
    rospy.init_node('sound_pp_test_talker', anonymous=True)
    start_time = rospy.get_time()
    r = rospy.Rate(10) # 10hz
    count=0
    while not rospy.is_shutdown():
        mod_id=count%3
        if mod_id==0:
          str = '/home/jetson/Music/bomb1.mp3'
        elif  mod_id==1:
          str = '/home/jetson/Music/kira1.mp3'
        else:
          str = '/home/jetson/Music/thunder1.mp3'
        if (count%100)<5:
          rospy.loginfo(str)
          pub.publish(str)
        count=count+1
        r.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
