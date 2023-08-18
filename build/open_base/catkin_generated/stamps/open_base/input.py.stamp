#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import String, Float64
from geometry_msgs.msg import Pose2D , Vector3 ,Twist

def data_input():
    koordinat = Vector3()
    koordinat.x = float(input("Velocity_x : ")) #VX
    koordinat.y = float(input("Velocity_Y : ")) #VY
    koordinat.z = float(input("Velocity_T :"))  #VTHETA
    
    pub_koordinat = rospy.Publisher('/Linear_Velocity', Vector3, queue_size=10)
    rospy.init_node('User_Input', anonymous=False)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
      rospy.loginfo(koordinat.x)
      rospy.loginfo(koordinat.y)
      rospy.loginfo(koordinat.z)
    
      pub_koordinat.publish(koordinat)
      rate.sleep()
  
if __name__ == '__main__':
    try:
      data_input()
    except rospy.ROSInterruptException:
       pass