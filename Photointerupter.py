
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
