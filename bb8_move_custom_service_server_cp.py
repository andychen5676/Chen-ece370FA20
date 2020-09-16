#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse
from geometry_msgs.msg import Twist, Vector3

def my_callback(request):
    print "Creating the square traj"
        
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    rate = rospy.Rate(1)
    move = Twist()
    a=0
    while a<4:
        move.linear.x = 0.5
        move.linear.y = 0
        move.linear.z = 0
        move.angular.x=0
        move.angular.y=0
        move.angular.z=0
        for i in xrange(4):
            pub.publish(move)
            rate.sleep()
        move.linear.x = 0
        move.linear.y = 0
        move.linear.z = 0
        move.angular.x=0
        move.angular.y=0
        move.angular.z=0.25
        for i in xrange(4):
            pub.publish(move)
            rate.sleep()
        a+=1


    move.linear.x = 0
    move.angular.z = 0
    pub.publish(move)
    return EmptyResponse()

rospy.init_node('square_service_server_node')
# Creates a service called /my_service with the defined callback
my_service = rospy.Service('square_trajectory', Empty, my_callback)

rospy.spin()  # Maintain the service open

