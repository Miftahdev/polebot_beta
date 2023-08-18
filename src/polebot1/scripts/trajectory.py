#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import String, Float64 , Int64
from geometry_msgs.msg import Pose2D , Vector3 ,Twist
import time
import math

global koordinat_X,koordinat_Y,koordinat_T , error_X,error_Y,error_T

KPX = 0.525 #0.1
KPY = 0.525
KPH = 0.5#0.001

L = 0.2

koordinat_X = 0
koordinat_Y = 0
koordinat_T = 0

posisi_X = 0
posisi_Y = 0
posisi_T = 0

theta = 0

MVX = 0
MVY = 0
MVH = 0

V1 = 0
V2 = 0
V3 = 0

sudut = 0

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
    posisi_T = posisi.z #kecepatan sudut ini teh
 
    return  posisi_X,posisi_Y,posisi_T

def calculation():
    rospy.init_node('Invers_Kinematik', anonymous=False)
    rospy.Subscriber("/coordinate", Vector3, data_coordinate)
    rospy.Subscriber("/Error_Position", Vector3, Error_Posisi)

    rate = rospy.Rate(100)
        
    while not rospy.is_shutdown():

        Error_X = round((koordinat_X - posisi_X),3)
        Error_Y = round((koordinat_Y - posisi_Y),3)
        omega = round((posisi_T),2)

        print("Error_X     : ", {Error_X})
        print("Error_Y     : ", {Error_Y})
        print("Omega       : ", {omega})
        sudut = Error_Y/Error_X
        theta = math.atan(degree*sudut)
        MVX = math.cos(theta)*(KPX * Error_X) -  math.sin(theta)(KPY * Error_Y)
        MVY = (math.sin(theta)*-1*(KPX * Error_X)) + math.cos(theta)(KPY * Error_Y) 
        MVH = (KPH * omega)

        MVX = min(max(MVX,-0.06),0.06) # batas jarak
        MVY = min(max(MVY,-0.04),0.04)
        # MVH = min(max(MVH,-0.04),0.04)

        print("MV_X     : ", {MVX})
        print("MV_Y     : ", {MVY})
        print("MV_Theta : ", {MVH})

        V1 = round(((((-0.5) * MVX) - (((math.sqrt(3) * MVY)/2)) + (L*MVH))),2)
        V2 = round((((MVX) + ((L*MVH)))),2)
        V3 = round(((((-0.5) * MVX) + (((math.sqrt(3) * MVY)/2)) + (L*MVH))),2)

        print("V1     : ", {V1})
        print("V2     : ", {V2})
        print("V3     : ", {V3})

        pub_V1 = rospy.Publisher('/V1', Float64, queue_size= 10)
        pub_V2 = rospy.Publisher('/V2', Float64, queue_size= 10)
        pub_V3 = rospy.Publisher('/V3', Float64, queue_size= 10)

        pub_V1.publish(V1)
        pub_V2.publish(V2)
        pub_V3.publish(V3)

        rate.sleep()
    return

if __name__ == '__main__':

    calculation()
    
    rospy.spin()

# def PID(Kp, ki , kd, MV_bar = 0):
#     e_prev = 0
#     t_prev = 0
#     I = 0

#     MV = MV_bar

#     while True :
#         t,PV,SP = yield MV
#         e = SP - PV
#         P = Kp*e
#         I = I + ki * e * (t - t_prev)
#         D = kd*(e - e_prev)/(t - t_prev)

#         MV = MV_bar + P + I + D

#         e_prev = e
#         t_prev = t