#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('sound_pp', String, queue_size=10)
    rospy.init_node('sound_pp_test_talker', anonymous=True)
    start_time = rospy.get_time()
    r = rospy.Rate(1) # 10hz
    count=0
    while not rospy.is_shutdown():
        mod_id=count%20
        str = ''
        if mod_id==0:
          str = 'warn1.mp3'
        elif  mod_id==5:
          str = 'warn4.mp3'
        elif  mod_id==10:
          str = 'warn9.mp3'
        elif  mod_id==15:
          str = 'warn0.mp3'

        if str != '':
          rospy.loginfo(str)
          pub.publish(str)
        count=count+1
        r.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
