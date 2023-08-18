#!/usr/bin/env python3

import rospy
from std_msgs.msg import String, Float64
from geometry_msgs.msg import Pose2D , Vector3 ,Twist
import math

def calculate():
    rospy.init_node('Circle_Trajectory', anonymous=False)

    data = 0
    while data < 1080:
        data +=1
        nilai = data/180
        VX = math.cos(nilai)
        VY = math.sin(nilai)
        VT = 0
        print("VX = ",{VX})
        global data_1, data_2,data_3
        pub_1 = rospy.Publisher("set_point_1", Float64, queue_size=10)
        pub_2 = rospy.Publisher("set_point_2", Float64, queue_size=10)
        pub_3 = rospy.Publisher("set_point_3", Float64, queue_size=10)
        rate = rospy.Rate(10)
        # rospy.sleep(2)
        while not rospy.is_shutdown():
            data_1 = VX
            data_2 = VY
            data_3 = VT

            rate.sleep()
            
if __name__ == '__main__':
    try:
        calculate()
    except rospy.ROSInterruptException:
        pass
