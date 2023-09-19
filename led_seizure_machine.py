# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
# SPDX-License-Identifier: MIT
"""CircuitPython Blink Example - the CircuitPython 'Hello, World!'"""
import time
import board
import random
import digitalio

led = digitalio.DigitalInOut(board.D4)
led.direction = digitalio.Direction.OUTPUT
led2 = digitalio.DigitalInOut(board.D3)
led2.direction = digitalio.Direction.OUTPUT

while True:
    ledDelay=0.05
    led.value = True
    led2.value=False
    time.sleep(ledDelay)
    led.value = False
    led2.value=True
    time.sleep(ledDelay)
