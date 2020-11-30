#! /usr/bin/env python

print "cc_keyboard_input"

import rospy
from std_msgs.msg import String
import numpy as numpy


rospy.init_node('cc_keypress')
pub = rospy.Publisher("/key_press", String, queue_size = 1)

while(True):
    val = raw_input("Input W/A/S/D: ")
    print (val)
    pub.publish(val)
