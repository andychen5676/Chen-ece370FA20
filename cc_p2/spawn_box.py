import rospy
from geometry_msgs.msg import Twist
from gazebo_msgs.srv import GetModelState


rospy.init_node('Spawnbox', anonymous = True)


def handel_setBox(req):
    #TODO: spawn box
    print(req)



s = rospy.Service('/box', Twist, handel_setBox)

rospy.spin()
