#!/usr/bin/env python3

import rospy
from std_msgs.msg import String, Float64 , Int64
from geometry_msgs.msg import Pose2D , Vector3 ,Twist
import math
import time

global V1, V2, V3

L = 0.2

def invers_kinematik(velocity):

    global V1, V2, V3

    rospy.loginfo(rospy.get_caller_id() + " VX : %f", velocity.x) # velocity.x kecepatan sumbu X
    rospy.loginfo(rospy.get_caller_id() + " VY : %f", velocity.y) # velocity.y kecepatan sumbu Y
    rospy.loginfo(rospy.get_caller_id() + " VT : %f", velocity.z) # velocity.z kecepatan theta

    V1 = (((-0.5 * velocity.x) + (math.sqrt(3/2) * velocity.y) + (L*velocity.z)))
    V2 = (((-0.5 * velocity.x) - (math.sqrt(3/2) * velocity.y) + (L*velocity.z)))
    V3 = (((velocity.x) + (L*velocity.z)))

    V1 = min(max(V1,-0.1),0.1) # batas pada setiap motor
    V2 = min(max(V2,-0.1),0.1)
    V3 = min(max(V3,-0.1),0.1)

    print("V1 : ",{V1})
    print("V2 : ",{V2})
    print("V3 : ",{V3})

    pub_V1.publish(V1)
    pub_V2.publish(V2)
    pub_V3.publish(V3)
    
    # rate = rospy.Rate(10)
    # while not rospy.is_shutdown():
    #     rate.sleep()
    
if __name__ == '__main__':

    rospy.init_node('Invers_kinematik', anonymous=False)
    rospy.Subscriber("/Velocity_Axis", Vector3, invers_kinematik)
    pub_V1 = rospy.Publisher('/V1', Float64, queue_size=10)
    pub_V2 = rospy.Publisher('/V2', Float64, queue_size=10)
    pub_V3 = rospy.Publisher('/V3', Float64, queue_size=10)

    rospy.spin()