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
#led=(255,255,255)
def god_save_me(color):
    for i in range(num_pixels):
            pixels[i] = color
            pixels.show()
while True:
    try:
        cm = sonar.distance
        print(cm)
        distancebasedcolor=(0, 255-cm*2, cm*2)
        print(distancebasedcolor)
        god_save_me(distancebasedcolor)
        #time.sleep(0.1)
    except RuntimeError:
        print("Retrying!")
    #time.sleep(0.1)
    
    
