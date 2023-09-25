# CircuitPython
This repository will actually serve as an aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Hello_CircuitPython

### Description & Code
I basically just wrote this to get my board to work and connect to VsCode. 
It took longer than I had hoped for this to work but im glad that I got it to work.
The software should be a lot more powerful than an Arduino. 
It compares an ARM processor core to a random 2008 microcontroller.

```python
from time import sleep

while True:
    print("Hello world!")
    sleep(1)

```


### Evidence

//Note to self: Please update this later



### Wiring
There is zero wiring for this assignment as it is a test program to print to the serial monitor.

### Reflection
It was super difficult to get everything set up. The programming was super easy for me to do but getting the board to work properly took a solid 3 and a half hours. I am so glad that we got it working however now I can save my work here and there is zero chance of me losing it. I was so done with using the web-based IDE that would barely run, was full of bugs, and didn't save my work half the time. 




## CircuitPython_Servo

### Description & Code
For this assignment, I was tasked with writing a program that would sweep a servo back and forth. After I got that working I needed to control a servo with either buttons or capacitive touch. Now because the buttons on this thing are so complicated I ended up having to use capacitive touch. Capacitive touch is when you touch a wire and it creates a tiny capacitor between you and the ground which will result in a current sike that can be detected by the microcontroller/processor. I almost got this to work but accidentally used a continuous rotation servo. I tried swapping the servos but the two that I picked out were both really broken. One of them had a screw that was ground to dust with an angle grinder and the other one was jammed inside. I finally got this to work however using a non-continuous rotation servo (0-180*)
```python
# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#towihriuweqhruiywqegr8owrge tesyt tests tetstets tst estsetsetset tsstese test
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Servo standard servo example"""
'''python
import touchio
import time
import board
import pwmio
from adafruit_motor import servo
from digitalio import DigitalInOut, Direction, Pull
angle=0
# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)
# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)
touch_pad = board.A0  # Will not work for Circuit Playground Express!
touch_pad2=board.A1
touch = touchio.TouchIn(touch_pad)
touch2 = touchio.TouchIn(touch_pad2)

while True:
    if touch.value:
        if angle>=180:
            angle=0
        angle=angle-1
        my_servo.angle = angle
    if touch2.value:
        if angle<=0:
            angle=179
        angle=angle+1
        my_servo.angle = angle
    time.sleep(0.05)

```

### Evidence
Here is a video that I recorded with canvas
[Sweeping Servo](https://github.com/solomon4000/eng3/blob/main/CircuitPython%20Servo_%20Solomon%20Lam%20(He_Him)%20-%20Google%20Chrome%202023-09-04%2013-47-12.mp4)

### Wiring
[Diagramn](https://github.com/solomon4000/eng3/blob/main/Screenshot%202023-09-13%208.49.49%20PM.png)
### Reflection
This assignment in all honesty wasn't to difficult. This wasn't nearly as hard as the next assignment that I did. All in all I kind of enjoyed this assignment because it taught me how to code the rather simple things in circuit python.


## CircuitPython_Ultrasonic_Sensor

### Description & Code Snippets
The goal of this assignment was to use an Adafruit metro to read the distance of something with an ultrasonic sensor and use it to write to a neopixel. I accomplished it by having it increase one value and decrease the other depending on the distance.

```python
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(board.D5, board.D6)
import neopixel
import digitalio

led = digitalio.DigitalInOut(board.D4)
pixel_pin = board.A0
num_pixels = 8

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)
cm = 10
#led=(255,255,255)
led.direction = digitalio.Direction.OUTPUT
def god_save_me(color):
    for i in range(num_pixels):
            pixels[i] = color
            pixels.show()
while True:
    led=True
    time.sleep(0.1)
    led=False
    time.sleep(0.1)
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
    
    
```

**Lastly, please end this section with a link to your code or file.**  


### Evidence
Pictures / Gifs of your finished work should go here.  You need to communicate what your thing does.
For making a GIF, I recommend [ezgif.com](https://www.ezgif.com) Remember you can insert pictures using Markdown or HTML to insert an image.


And here is how you should give image credit to someone if you use their work:

Image credit goes to [Rick A](https://www.youtube.com/watch?v=dQw4w9WgXcQ&scrlybrkr=8931d0bc)



### Wiring
[tinkercad.com](https://www.tinkercad.com/learn/circuits).  If you can't find the particular part you need, get creative, and just drop a note into the circuit diagram, explaining.
For example, I use an Arduino Uno to represent my Circuitpython device but write a note saying which board I'm actually using.
Then post an image here.   [Here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)


### Reflection
Don't just tell the reader what went wrong or was challenging!  Describe how you figured it out, share the things that helped you succeed (tutorials, other people's repos, etc.), and then share what you learned from that experience.  **Your underlying goal for the reflection, is to concisely pass on the RIGHT knowledge that will help the reader recreate this assignment better or more easily.  Pass on your wisdom!**





## NextAssignment

### Description & Code Snippets
Write a couple sentences here, describing this assignment, and make sure that you hit these two points:
* What was the goal of the assignment?
* How did you accomplish that goal?
  How you accomplished the goal is NOT a reflection, it is you telling the reader how to do this assignment, in broad strokes.

  Your description is the right place to draw the reader's attention to any important chunks of code. Here's how you make code look like code:

```python
Code goes here

```

**Lastly, please end this section with a link to your code or file.**  

### Evidence

### Wiring
[tinkercad.com](https://www.tinkercad.com/learn/circuits).  If you can't find the particular part you need, get creative, and just drop a note into the circuit diagram, explaining.
For example, I use an Arduino Uno to represent my Circuitpython device but write a note saying which board I'm actually using.
Then post an image here.   [Here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)
### Reflection
Don't just tell the reader what went wrong or was challenging!  Describe how you figured it out, share the things that helped you succeed (tutorials, other people's repos, etc.), and then share what you learned from that experience.  **Your underlying goal for the reflection, is to concisely pass on the RIGHT knowledge that will help the reader recreate this assignment better or more easily.  Pass on your wisdom!**

