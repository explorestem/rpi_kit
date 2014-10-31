# alarm.py - A complete alarm system using a PIR
# Part of the Alarm System project
# Written by David Whale 2014

import RPi.GPIO as GPIO

import time
import pygame

pygame.mixer.init()
alarm = pygame.mixer.Sound("alarm.wav")
beep  = pygame.mixer.Sound("beep.wav")

LED = 15
BUTTON = 4
PIR = 14
state = "idle"

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN)
GPIO.setup(PIR, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

while True:
	time.sleep(0.5)
	button = not GPIO.input(BUTTON)
	pir = GPIO.input(PIR)
	GPIO.output(LED, pir)

	if state == "idle":
		if button:
			print("Alarm armed")
			beep.play()
			time.sleep(0.5)
			beep.play()
			time.sleep(1)
			state = "armed"

	elif state == "armed":
		if pir:
			print("Alarm tripped")
			alarm.play(loops=-1)
			state = "sounding"
		elif button:
			print("Disabling alarm")
			beep.play()
			time.sleep(1)
			state = "idle"

	elif state == "sounding":
		if button:
			print("Resetting alarm")
			alarm.stop()
			time.sleep(0.5)
			beep.play()
			time.sleep(1)
			state = "idle"
			
# END
