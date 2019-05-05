#!/usr/bin/env python
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685
import rospy
from roboy_middleware_msgs.msg import MotorCommand
from std_msgs.msg import Int8
from std_msgs.msg import Int16

min_velocity = -130
max_velocity = 130

def map_velocities_to_pwm_signal(velocity):
    stepsize = 0.3076 # 40/130
    max_clockwise_signal = 310 # min_clockwise_signal = 280 - fastest at min
    min_counter_clockwise_signal = 325 # max_counter_clockwise_signal = 365 - fastest at max
    if (velocity < 0 and velocity >= min_velocity):
        pwm_signal = max_clockwise_signal - (-velocity)*stepsize
        print("in neg check: ", pwm_signal)
    elif (velocity > 0 and velocity <= max_velocity):
        pwm_signal = min_counter_clockwise_signal + velocity*stepsize
        print("in pos check: ", pwm_signal)
    elif velocity == 0:
        pwm_signal = 0
        print("Turning off box motors.")
    else:
        print("Carefull, stay within speed boundaries of -130 to 130!")
    return int(pwm_signal)


def move_box_callback(msg):
    for (motor,setpoint) in zip(msg.motors,msg.set_points):
        set_servo_pulse(motor, setpoint)
        #rospy.loginfo(str(motor) + " " + str(setpoint))


def gripper_command_callback(msg):
    gripper_pin = 3
    velocity = msg.data
    stepsize = 0.23076 # 30/130
    # max_counter_clockwise_signal = 175 # min_clockwise_signal = 150 - fastest at min
    # min_clockwise_signal = 120 # max_clockwise_signal = 150 - fastest at max
    if (velocity < 0 and velocity >= min_velocity):
        pwm_signal = 150 + velocity*stepsize
        print("in neg check: ", pwm_signal)
    elif (velocity > 0 and velocity <= max_velocity):
        pwm_signal = 150 - velocity*stepsize
        print("in pos check: ", pwm_signal)
    elif velocity == 0:
        pwm_signal = 150 # turns off gripper
        print("Turning off box motors.")
    else:
        print("Carefull, stay within speed boundaries of -130 to 130!")

    pwm.set_pwm_freq(50)
    pwm.set_pwm(gripper_pin, 0, int(pwm_signal))


# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, input_speed):
    output_signal = map_velocities_to_pwm_signal(input_speed)
    pwm.set_pwm_freq(50)
    pwm.set_pwm(channel, 0, int(output_signal))


# callback for gripper motor
# def set_speed_callback(msg):
    # pwm.set_pwm(3, 0, msg.data)


# Main function.
if __name__ == '__main__':
    # Initialise the PCA9685 using the default address (0x40).
    pwm = Adafruit_PCA9685.PCA9685()

    # Initialize the node and name it.
    rospy.init_node('the_claw')
    rospy.Subscriber("the_claw/MoveBox", MotorCommand, move_box_callback)
    rospy.Subscriber("the_claw/CommandGripper", Int16, gripper_command_callback)
    rospy.Subscriber("the_claw/SetSpeed", Int8, set_speed_callback)

    rospy.spin()
