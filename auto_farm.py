import vgamepad as vg
import tkinter as tk
import time
import datetime
import logging
import threading
import sys
from pynput.keyboard import Listener, KeyCode
from python_imagesearch.imagesearch import imagesearch_loop, imagesearch, imagesearch_numLoop

GAMEPAD = vg.VX360Gamepad()
BUTTON_LIST = {
	"A": vg.XUSB_BUTTON.XUSB_GAMEPAD_A,
	"B": vg.XUSB_BUTTON.XUSB_GAMEPAD_B,
	"X": vg.XUSB_BUTTON.XUSB_GAMEPAD_X,
	"Y": vg.XUSB_BUTTON.XUSB_GAMEPAD_Y,
	"LB": vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER,
	"RB": vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER,
	"LSB": vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB,
    "RSB": vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB,
	"START": vg.XUSB_BUTTON.XUSB_GAMEPAD_START,
	"BACK": vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK,
	"UP": vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP,
	"DOWN": vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN,
	"LEFT": vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT,
	"RIGHT": vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT
}
START_END = False
IS_FIGHT_FINISHED = False

# Create a logger
logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)

# Create a formatter to define the log format
formatter = logging.Formatter('%(asctime)s - %(message)s')

# Create a file handler to write logs to a file
file_handler = logging.FileHandler('auto_farm_logs.txt')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Create a stream handler to logger.info logs to the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # You can set the desired log level for console output
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def teleportToQuest():
	logger.info("Teleporting to quest counter")
	# open up the shortcut menu
	logger.info("Opening shortcut")
	GAMEPAD.left_trigger_float(value_float=1.0)
	GAMEPAD.update()
	time.sleep(1.0)
	GAMEPAD.left_trigger_float(value_float=0.0)
	GAMEPAD.update()

	# press on fast travel
	pressButton("A")
	# press on teleport to quest counter
	pressButton("A")
	time.sleep(1.5)

	logger.info("Walking to quest board")
	# walk 1 second up to counter
	GAMEPAD.left_joystick_float(x_value_float=0.0, y_value_float=1.0)
	GAMEPAD.update()
	time.sleep(1)
	GAMEPAD.left_joystick_float(x_value_float=0.0, y_value_float=0.0)
	GAMEPAD.update()
	# interact with the quest counter
	pressButton("Y")
	time.sleep(2)

def startSlimeQuest():
	# press on undertake quest
	pressButton("A")
	# go to by difficulty
	pressButton("RB")
	# default on easy diff so go up one
	pressButton("UP")
	# press on maniac/proud difficulty
	pressButton("A")
	# go to maniac difficulty
	pressButton("LB")
	# press on 1st quest (should be slimepede)
	pressButton("A")
	# accept the quest
	pressButton("A")
	# press closed party
	pressButton("A")
	time.sleep(1.5)

	# ready up for quest
	pressButton("X")
	time.sleep(0.5)
	# ready and depart to quest
	pressButton("A")

	# sleep for 22 seconds then get into fight to account for
	# loading + intro 
	logger.info("Waiting 26 seconds for load")
	time.sleep(26)

def startSlimeSubsequent():
	# press on undertake quest
	pressButton("A")
	time.sleep(0.5)
	# press on proud diff
	pressButton("A")
	# press on slimepede
	pressButton("A")
	# press on accept quest
	pressButton("A")
	# press on closed party
	pressButton("A")
	time.sleep(1.5)

	# ready up for quest
	pressButton("X")
	time.sleep(0.5)
	# ready and depart to quest
	pressButton("A")

	# sleep for 22 seconds then get into fight to account for
	# loading + intro 
	logger.info("Waiting 26 seconds for load")
	time.sleep(26)

def startNewSlimeQuest():
	# press on undertake quest
	pressButton("A")
	time.sleep(0.5)
	# go to by difficulty
	pressButton("RB")
	# default easy/normal difficulty so go left
	pressButton("LEFT")
	# press on fatebreaker difficulty
	pressButton("A")
	# default on choas++ so go left once
	pressButton("LB")
	# go up one
	pressButton("UP")
	pressButton("LEFT")
	pressButton("DOWN")
	pressButton("DOWN")
	# press on the quest
	pressButton("A")
	# accept the quest
	pressButton("A")
	# press closed party
	pressButton("A")
	time.sleep(1.5)

	# ready up for quest
	pressButton("X")
	time.sleep(0.5)
	# ready and depart to quest
	pressButton("A")

	# sleep for 22 seconds then get into fight to account for
	# loading + intro 
	logger.info("Waiting 10 seconds for load")
	time.sleep(10)
	
def startNewSlimeSubsequent():
	# press on undertake quest
	pressButton("A")
	time.sleep(0.5)
	# press on fatebreaker diff
	pressButton("A")
	# press on revenge of the ooze
	pressButton("A")
	# press on accept quest
	pressButton("A")
	# press on closed party
	pressButton("A")
	time.sleep(1.5)

	# ready up for quest
	pressButton("X")
	time.sleep(0.5)
	# ready and depart to quest
	pressButton("A")

	# sleep for 22 seconds then get into fight to account for
	# loading + intro 
	logger.info("Waiting 10 seconds for load")
	time.sleep(10)

def startWorldQuest():
	# press on undertake quest
	pressButton("A")
	time.sleep(0.5)
	# go to by difficulty
	pressButton("RB")
	# default easy/normal difficulty so go left
	pressButton("LEFT")
	# press on fatebreaker difficulty
	pressButton("A")
	# default on choas++ so go left once
	# pressButton("LB")
	# go up one
	pressButton("UP")

	pressButton("UP")
	pressButton("UP")
	pressButton("UP")
	pressButton("UP")
	# press on the quest
	pressButton("A")
	# accept the quest
	pressButton("A")
	# press closed party
	pressButton("A")
	time.sleep(3)

	# ready up for quest
	pressButton("X")
	time.sleep(0.5)
	# ready and depart to quest
	pressButton("A")

	# sleep for 22 seconds then get into fight to account for
	# loading + intro 
	logger.info("Waiting 10 seconds for load")
	time.sleep(10)

def startWorldSubsequentQuest():
	# press on undertake quest
	pressButton("A")
	time.sleep(0.5)
	# press on fatebreaker diff
	pressButton("A")
	# press on rthe world quest
	pressButton("A")
	# press on accept quest
	pressButton("A")
	# press on closed party
	pressButton("A")
	time.sleep(3)

	# ready up for quest
	pressButton("X")
	time.sleep(0.5)
	# ready and depart to quest
	pressButton("A")

	# sleep for 22 seconds then get into fight to account for
	# loading + intro 
	logger.info("Waiting 10 seconds for load")
	time.sleep(10)

def startFortitudeQuest():
	# press on undertake quest
	pressButton("A")
	# go to by difficulty
	pressButton("RB")
	# default on easy diff so go down to extreme
	pressButton("DOWN")
	# press on extreme difficulty
	pressButton("A")
	# down 3 times
	pressButton("DOWN")
	pressButton("DOWN")
	pressButton("DOWN")
	# press on pillar quest
	pressButton("A")
	# accept the quest
	pressButton("A")
	# press closed party
	pressButton("A")
	time.sleep(1.5)

	# ready up for quest
	pressButton("X")
	time.sleep(0.5)
	# ready and depart to quest
	pressButton("A")

	# sleep for 22 seconds then get into fight to account for
	# loading + intro 
	logger.info("Waiting 24 seconds for load")
	time.sleep(24)

def startFortitudeSubsequent():
	# press on undertake quest
	pressButton("A")
	# press on extreme difficulty
	pressButton("A")
	# down 3 times
	pressButton("DOWN")
	pressButton("DOWN")
	pressButton("DOWN")
	# press on pillar quest
	pressButton("A")
	# accept the quest
	pressButton("A")
	# press closed party
	pressButton("A")
	time.sleep(1.5)

	# ready up for quest
	pressButton("X")
	time.sleep(0.5)
	# ready and depart to quest
	pressButton("A")

	# sleep for 22 seconds then get into fight to account for
	# loading + intro 
	logger.info("Waiting 22 seconds for load")
	time.sleep(22)

def startLuciliusQuest():
	# press on undertake quest
	pressButton("A")
	# go to by difficulty
	pressButton("RB")
	# default on easy diff so go down to proud
	pressButton("UP")
	# press on proud difficulty
	pressButton("A")
	# UP 5 time
	pressButton("UP")
	pressButton("UP")
	pressButton("UP")
	pressButton("UP")
	pressButton("UP")
	# press on luci quest
	pressButton("A")
	# accept the quest
	pressButton("A")
	# press closed party
	pressButton("A")
	time.sleep(1.5)

	# ready up for quest
	pressButton("X")
	time.sleep(0.5)
	# ready and depart to quest
	pressButton("A")

	# sleep for 22 seconds then get into fight to account for
	# loading + intro 
	logger.info("Waiting 24 seconds for load")
	time.sleep(24)

def startLuciliusSubsequent():
	# press on undertake quest
	pressButton("A")
	# press on proud difficulty
	pressButton("A")
	# up to go to bottom of list
	# pressButton("UP")
	
	# press on luci quest
	pressButton("A")
	# accept the quest
	pressButton("A")
	# press closed party
	pressButton("A")
	time.sleep(1.5)

	# ready up for quest
	pressButton("X")
	time.sleep(0.5)
	# ready and depart to quest
	pressButton("A")

	# sleep for 22 seconds then get into fight to account for
	# loading + intro 
	logger.info("Waiting 22 seconds for load")
	time.sleep(22)

def startBehemoth():
	# press on undertake quest
	pressButton("A")
	# go to by difficulty
	pressButton("RB")
	# default on easy diff so go down to proud
	pressButton("UP")
	# press on proud difficulty
	pressButton("A")
	# UP 6 time
	pressButton("UP")
	pressButton("UP")
	pressButton("UP")
	pressButton("UP")
	pressButton("UP")
	pressButton("UP")
	# press on behemoth quest
	pressButton("A")
	# accept the quest
	pressButton("A")
	# press closed party
	pressButton("A")
	time.sleep(1.5)

	# ready up for quest
	pressButton("X")
	time.sleep(0.5)
	# ready and depart to quest
	pressButton("A")

	# sleep for 22 seconds then get into fight to account for
	# loading + intro 
	logger.info("Waiting 24 seconds for load")
	time.sleep(24)

def startBehemothSubsequent():
	# press on undertake quest
	pressButton("A")
	# press on proud difficulty
	pressButton("A")
	# press on behemoth quest
	pressButton("A")
	# accept the quest
	pressButton("A")
	# press closed party
	pressButton("A")
	time.sleep(1.5)

	# ready up for quest
	pressButton("X")
	time.sleep(0.5)
	# ready and depart to quest
	pressButton("A")

	# sleep for 22 seconds then get into fight to account for
	# loading + intro 
	logger.info("Waiting 22 seconds for load")
	time.sleep(24)

def startZathbaVolunteers():
	# press on undertake quest
	pressButton("A")
	# go to by difficulty
	pressButton("RB")
	# default on easy diff so go down to proud
	pressButton("UP")
	# press on proud difficulty
	pressButton("A")

	# UP 3 time
	pressButton("UP")
	pressButton("UP")
	pressButton("UP")

	# press on zathba quest
	pressButton("A")
	# accept the quest
	pressButton("A")
	# press closed party
	pressButton("A")
	time.sleep(1.5)

	# ready up for quest
	pressButton("X")
	time.sleep(0.5)
	# ready and depart to quest
	pressButton("A")

	# sleep for 22 seconds then get into fight to account for
	# loading + intro 
	logger.info("Waiting 24 seconds for load")
	time.sleep(24)

def startZathbaVolunteersSubsequent():
	# press on undertake quest
	pressButton("A")
	# press on proud difficulty
	pressButton("A")
	# press on zathba quest
	pressButton("A")
	# accept the quest
	pressButton("A")
	# press closed party
	pressButton("A")
	time.sleep(1.5)

	# ready up for quest
	pressButton("X")
	time.sleep(0.5)
	# ready and depart to quest
	pressButton("A")

	# sleep for 22 seconds then get into fight to account for
	# loading + intro 
	logger.info("Waiting 22 seconds for load")
	time.sleep(24)


def startProtoQuest():
	# press on undertake quest
	pressButton("A")
	# go to by difficulty
	pressButton("RB")
	# default on easy diff so go down to proud
	pressButton("UP")
	# press on proud difficulty
	pressButton("A")
	# UP 2 time
	pressButton("UP")
	pressButton("UP")
	# press on proto quest
	pressButton("A")
	# accept the quest
	pressButton("A")
	# press closed party
	pressButton("A")
	time.sleep(1.5)

	# ready up for quest
	pressButton("X")
	time.sleep(0.5)
	# ready and depart to quest
	pressButton("A")

	# sleep for 22 seconds then get into fight to account for
	# loading + intro 
	logger.info("Waiting 24 seconds for load")
	time.sleep(24)

def startProtoSubsequent():
	# press on undertake quest
	pressButton("A")
	# press on proud difficulty
	pressButton("A")
	# up twice go to bottom of list
	pressButton("UP")
	pressButton("UP")
	# press on proto quest
	pressButton("A")
	# accept the quest
	pressButton("A")
	# press closed party
	pressButton("A")
	time.sleep(1.5)

	# ready up for quest
	pressButton("X")
	time.sleep(0.5)
	# ready and depart to quest
	pressButton("A")

	# sleep for 22 seconds then get into fight to account for
	# loading + intro 
	logger.info("Waiting 22 seconds for load")
	time.sleep(22)

def startBossRush():
	# press on undertake quest
	pressButton("A")
	# go to by difficulty
	pressButton("RB")
	# default on easy diff so go down to proud
	pressButton("UP")
	# press on proud difficulty
	pressButton("A")
	# UP 1 time to get to bottom of list
	pressButton("UP")
	# go up 8 quests
	pressButton("LEFT")
	# down one to start furrycane
	pressButton("DOWN")
	# press on quest
	pressButton("A")
	# accept the quest
	pressButton("A")
	# press closed party
	pressButton("A")
	time.sleep(1.5)

	# ready up for quest
	pressButton("X")
	time.sleep(0.5)
	# ready and depart to quest
	pressButton("A")

	# sleep for 22 seconds then get into fight to account for
	# loading + intro 
	logger.info("Waiting 24 seconds for load")
	time.sleep(24)

def startBossRushSubsequent(boss_order):
	# press on undertake quest
	pressButton("A")
	# press on proud difficulty
	pressButton("A")
	# up to go to bottom of list
	pressButton("UP")
	# go up 8 quests
	pressButton("LEFT")

	# furrycane
	if (boss_order == 0):
		logger.info("Furrycane cycle")
		pressButton("DOWN")
	# managarmr
	elif (boss_order == 1):
		logger.info("Managarmr cycle")
		for i in range(2):
			pressButton("DOWN")
	# vulkan
	elif (boss_order == 2):
		logger.info("Vulkan cycle")
		for i in range(3):
			pressButton("DOWN")
	# pyet-a
	elif (boss_order == 3 or boss_order == 4):
		logger.info("Pyet-A cycle")
		for i in range(6):
			pressButton("DOWN")
		
	# press on quest
	pressButton("A")
	# accept the quest
	pressButton("A")
	# press closed party
	pressButton("A")
	time.sleep(1.5)

	# ready up for quest
	pressButton("X")
	time.sleep(0.5)
	# ready and depart to quest
	pressButton("A")

	# sleep for 22 seconds then get into fight to account for
	# loading + intro 
	logger.info("Waiting 22 seconds for load")
	time.sleep(22)

def startTripleBossQuest():
	# press on undertake quest
	pressButton("A")
	# go to by difficulty
	pressButton("RB")
	# default on easy diff so go down to bottom
	pressButton("UP")
	# press on proud difficulty
	pressButton("A")
	
	# 5 DOWN to worst vacation ever
	# 6 to trade barriers
	# 8 to banquet of ice
	# 9 to freer folca
	for i in range(5):
		pressButton("DOWN")

	# press on quest
	pressButton("A")
	# accept the quest
	pressButton("A")
	# press closed party
	pressButton("A")
	time.sleep(1.5)

	# ready up for quest
	pressButton("X")
	time.sleep(0.5)
	# ready and depart to quest
	pressButton("A")

	# sleep for 22 seconds then get into fight to account for
	# loading + intro 
	logger.info("Waiting 24 seconds for load")
	time.sleep(24)

def startTripleBossSubsequent(triple_boss_order):
	# press on undertake quest
	pressButton("A")
	# press on proud difficulty
	pressButton("A")

	# worst vacation ever
	if (triple_boss_order == 0):
		logger.info("Worst vacation cycle")
		for i in range(5):
			pressButton("DOWN")
	# trade barrier
	elif (triple_boss_order == 1):
		logger.info("Trade barrier cycle")
		for i in range(6):
			pressButton("DOWN")
	# banquet of ice
	elif (triple_boss_order == 2):
		logger.info("Banquet of ice cycle")
		for i in range(8):
			pressButton("DOWN")
	# freer folca
	elif (triple_boss_order == 3):
		logger.info("Freer folca cycle")
		for i in range(9):
			pressButton("DOWN")
		
	# press on quest
	pressButton("A")
	# accept the quest
	pressButton("A")
	# press closed party
	pressButton("A")
	time.sleep(1.5)

	# ready up for quest
	pressButton("X")
	time.sleep(0.5)
	# ready and depart to quest
	pressButton("A")

	# sleep for 22 seconds then get into fight to account for
	# loading + intro 
	logger.info("Waiting 22 seconds for load")
	time.sleep(22)

def lanceSpam():
	GAMEPAD.press_button(button=BUTTON_LIST["Y"])
	GAMEPAD.press_button(button=BUTTON_LIST["B"])
	# GAMEPAD.left_trigger_float(value_float=1.0)
	GAMEPAD.update()
	time.sleep(0.05)
	GAMEPAD.release_button(button=BUTTON_LIST["Y"])
	GAMEPAD.release_button(button=BUTTON_LIST["B"])
	# GAMEPAD.left_trigger_float(value_float=0)
	GAMEPAD.update()
	time.sleep(0.05)

def walkForward():
	GAMEPAD.left_joystick_float(x_value_float=0.0, y_value_float=1.0)
	GAMEPAD.update()
	time.sleep(2)
	GAMEPAD.left_joystick_float(x_value_float=0.0, y_value_float=0.0)
	GAMEPAD.update()

def pressButtonSimultaneously(button1, button2):
	GAMEPAD.press_button(button=BUTTON_LIST[button1])
	GAMEPAD.press_button(button=BUTTON_LIST[button2])
	GAMEPAD.update()
	time.sleep(0.05)
	GAMEPAD.release_button(button=BUTTON_LIST[button1])
	GAMEPAD.release_button(button=BUTTON_LIST[button2])
	GAMEPAD.update()
	time.sleep(0.05)

def pressButton(xbox_button):
	GAMEPAD.press_button(button=BUTTON_LIST[xbox_button])
	GAMEPAD.update()
	time.sleep(0.15)
	GAMEPAD.release_button(button=BUTTON_LIST[xbox_button])
	GAMEPAD.update()
	time.sleep(0.15)

# TODO: optimize this don't need 2
def mashAttack(min):
	logger.info("Mashing Attack")
	t_end = time.time() + 60 * min
	while time.time() < t_end:
		pressButton("X")

def mashAButton(seconds):
	t_end = time.time() + seconds
	while time.time() < t_end:
		pressButton("A")

def mashButton(button, seconds):
	t_end = time.time() + seconds
	while time.time() < t_end:
		pressButton(button)
	
def start_end_farm(key):
	if key == KeyCode(char='9'):
		global START_END
		START_END = not START_END

def moveUp(seconds):
	GAMEPAD.left_joystick_float(x_value_float=0.0, y_value_float=1.0)
	GAMEPAD.update()
	time.sleep(seconds)
	GAMEPAD.left_joystick_float(x_value_float=0.0, y_value_float=0.0)
	GAMEPAD.update()

def runUp(seconds):
	GAMEPAD.left_joystick_float(x_value_float=0.0, y_value_float=1.0)
	GAMEPAD.update()
	GAMEPAD.press_button(button=BUTTON_LIST["LSB"])
	GAMEPAD.update()
	time.sleep(seconds)
	GAMEPAD.release_button(button=BUTTON_LIST["LSB"])
	GAMEPAD.update()
	GAMEPAD.left_joystick_float(x_value_float=0.0, y_value_float=0.0)
	GAMEPAD.update()

def teleportKnick():
	logger.info("Teleporting to knickknack")
	# open up the shortcut menu
	logger.info("Opening shortcut")
	GAMEPAD.left_trigger_float(value_float=1.0)
	GAMEPAD.update()
	time.sleep(1.0)
	GAMEPAD.left_trigger_float(value_float=0.0)
	GAMEPAD.update()

	# press on fast travel
	pressButton("A")
	# press on teleport to knickknack
	pressButton("DOWN")
	pressButton("DOWN")
	pressButton("A")
	time.sleep(1.5)

	logger.info("Walking to knickknack")
	# walk 1 second up
	moveUp(1)
	# interact with the quest counter
	pressButton("Y")
	time.sleep(2)

	gambaSigils()

def gambaSigils():
	logger.info("Gamba gamba")
	# down 3 then down 2
	pressButton("DOWN")
	pressButton("DOWN")
	pressButton("DOWN")
	pressButton("A")
	pressButton("DOWN")
	pressButton("DOWN")
	logger.info("TIME TO GAMBA for 2 MIN")
	# mashAButton(120)
	pressButton("A")
	pressButton("A")
	pressButton("DOWN")
	pressButton("A")
	pressButton("A")
	time.sleep(5)

	# done with gamba
	mashButton("B", 3)
	time.sleep(2)

def printTest():
	while(not IS_FIGHT_FINISHED):
		logger.info("Fight not finished")
		time.sleep(1)
	logger.info("Fight finished")
		

def isTest():
	logger.info("Testing image serach")
	pos = imagesearch_loop("./Granblue_ImageSearch/battle_results.png", timesample=1, precision=0.75)
	logger.info("position : ", pos[0], pos[1])
	global IS_FIGHT_FINISHED 
	IS_FIGHT_FINISHED = True

def luciAttackSpam():
	while(not IS_FIGHT_FINISHED):
		# every 25 minutes press A
		i = 0
		t_end = time.time() + 60 * 15
		# while time.time() < t_end:
		# i = 3 is a second I think
		while (i < 5000 and not IS_FIGHT_FINISHED):
			if (i % 3 == 0):
				GAMEPAD.left_trigger_float(value_float=1.0)
				GAMEPAD.update()
				time.sleep(0.05)
				GAMEPAD.left_trigger_float(value_float=0)
				GAMEPAD.update()
				time.sleep(0.05)
			walkForward()
			# lanceSpam()
			# pressButtonSimultaneously("LSB", "RSB")
			i = i + 1
		logger.info("Should be done with fight since battle_results detected.")
		# for i in range(5):
		# 	pos = imagesearch("./Granblue_ImageSearch/battle_results.png", precision=0.75)
		# 	time.sleep(1)
		# if pos[0] != -1:
		logger.info("Pressing LEFT in case stuck\n")
		pressButton("LEFT")
	logger.info("Stop moving. Battle should be over!")

def checkBattleScreen():
	logger.info("Checking battle results screen\n")
	global IS_FIGHT_FINISHED
	while(not IS_FIGHT_FINISHED or pos[0] == -1):
		pos = imagesearch("./Granblue_ImageSearch/battle_results.png", precision=0.75)
		time.sleep(5)
	IS_FIGHT_FINISHED = True
	logger.info("Detected battle results screen")

def protoStart():
	# walk to the left and hold block
	logger.info("Walking to the left side of the ship for 5 seconds and holding block\n")
	GAMEPAD.left_joystick_float(x_value_float=-1.0, y_value_float=0.0)
	GAMEPAD.update()
	time.sleep(5)
	GAMEPAD.left_joystick_float(x_value_float=0.0, y_value_float=0.0)
	GAMEPAD.update()
	logger.info("Move up 2 seconds")
	moveUp(2)
	hold_block_mash_b()

def hold_block_mash_b():
	logger.info("Holding block and mashing B until fight is over")
	while(not IS_FIGHT_FINISHED):
		GAMEPAD.press_button(button=BUTTON_LIST["LB"])
		GAMEPAD.left_joystick_float(x_value_float=-1.0, y_value_float=1.0)
		GAMEPAD.update()
		pressButton("B")
		time.sleep(1)
	logger.info("Letting go of block. Fight is over")
	GAMEPAD.release_button(button=BUTTON_LIST["LB"])
	GAMEPAD.left_joystick_float(x_value_float=0.0, y_value_float=0.0)
	GAMEPAD.update()

def holdBlock():
	logger.info("Holding block until fight is over")
	while(not IS_FIGHT_FINISHED):
		GAMEPAD.press_button(button=BUTTON_LIST["LB"])
		GAMEPAD.update()
	logger.info("Letting go of block. Fight is over")
	GAMEPAD.release_button(button=BUTTON_LIST["LB"])
	GAMEPAD.update()

def checkQuestFinished():
	logger.info("Checking if we are on battle results screen every 1.0 seconds")
	# pos = imagesearch("./Granblue_ImageSearch/collect_treasure.png", precision=0.75)
	pos = imagesearch_loop("./Granblue_ImageSearch/battle_results.png", timesample=1.0, precision=0.75)
	time.sleep(1.5)
	# time.sleep(1)
	# while(pos[0] == -1):
		# logger.info('searching')
		# pos = imagesearch("./Granblue_ImageSearch/battle_results.png", precision=0.75)
		# time.sleep(2)
		# logger.info("2nd search")
		# time.sleep(2)
	#pos = imagesearch_loop("./Granblue_ImageSearch/collect_treasure.png", timesample=1.0, precision=0.8)
	logger.info("Battle results/Failure screen detected.")
	global IS_FIGHT_FINISHED
	IS_FIGHT_FINISHED = True

	# TODO - if fail then handle

def tradeSigils():
	logger.info("Gamba sigils")
	# press knickknack vouchers
	pressButton("DOWN")
	pressButton("DOWN")
	pressButton("A")
	# select trade sigils
	pressButton("DOWN")
	pressButton("A")
	# press sort/trade all
	pressButton("BACK")
	pressButton("X")
	pressButton("DOWN")
	pressButton("A")
	# select trade
	pressButton("A")
	pressButton("DOWN")
	# press OK
	pressButton("A")
	time.sleep(0.5)
	# back to menu
	# TODO: why does it need an extra b input here???
	pressButton("B")
	pressButton("B")
	pressButton("B")
	time.sleep(1)
	# transmute sigils
	pressButton("DOWN")
	pressButton("A")
	pressButton("DOWN")
	pressButton("DOWN")
	logger.info("TIME TO GAMBA SIGILS")
	
	for i in range(2):
		# select trade
		pressButton("A")
		pressButton("A")
		pressButton("DOWN")
		pressButton("A")
		pressButton("A")
		time.sleep(5)

		# close results
		pressButton("B")
	# back to menu
	pressButton("B")
	time.sleep(1)
	while(True):
		# go up to knick vouchers
		pressButton("UP")
		pressButton("A")
		# select trade sigils
		pressButton("A")
		# press sort/trade all
		pressButton("BACK")
		pressButton("X")
		pressButton("DOWN")
		pressButton("A")
		# select trade
		pressButton("A")
		pressButton("DOWN")
		# press OK
		pressButton("A")
		time.sleep(0.5)
		# back to menu
		pressButton("B")
		pressButton("B")
		pressButton("B")
		time.sleep(1)
		# transmute sigils
		pressButton("DOWN")
		pressButton("A")
		logger.info("TIME TO GAMBA SIGILS")
		for i in range(2):
			# select trade
			pressButton("A")
			pressButton("A")
			pressButton("DOWN")
			pressButton("A")
			pressButton("A")
			time.sleep(5)

			# close results
			pressButton("B")
		# back to menu
		pressButton("B")
		time.sleep(1)


def tradeWrightstones():
	# assuming in siero's menu already
	pressButton("DOWN")
	pressButton("DOWN")
	# enter knickknack vouchers
	pressButton("A")

	pressButton("DOWN")
	pressButton("DOWN")
	# trade wrightstones
	pressButton("A")

	# select up to 20 wrightstones to trade
	for i in range(20):
		pressButton("A")
		pressButton("DOWN")

	# initiate the trade
	pressButton("X")
	pressButton("DOWN")
	pressButton("A")
	pressButton("A")
	pressButton("DOWN")
	pressButton("A")
	pressButton("A")

	# exit back to the siero's menu
	pressButton("B")
	pressButton("B")
	time.sleep(1)

	# select transmute sigils
	pressButton("DOWN")
	pressButton("A")
	# go down 2 to level 3 transmute
	# trade 30 vouchers
	pressButton("DOWN")
	pressButton("DOWN")
	pressButton("A")
	pressButton("A")
	pressButton("DOWN")
	pressButton("A")
	pressButton("A")
	time.sleep(4)
	# get off sigil results screen
	pressButton("A")
	
	# go back to trade wrightstones
	pressButton("B")
	time.sleep(1)
	pressButton("UP")
	pressButton("A")
	# select trade wrightstones
	pressButton("A")

	# start looping here
	while(True):
		for i in range(20):
			pressButton("A")
			pressButton("DOWN")

		# initiate the trade
		pressButton("X")
		pressButton("DOWN")
		pressButton("A")
		pressButton("A")
		pressButton("DOWN")
		pressButton("A")
		pressButton("A")

		# exit back to the siero's menu
		pressButton("B")
		pressButton("B")
		time.sleep(1)
		# select transmute sigils
		pressButton("DOWN")
		pressButton("A")
		
		# transmute level 3 sigils
		pressButton("A")
		pressButton("A")
		pressButton("DOWN")
		pressButton("A")
		pressButton("A")
		time.sleep(4)
		# get off sigil results screen
		pressButton("A")

		# go back to trade wrightstones
		pressButton("B")
		time.sleep(1)
		pressButton("UP")
		pressButton("A")
		# select trade wrightstones
		pressButton("A")
		time.sleep(1)

if __name__ == '__main__':
	# Collect all event until released
	# wait 3 seconds before starting
	# press a button to wake the device up
	logger.info("Ranged main character required to be optimal")
	logger.info("Recommended to set the game to 720p 30fps if you go afk")
	logger.info("Make sure the quest board is in default state before running.")
	logger.info("Choose a farm. In the terminal, type 1 then press enter to farm slimes for example\n")
	farm_mode = input("Slimepede Farm [1] | Fortitude Crystal Farm (INEFFICIENT) [2] | TEST SCREEN CAPTURE [3]\n"
					  "Lucilius Farm [4] | Boss Rush (Terminus mats) [5] | Proto Bahamut Farm [6]\n"
					  "Triple Bosses (Silver centrum + ex refiniums + L crystals) [7] | Behemoth [8]\n"
					  "Trade Wrightstones [9] | Trade Sigils [0] | Spam Single Quest [20]\n\n")
	if farm_mode == '1':
		logger.info("Starting Slimepede Farm")
	elif farm_mode == '2':
		logger.info("Starting Fortitude Crystal Farm")
	elif farm_mode =='3':
		# TODO: Add try catch for all screen captures
		logger.info("Testing screen capture for user")
		logger.info("Sleeping for 3 seconds for you to alt tab to game")
		time.sleep(3)
		logger.info("Attempting to detect the main menu")
		pos = imagesearch_loop("./Granblue_ImageSearch/main_menu.png", timesample=1.0, precision=0.75)
		logger.info("Detected the main menu we good.\n")
		
		logger.info("Start a mission and test if this can detect when it starts and the post battle screen\n")
		time.sleep(5)
		logger.info("Begin checking for start of quest. Looking for the time left at top right corner every 1 second\n")
		time.sleep(2)
		pos = imagesearch_loop("./Granblue_ImageSearch/time_left.png", timesample=1.0, precision=0.75)
		logger.info("Time left detected. Will check for post battle results screen now")
		time.sleep(3)
		pos = imagesearch_loop("./Granblue_ImageSearch/post_battle_status.png", timesample=1.0, precision=0.75)
		logger.info("Post battle result screen detected. You are good to go.\n\n")
		logger.info("EXIT OUT AND RESTART PROGRAM\n")
		time.sleep(5)


	elif farm_mode == '4':
		logger.info("Starting Luci farm")
	elif farm_mode == '5':
		logger.info("Starting boss rush (Furycane > Managarmr > Vulkan > Pyet-A (2x))")
	elif farm_mode == '6':
		logger.info("Starting proto farm")
	elif farm_mode == '7':
		logger.info("Starting triple bosses (Worst vacation > trade > banquent > freer)")
	elif farm_mode == '8':
		logger.info('Starting behenmoth')
	elif farm_mode == '9':
		logger.info("testing trading wrightstones")
		# checkQuestFinished()
		logger.info("Sleeping for 3 seconds to alt tab")
		time.sleep(3)
		pressButton("A")
		pressButton("A")
		time.sleep(1)
		pressButton("Y")
		time.sleep(2)
		# tradeWrightstones()
	elif farm_mode == '11':
		logger.info("Starting berserker echo farm")

	elif farm_mode == '15':
		logger.info("Starting new slime farm")
	elif farm_mode == '16':
		logger.info("Starting the world farm")

	elif farm_mode == '0':
		logger.info("testing trading sigils")
		# checkQuestFinished()
		logger.info("Sleeping for 3 seconds to alt tab")
		time.sleep(3)
		pressButton("A")
		pressButton("A")
		time.sleep(1)
		pressButton("Y")
		time.sleep(2)
		tradeSigils()
	elif farm_mode == '20':
		logger.info("Spamming one quest over and over!")
	else:
		logger.info("invalid buh")
	
	logger.info("Waiting 5 seconds to alt tab into the game")
	time.sleep(5)
	logger.info("Button checking")
	pressButton("A")
	pressButton("A")

	# full_run = 10 runs and total_runs = per completed run
	full_run = 0
	total_runs = 0
	boss_order = 0
	triple_boss_order = 0
	while True:
		if farm_mode != '20':
			logger.info("Back in town #" + str(full_run))
			# logger.info("Boss order: " + str(boss_order))
			logger.info("Waiting 10 seconds to account for loads")
			# sleep 10 seconds to account for load times on repeat
			time.sleep(10)
		if (total_runs % 20 == 0) and (total_runs != 0):
			logger.info("Been 30 runs TIME TO GAMBA")
			teleportKnick()
		if (triple_boss_order == 4):
			logger.info("Resetting triple boss order")
			triple_boss_order = 0
		if (boss_order == 5):
			logger.info("Resetting boss order so it loops")
			boss_order = 0

		if farm_mode != '20':
			teleportToQuest()
			
		if farm_mode == '1':
			if full_run < 1:
				startSlimeQuest()
			else:
				startSlimeSubsequent()
		
		elif farm_mode == '2':
			if full_run < 1:
				startFortitudeQuest()
			else:
				startFortitudeSubsequent()
		elif farm_mode == '4':
			if full_run < 1:
				startLuciliusQuest()
			else:
				startLuciliusSubsequent()
		elif farm_mode == '5':
			if full_run < 1:
				startBossRush()
			else:
				startBossRushSubsequent(boss_order)
		elif farm_mode == '6':
			if full_run < 1:
				startProtoQuest()
			else:
				startProtoSubsequent()
		elif farm_mode == '7':
			if full_run < 1:
				startTripleBossQuest()
			else:
				startTripleBossSubsequent(triple_boss_order)
		elif farm_mode == '8':
			if full_run < 1:
				startBehemoth()
			else:
				startBehemothSubsequent()
		elif farm_mode == '11':
			if full_run < 1:
				startZathbaVolunteers()
			else:
				startZathbaVolunteersSubsequent()
		elif farm_mode == '15':
			if full_run < 1:
				startNewSlimeQuest()
			else:
				startNewSlimeSubsequent()
		elif farm_mode == '16':
			if full_run < 1:
				startWorldQuest()
			else:
				startWorldSubsequentQuest()

		if farm_mode == '1' or farm_mode == '2' or farm_mode == '15':	
			logger.info("Starting Quest")
			now = datetime.datetime.now()
			logger.info("Current date and time : ")
			logger.info(now.strftime("%Y-%m-%d %H:%M:%S"))
			logger.info("Moving up 5 seconds")
			runUp(5)
			if farm_mode == '1' or farm_mode == '15':
				mashAttack(2.99)
			elif farm_mode == '2':
				mashAttack(3.99)
			total_runs = total_runs + 1
			logger.info("Quest Complete")
			logger.info("Completed fight #" + str(total_runs))
			# 0:00 (end of quest) takes 20 seconds to get to
			# results screen -- not sure about pose time
			time.sleep(20)
			# wait through the battle results screen
			time.sleep(30)

			# 60 seconds for 2nd battle screen
			# press repeat quest and accept
			time.sleep(10)
			logger.info("Repeating")
			pressButton("X")
			pressButton("A")
			# click through and repeat
			logger.info("Continuing")
			pressButton("A")
			pressButton("A")
			logger.info("Now loading")
			# loop through 9 more times for the quest
			i = 0
			while i < 9:
				# wait for time to load level
				time.sleep(10)
				#TODO: This is +1 higher than it actually is
				logger.info("Done loading. Starting fight")
				now = datetime.datetime.now()
				logger.info("Current date and time : ")
				logger.info(now.strftime("%Y-%m-%d %H:%M:%S"))
				logger.info("Moving up 5 seconds")
				runUp(5)
				if farm_mode == '1' or farm_mode == '15':
					mashAttack(2.99)
				elif farm_mode == '2':
					mashAttack(3.99)
				total_runs = total_runs + 1
				logger.info("Quest #" + str(total_runs) + " Complete. Waiting 30 seconds")
				# end of level now wait for battle results screen
				time.sleep(30)
				# mash A to get through results screen faster
				logger.info("Mashing A to go fast\n")
				mashAButton(8)
				i = i + 1
			full_run = full_run + 1
		
		elif farm_mode == '4' or farm_mode == '8' or farm_mode == '11' or farm_mode == '16':
			logger.info("Actually starting luci/behemoth/zathba/world")
			i = 0
			while i < 10:
				logger.info("Starting Luci/behemoth/World. Look for quest timer every half second")
				pos = imagesearch_loop("./Granblue_ImageSearch/time_left.png", timesample=0.5, precision=0.75)
				now = datetime.datetime.now()
				logger.info("Quest timer detected")
				logger.info("Starting fight")

				# reset pos and keep looping
				#pos.clear()

				logger.info("Creating MultiThreads")
				luciAttackThread = threading.Thread(target=luciAttackSpam)
				luciBattleScreen = threading.Thread(target=checkBattleScreen)
				isQuestFinishedThread = threading.Thread(target=checkQuestFinished)
				luciAttackThread.start()
				# luciBattleScreen.start()
				isQuestFinishedThread.start()

				luciAttackThread.join()
				# luciBattleScreen.join()
				isQuestFinishedThread.join()
				#pos.clear()

				# TODO - walk and collect the chests
				# TODO - not checking for treasure screen

				# logger.info("Detected Quest ending timer to collect treasure. Waiting 30 seconds for results screen.")

				#walkAndCollectTreaures()

				# first completion/fail repeat the quest
				if i == 0:
					# logger.info("Now we wait 1 minute to get to post battle results screen.")
					# time.sleep(60)
					# logger.info("Searching for post battle screen (again if fail)")

					# pos = imagesearch_loop("./Granblue_ImageSearch/post_battle_status.png", timesample=0.5, precision=0.75)
					logger.info("Post battle results screen detected.")
					total_runs = total_runs + 1
					logger.info("Quest #" + str(total_runs) + " Complete.\n")

					time.sleep(5)
					logger.info("Repeating the quest another 9 times.")
					# testing up button twice in case of buffer?
					logger.info("TESTING UP BUTTON TWICE")
					pressButton("UP")
					pressButton("UP")
					time.sleep(1)
					pressButton("X")
					time.sleep(1)
					pressButton("A")
					# click through and repeat
					logger.info("Continuing")
					pressButton("A")
					pressButton("A")
					logger.info("Now waiting 10 seconds for load")
					time.sleep(10)
					i = i + 1
					IS_FIGHT_FINISHED = False
				
				# 2 - 10 quests should auto repeat
				else:
					# logger.info("Looking for battle results screen every second")
					# pos = imagesearch_loop("./Granblue_ImageSearch/battle_results.png", timesample=1, precision=0.8)
					# logger.info("Battle results screen detected.")
					logger.info("Searching for post battle screen (again if fail)")
					pos = imagesearch_loop("./Granblue_ImageSearch/post_battle_status.png", timesample=0.5, precision=0.75)
					logger.info("Post battle results screen detected.")

					total_runs = total_runs + 1
					logger.info("Quest #" + str(total_runs) + " Complete.\n")
					
					time.sleep(5)
					# mash A to get through results screen faster
					logger.info("Mashing A to go fast\n")
					mashAButton(8)
					logger.info("Loading 10 seconds to wait")
					time.sleep(10)
					i = i + 1
					IS_FIGHT_FINISHED = False
			full_run = full_run + 1
		
		elif farm_mode == '20':
			i = 0
			while i < 500:
				logger.info("Starting a quest and just repeating. Look for quest timer every half second")
				try:
					pos = imagesearch_loop("./Granblue_ImageSearch/time_left.png", timesample=0.5, precision=0.75)
					now = datetime.datetime.now()
					logger.info("Quest timer detected)")
					logger.info("Starting fight")

					# reset pos and keep looping
					#pos.clear()

					logger.info("Creating MultiThreads")
					luciAttackThread = threading.Thread(target=luciAttackSpam)
					# luciBattleScreen = threading.Thread(target=checkBattleScreen)
					isQuestFinishedThread = threading.Thread(target=checkQuestFinished)
					luciAttackThread.start()
					# luciBattleScreen.start()
					isQuestFinishedThread.start()

					luciAttackThread.join()
					# luciBattleScreen.join()
					isQuestFinishedThread.join()
					
					
					# logger.info("Searching for post battle screen (again if fail)")
					logger.info("Checking for post_battle_status screen every 1.0 seconds")
					pos = imagesearch_loop("./Granblue_ImageSearch/post_battle_status.png", timesample=0.5, precision=0.75)
					logger.info("Post battle results screen detected.")

					total_runs = total_runs + 1
					logger.info("Quest #" + str(total_runs) + " Complete.\n")
					
					time.sleep(3)
					if i == 0:
						logger.info("First quest. Pressing repeat quest")
						logger.info("Trying to press X AND A")
						pressButton("X")
						time.sleep(1)
						pressButton("A")
					else:
						logger.info("Trying to press UP AND A")
						pressButton("UP")
						time.sleep(1)
						pressButton("A")
					# mash A to get through results screen faster
					# logger.info("Mashing A to go fast\n")
					mashAButton(8)
					# pressButton("A")
					logger.info("Loading 10 seconds to wait")
					time.sleep(10)
					i = i + 1
					IS_FIGHT_FINISHED = False
				except Exception as e:
					logger.exception("\nbuhhh... Something went wrong.. Check the logs for details.")
					logger.info("Exiting the program gracefully... buhhh")
					time.sleep(3)
					sys.exit()



		elif farm_mode == '5' or farm_mode == '6' or farm_mode == '7':
			if farm_mode == '5':
				logger.info("Boss rush time")
			if farm_mode == '6':
				logger.info("Proto time")
			if farm_mode == '7':
				logger.info("Triple boss time")
			i = 0
			while i < 10:
				if farm_mode == '5':
					logger.info("Starting boss rush. Look for quest timer every half second")
				if farm_mode == '6':
					logger.info("Starting proto. Look for quest timer every half second")
				if farm_mode == '7':
					logger.info("Starting triple bosses. Look for quest timer every half second")
				pos = imagesearch_loop("./Granblue_ImageSearch/time_left.png", timesample=0.5, precision=0.75)
				logger.info("Quest timer detected at: ", pos[0], pos[1])
				logger.info("Starting fight")
				now = datetime.datetime.now()
				logger.info("Current date and time : ")
				logger.info(now.strftime("%Y-%m-%d %H:%M:%S"))

				# logger.info("Creating MultiThreads")
				if farm_mode == '6':
					protoStartThread = threading.Thread(target=protoStart)
					isQuestFinishedThread = threading.Thread(target=checkQuestFinished)
					protoStartThread.start()
					isQuestFinishedThread.start()

					protoStartThread.join()
					isQuestFinishedThread.join()
				else:
					holdBlockThread = threading.Thread(target=holdBlock)
					isQuestFinishedThread = threading.Thread(target=checkQuestFinished)
					holdBlockThread.start()
					isQuestFinishedThread.start()

					holdBlockThread.join()
					isQuestFinishedThread.join()

				# first completion/fail repeat the quest
				if i == 0:
					logger.info("Searching for post battle screen (again if fail)")

					pos = imagesearch_loop("./Granblue_ImageSearch/post_battle_status.png", timesample=0.5, precision=0.75)
					logger.info("Post battle results screen detected.")
					total_runs = total_runs + 1
					logger.info("Quest #" + str(total_runs) + " Complete.\n")

					time.sleep(5)
					logger.info("Repeating the quest another 9 times.")
					pressButton("X")
					time.sleep(0.5)
					pressButton("A")
					# click through and repeat
					logger.info("Continuing")
					pressButton("A")
					pressButton("A")
					logger.info("Now waiting 10 seconds for load\n")
					time.sleep(10)
					i = i + 1
					IS_FIGHT_FINISHED = False
				
				# 2 - 10 quests should auto repeat
				else:
					logger.info("Searching for post battle screen (again if fail)")
					pos = imagesearch_loop("./Granblue_ImageSearch/post_battle_status.png", timesample=0.5, precision=0.75)
					logger.info("Post battle results screen detected.")

					total_runs = total_runs + 1
					logger.info("Quest #" + str(total_runs) + " Complete.\n")
					
					time.sleep(5)
					# mash A to get through results screen faster
					logger.info("Mashing A to go fast\n")
					mashAButton(8)
					logger.info("Loading 10 seconds to wait\n")
					time.sleep(10)
					i = i + 1
					IS_FIGHT_FINISHED = False
			if farm_mode == '5':
				boss_order = boss_order + 1
			if farm_mode == '7':
				triple_boss_order = triple_boss_order + 1
			full_run = full_run + 1