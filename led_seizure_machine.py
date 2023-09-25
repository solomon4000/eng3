# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
# SPDX-License-Identifier: MIT
# Build this circuit with two 100W COB leds being driven with an irf520 MOSFET
# Trust me don't do it 💀💀💀
"""CircuitPython Blink Example - the CircuitPython 'Hello, World!'"""
import time
import board
import digitalio

led = digitalio.DigitalInOut(board.LED)
led2=digitalio.DigitalInOut(board.D4)
led2.direction=digitalio.Direction.OUTPUT
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    led.value=False
    time.sleep(0.1)
    led.value = False
    led.value=True
    time.sleep(0.1)
