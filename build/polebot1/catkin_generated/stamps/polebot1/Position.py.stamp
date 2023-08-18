#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64 , String , Int64
from geometry_msgs.msg import Vector3 , Twist 
import math
import time

# pulse per meter
# PPM1 = 345.22292992 #4315.286624
# PPM2 = 341.910828   #4273.88535
# PPM3 = 342.42038216 #4280.254777 

# D1 = 0.0
# D2 = 0.0
# D3 = 0.0

# SX  = 0.0
# SY  = 0.0
# ST  = 0.0

L = 0.2
X_max = 708.3333333333334 
Y_max = 788.0831174438391 #2100 
Theta_max = 4671.66 #2872 #180.8 

global VX , VY, VT , enc1 , enc1 , enc3 , V1 , V2, V3

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
    # rospy.loginfo(rospy.get_caller_id() + " Pulse_M1 : %f" , encoder1.data)
    enc1 = encoder1.data
    # rospy.sleep(0.0001)
    # rate = rospy.Rate(0.001)

def encoder_Motor2(encoder2):
    global enc2
    # rospy.loginfo(rospy.get_caller_id() + " Pulse_M2 : %f" , encoder2.data)
    enc2 = encoder2.data
    # rospy.sleep(0.0001)
    # rate = rospy.Rate(0.001)

def encoder_Motor3(encoder3):
    global enc3
    # rospy.loginfo(rospy.get_caller_id() + " Pulse_M3 : %f" , encoder3.data)
    enc3 = encoder3.data
    # rospy.sleep(0.0001)
    # rate = rospy.Rate(0.0001)

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

    rospy.init_node('Integrasi_Node', anonymous=False)
    rospy.Subscriber("/encoderValue_1",Int64,encoder_Motor1)
    rospy.Subscriber("/encoderValue_2",Int64,encoder_Motor2)
    rospy.Subscriber("/encoderValue_3",Int64,encoder_Motor3)
    
    rospy.Subscriber("/V1", Float64, Velocity_1)
    rospy.Subscriber("/V2", Float64, Velocity_2)
    rospy.Subscriber("/V3", Float64, Velocity_3)

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():

        # D1 = enc1 / PPM1
        # D2 = enc2 / PPM2
        # D3 = enc3 / PPM3

        SX = (((2*enc2) - enc1 - enc3)/3)
        SY = (((math.sqrt(3)*enc3) - (math.sqrt(3)*enc1))/3)
        ST = ((V1 + V2 + V3)/(3*L))

        print("X = ",{SX})
        print("Y = ",{SY})
        print("H = ",{ST})

        Pos_X = round((1 *((SX)/X_max)),3)
        Pos_Y = round((1 *((SY)/Y_max)),2)
        omega = round((ST),2)

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

     # Pos_Theta = (6.283 *((ST)/Theta_max)) # ini kalau kecepatan sudut
 # Pos_Theta = round((360 *((ST)/Theta_max)),0) # ini awal
 # Pos_Theta = min(max(Pos_Theta,0),360)
      
#         # kenapa 43 itu konversi ke radian/s

#         # if Pos_Theta >= 6.283 :
#             # Pos_Theta == 0
#         # elif Pos_Theta <= -6.283 :
#             # Pos_Theta == 0
# #