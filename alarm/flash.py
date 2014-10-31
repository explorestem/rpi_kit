# flash.py - flash an LED
# Part of the Alarm System project
# Written by David Whale 2014

import RPi.GPIO as GPIO
import time

LED = 15

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

while True:
	GPIO.output(LED, True)
	time.sleep(1)
	GPIO.output(LED, False)
	time.sleep(1)
	
# END
