#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import String, Float64 , Int64
from geometry_msgs.msg import Pose2D , Vector3 ,Twist
import time
import math

global koordinat_X,koordinat_Y,koordinat_T , error_X,error_Y,error_T

KPX = 0.01
KPY = 0.02
KPH = 0

L = 0.2

koordinat_X = 0.0
koordinat_Y = 0.0
koordinat_T = 0.0

posisi_X = 0.0
posisi_Y = 0.0
posisi_T = 0.0

def data_coordinate(koordinat):
  
  global koordinat_X,koordinat_Y,koordinat_T

  koordinat_X = koordinat.x    
  koordinat_Y = koordinat.y    
  koordinat_T = koordinat.z   

  return koordinat_X,koordinat_Y,koordinat_T 

def Error_Posisi(posisi):

  global posisi_X,posisi_Y,posisi_T

  posisi_X = posisi.x 
  posisi_Y = posisi.y 
  posisi_T = posisi.z 
 
  return  posisi_X,posisi_Y,posisi_T

def calculation():

  rospy.init_node('Error', anonymous=False)
  rospy.Subscriber("/coordinate", Vector3, data_coordinate)
  rospy.Subscriber("/Error_Position", Vector3, Error_Posisi)

  rate = rospy.Rate(10)

  while not rospy.is_shutdown():

    Error_X = (koordinat_X - posisi_X)#/7
    Error_Y = (koordinat_Y - posisi_Y)#/7
    Error_T = (koordinat_T - posisi_T)

    MVX = KPX * Error_X  
    MVY = KPY * Error_Y  
    MVH = KPH * Error_T 

    velocity = Vector3()
    velocity.x = MVX 
    velocity.y = MVY 
    velocity.z = MVH 

    pub_velocity = rospy.Publisher('/Velocity_Total', Vector3, queue_size=10)
    pub_velocity.publish(velocity)
    
    print("Error_X     : ", {Error_X})
    print("Error_Y     : ", {Error_Y})
    print("Error_Theta : ", {Error_T})

    print("MV_X     : ", {velocity.x})
    print("MV_Y     : ", {velocity.y})
    print("MV_Theta : ", {velocity.z})

    rate.sleep()
  return

if __name__ == '__main__':

    calculation()
    
    rospy.spin()

