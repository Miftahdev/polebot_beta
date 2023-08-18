#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64 , String , Int64
from geometry_msgs.msg import Vector3 , Twist 
import math
import time

L = 0.2
X_max = 857.9617834#708.3333333333334 
Y_max = 859.5541401#788.0831174438391 #2100 
Theta_max = 4671.66 #2872 #180.8 

global VX , VY, VT , enc1 , enc2 , enc3 , V1 , V2, V3

enc1 = 0
enc2 = 0
enc3 = 0

V1 = 0
V2 = 0
V3 = 0

SX = 0
SY = 0
ST = 0

Pos_X = 0
Pos_Y = 0

def encoder_Motor1(encoder1):
    global enc1
    enc1 = encoder1.data

def encoder_Motor2(encoder2):
    global enc2
    enc2 = encoder2.data

def encoder_Motor3(encoder3):
    global enc3
    enc3 = encoder3.data

def Velocity_1(Vel_1):
    global V1
    V1 = Vel_1.data

def Velocity_2(Vel_2):
    global V2
    V2 = Vel_2.data

def Velocity_3(Vel_3):
    global V3
    V3 = Vel_3.data

def Forward_Kinematik():

    rospy.init_node('Odometri', anonymous=False)
    rospy.Subscriber("/encoderValue_1",Int64,encoder_Motor1)
    rospy.Subscriber("/encoderValue_2",Int64,encoder_Motor2)
    rospy.Subscriber("/encoderValue_3",Int64,encoder_Motor3)
    
    rospy.Subscriber("/V1", Float64, Velocity_1)
    rospy.Subscriber("/V2", Float64, Velocity_2)
    rospy.Subscriber("/V3", Float64, Velocity_3)

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():

        SX = (((2*enc2) - enc1 - enc3)/3)
        SY = (((math.sqrt(3)*enc3) - (math.sqrt(3)*enc1))/3)
        ST = ((V1 + V2 + V3)/(3*L))

        print("X = ",{SX})
        print("Y = ",{SY})
        print("H = ",{ST})

        Pos_X = round((1 *((SX)/X_max)),3)
        Pos_Y = round((1 *((SY)/Y_max)),3)
        omega = round((ST),1)

        print("Posisi_X = ",{Pos_X})
        print("Posisi_Y = ",{Pos_Y})
        print("Omega    = ",{omega})

        Posisi = Vector3()
        Posisi.x = Pos_X
        Posisi.y = Pos_Y
        Posisi.z = omega

        pub_posisi = rospy.Publisher('/Error_Position', Vector3, queue_size=10)
        pub_posisi.publish(Posisi)
        rate.sleep()
    return

if __name__ == '__main__':
    Forward_Kinematik()

    rospy.spin()