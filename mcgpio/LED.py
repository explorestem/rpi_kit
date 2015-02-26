# LED.py
# part 1: flash an LED

import time
import RPi.GPIO as GPIO

RED_LED = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_LED, GPIO.OUT)

while True:
	GPIO.output(RED_LED, True)
	time.sleep(1)
	GPIO.output(RED_LED, False)
	time.sleep(1)

