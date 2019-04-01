#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

def blink(duration):
    """Control LED on-time with duration parameter"""
    GPIO.output(18, True)
    time.sleep(duration)
    GPIO.output(18, False)
    time.sleep(0.25)

def dash():
    """Blink LED for a morse-code dash"""
    blink(0.50)

def dot():
    """Blink LED for a morse-code dot"""
    blink(0.25)

def morse_S():
    """Blink LED for morse-code letter S"""
    dot()
    dot()
    dot()
    # space at end of letter
    time.sleep(0.25)

def morse_O():
    """Blink LED for a morse-code letter O"""
    dash()
    dash()
    dash()
    # space at end of letter
    time.sleep(0.25)

# GPIO setup for raspberry-pi; 
# no warnings when changing IOs to Out
# use Broadcom GPIO pin numbering
# and set pin 18 to an output to drive the LED
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

while True:
    try:
        morse_S()
        morse_O()
        morse_S()
        time.sleep(2)
    except KeyboardInterrupt:
# GPIO reset configuration
        GPIO.cleanup()
        exit
    except RuntimeError:
        exit

