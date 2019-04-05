#!/usr/bin/env python
"""
Finds the distance between the sensor and the object directly in front
"""

import RPi.GPIO as GPIO
import time
import smbus
from os import system as sys
import lcd_i2c as lcd
# reference
# https://stackoverflow.com/questions/287871/print-in-terminal-with-colors#287944
class color:
    HEADER = '\x1b[1;30;44m'
    ERROR = '\x1b[1;31;40m'
    RESET = '\x1b[0m'

def clear():
    sys('clear')
    print(color.HEADER + "  == Range Finder ==  " + color.RESET)

TRIG = 17
ECHO = 27

GPIO.setmode(GPIO.BCM)

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

current_state = 0
lcd.lcd_init()
     
lcd.lcd_string(" Distance: ",lcd.LCD_LINE_1)
try:
    while True:
        #Do it every second
        time.sleep(1)

        #Send pulse to trigger
        GPIO.output(TRIG,True)
        time.sleep(0.00001)
        GPIO.output(TRIG,False)

        #measure the echo time
        while GPIO.input(ECHO) == 0:
            pass

        start = time.time()
        while GPIO.input(ECHO) == 1:
            pass
        end = time.time()

        pulse_duration = end - start
        distance = round((pulse_duration * 17150), 1)

        clear()
        print(" ")

        stringmessage = "dist: " + str(distance).zfill(6) + "cm.          "
        # write to standard input
        print(stringmessage)

        # reset lcd display and send new message
        lcd.lcd_string("    " + str(distance).zfill(6) + "       " ,lcd.LCD_LINE_2)

except KeyboardInterrupt:
    print(" ")
    print(color.ERROR + " Script terminated by User. Bye." + color.RESET)
    pass
finally:
    p.stop()
    GPIO.cleanup()

