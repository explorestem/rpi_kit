# PowerSensor.py
# part 2: flash an LED when a power block is sensed


import time
import RPi.GPIO as GPIO

import mcpi.minecraft as minecraft
import mcpi.block as block
import random

RED_LED = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_LED, GPIO.OUT)

SIZE = 10
POWER_BLOCKS = 20
DEPTH = 1

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
mc.setBlocks(pos.x, pos.y-1, pos.z,pos.x+SIZE, pos.y-1, pos.z+SIZE, block.SAND.id)

for b in range(POWER_BLOCKS):
	mc.setBlock(pos.x + random.randint(0, SIZE), pos.y-DEPTH, pos.z+random.randint(0, SIZE), block.WOOL.id, 14) # RED

while True:
	time.sleep(1)
	pos = mc.player.getTilePos()
	b = mc.getBlock(pos.x, pos.y-DEPTH, pos.z)
	if b == block.WOOL.id:
		GPIO.output(RED_LED, True)
		time.sleep(1)
		GPIO.output(RED_LED, False)

