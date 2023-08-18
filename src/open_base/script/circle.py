#!/usr/bin/env python3

import rospy
from std_msgs.msg import String, Float64
from geometry_msgs.msg import Pose2D , Vector3 ,Twist
import math
import time
 

def calculate(koordinat):

    global VX, VY, VT
    
    rospy.loginfo(rospy.get_caller_id() + "Koordinat X : %f" ,koordinat.x)
    rospy.loginfo(rospy.get_caller_id() + "Koordinat Y : %f" ,koordinat.y)
    rospy.loginfo(rospy.get_caller_id() + "Koordinat Z : %f" ,koordinat.z)
    data = 0
    while data < koordinat.x :
        data +=1
        nilai = data/180
        velocity = Vector3()
        velocity.x = math.cos(nilai)
        velocity.y = math.sin(nilai)
        velocity.z = 0
        pub_velocity.publish(velocity)
        
        print("VX = ",{velocity.x})
        print("VY = ",{velocity.y})
        print("VZ = ",{velocity.z})
        rospy.sleep(2)

    velocity.x = 0
    velocity.y = 0
    velocity.z = 0
    pub_velocity.publish(velocity)
    print("VX = ",{velocity.x})
    print("VY = ",{velocity.y})
    print("VZ = ",{velocity.z})
    

if __name__ == '__main__':

    rospy.init_node('Circle_Trajectory', anonymous=False)
    rospy.Subscriber("/Linear_Velocity", Vector3, calculate)
    pub_velocity = rospy.Publisher('/Angular_Velocity', Vector3,queue_size=10)
    rospy.spin()



