#!/usr/bin/env python
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685
from roboy_middleware_msgs.msg import MotorCommand

class Mover():
    "Class that calculates pwm inputs depending on velocities input (RPM)."

    def __init__(self, servo_pwm_pins, velocities):
        self.servo_pwm_pins = servo_pwm_pins
        self.velocities = velocities
        self.set_pwm_freq = []

    def map_velocities_to_pwm_signal(self):
        stepsize = 0.3077
        clockwise_signal = [270, 310]
        counter_clockwise_signal = [325, 365]
