import vgamepad as vg
import tkinter as tk
from pynput.keyboard import Listener, KeyCode
import time

GAMEPAD = vg.VX360Gamepad()
BUTTON_LIST = {
	"A": vg.XUSB_BUTTON.XUSB_GAMEPAD_A,
	"B": vg.XUSB_BUTTON.XUSB_GAMEPAD_B,
	"X": vg.XUSB_BUTTON.XUSB_GAMEPAD_X,
	"Y": vg.XUSB_BUTTON.XUSB_GAMEPAD_Y,
	"LB": vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER,
	"RB": vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER,
	"START": vg.XUSB_BUTTON.XUSB_GAMEPAD_START,
	"UP": vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP,
	"DOWN": vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN,
	"LEFT": vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT,
	"RIGHT": vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT
}
START_END = False

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
	print("Waiting 22 seconds for load")
	time.sleep(22)

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
	print("Waiting 22 seconds for load")
	time.sleep(22)

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
	print("Waiting 22 seconds for load")
	time.sleep(22)

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

def pressButton(xbox_button):
	GAMEPAD.press_button(button=BUTTON_LIST[xbox_button])
	GAMEPAD.update()
	time.sleep(0.15)
	GAMEPAD.release_button(button=BUTTON_LIST[xbox_button])
	GAMEPAD.update()
	time.sleep(0.2)

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


if __name__ == '__main__':
	# Collect all event until released
	# wait 3 seconds before starting
	# press a button to wake the device up
	print("Ranged main character required to be optimal")
	print("Recommended to set the game to 720p 30fps if you go afk")
	print("Make sure the quest board is in default state before running.")
	print("Choose a farm. In the terminal, type 1 then press enter to farm slimes for example\n")
	farm_mode = input("Slimepede Farm [1] | Fortitude Crystal Farm [2]\n")
	if farm_mode == '1':
		print("Starting Slimepede Farm")
	elif farm_mode == '2':
		print("Starting Fortitude Crystal Farm")
	else:
		print("1 or 2 chief cause I ain't writing code for other exceptions right now. Restart it")
	
	print("Waiting 5 seconds to alt tab into the game")
	time.sleep(5)
	print("Button checking")
	pressButton("A")
	pressButton("A")
	full_run = 0
	total_runs = 0
	while True:
		print("Back in town #" + str(full_run))
		print("Waiting 10 seconds to account for loads")
		# sleep 10 seconds to account for load times on repeat
		time.sleep(10)
		if (total_runs % 30 == 0) and (total_runs != 0):
			print("Been 30 runs TIME TO GAMBA")
			teleportKnick()
		
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
		else:
			print("Restart program buddy ain't working choose 1 or 2")
		
		print("Starting Quest")
		print("Moving up 3 seconds")
		moveUp(3)
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
			time.sleep(12)
			#TODO: This is +1 higher than it actually is
			print("Done loading. Starting fight")
			print("Moving up 3 seconds")
			moveUp(3)
			if farm_mode == '1':
				mashAttack(2.99)
			elif farm_mode == '2':
				mashAttack(3.99)
			total_runs = total_runs + 1
			print("Quest #" + str(total_runs) + "Complete. Waiting 30 seconds")
			# end of level now wait for battle results screen
			time.sleep(30)
			# mash A to get through results screen faster
			print("Mashing A to go fast\n")
			mashAButton(8)
			i = i + 1
		full_run = full_run + 1