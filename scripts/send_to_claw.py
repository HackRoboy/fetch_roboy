#!/usr/bin/env python
from __future__ import division
import time

import rospy
from roboy_middleware_msgs.msg import MotorCommand
from std_msgs.msg import Int8

def talker():
    pub = rospy.Publisher('the_claw/MotorCommand', MotorCommand, queue_size=10)
    rospy.init_node('talker',anonymous=True)
    rate = rospy.Rate(0.1) #10 Hz

    while not rospy.is_shutdown():
        cmd = MotorCommand()
        cmd.id = 0
        cmd.motors = [6]
        cmd.set_points = [0.5]
        rospy.loginfo(cmd)
        pub.publish(cmd)
	rate.sleep()
	cmd.id = 0
	cmd.motors =[6]
	cmd.set_points =[1.0]
	rospy.loginfo(cmd)
	pub.publish(cmd)
	rate.sleep()
	

# Main function.
if __name__ == '__main__':
    # Initialise the PCA9685 using the default address (0x40).
     try:
        talker()
     except rospy.ROSInterruptException:
        pass
