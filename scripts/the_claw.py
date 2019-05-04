#!/usr/bin/env python
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685
import rospy
from roboy_middleware_msgs.msg import MotorCommand
from std_msgs.msg import Int8

def motor_command_callback(msg):
    for (motor,setpoint) in zip(msg.motors,msg.set_points):
    	pwm.set_pwm(motor, 0, int(setpoint))
	#rospy.loginfo(str(motor) + " " + str(setpoint))

def set_speed_callback(msg):
    pwm.set_pwm(7, 0, 180+msg.data)
    pwm.set_pwm(7, 0, 180-msg.data)


# Main function.
if __name__ == '__main__':
    # Initialise the PCA9685 using the default address (0x40).
    pwm = Adafruit_PCA9685.PCA9685()
    # Set frequency to 60hz, good for servos.
    pwm.set_pwm_freq(60)
    # Initialize the node and name it.
    rospy.init_node('the_claw')
    rospy.Subscriber("the_claw/MotorCommand", MotorCommand, motor_command_callback)
    rospy.Subscriber("the_claw/SetSpeed", Int8, set_speed_callback)

    rospy.spin()
