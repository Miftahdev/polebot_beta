#!/usr/bin/env python3

import rospy
from std_msgs.msg import String, Float64 , Int64
from geometry_msgs.msg import Pose2D , Vector3 ,Twist
import math
import time
global Time_Desired

def input_callback(velocity):
    global VX, VY, VT ,Time_Desired
    rospy.loginfo(rospy.get_caller_id() + "Velocity : %f" ,velocity.data)

    for i in range(velocity.data):

        # nilai = data/180
        velocity = Vector3()
        velocity.x = math.cos(i)/5
        velocity.y = math.sin(i)/5
        velocity.z = 0

        pub_velocity.publish(velocity)
        
        print("VX = ",{velocity.x})
        print("VY = ",{velocity.y})
        print("VZ = ",{velocity.z})
        rospy.sleep(1)

    velocity.x = 0
    velocity.y = 0
    velocity.z = 0
    pub_velocity.publish(velocity)
    print("VX = ",{velocity.x})
    print("VY = ",{velocity.y})
    print("VZ = ",{velocity.z})
    
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        rate.sleep()

if __name__ == '__main__':
   
    rospy.init_node('Circle_Trajectory', anonymous=False)
    rospy.Subscriber("/Velocity", Int64, input_callback)
    pub_velocity = rospy.Publisher('/Velocity_Axis', Vector3,queue_size=10)
    rospy.spin()
    