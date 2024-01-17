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
