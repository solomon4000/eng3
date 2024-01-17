import digitalio
import board
from lib.lcd.lcd import LCD
from lib.lcd.i2c_pcf8574_interface import I2CPCF8574Interface
lcd = LCD(I2CPCF8574Interface(board.I2C(), 0x3f), num_rows=2, num_cols=16)
lcd.set_cursor_pos(0,0)
lcd.print("Hello world")

#fuck you fucking board ive wasted 2 fucking hours on now on a programn with 9 goddamn lines of fucking code you peice of shit