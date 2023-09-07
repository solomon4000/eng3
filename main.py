# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#towihriuweqhruiywqegr8owrge tesyt tests tetstets tst estsetsetset tsstese test
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Servo standard servo example"""
import time
import board
import pwmio
from adafruit_motor import servo
from digitalio import DigitalInOut, Direction, Pull

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)
switch = DigitalInOut(board.D7)
switch2 = DigitalInOut(board.D8)
# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)
