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
I basicaly just wrote this to get my board to work and connect to VsCode. 
It took longer than I had hoped for this to work but im glad that I got it to work.
The software should be a lot more powerfull than an arduino. 
It's comparing an ARM procesor core to a random 2008 microcontroller.

```python
from time import sleep

while True:
    print("Hello world!")
    sleep(1)

```


### Evidence

//Note to self: please update this later



### Wiring
There is zero wiring for this assignment as it is a test program to pring to the serial monitor.

### Reflection
It was super difficult to get everything setup. The programing was super easy for me to do but getting the board to work properley took a solid 3 and a half hours. I am so glad that we got it working however as now I can save my work to here and there is zero chance of me loosing it. I was so done with using the web based IDE that would barely ran, was full of bugs, and didn't save my work half the time. 




## CircuitPython Servo

### Description & Code
For this assignment I was tasked with writing a program that would sweep a servo back and forth. After I got that working I needed to control a servo with either buttons or capacitive touch. Now because the buttons on this thing are so complicated I ended up having to use capacitive touch. Capacitive touch is when you touch a wire and it creates a tiny capacitor between you and ground which will result in a current sike that can be detected by the microcontroller/processor. I almost got this to work but accidentaly used a continuos rotation servo. I tried swapping the servos but the two that I picked out were both really broken. One of them had a screw that was ground to dust with an angle grinder and the other one was jammed inside.
```python
# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#towihriuweqhruiywqegr8owrge tesyt tests tetstets tst estsetsetset tsstese test
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Servo standard servo example"""
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
[Sweeping Servo]([https://user-images.githubusercontent.com/54641488/192549584-18285130-2e3b-4631-8005-0792c2942f73.gif](https://github.com/solomon4000/eng3/blob/main/CircuitPython%20Servo_%20Solomon%20Lam%20(He_Him)%20-%20Google%20Chrome%202023-09-04%2013-47-12.mp4)https://github.com/solomon4000/eng3/blob/main/CircuitPython%20Servo_%20Solomon%20Lam%20(He_Him)%20-%20Google%20Chrome%202023-09-04%2013-47-12.mp4)

### Wiring

### Reflection



## CircuitPython_LCD

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

