# button.py - sense a button press
# Part of the Alarm System project
# Written by David Whale 2014

import RPi.GPIO as GPIO
import time

LED = 15
BUTTON = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

while True:
	time.sleep(0.1)
	if GPIO.input(BUTTON) == False:
		GPIO.output(LED, True)
		time.sleep(1)
		GPIO.output(LED, False)
		time.sleep(1)
		
# END
