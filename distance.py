# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)
import neopixel

led = neopixel.NeoPixel(board.NEOPIXEL, 1)

led.brightness = 1.0
while True:
    try:
        print((sonar.distance,))
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
    led=(0, sonar.distance, 255-sonar.distance) 
    
