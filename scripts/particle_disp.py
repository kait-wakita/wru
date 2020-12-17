#!/usr/bin/env python
#
# display particle average and std
#

import rospy
import numpy as np
import tf
from geometry_msgs.msg import PoseArray


class ParticleDisp(object):
    def __init__(self):
        self.sub = rospy.Subscriber('/particlecloud', PoseArray, self.callback)


        
    def callback(self, msg):
        n = len(msg.poses)
        #print("%d particles" %(n))

        pt = np.array(msg.poses)
        pd = np.zeros((n,3))
        
        for i in range(n):
            pd[i][0]= pt[i].position.x
            pd[i][1]= pt[i].position.y
            e = tf.transformations.euler_from_quaternion((pt[i].orientation.x, pt[i].orientation.y, pt[i].orientation.z, pt[i].orientation.w))
            pd[i][2] = e[2]
            #print("%5.2f   %5.2f  %5.2f  " %(pd[i][0], pd[i][1], pd[i][2]))

        print("%5.2f,%5.2f,  %5.2f,%5.2f,  %5.2f,%5.2f" %(np.average(pd[:,0]),np.std(pd[:,0]), np.average(pd[:,1]),np.std(pd[:,1]), np.average(pd[:,2]),np.std(pd[:,2])))

            
if __name__ == '__main__':
    rospy.init_node('particle_disp')
    color = ParticleDisp()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        pass

