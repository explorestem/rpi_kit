# PIR.py - sense a PIR movement
# Part of the Alarm System project
# Written by David Whale 2014

import RPi.GPIO as GPIO
import time

LED = 15
PIR = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

while True:
	time.sleep(0.1)
	if GPIO.input(PIR):
		print("PIR low, TRIGGERED")
		GPIO.output(LED, True)
		#time.sleep(1)
		#GPIO.output(LED, False)
		#time.sleep(1)
	else:
		print("PIR high, IDLE")
		GPIO.output(LED, False)
		
# END
