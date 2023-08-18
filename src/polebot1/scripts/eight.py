#!/usr/bin/env python3

import rospy
from std_msgs.msg import String, Float64 , Int64
from geometry_msgs.msg import Pose2D , Vector3 ,Twist
import math
import time
global Time_Desired

def input_callback():

    rospy.init_node('Circle_Trajectory', anonymous=False)

    # for i in range(0,360):
    for i in range(0,390):

        koordinat = Vector3()
        koordinat.x = round((math.cos(math.radians(i))),3)
        koordinat.y = round((math.sin(math.radians(2*i)))/2,3) 
        koordinat.z = 0

        pub_koordinat = rospy.Publisher('/coordinate', Vector3,queue_size=10)
        pub_koordinat.publish(koordinat)
        
        print("koordinat_X :  ",{koordinat.x})
        print("koordinat_Y :  ",{koordinat.y})
        # print("koordinat_H :  ",{koordinat.z})
        rospy.sleep(0.1)
    
    pub_koordinat.publish(koordinat)

    print("Koordinat_X = ",{koordinat.x})
    print("Koordinat_X = ",{koordinat.y})

    pub_koordinat = rospy.Publisher('/coordinate', Vector3,queue_size=10)

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        rate.sleep()

if __name__ == '__main__':
   input_callback()
   rospy.spin()
    