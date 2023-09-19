import board
import digitalio
import time

mosfet1=digitalio.DigitalInOut(board.D8)
mosfet2=digitalio.DigitalInOut(board.D9)
mosfet3=digitalio.DigitalInOut(board.D7)
mosfet4=digitalio.DigitalInOut(board.D6)

while True:
    mosfet1.value=True
    mosfet2.value=True
    mosfet3.value=False
    mosfet4.value=False
    time.sleep(1/60)
    mosfet1.value=False
    mosfet2.value=False
    mosfet3.value=True
    mosfet4.value=True