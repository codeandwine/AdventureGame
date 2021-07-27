import time
import random

start = time.time()


def print_sleep(message, seconds):
    print(message)
    time.sleep(seconds)
    # change ^ this line for the pauses


def intro(weapon, enemy):
    print_sleep("You find you are in the Jungle of Belize, filled with Mayan "
                "witchcraft and supernatural creatures.", 1)
    print_sleep("Rumor has it that an evil sprit is still roaming "
                "the mountains.", 1)
    print_sleep("In front of you is a Mayan Temple.", 1)
    print_sleep("Beside the temple there is a roaring river.", 1)
    print_sleep("In your hand you hold a hatchet, though it's a bit blunt.\n", 2)
    options(weapon, enemy)


def options(weapon, enemy):
    start = '0'
    print_sleep("Enter 1 to knock on the door of the Mayan Temple.", 1)
    print_sleep("Enter 2 to drink some water from the river.", 1)

    while start not in ['1', '2']:
        start = input("(Please enter the numbers 1 or 2.)\n")

        if start == '1':
            knock_on_door(weapon, enemy)
        elif start == '2':
            drink_water(weapon, enemy)


def knock_on_door(weapon, enemy):
    first_step = '0'
    print_sleep("You walk towards the weird door at the top of the Temple.", 1)
    print_sleep(f"You are about to reach the door when a grotesque looking "
                f"{enemy} opens the door.", 2)
    print_sleep("Holy Molly! This is the evil spirit encarnate!", 1.5)
    print_sleep(f"The ugly {enemy} attacks you. You are quite frightened "
                "about this!", 1)
    print_sleep("What should you do?", 1)
    print_sleep(f"1. Use the {weapon} to pierce his heart.", 1)
    print_sleep("2. RUN AWAY!", 1)

    while first_step not in ['1', '2']:
        first_step = input("(Please enter the numbers 1 or 2.)\n")

        if first_step == '1':
            pierce_heart(weapon, enemy)
        elif first_step == '2':
            run_away(weapon, enemy)


def drink_water(weapon, enemy):
    if weapon == "Magical Sword":
        print_sleep("You have been here before. You already found the Magical "
                    "sword. You drink some water.", 1)
    else:
        print_sleep("You walk towards the river bank. ", 1.5)
        print_sleep("As you bend down to drink, you see something glistening "
                    "in the water. You have found a magical sword!", 1.5)
        print_sleep("You rid yourself of your hatchet and take the sword.", 1.5)
        weapon = "Magical Sword"

    print_sleep("You head back to the jungle.\n", 2)
    options(weapon, enemy)


def run_away(weapon, enemy):
    print_sleep("You run back to where you started in the Jungle of Belize!", 2)
    print_sleep(f"Luckily the {enemy} didn't follow you.\n", 1)
    options(weapon, enemy)


def pierce_heart(weapon, enemy):
    play_again = "x"

    if weapon == "Magical Sword":
        print_sleep(f"As the {enemy} makes a move at you, you take the "
                    f"{weapon} and pierce his heart.", 2)
        print_sleep("The body collapses and the spirit "
                    "is thrown down into the underworld.", 1.5)
        print_sleep("You have rid the Mayan Temple of the evil spirit!", 1)
        print_sleep("You have won!", 1)
    elif weapon == "Hatchet":
        print_sleep(f"You do your best to aim at {enemy}'s heart.", 2)
        print_sleep("The human form of it is too swift and he evades your "
                    "strike.", 1.5)
        print_sleep("He possesses your body and steals your soul!", 1)
        print_sleep("You have been defeated! :(", 1.5)

    while play_again not in ['y', 'n']:
        play_again = input("Would you like to play again? (y/n)\n").lower()

        if play_again == 'y':
            print_sleep("Fantastic! Let's take you back...\n", 2)
            weapon = "Hatchet"
            intro(weapon, enemy)
        elif play_again == 'n':
            bye()


def bye():
    print_sleep("Thanks for playing! See you next time. :)", 1)


enemies = ['Death Spirit', 'Duende', 'Zipacná', 'Xibalba', 'Buluc Chabtan']
enemy = random.choice(enemies)
weapon = "Hatchet"
intro(weapon, enemy)

end = time.time()
print("The program took: {}".format(end-start))
