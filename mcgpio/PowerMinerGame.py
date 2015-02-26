# PowerMinerGame.py part 4: use power to find power!

import time
import RPi.GPIO as GPIO

import mcpi.minecraft as minecraft
import mcpi.block as block
import random

RED_LED = 27
AMBER_LED = 17
BUTTON  = 11
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(AMBER_LED, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN)

SIZE = 10
POWER_BLOCKS = 20
DEPTH = 10 # 1 for visible, 2 for hidden, 10 for deep holes!

power = 1000
blocks = POWER_BLOCKS

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
mc.setBlocks(pos.x, pos.y-1, pos.z,pos.x+SIZE, pos.y-1, pos.z+SIZE, block.SAND.id)
mc.setBlocks(pos.x, pos.y, pos.z, pos.x+SIZE, pos.y+SIZE, pos.z+SIZE, block.AIR.id)

for b in range(POWER_BLOCKS):
	mc.setBlock(pos.x + random.randint(0, SIZE), pos.y-DEPTH, pos.z+random.randint(0, SIZE), block.WOOL.id, 14) # RED

while power > 0 and blocks > 0:
	time.sleep(1)
	power = power - 1
	mc.postToChat("power:" + str(power) + " blocks:" + str(blocks))

	pos = mc.player.getTilePos()
	b = mc.getBlock(pos.x, pos.y-DEPTH, pos.z)
	button = GPIO.input(BUTTON)
	if button:
		power = power - 10
		if b == block.WOOL.id:
			GPIO.output(RED_LED, True)
			time.sleep(1)
			GPIO.output(RED_LED, False)
			power = power + 100
			mc.setBlocks(pos.x, pos.y-DEPTH, pos.z, pos.x, pos.y, pos.z, block.AIR.id)
			blocks = blocks - 1
		else:
			GPIO.output(AMBER_LED, True)
			time.sleep(1)
			GPIO.output(AMBER_LED, False)

mc.postToChat("game over: final power:" + str(power) + " blocks left:" + str(blocks))

