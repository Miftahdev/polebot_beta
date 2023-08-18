#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import String, Float64 , Int64
from geometry_msgs.msg import Pose2D , Vector3 ,Twist

def data_input():
    
    Velocity_Input = int(input("VELOCITY_INPUT : "))# time input
    
    pub_velocity= rospy.Publisher('/Velocity', Int64, queue_size=10)
    rospy.init_node('User_Input', anonymous=False)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
      rospy.loginfo(Velocity_Input)
      pub_velocity.publish(Velocity_Input)
      rate.sleep()
  
if __name__ == '__main__':
    try:
      data_input()
    except rospy.ROSInterruptException:
       pass