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
        stop = time.time()
        
        pulse_duration = stop - start
        distance = round((pulse_duration * 17150), 2)

        clear()
        print(" ")
        print("  Distance: %s cm." %(distance))

except KeyboardInterrupt:
    print(" ")
    print(color.ERROR + " Script terminated by User. Bye." + color.RESET)
    pass
finally:
    GPIO.output(TRIG,False)
    GPIO.cleanup()

