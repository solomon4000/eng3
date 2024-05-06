# CircuitPython

## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#MotorControl)
* [Onshape_Swing_arm](#Onshape_Swing_arm)
---

## Hello_CircuitPython

### Description & Code
I basically just wrote this to get my board to work and connect to VsCode. 
It took longer than I had hoped for this to work but im glad that I got it to work.
The software should be a lot more powerful than an Arduino. 
```python
from time import sleep

while True:
    print("Hello world!")
    sleep(1)

```


### Evidence

![image](https://github.com/solomon4000/eng3/assets/90640484/519774d0-49d0-4d0e-a8ad-c077aa374fba)




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
![image](https://github.com/solomon4000/eng3/blob/main/ezgif.com-video-to-gif.gif) 



### Wiring
![capture](https://github.com/solomon4000/eng3/blob/main/Capture.PNG)


### Reflection
This assignment was absurdly difficult. This is because it would bug out and crash every time. 
I spent two block days just trying to get my code to upload. I am not sure how I maneged to actualy do this in the end. 
It was way to hard for me to do because it would not cooperate. I found the best way to do it is to install a clean operating system to the board.
I did not like this assignment at all and spent so much time on this.





## MotorControl

### Description & Code Snippets
The goal of this assignment is to make a Adafruit Metro control a motor with a potentiometer. 
It will spin faster the more you turn it one way and if you turn it backwards it will spin the other way. 
It required around 8 lines of code to write. It was way easier than last time.
I am glad we used a power MOSFET instead of a to-92 BJT. I don't think you can drive any bigger of a motor with a 2n2222.
```python
import board
import analogio

motor=analogio.AnalogOut(board.A0)
pot=analogio.AnalogIn(board.A1)
while True:
    speed=pot.value
    motor.value=pot.value

```

### Evidence
[video](https://drive.google.com/file/d/14ck8YZ2rQx7RsFLB73tYePxirN_MLrNF/view?usp=share_link)
### Wiring
![image](https://github.com/solomon4000/eng3/assets/90640484/d0d37feb-503e-4b8c-adf3-99a193652d14)

### Reflection
I didn't spend any time on this. I maneged to get it complete within a couple minutes. 
It was realy easy except for the fact that I couldn't remeber what was the gate/drain/source.

## Onshape_Swing_arm

### Description
The purpose of this assingment was to 3D model a mystery part with just some drawings. 
It was very trivial due to the fact that it was very simple shapes that I had to create. 
I maneged to get this done in around one day. I did pretty good.

### Evidence
![image](https://github.com/solomon4000/eng3/assets/90640484/0c159551-2582-4987-93ef-6ad954d52f0d)


### Part link 
[Document](https://cvilleschools.onshape.com/documents/defe20b1b9dc44ffe5f45cb8/w/382815002ab9d6151072951e/e/53fc0df9791c9142b67e38cc)

### Reflection
This asignment was pretty easy for me to do. I learned to pay closer attention to the details. 
This is because I thought that simply changing one dimension would be all that is neccesary to get it to change. 
When I attempted this however all of the other lines/angles changed because nothing was constrained properly. 
In order to have a good outcome you have to make sure that each angle is related to the other in the right way, 
or else it will completley mess up when you try to modify one variable.

## Onshape_Hanger

### Description
The prupose of this assignment was to build a 3D model of another mysterious part to practice designing things from 2D drawings in Onshape.
I liked it as it helped me shapen my rusty Onshape skills.
### Evidence
![image](https://github.com/solomon4000/eng3/assets/90640484/6d55901b-84fb-4cec-8aae-34033f36d4f3)

### Document Link
[Document](https://cvilleschools.onshape.com/documents/defe20b1b9dc44ffe5f45cb8/w/382815002ab9d6151072951e/e/53fc0df9791c9142b67e38cc)

### Reflection
This asignment was also rather easy for me to do. It only took me one class period for me to complete this assignment. 
One lesson I learned was to pay attention to small details. I went checking every filet, extrude, and hole only to realize that I forgot to mirror two features. I spent a lot of time trying to figure out what the problem was but I did eventualy realize that I forgot to mirror something even though it looked completley right to my brain.

## Onshape_Multipart_Studio
### Description
In this assignment I made a microphone stand in onshape. This required the use of multiple parts as it was quite sophisticated and complex. If you notice I have it upside down as I created the sketch on the wrong plane. Oh well i'm human like the rest of us and is to lazy to fix such small irelavent mistakes.

### Evidence
![image](https://github.com/solomon4000/eng3/blob/main/Screenshot%202024-01-07%20185224.png)

### Document Link
[Document](https://cvilleschools.onshape.com/documents/8dc95f82a347957a36093b26/w/5efdba9ff861aa81f4b4eb57/e/d74a9a315c8fc1ded22e967a)

### Reflection 
This is one of those assignments I don't like to do, not because of how difficult it is but rather because of how I have to do the same thing over and over with tiny variations each time. I would rather do something complex that ends up being satisfying in the end because of how complicated it is not doing one thing over and over but making part XYZ 3mm longer.

## Onshape_Pliers

### Description
The purpose of this assignment was to make a pair of pliers in an assembaly. I was given the parts that I needed so that if I did the assembaly right it would consistently be correct. I did not like this assignment as like last time it was doing one assignment multiple times.

### Evidence
![image](https://github.com/solomon4000/eng3/assets/90640484/d193987d-d533-47fd-97ad-025397397524)


### Description
[Document](https://cvilleschools.onshape.com/documents/a3e877a128ffd4c685250757/w/b4915ca675761f21034702f9/e/96ee70b03795abed110595d8)

### Reflection
This is another assignment that took a long time because I had to make a copy of one thing and make a slight variation of it each time. I would rather be doing one assignment that is more complicated like an engine, mechanical transmission or turbojet, because it would be really satisfying in the end seeing the result. I learned how to have patience with onshape while working on this. 


## Rotary_Encoder_LCD
### Description
In this assignment I made an lcd print stop, go slowly, or go. I did this using the rotary encoder with the built in LCD library. 
I despised this assignment with every fiber of my being as I spent 8 hours trying to get a peice of code with 9 lines on it to work. 
I solved this problem in the end however as I found that the LCD was drawing to much power on startup (though there weren't any capacitors of any size on the board which makes it bizare). 

### Evidence
//fill this in later

### Code
```python
import rotaryio
import board
import neopixel
import digitalio
from lib.lcd.lcd import LCD
from lib.lcd.i2c_pcf8574_interface import I2CPCF8574Interface
enc = rotaryio.IncrementalEncoder(board.D4, board.D3, divisor=2)
lcd = LCD(I2CPCF8574Interface(board.I2C(), 0x3f), num_rows=2, num_cols=16)
led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 0.3
led[0] = (255, 0, 0)
button = digitalio.DigitalInOut(board.D2)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
button_state = None
lcd.set_cursor_pos(0,0)
lcd.print("Hello world")
while True:
    if not button.value and button_state is None:
        button_state = "pressed"
    if button.value and button_state == "pressed":
        print("Button is pressed")
        button_state = None
```
### Reflection
I have found that the best way to ensure succes is to make sure that the lcd is not plugged in before the board gets turned on. Once the board opens you can connect the LCD to the board. This is because it creates a power surge on the microcontroller.

## Photo interupter

### Description
This assignment was not to difficult because I used some code I found from last year. 
I was instructed to make a photo interupter count how many times I passed a solid object through it.
This was very simple as I just had to count how many times a certain pin was activated.

### Evidence
![A14](https://github.com/solomon4000/eng3/assets/90640484/ae3faca4-968e-4ab2-bb7c-e5fdfb22e200)


### Code
```python
#this shouldnt be so difficult
#Why won't it work?
import time
import digitalio
import board
from digitalio import DigitalInOut, Direction, DriveMode, Pull
print("srdg")
photointerupter=digitalio.DigitalInOut(board.D7)
photointerupter.direction.INPUT
photointerupter.pull = Pull.UP
now = time.monotonic()  # Time in seconds since power on
count=0
thing=False
while True:
    if photointerupter.value:
         count=count+1
         print("test")
    if (now + 4) < time.monotonic():  # If 3 milliseconds elapses
        print(count)
        count=0
        now = time.monotonic()
    time.sleep(0.05)
```
### Reflection
This assignment was not very difficult as I just had to count how many times it passed through the detector. 
You will have noticed my comments at the top and that is because with circuit python I have spent more time trying to get code
to upload to the board than I have spent getting the code to work.

## Stepper motor and limit switches
### Description
For this assignment I had to make a stepper spin one way and then spin the other when a switch is toggled. I did this with interupts and such. This assignment was not to difficult.

### Evidence
//Update this later
### Code
```python
"""
Engineering 3 
Limit Switch + Stepper Motor STARTER CODE

"""

# Imports the needed libraries for your board. 
import asyncio
import board
import keypad
import time
import digitalio
from lib.adafruit_motor import stepper


DELAY = 0.002   # Sets the delay time for in-between each step of the stepper motor.
STEPS = 200    # Sets the number of steps. 100 is half a full rotation for the motor we're using. 

# Set up the digital pins used for the four wires of the stepper motor. 
coils = (
    digitalio.DigitalInOut(board.D9),   # A1
    digitalio.DigitalInOut(board.D10),  # A2
    digitalio.DigitalInOut(board.D11),  # B1
    digitalio.DigitalInOut(board.D12),  # B2
)

# Sets each of the digital pins as an output.
for coil in coils:
    coil.direction = digitalio.Direction.OUTPUT

# Creates an instance of the stepper motor so you can send commands to it (using the Adafruit Motor library). 
motor = stepper.StepperMotor(coils[0], coils[1], coils[2], coils[3], microsteps=None)


async def catch_pin_transitions(pin):
    # Print a message when pin goes low and when it goes high.
    with keypad.Keys((pin,), value_when_pressed=False) as keys:
            event = keys.events.get()
            print("kjhgfdsdddddd")
            if event:
                print("fdgh")
                if event.pressed:
                    print("Limit Switch was pressed.")
                    # FILL THIS IN: MAKE THE MOTOR ARM SPIN BACKWARDS. 
                    for step in range(STEPS):
                        motor.onestep( style=stepper.DOUBLE)
                        
                        time.sleep(DELAY)


                elif event.released:
                    print("Limit Switch was released.")
            await asyncio.sleep(0)

async def run_motor(DELAY):
        print("motorrunning")
        for step in range(STEPS):
            motor.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
                
            time.sleep(DELAY)

async def main():
    while(True):
        motor_task=asyncio.create_task(run_motor(DELAY))
        print("motor")
        interrupt_task = asyncio.create_task(catch_pin_transitions(board.D0))
        print("main")
        
        # FILL THIS IN: 
        # CREATE ANOTHER TASK CALLED: motor_task.
        # USE asyncio.create_task() to call the run_motor() function you wrote.
        
        await asyncio.gather(interrupt_task, motor_task)
while True:
    asyncio.run(main())
```
### Reflection
I did this assignment fine. It took me a long time to get it to work with circuit python. This assignment is starting to put me a little on the end of the line.
Last year I started working on a project a month or two after doing some code. I then learned a little more code near the end of the semester
and worked on another project in the second semester. I have spent the last 5 months doing code, onshape, and more code.
The project we are supposed to do is more complex than the project last year and I am given less time.
In this time my sophmore freind has already completed her project for this semester. 
With all due respect I want to get started working on something now. I can't spend the entire year doing 3D cad and small code assignments.


## Onshape robot gripper
### Description
In this assignment I have been told to create a working robot arm in onshape. I was bored so I decided to use 24 arms. I can't think of anything else to add to this. I used a basic worm gear.

### Evidence
![image](https://github.com/solomon4000/eng3/assets/90640484/d7c7e77f-3100-449c-9729-0ec4dfe9de06)
### Document link
[document](https://cvilleschools.onshape.com/documents/32173eae7107252bfa0d62d8/w/ae7835291b68435ee0f92a57/e/834003dde04d9d3635203690) 

### Reflection
This is hopefully the last assignment that I have to do before a big project. I am really concerned if I will have enough time to finish the project at this point. I am really strugling.

## IR Sensor

### Description
This assignment I had to write code that counted how many times I waved my hand in front of it. I do not understand why I had to do this because an ultrasonic sesnsor would work better.

### Evidence


