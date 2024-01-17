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
Speaker=digitalio.DigitalInOut(board.D0)
Speaker.direction=digitalio.Direction.OUTPUT
while True:
    led.value = True
    Speaker.value=True
    led2.value=False
    time.sleep(0.025)
    led.value = False
    led2.value=True
    Speaker.value=False
    time.sleep(0.025)
