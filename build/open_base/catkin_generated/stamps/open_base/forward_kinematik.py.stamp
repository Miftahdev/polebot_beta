#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64 , String
from geometry_msgs.msg import Vector3 , Twist 
import math
import time

global VX , VY, VT

def encoder_1 (enc_1):
    rospy.loginfo(rospy.get_caller_id() + "ENC1 : %f", enc_1.data)

def encoder_2 (enc_2):

    rospy.loginfo(rospy.get_caller_id() + "ENC2 : %f", enc_2.data)

def encoder_3 (enc_3):
    rospy.loginfo(rospy.get_caller_id() + "ENC3 : %f", enc_3.data)

# VX = (((2*enc_2.data) - enc_1.data - enc_3.data)/3)
# VY = ((math.sqrt(3)*enc_3.data) - (math.sqrt(3)*enc_1.data)/3)
# VT = ((enc_1.data + enc_2.data + enc_3.data)/3)

# print("X : ", {VX})
# print("Y : ", {VY})
# print("Theta : ", {VT})


def connect ():
    rospy.init_node('Forward_Kinematik', anonymous=False)
    rospy.Subscriber("/encoderValue_1",Float64,encoder_1)
    rospy.Subscriber("/encoderValue_2",Float64,encoder_2)
    rospy.Subscriber("/encoderValue_3",Float64,encoder_3)

    rospy.spin()

if __name__ == '__main__':
    connect()