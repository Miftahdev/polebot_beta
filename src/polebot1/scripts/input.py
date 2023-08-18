#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import String, Float64 , Int64
from geometry_msgs.msg import Pose2D , Vector3 ,Twist
import time
import math

Pi = 3.14159265359

def data_input():
    
    coordinate_x = float(input("coordinate_X     :  ")) #VX
    coordinate_y = float(input("coordinate_Y     :  ")) #VY
    coordinate_z = float(input("coordinate_Theta :  "))  #VTHETA
    
    coordinate = Vector3()
    coordinate.x = coordinate_x
    coordinate.y = coordinate_y
    coordinate.z = coordinate_z
    # coordinate.z = (((coordinate_z)*Pi)/180*7)

    pub_coordinate = rospy.Publisher('/coordinate', Vector3, queue_size=10)
    
    rospy.init_node('User_Input', anonymous=False)
    rate = rospy.Rate(10)
      
    while not rospy.is_shutdown():

      print("coordinate_X     : ", {coordinate.x})
      print("coordinate_Y     : ", {coordinate.y})
      print("coordinate_Theta : ", {coordinate.z})
    
      # rospy.Subscriber('/Posisi', Vector3, data_input)
      pub_coordinate.publish(coordinate)
      rate.sleep()
        
if __name__ == '__main__':
    # try:
      data_input()
    # except rospy.ROSInterruptException:
    #    pass