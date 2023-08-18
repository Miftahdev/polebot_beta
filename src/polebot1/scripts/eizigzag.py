#!/usr/bin/env python3

import rospy
from std_msgs.msg import String, Float64 , Int64
from geometry_msgs.msg import Pose2D , Vector3 ,Twist
import math
import time
global Time_Desired

def input_callback():

    rospy.init_node('zigzag', anonymous=False)

    for i in range(0,6):

        koordinat = Vector3()
        koordinat.x = round((0.2 * i),2) 
        koordinat.y = round((0.2 * i),2)
        koordinat.z = 0

        pub_koordinat = rospy.Publisher('/coordinate', Vector3,queue_size=10)
        pub_koordinat.publish(koordinat)
        
        print("koordinat_X :  ",{koordinat.x})
        print("koordinat_Y :  ",{koordinat.y})
        # print("koordinat_H :  ",{koordinat.z})
        rospy.sleep(1)
    
    for i in range(6,16):
        
        koordinat = Vector3()
        koordinat.x = round((0.2 * i),2) 
        koordinat.y = round((((0.2)*-1) * i +2),2)
        koordinat.z = 0

        pub_koordinat = rospy.Publisher('/coordinate', Vector3,queue_size=10)
        pub_koordinat.publish(koordinat)

        print("koordinat_X : ",{koordinat.x})
        print("koordinat_Y : ",{koordinat.y})
        # print("koordinat_H : ",{koordinat.z})
        rospy.sleep(1)
    
    for i in range(16,21):

        koordinat = Vector3()
        koordinat.x = round((0.2 * i ),2)
        koordinat.y = round(( 0.2 * i - 4),2)
        koordinat.z = 0

        pub_koordinat = rospy.Publisher('/coordinate', Vector3,queue_size=10)
        pub_koordinat.publish(koordinat)
        
        print("koordinat_X : ",{koordinat.x})
        print("koordinat_Y : ",{koordinat.y})
        # print("koordinat_H : ",{koordinat.z})
        rospy.sleep(1)

    rospy.sleep(5)
    print("REVERSE")

    for i in range(21,26):

        koordinat = Vector3()
        koordinat.x = round(((0.2 * i *-1)+8),2)
        koordinat.y = round(( 0.2 * i - 4),2)
        koordinat.z = 0

        pub_koordinat = rospy.Publisher('/coordinate', Vector3,queue_size=10)
        pub_koordinat.publish(koordinat)
        
        print("koordinat_X : ",{koordinat.x})
        print("koordinat_Y : ",{koordinat.y})
        # print("koordinat_H : ",{koordinat.z})
        rospy.sleep(1)
    
    for i in range(26,35):

        koordinat = Vector3()
        koordinat.x = round(((0.2 * i *-1)+8),2)
        koordinat.y = round(((0.2 * i *-1)+ 6),2)
        koordinat.z = 0

        pub_koordinat = rospy.Publisher('/coordinate', Vector3,queue_size=10)
        pub_koordinat.publish(koordinat)
        
        print("koordinat_X : ",{koordinat.x})
        print("koordinat_Y : ",{koordinat.y})
        # print("koordinat_H : ",{koordinat.z})
        rospy.sleep(1)
    
    for i in range(35,41):

        koordinat = Vector3()
        koordinat.x = round(((0.2 * i *-1)+8),2)
        koordinat.y = round((0.2 * i - 8),2)
        koordinat.z = 0

        pub_koordinat = rospy.Publisher('/coordinate', Vector3,queue_size=10)
        pub_koordinat.publish(koordinat)
        
        print("koordinat_X : ",{koordinat.x})
        print("koordinat_Y : ",{koordinat.y})
        # print("koordinat_H : ",{koordinat.z})
        rospy.sleep(1)

    # koordinat.x = 3.8499999999999996
    # koordinat.y = -0.21999999999999975
    # koordinat.z = 0

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
    