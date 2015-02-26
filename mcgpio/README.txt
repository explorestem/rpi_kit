The Minecraft Power Miner Game!
===============================

Written by @whaleygeek for the Cambridge Raspberry Pi 3rd Birthday Party.
Donated to ExploreSTEM for use in The IET portable raspberry pi kits.

This is a game of skill, that teaches programming skills both in Minecraft
and with GPIO hardware.

It has inputs, processing, and outputs, both inside Minecraft, and also
in the real world!

The program is written using standard GPIO, but mapped to the right pins
for the Pimoroni Pibrella board. But you can use any hardware you like.

The pin mappings are (BCM GPIO numbers)
RED_LED = 27
AMBER_LED = 17
GREEN_LED = 4
BUTTON = 11

Power blocks are burried under the sand,
and you have a hardware power tester that is finely tuned to sense the
power blocks under ground. The object of the game is to find all power
blocks by using your power tester, without running out of power.


The game is developed in 4 logical steps

part 1: LED.py (hardware output, LED control)

  First start with output in the real work by flashing the red LED with GPIO.
  This tests that you can use hardware as an output.
  
  The red LED will flash on for 1 second, off for one second.


part 2: PowerSensor.py (minecraft input, block sensing)

  Now add in some minecraft input sensing - if you are standing on a wool
  block, then the red LED will flash while you stand on it.
  
  A simple 10x10 arena is built with red blocks at random locations.
  These blocks are built at a visible height to make your program easier
  to test at this stage.


part 3: PowerTester.py (hardware input, button)

  Now add in some hardware input - use a button to enable the power sensor.
  When you press the button, the power sensor will check if there is a
  power block below you, and if there is, it will flash the red LED.
  If there is not a power block below you, it will do nothing.


part 4: PowerMinerGame.py (minecraft output, on chat)

  The final step is to add a score and a time limit into the game to
  make it challenging to play! You have limited power reserves, which#
  drain away slowly all the while you are playing the game. Every time
  you press the button to test to see if there is a power block below
  you, power is drained and your power reserves go down.

  If you are unlucky and don't find a power block, the amber LED flashes
  and your power is drained a bit.

  If you are lucky and find a power block, the block is removed and
  all the energy stored in it is loaded into your power bank, replenishing
  your power reserves so you can keep playing a bit longer.

  But there is a twist! When the power block is used, it zaps up from under
  the arena, leaving a hole in the arena that you can fall down. As you
  play the game for longer, it gets harder to avoid all the holes! You
  can't cheat and fly above the holes, because your power tester is
  carefully tuned to just the depth of the power blocks, so if you are
  not standing on the sand arena, the power tester will not work!


  See how many power blocks you can collect - can you collect them all
  before your power reserves run out? Challenge your friends to complete
  the game and see who can collect all the blocks and have the most power
  left in their reserves at the end!

  Make the game easier or harder by changing the constants at the top
  of the program - give yourself more power reserves, make a different
  sized arena, change how deep the power blocks are burried under
  ground! Or add your own ideas to the game to make it your own,
  and share your version of the game with your friend for them to
  try and beat your high score!


David Whale
@whaleygeek
February 2015


