# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(board.D5, board.D6)
import neopixel

pixel_pin = board.A0
num_pixels = 8

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)
cm = 10
while True:
    try:
        cm = sonar.distance
        print(cm)
        led=(0, cm, 255-cm)
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
    
    
