"""
Rotary Encoder + LCD Code
Traffic Light 
Use a rotary encoder, an LCD, and the on-board NeoPixel LED to create a menu-based traffic light control.

Engineering 3
Ms. Gibson
"""
# Import libraries
import rotaryio
import board
import neopixel 
import digitalio
from lib.lcd.lcd import LCD
from lib.lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import time

#Initialize rotary encoder using the rotaryio library.
 # type: ignore
enc = rotaryio.IncrementalEncoder(board.D4, 
board.D3, 
divisor=2)
 # type: ignore
lcd = LCD(I2CPCF8574Interface
(board.I2C(), 0x3f),
 num_rows=2, num_cols=16)

# Initialize the on-board neopixel and set the brightness.
led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 1.0
led2=digitalio.DigitalInOut(board.D5)
led2.direction=digitalio.Direction.OUTPUT
# Set up the rotary encoder as a button using digital pin 2. 
button = digitalio.DigitalInOut(board.D2)
button.direction = digitalio.Direction.INPUT # Set the button as an input.
button.pull = digitalio.Pull.UP              # Use the internal pull-up resistor.
button_state = None                          # Set the button_state as None for now!

# PSEUDOCODE: Create a list called "menu," and store the strings "stop", "caution", "go".
menu = ["Stop","Caution","Go"]

# These variables will help us keep track of our rotary encoder's position & our place in the menu.
menu_index = 0
last_index = None

# Set the cursor position on the LCD as (0,0), and print instructions to the user.
lcd.set_cursor_pos(0,0)
hasbeenpushed=False
iterations=1000
lcd.print("Push for:")
# While loop runs the code inside continuously. 
while True:

    # Set the menu_index to the position of the rotary encoder. 
    menu_index = enc.position

    # PSEUDOCODE: If your last index is None OR your menu index does not match your last index:
        # Set the cursor position to the second row and to the far left.
        # Print blank spaces to clear what was there before.
        # Set the cursor back to the previous position.
    
        # FILL THIS IN: Get our spot in the menu.
    menu_index_lcd = menu_index % 3    
    menu_index_lcd2=menu_index_lcd
        # Display stop, caution, or go to the LCD, depending on our encoder's position.
    

    if menu_index_lcd2==menu_index_lcd:
        hasbeenpushed=False
    else:
        hasbeenpushed=True
    # PSEUDOCODE: Then, set your last index to your menu index.
    if hasbeenpushed:
        lcd.clear()
        lcd.print("Push for:")
        lcd.print(menu[menu_index_lcd])
    
    # If the rotary encoder is pressed as a button, set the button_state to "pressed".
    if not button.value and button_state is None:
        button_state = "pressed"
    
    # If it is pressed, set the state back to None, & print that the button is pressed to the Serial Monitor.
    if button.value and button_state == "pressed":

        button_state = None
        print("Button is pressed")
        lcd.clear()
        lcd.print("Push for:")
        lcd.print(menu[menu_index_lcd])
        # PSEUDOCODE: Depending on what the user selects, change the color of the neopixel using RGB values.
        if menu_index_lcd == 0:        # Stop is red.
            led[0] = (255, 0, 0)

                                       # Caution is yellow.
        if menu_index_lcd==1:
            led[0]=(255,255,0)                               
                                       
                                       # Go is green.
        if menu_index_lcd==2:
            led[0]=(0,255,0)
        