#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64 , String , Int64
from geometry_msgs.msg import Vector3 , Twist 
import math
import time

L = 0.2

global VX , VY, VT , enc1 , enc1 , enc3

pulse = Vector3()

def encoder_Motor1(encoder1):
    global enc1
    rospy.loginfo(rospy.get_caller_id() + " Pulse_M1 : %f" , encoder1.data)
    enc1 = encoder1.data
    pulse.x = enc1
    pub_posisi.publish(pulse)
    rospy.sleep(0.1)

def encoder_Motor2(encoder2):
    global enc2
    rospy.loginfo(rospy.get_caller_id() + " Pulse_M2 : %f" , encoder2.data)
    enc2 = encoder2.data
    pulse.y = enc2
    pub_posisi.publish(pulse)
    rospy.sleep(0.1)

def encoder_Motor3(encoder3):
    global enc3
    rospy.loginfo(rospy.get_caller_id() + " Pulse_M3 : %f" , encoder3.data)
    enc3 = encoder3.data
    pulse.z = enc3
    pub_posisi.publish(pulse)
    rospy.sleep(0.1)

rospy.init_node('Integrasi_Node', anonymous=False)

rospy.Subscriber("/encoderValue_1",Int64,encoder_Motor1)
rospy.Subscriber("/encoderValue_2",Int64,encoder_Motor2)
rospy.Subscriber("/encoderValue_3",Int64,encoder_Motor3)

pub_posisi = rospy.Publisher('/Position', Vector3, queue_size=10)

# rate = rospy.Rate(10)

# while not rospy.is_shutdown():
    # rate.sleep()

if __name__ == '__main__':
    
    rospy.spin()