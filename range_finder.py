#!/usr/bin/env python
"""
Finds the distance between the sensor and the object directly in front
"""

import RPi.GPIO as GPIO
import time
from os import system as sys

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
try:
    while True:
        time.sleep(0.1)

        # send pulse to trigger
        GPIO.output(TRIG,1)
        time.sleep(0.00001)
        GPIO.output(TRIG,0)

        #measure the echo time
        while GPIO.input(ECHO) == 0:
            pass

        start = time.time()
        while GPIO.input(ECHO) == 1:
            pass
        stop = time.time()

        print(" ")
        print("  Distance: %s" %((stop - start) * 170))

except KeyboardInterrupt:
    print(" ")
    print(color.ERROR + " Script terminated by User. Bye." + color.RESET)
    pass
finally:
    GPIO.output(on_led,False)
    GPIO.cleanup()

