#! /usr/bin/env python
import rospy    # the main module for ROS_python programs
from std_srvs.srv import Trigger, TriggerResponse #creating a trigger service
from nav_msgs.srv import GetMap,GetMapRequest

from gazebo_msgs.srv import GetModelState,GetModelStateRequest
import os
import time as t
import numpy as np

name = 'box'
box_i = 0

rob_proxy = None

def trigger_response(request):
    global box_i
    '''
    Callback function used by the service server to process
    requests from clients. it returns a TriggerResponse
    '''

    DropBoxBool = False

    a = getRobotLocation()
    x = a[0]
    y = a[1]

 

    b = getBoxLocation(x,y)
    if(b != None):
        if(not checkBoxLocation(b[0],b[1])):
            dropBox(b[0],b[1])
            DropBoxBool = True

    
    return TriggerResponse(
        success=DropBoxBool,
        message=" done " 
    )

def dropBox(x,y):
    global box_i
    saveBoxVal(x,y)
    b0 = "./drop_box.sh "
    b1 = name + str(box_i) + " "
    box_i += 1
    b2 = str(x) + " "
    b3 = str(y) + " "
    b4 = "&"
    buff = b0 + b1 + b2 + b3 + b4

    os.system(buff)

box_x = []
box_y = []
def saveBoxVal(x,y):
    global box_x, box_y
    box_x.append(x)
    box_y.append(y)

def checkBoxLocation(x,y):
    global box_x, box_y
    
    for i in range(len(box_x)):
        xx = box_x[i]
        yy = box_y[i]
        d = np.sqrt((xx-x)*(xx-x)+(yy-y)*(yy-y))
        if(d<1.01):
            return True
    return False



def delBox(bi):
    buff = "rosservice call gazebo/delete_model " + name + str(bi) + " &"
    os.system(buff)

def delBoxAll(bi):
    for i in range(bi):
        delBox(i)
        t.sleep(0.1)

def getBoxLocation(x,y):

    #set initial original point
    x0 = 0.0
    y0 = 0.0
    x_dist = x - x0
    y_dist = y - y0
    #determine if the robot is inside the square (50 - 2)m
    if(-24.0<x_dist<24.0 and -24.0<y_dist<24.0 ):#if robot is in range do nothing
        return None
    else:#if robot is at upper bound, drop upper bound box
        if(x_dist >= 24.0 and -24.0<y_dist < 24.0):
            xn = x + 1
            yn = y
        #if robot is at lower bound, drop lower bound box    
        if(x_dist <= -24.0 and y_dist < 24.0):
            xn = x - 1
            yn = y
        if(x_dist < 24.0 and y_dist >= 24.0):
            xn = x
            yn = y + 1
        if(x_dist < 24.0 and y_dist <= -24.0):
            xn = x
            yn = y - 1
        if(x_dist >= 24.0 and y_dist >= 24.0):
            xn = x + 1
            yn = y + 1
        if(x_dist >= 24.0 and y_dist <= -24.0):
            xn = x + 1
            yn = y - 1
        if(x_dist <= -24.0 and y_dist >= 24.0):
            xn = x - 1
            yn = y + 1
        if(x_dist <= -24.0 and y_dist <= -24.0):
            xn = x - 1
            yn = y - 1

    
    return (xn,yn)

def getRobotLocation():
    a = GetModelStateRequest(model_name='cc_robot')
    a.model_name = "cc_robot"
    s = robot_proxy(a)
    #print a
    #print s
    x = s.pose.position.x
    y = s.pose.position.y
    print "Robot Current Location:"
    print "x = " + str(x) + " y = " + str(y)
    return(x,y)





rospy.init_node('service_example')
#delBoxAll(255)
my_service =rospy.Service('/box', Trigger, trigger_response)

rospy.wait_for_service('/gazebo/get_model_state')
robot_proxy = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
rospy.spin()