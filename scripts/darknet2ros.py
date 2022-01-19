#!/usr/bin/env python
#######################################################################
# convert darknet(modified for darknet2ros) ext. output to ROS topic
#    2021-12-01 T.Wakita  
#######################################################################
#   usage:
#     ./darknet detector demo cfg/coco.data cfg/yolov4-tiny.cfg yolov4-tiny.weights -ext_output | python darknet2ros.py
#   IN:
#      stdin (darket ext. output)
#   OUT:
#      /darknet_bboxes (darknet_ros_msgs/BoundingBoxes)
#
import rospy, sys
from std_msgs.msg import String
from darknet_ros_msgs.msg import BoundingBoxes, BoundingBox

rospy.init_node('darknet2ros')
pub = rospy.Publisher('darknet_bboxes', BoundingBoxes, queue_size=10)
rate = rospy.Rate(100)

ss=0
bb=BoundingBoxes()

while not rospy.is_shutdown():
    F=sys.stdin
    s=F.readline()
    if s.find('Objects') == 0:
        pub.publish(bb)        
        bb=BoundingBoxes()
        ss=ss+1
        bb.header.seq=ss
        bb.image_header.seq=ss
    elif s.find('OBJ') == 0:
        b=BoundingBox()
        r=s.split(':')
        b.Class = r[1]
        b.probability = float(r[2])
        b.xmin = int(r[3])
        b.ymin = int(r[4])
        b.xmax = int(r[3])+int(r[5])
        b.ymax = int(r[4])+int(r[6])
        bb.bounding_boxes.append(b)

