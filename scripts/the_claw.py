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
    	set_servo_pulse(motor,int(setpoint))
	#rospy.loginfo(str(motor) + " " + str(setpoint))

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 50 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse1 = pulse*1000
    pulse2 = pulse1//pulse_length
    print('{0}us pulse'.format(pulse2))
    pwm.set_pwm(channel,0, pulse2)


def set_speed_callback(msg):
    set_servo_pulse(7,msg.data)
   # pwm.set_pwm(7, 0,msg.data)  
   # time.sleep(5)
   # pwm.set_pwm(7, 0, 0)

# Main function.
if __name__ == '__main__':
    # Initialise the PCA9685 using the default address (0x40).
    pwm = Adafruit_PCA9685.PCA9685()
    # Set frequency to 60hz, good for servos.
    print('Starting \n')
    pwm.set_pwm_freq(50)
    pwm.set_pwm(7,0, 200)
    print('Sleeping \n ')
    time.sleep(3)
    pwm.set_pwm(7,0,0)
    print('Finished')
    # Initialize the node and name it.
    rospy.init_node('the_claw')
    rospy.Subscriber("the_claw/MotorCommand", MotorCommand, motor_command_callback)
    rospy.Subscriber("the_claw/SetSpeed", Int8, set_speed_callback)

    rospy.spin()
