#! /usr/bin/env python

import rospy
from std_srvs.srv import Trigger, TriggerRequest
from nav_msgs.srv import GetMap, GetMapRequest
import time as t

#init a node
rospy.init_node('service_client')

#wait for this service to be running
rospy.wait_for_service('/box')

#create the connection to the service(Trigger service)
serv = rospy.ServiceProxy('/box', Trigger)

#create an object of the type TriggerRequest. needed for trigger service
sos = TriggerRequest()

#send the request through t he connection
tick = t.time()
result = serv(sos)
tock = t.time()
print(tock - tick)

#done
print result