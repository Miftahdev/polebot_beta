#!/usr/bin/env python3

import rospy
from std_msgs.msg import String, Float64
from geometry_msgs.msg import Pose2D , Vector3 ,Twist
import math
import time

global V1, V2, V3

L = 20

def invers_kinematik(velocity):
    rospy.loginfo(rospy.get_caller_id() + "VX : %f", velocity.x)
    rospy.loginfo(rospy.get_caller_id() + "VY : %f", velocity.y)
    rospy.loginfo(rospy.get_caller_id() + "VT : %f", velocity.z)

    V1 = ((-1*(velocity.x/2)) - ((math.sqrt(3*velocity.y))/2) + (L*velocity.z))
    V2 = ((velocity.x) + (L*velocity.z))
    V3 = ((-1*(velocity.x/2)) + ((math.sqrt(3*velocity.y)/2)) + (L*velocity.z))
    
    print("V1 : ",{V1})
    print("V2 : ",{V2})
    print("V3 : ",{V3})

    pub_V1 = rospy.Publisher('/V1', Float64, queue_size=10)
    pub_V2 = rospy.Publisher('/V2', Float64, queue_size=10)
    pub_V3 = rospy.Publisher('/V3', Float64, queue_size=10)

    pub_V1.publish(V1)
    pub_V2.publish(V2)
    pub_V3.publish(V3)

def connect_2():
    rospy.init_node('Invers_kinematik', anonymous=False)
    rospy.Subscriber("/Angular_Velocity", Vector3, invers_kinematik)

    rospy.spin()

if __name__ == '__main__':
    connect_2()