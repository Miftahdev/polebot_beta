#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64 , String , Int64
from geometry_msgs.msg import Vector3 , Twist 
import math
import time

L = 0.2

global VX , VY, VT , enc1 , enc1 , enc3 , pulse_m1 , pulse_m2 , pulse_m3

def encoder_Motor1(encoder1):
    global enc1
    rospy.loginfo(rospy.get_caller_id() + " Pulse M1 : %f" ,encoder1.data)
    enc1 = encoder1.data

def encoder_Motor2(encoder2):
    global enc2
    rospy.loginfo(rospy.get_caller_id() + " Pulse M2 : %f" ,encoder2.data)
    enc2 = encoder2.data

def encoder_Motor3(encoder3):
    global enc3
    rospy.loginfo(rospy.get_caller_id() + " Pulse M3 : %f" ,encoder3.data)
    enc3 = encoder3.data

pulse = Vector3()
enc1 = pulse.x
enc2 = pulse.y
enc3 = pulse.z

VX = (((2*pulse.y) - pulse.x - pulse.z)/3)
VY = ((math.sqrt(3)*pulse.z) - (math.sqrt(3)*pulse.x)/3)
VT = ((pulse.x + pulse.y + pulse.z)/3*L)

print("X :       ", {VX})
print("Y :       ", {VY})
print("Heading : ", {VT})

Error_Posisi = Vector3()
VX = Error_Posisi.x
VY = Error_Posisi.y
VZ = Error_Posisi.z

rospy.init_node('Forward_Kinematik', anonymous=False)
pub_posisi = rospy.Publisher('/Error_Position', Vector3, queue_size=10)
pub_posisi.publish(Error_Posisi)    
rate = rospy.Rate(10)
while not rospy.is_shutdown():
    rate.sleep()

if __name__ == '__main__':
    
    rospy.Subscriber("/encoderValue_1",Int64,encoder_Motor1)
    rospy.Subscriber("/encoderValue_2",Int64,encoder_Motor2)
    rospy.Subscriber("/encoderValue_3",Int64,encoder_Motor3)

    rospy.spin()