#! /usr/bin/env python

import rospy
from std_srvs.srv import Trigger, TriggerRequest

#init a node
rospy.init_node('service_client')

#wait for this service to be running
rospy.wait_for_service('/service_example_topic')

#create the connection to the service(Trigger service)
sos_service = rospy.ServiceProxy('/service_example_topic', Trigger)

#create an object of the type TriggerRequest. needed for trigger service
sos = TriggerRequest()

#send the request through t he connection
result = sos_service(sos)

#done
print result