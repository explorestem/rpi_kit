# PIRSound.py - sense a PIR movement and play a sound
# Part of the Alarm System project
# Written by David Whale 2014

import RPi.GPIO as GPIO

import time
import pygame

pygame.mixer.init()
beep = pygame.mixer.Sound("beep.wav")

LED = 15
BUTTON = 4
PIR = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN)
GPIO.setup(PIR, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

while True:
	time.sleep(0.1)
	if GPIO.input(PIR):
		GPIO.output(LED, True)
		beep.play()
		time.sleep(1)
		GPIO.output(LED, False)
		
# END
