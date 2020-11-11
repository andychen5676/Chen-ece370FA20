#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan 
from geometry_msgs.msg import Twist

def callback(msg): 
  print str(msg.ranges[360]) + " " + str(msg.ranges[179]) + " " + str(msg.ranges[539]) #print the distance to the wall

#move forward until postion to the wall is less than 1
  if msg.ranges[360] > 0.5:
      move.linear.x = 0.6
      move.angular.z = 0.0

#turn left when the position is less than 0.5 to a wall
  if msg.ranges[360] < 0.5: 
      move.linear.x = 0.0
      move.angular.z = 0.3
        
#if the left side is less than 0.3, turn robot right
  if msg.ranges[719] < 0.3:
      move.linear.x = 0.0
      move.angular.z = -0.2
        
#If the right side is less than 0.3, turn robot left
  if msg.ranges[0] < 0.3:
      move.linear.x = 0.0
      move.angular.z = 0.2
# If the right side and front is less than 0.3, turn robot left
  if (msg.ranges[179]<1.5 and msg.ranges[360]< 1):
      move.linear.x = 0.0
      move.angular.z = 0.3

#if the left side and front is less than 0.3, turn robot right
  if (msg.ranges[539]< 1.5 and msg.ranges[360] < 1):
      move.linear.x = 0.0
      move.angular.z = -0.3
#if there is no object surrounding stop the robot   
  if (msg.ranges[360]>500 and msg.ranges[0]>500 and msg.ranges[719]>500 and msg.ranges[179]>500 and msg.ranges[539]>500):
      move.linear.x = 0.0
      move.angular.z = 0.0
#if the right front has object, go alone the object in parallel   
  if (msg.ranges[179] == 1.414 * msg.ranges[0]):
      move.linear.x = 0.6
      move.angular.z = 0.0
#if the right front has object, go alone the object in parallel  
  if (msg.ranges[539] == 1.414 * msg.ranges[719]):
      move.linear.x = 0.6
      move.angular.z = 0.0

  pub.publish(move)

rospy.init_node('topics_quiz_node')
sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback) #subscribe to the laser's topic
pub = rospy.Publisher('/cmd_vel', Twist,queue_size = 10)
move = Twist()

rospy.spin()