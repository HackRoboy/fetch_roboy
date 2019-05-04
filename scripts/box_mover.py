#!/usr/bin/env python
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685
from roboy_middleware_msgs.msg import MotorCommand

class Mover():
    "Class that calculates pwm inputs depending on velocities input (RPM)."

    def __init__(self, servo_pwm_pin, velocity):
        self.max_vel = 130 # max RPM
        self.min_vel = -130
        self.servo_pwm_pin = servo_pwm_pin
        self.velocity = velocity
        if not (velocity <= 130 and velocity >= -130):
            print("Out of range! Valid velocity range is -130 to 130.")

    def map_velocities_to_pwm_signal(self):
        stepsize = 0.3076 # 40/130
        max_clockwise_signal = [270] # min_clockwise_signal = 310 - fastest at min
        min_counter_clockwise_signal = [325] # max_counter_clockwise_signal = 365 - fastest at max
        if (self.velocity < 0 and self.velocity >= -130):
            pwm_signal = max_clockwise_signal - self.velocity*stepsize
            print("in neg check: ", pwm_signal)
        elif (self.velocity > 0 and self.velocity <= 130) :
            pwm_signal = min_counter_clockwise_signal + self.velocity*stepsize
            print("in pos check: ", pwm_signal)
        pwm_signal = 0
        print("0 : ", pwm_signal)

        return int(pwm_signal)
