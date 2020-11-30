#! /usr/bin/env python
import rospy    # the main module for ROS_python programs
from std_srvs.srv import Trigger, TriggerResponse #creating a trigger service


def trigger_response(request):
    '''
    Callback function used by the service server to process
    requests from clients. it returns a TriggerResponse
    '''
    return TriggerResponse(
        success=True,
        message="Robots, cats, but not dogs."
    )

rospy.init_node('service_example')
my_service =rospy.Service('/service_example_topic',Trigger, trigger_response)
rospy.spin()