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

global VX , VY, VT , enc1 , enc2 , enc3 , V1 , V2, V3 , Pos_X , Pos_Y , omega

def Error_Posisi(posisi):

    posisi_X = posisi.x 
    posisi_Y = posisi.y 
    posisi_T = posisi.z

    # print(posisi_X)
    print(posisi_X,",",posisi_Y)

    rospy.sleep(0.1)
def Show_Position():

    rospy.init_node('Data_Posisi', anonymous=False)
    rospy.Subscriber("/Error_Position", Vector3, Error_Posisi)
    rospy.spin()

if __name__ == '__main__':
    Show_Position()