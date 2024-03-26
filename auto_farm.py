import vgamepad as vg
import tkinter as tk
import time
import datetime
import threading
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
	"UP": vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP,
	"DOWN": vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN,
	"LEFT": vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT,
	"RIGHT": vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT
}
START_END = False
IS_FIGHT_FINISHED = False

def teleportToQuest():
	print("Teleporting to quest counter")
	# open up the shortcut menu
	print("Opening shortcut")
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

	print("Walking to quest board")
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
	print("Waiting 26 seconds for load")
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
	print("Waiting 26 seconds for load")
	time.sleep(26)

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
	print("Waiting 24 seconds for load")
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
	print("Waiting 22 seconds for load")
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
	# UP 1 time
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
	print("Waiting 24 seconds for load")
	time.sleep(24)

def startLuciliusSubsequent():
	# press on undertake quest
	pressButton("A")
	# press on proud difficulty
	pressButton("A")
	# up to go to bottom of list
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
	print("Waiting 22 seconds for load")
	time.sleep(22)

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
	print("Waiting 24 seconds for load")
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
	print("Waiting 22 seconds for load")
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
	print("Waiting 24 seconds for load")
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
		print("Furrycane cycle")
		pressButton("DOWN")
	# managarmr
	elif (boss_order == 1):
		print("Managarmr cycle")
		for i in range(2):
			pressButton("DOWN")
	# vulkan
	elif (boss_order == 2):
		print("Vulkan cycle")
		for i in range(3):
			pressButton("DOWN")
	# pyet-a
	elif (boss_order == 3 or boss_order == 4):
		print("Pyet-A cycle")
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
	print("Waiting 22 seconds for load")
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
	print("Waiting 24 seconds for load")
	time.sleep(24)

def startTripleBossSubsequent(triple_boss_order):
	# press on undertake quest
	pressButton("A")
	# press on proud difficulty
	pressButton("A")

	# worst vacation ever
	if (triple_boss_order == 0):
		print("Worst vacation cycle")
		for i in range(5):
			pressButton("DOWN")
	# trade barrier
	elif (triple_boss_order == 1):
		print("Trade barrier cycle")
		for i in range(6):
			pressButton("DOWN")
	# banquet of ice
	elif (triple_boss_order == 2):
		print("Banquet of ice cycle")
		for i in range(8):
			pressButton("DOWN")
	# freer folca
	elif (triple_boss_order == 3):
		print("Freer folca cycle")
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
	print("Waiting 22 seconds for load")
	time.sleep(22)

def lanceSpam():
	GAMEPAD.press_button(button=BUTTON_LIST["Y"])
	GAMEPAD.press_button(button=BUTTON_LIST["B"])
	GAMEPAD.left_trigger_float(value_float=1.0)
	GAMEPAD.update()
	time.sleep(0.05)
	GAMEPAD.release_button(button=BUTTON_LIST["Y"])
	GAMEPAD.release_button(button=BUTTON_LIST["B"])
	GAMEPAD.left_trigger_float(value_float=0)
	GAMEPAD.update()
	time.sleep(0.05)

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
	print("Mashing Attack")
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
	print("Teleporting to knickknack")
	# open up the shortcut menu
	print("Opening shortcut")
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

	print("Walking to knickknack")
	# walk 1 second up
	moveUp(1)
	# interact with the quest counter
	pressButton("Y")
	time.sleep(2)

	gambaSigils()

def gambaSigils():
	print("Gamba gamba")
	# down 3 then down 2
	pressButton("DOWN")
	pressButton("DOWN")
	pressButton("DOWN")
	pressButton("A")
	pressButton("DOWN")
	pressButton("DOWN")
	print("TIME TO GAMBA for 2 MIN")
	mashAButton(120)

	# done with gamba
	mashButton("B", 6)
	time.sleep(2)

def printTest():
	while(not IS_FIGHT_FINISHED):
		print("Fight not finished")
		time.sleep(1)
	print("Fight finished")
		

def isTest():
	print("Testing image serach")
	pos = imagesearch_loop("./Granblue ImageSearch/SBA_ready.png", timesample=5, precision=0.75)
	print("position : ", pos[0], pos[1])
	global IS_FIGHT_FINISHED 
	IS_FIGHT_FINISHED = True

def luciAttackSpam():
	while(not IS_FIGHT_FINISHED):
		lanceSpam()
		pressButtonSimultaneously("LSB", "RSB")

def protoStart():
	# walk to the left and hold block
	print("Walking to the left side of the ship for 5 seconds and holding block\n")
	GAMEPAD.left_joystick_float(x_value_float=-1.0, y_value_float=0.0)
	GAMEPAD.update()
	time.sleep(5)
	GAMEPAD.left_joystick_float(x_value_float=0.0, y_value_float=0.0)
	GAMEPAD.update()
	print("Move up 2 seconds")
	moveUp(2)
	hold_block_mash_b()

def hold_block_mash_b():
	print("Holding block and mashing B until fight is over")
	while(not IS_FIGHT_FINISHED):
		GAMEPAD.press_button(button=BUTTON_LIST["LB"])
		GAMEPAD.left_joystick_float(x_value_float=-1.0, y_value_float=1.0)
		GAMEPAD.update()
		pressButton("B")
		time.sleep(1)
	print("Letting go of block. Fight is over")
	GAMEPAD.release_button(button=BUTTON_LIST["LB"])
	GAMEPAD.left_joystick_float(x_value_float=0.0, y_value_float=0.0)
	GAMEPAD.update()

def holdBlock():
	print("Holding block until fight is over")
	while(not IS_FIGHT_FINISHED):
		GAMEPAD.press_button(button=BUTTON_LIST["LB"])
		GAMEPAD.update()
	print("Letting go of block. Fight is over")
	GAMEPAD.release_button(button=BUTTON_LIST["LB"])
	GAMEPAD.update()

def checkQuestFinished():
	print("Checking if we are on battle results/post results screen every 1.0 seconds")
	pos = imagesearch("./Granblue ImageSearch/collect_treasure.png", precision=0.75)
	time.sleep(1)
	while(pos[0] == -1):
		# print('searching')
		# pos = imagesearch("./Granblue ImageSearch/battle_results.png", precision=0.75)
		# time.sleep(2)
		# print("2nd search")
		pos = imagesearch("./Granblue ImageSearch/post_battle_status.png", precision=0.75)
		time.sleep(1.5)
		# time.sleep(2)
	#pos = imagesearch_loop("./Granblue ImageSearch/collect_treasure.png", timesample=1.0, precision=0.8)
	print("Battle results/Failure screen detected.")
	global IS_FIGHT_FINISHED
	IS_FIGHT_FINISHED = True

	# TODO - if fail then handle

def walkAndCollectTreaures():
	print("Attempting to collect all tresures within 30 seconds")
	print("Going to use 3 lance heavy attacks with the sigil")
	for i in range(3):
		pressButton("Y")
	print("Walking up for a second")
	moveUp(1)
	print("Spamming B to collect treasure")
	mashButton("B", 1)
	
	print("Move left and spam B")
	# getting 2nd chest 
	# TODO: optimize this 
	GAMEPAD.left_joystick_float(x_value_float=-1.0, y_value_float=0.0)
	GAMEPAD.update()
	time.sleep(1)
	GAMEPAD.left_joystick_float(x_value_float=0.0, y_value_float=0.0)
	GAMEPAD.update()
	mashButton("B", 1)

	# getting 1st chest
	GAMEPAD.left_joystick_float(x_value_float=-1.0, y_value_float=0.0)
	GAMEPAD.update()
	time.sleep(1)
	GAMEPAD.left_joystick_float(x_value_float=0.0, y_value_float=0.0)
	GAMEPAD.update()
	mashButton("B", 1)

	# walk over to the 4th and 5th chest holding right and spamming B for 8 seconds
	GAMEPAD.left_joystick_float(x_value_float=1.0, y_value_float=0.0)
	GAMEPAD.update()
	mashButton("B", 8)
	GAMEPAD.left_joystick_float(x_value_float=0.0, y_value_float=0.0)
	GAMEPAD.update()
	
	print("Hopefully all chests have been collected. Now to the battle results screen.")

if __name__ == '__main__':
	# Collect all event until released
	# wait 3 seconds before starting
	# press a button to wake the device up
	print("Ranged main character required to be optimal")
	print("Recommended to set the game to 720p 30fps if you go afk")
	print("Make sure the quest board is in default state before running.")
	print("Choose a farm. In the terminal, type 1 then press enter to farm slimes for example\n")
	farm_mode = input("Slimepede Farm [1] | Fortitude Crystal Farm (INEFFICIENT) [2] | TEST SCREEN CAPTURE [3]\n"
					  "Lucilius Farm [4] | Boss Rush (Terminus mats) [5] | Proto Bahamut Farm [6]\n"
					  "Triple Bosses (Silver centrum + ex refiniums + L crystals) [7]\n\n")
	if farm_mode == '1':
		print("Starting Slimepede Farm")
	elif farm_mode == '2':
		print("Starting Fortitude Crystal Farm")
	elif farm_mode =='3':
		print("Testing screen capture for user")
		print("Sleeping for 3 seconds for you to alt tab to game")
		time.sleep(3)
		print("Attempting to detect the main menu")
		pos = imagesearch_loop("./Granblue ImageSearch/main_menu.png", timesample=1.0, precision=0.75)
		print("Detected the main menu we good.\n")
		
		print("Start a mission and test if this can detect when it starts and the post battle screen\n")
		time.sleep(5)
		print("Begin checking for start of quest. Looking for the time left at top right corner every 1 second\n")
		time.sleep(2)
		pos = imagesearch_loop("./Granblue ImageSearch/time_left.png", timesample=1.0, precision=0.75)
		print("Time left detected. Will check for post battle results screen now")
		time.sleep(3)
		pos = imagesearch_loop("./Granblue ImageSearch/post_battle_status.png", timesample=1.0, precision=0.75)
		print("Post battle result screen detected. You are good to go.\n\n")
		print("EXIT OUT AND RESTART PROGRAM\n")
		time.sleep(5)


	elif farm_mode == '4':
		print("Starting Luci farm")
	elif farm_mode == '5':
		print("Starting boss rush (Furycane > Managarmr > Vulkan > Pyet-A (2x))")
	elif farm_mode == '6':
		print("Starting proto farm")
	elif farm_mode == '7':
		print("Starting triple bosses (Worst vacation > trade > banquent > freer)")
	elif farm_mode == '9':
		print("testing something")
		checkQuestFinished()
	else:
		print("invalid buh")
	
	print("Waiting 5 seconds to alt tab into the game")
	time.sleep(5)
	print("Button checking")
	pressButton("A")
	pressButton("A")

	# full_run = 10 runs and total_runs = per completed run
	full_run = 0
	total_runs = 0
	boss_order = 0
	triple_boss_order = 0
	while True:
		print("Back in town #" + str(full_run))
		# print("Boss order: " + str(boss_order))
		print("Waiting 10 seconds to account for loads")
		# sleep 10 seconds to account for load times on repeat
		time.sleep(10)
		if (total_runs % 20 == 0) and (total_runs != 0):
			print("Been 30 runs TIME TO GAMBA")
			teleportKnick()
		if (triple_boss_order == 4):
			print("Resetting triple boss order")
			triple_boss_order = 0
		if (boss_order == 5):
			print("Resetting boss order so it loops")
			boss_order = 0
		
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

		if farm_mode == '1' or farm_mode == '2':	
			print("Starting Quest")
			now = datetime.datetime.now()
			print("Current date and time : ")
			print(now.strftime("%Y-%m-%d %H:%M:%S"))
			print("Moving up 5 seconds")
			runUp(5)
			if farm_mode == '1':
				mashAttack(2.99)
			elif farm_mode == '2':
				mashAttack(3.99)
			total_runs = total_runs + 1
			print("Quest Complete")
			print("Completed fight #" + str(total_runs))
			# 0:00 (end of quest) takes 20 seconds to get to
			# results screen -- not sure about pose time
			time.sleep(20)
			# wait through the battle results screen
			time.sleep(30)

			# 60 seconds for 2nd battle screen
			# press repeat quest and accept
			time.sleep(10)
			print("Repeating")
			pressButton("X")
			pressButton("A")
			# click through and repeat
			print("Continuing")
			pressButton("A")
			pressButton("A")
			print("Now loading")
			# loop through 9 more times for the quest
			i = 0
			while i < 9:
				# wait for time to load level
				time.sleep(16)
				#TODO: This is +1 higher than it actually is
				print("Done loading. Starting fight")
				now = datetime.datetime.now()
				print("Current date and time : ")
				print(now.strftime("%Y-%m-%d %H:%M:%S"))
				print("Moving up 5 seconds")
				runUp(5)
				if farm_mode == '1':
					mashAttack(2.99)
				elif farm_mode == '2':
					mashAttack(3.99)
				total_runs = total_runs + 1
				print("Quest #" + str(total_runs) + " Complete. Waiting 30 seconds")
				# end of level now wait for battle results screen
				time.sleep(30)
				# mash A to get through results screen faster
				print("Mashing A to go fast\n")
				mashAButton(8)
				i = i + 1
			full_run = full_run + 1
		
		elif farm_mode == '4':
			print("Actually starting luci")
			i = 0
			while i < 10:
				print("Starting Luci. Look for quest timer every half second")
				pos = imagesearch_loop("./Granblue ImageSearch/time_left.png", timesample=0.5, precision=0.75)
				now = datetime.datetime.now()
				print("Current date and time : ")
				print(now.strftime("%Y-%m-%d %H:%M:%S"))
				print("Quest timer detected at: ", pos[0], pos[1])
				print("Starting fight")

				# reset pos and keep looping
				#pos.clear()

				print("Creating MultiThreads")
				luciAttackThread = threading.Thread(target=luciAttackSpam)
				isQuestFinishedThread = threading.Thread(target=checkQuestFinished)
				luciAttackThread.start()
				isQuestFinishedThread.start()

				luciAttackThread.join()
				isQuestFinishedThread.join()
				#pos.clear()

				# TODO - walk and collect the chests
				# TODO - not checking for treasure screen

				# print("Detected Quest ending timer to collect treasure. Waiting 30 seconds for results screen.")

				#walkAndCollectTreaures()

				# first completion/fail repeat the quest
				if i == 0:
					# print("Now we wait 1 minute to get to post battle results screen.")
					# time.sleep(60)
					print("Searching for post battle screen (again if fail)")

					pos = imagesearch_loop("./Granblue ImageSearch/post_battle_status.png", timesample=0.5, precision=0.75)
					print("Post battle results screen detected.")
					total_runs = total_runs + 1
					print("Quest #" + str(total_runs) + " Complete.\n")

					time.sleep(5)
					print("Repeating the quest another 9 times.")
					pressButton("X")
					time.sleep(0.5)
					pressButton("A")
					# click through and repeat
					print("Continuing")
					pressButton("A")
					pressButton("A")
					print("Now waiting 10 seconds for load")
					time.sleep(10)
					i = i + 1
					IS_FIGHT_FINISHED = False
				
				# 2 - 10 quests should auto repeat
				else:
					# print("Looking for battle results screen every second")
					# pos = imagesearch_loop("./Granblue ImageSearch/battle_results.png", timesample=1, precision=0.8)
					# print("Battle results screen detected.")
					print("Searching for post battle screen (again if fail)")
					pos = imagesearch_loop("./Granblue ImageSearch/post_battle_status.png", timesample=0.5, precision=0.75)
					print("Post battle results screen detected.")

					total_runs = total_runs + 1
					print("Quest #" + str(total_runs) + " Complete.\n")
					
					time.sleep(5)
					# mash A to get through results screen faster
					print("Mashing A to go fast\n")
					mashAButton(8)
					print("Loading 10 seconds to wait")
					time.sleep(10)
					i = i + 1
					IS_FIGHT_FINISHED = False
			full_run = full_run + 1

		elif farm_mode == '5' or farm_mode == '6' or farm_mode == '7':
			if farm_mode == '5':
				print("Boss rush time")
			if farm_mode == '6':
				print("Proto time")
			if farm_mode == '7':
				print("Triple boss time")
			i = 0
			while i < 10:
				if farm_mode == '5':
					print("Starting boss rush. Look for quest timer every half second")
				if farm_mode == '6':
					print("Starting proto. Look for quest timer every half second")
				if farm_mode == '7':
					print("Starting triple bosses. Look for quest timer every half second")
				pos = imagesearch_loop("./Granblue ImageSearch/time_left.png", timesample=0.5, precision=0.75)
				print("Quest timer detected at: ", pos[0], pos[1])
				print("Starting fight")
				now = datetime.datetime.now()
				print("Current date and time : ")
				print(now.strftime("%Y-%m-%d %H:%M:%S"))

				# print("Creating MultiThreads")
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
					print("Searching for post battle screen (again if fail)")

					pos = imagesearch_loop("./Granblue ImageSearch/post_battle_status.png", timesample=0.5, precision=0.75)
					print("Post battle results screen detected.")
					total_runs = total_runs + 1
					print("Quest #" + str(total_runs) + " Complete.\n")

					time.sleep(5)
					print("Repeating the quest another 9 times.")
					pressButton("X")
					time.sleep(0.5)
					pressButton("A")
					# click through and repeat
					print("Continuing")
					pressButton("A")
					pressButton("A")
					print("Now waiting 10 seconds for load\n")
					time.sleep(10)
					i = i + 1
					IS_FIGHT_FINISHED = False
				
				# 2 - 10 quests should auto repeat
				else:
					print("Searching for post battle screen (again if fail)")
					pos = imagesearch_loop("./Granblue ImageSearch/post_battle_status.png", timesample=0.5, precision=0.75)
					print("Post battle results screen detected.")

					total_runs = total_runs + 1
					print("Quest #" + str(total_runs) + " Complete.\n")
					
					time.sleep(5)
					# mash A to get through results screen faster
					print("Mashing A to go fast\n")
					mashAButton(8)
					print("Loading 10 seconds to wait\n")
					time.sleep(10)
					i = i + 1
					IS_FIGHT_FINISHED = False
			if farm_mode == '5':
				boss_order = boss_order + 1
			if farm_mode == '7':
				triple_boss_order = triple_boss_order + 1
			full_run = full_run + 1