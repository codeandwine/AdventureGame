import time
import random

start = time.time()
enemies = ['Death Spirit', 'Duende', 'Zipacná', 'Xibalba', 'Buluc Chabtan']
enemy = random.choice(enemies)
weapon = "Hatchet"

def print_sleep(message):
	print(message)
	time.sleep(1.5) #change this line for the pauses

def intro():
	print_sleep("You find you are in the Jungles of Belize, filled with Mayan witchcraft and supernatural creatures.")
	print_sleep("Rumor has it that an evil sprit is still roaming the mountains.")
	print_sleep("In front of you is a Mayan Temple.")
	print_sleep("Beside the temple there is a roaring river.")
	print_sleep("In your hand you hold a hatchet, though it's a bit blunt.\n")
	options()

def options():
	start = '0'
	print_sleep("Enter 1 to knock on the door of the Mayan Temple.")
	print_sleep("Enter 2 to drink some water from the river.")
	print_sleep("(Please enter the numbers 1 or 2.)")

	start = input()
	if start == '1':
		knock_on_door()
	elif start == '2':
		drink_water()
	else:
		"You didn't enter the numbers specified!"


def knock_on_door():
	first_step = '0'
	print_sleep("You walk towards the weird door at the top of the Temple.")
	print_sleep(f"You are about to reach the door when a grotesque looking {enemy} opens the door.")
	print_sleep("Holy Molly! This is the evil spirit encarnate!")
	print_sleep(f"The ugly {enemy} attacks you. You are quite frightened about this!")
	print_sleep("What should you do?")
	print_sleep(f"1. Use the {weapon}} to pierce his heart.")
	print_sleep("2. RUN AWAY!")

	first_step = input()
	if first_step == '1':
		pierce_heart()
	elif first_step == '2':
		run_away()

def drink_water():
	print_sleep("You walk towards the river bank. ")
	print_sleep("As you are you bend down to drink, you see something glistening")
	print_sleep(" in the water. You have found a magical sword!")
	print_sleep("You rid yourself of your hatchet and take the sword.")
	print_sleep("You head back to the jungle.\n")
	weapon = "Magical sword"
	options()


def pierce_heart():
	play_again = "x"

	if weapon == "Magical Sword":
		print_sleep(f"As the {enemy} makes a move at you, you take the {weapon}",
					" and pierce his heart.")
		print_sleep("The body collapses and the spirit ",
					"is thrown down into the underworld.")
		print_sleep("You have rid the Mayan Temple of the evil spirit!")
		print_sleep("You have won!")
	elif weapon == "Hatchet":
		print_sleep(f"You do your best to aim at {enemy}'s heart.")
		print_sleep("The human form of it is too swift and he evades your strike.")
		print_sleep("He possesses your body and steals your soul!")
		print_sleep("You have been defeated! :(")

	print_sleep("Would you like to play again? (y/n)")
	play_again = input()
	if play_again == 'y':
		intro()
	elif play_again == 'n':
		bye()

def bye():
	print_sleep("Thanks for playing! See you next time. :)")

intro()

end = time.time()
print("The program took: {}".format(end-start))
