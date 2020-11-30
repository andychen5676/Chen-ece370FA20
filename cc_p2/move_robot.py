#! /usr/bin/env python

import rospy
from sensor_msgs.msg import JointState
from nav_msgs.msg import Odometry
from std_msgs.msg import String
from geometry_msgs.msg import Twist

x0 = 0.0 # x
y0 = 0.0 # y
t0 = 0.0 # theta

tt0 = None

def callback(msg):
    print msg.data
    d = msg.data
    tw = Twist()
    if(d == "w"):
        tw.linear.x = 0.5
    elif(d == "s"):
        tw.linear.x = -0.5
    elif(d == "d"):
        tw.angular.z = -0.5
    elif(d =="a"):
        tw.angular.z = 0.5
    else:
        pass
    pub.publish(tw)


rospy.init_node('cc_move_robot')
sub = rospy.Subscriber('/key_press', String, callback)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)

rospy.spin()
