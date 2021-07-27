import time
import random

start = time.time()


def print_pause(message, seconds):
    print(message)
    time.sleep(seconds)
    # change ^ this line for the pauses


def intro(weapon, enemy):
    print_pause("You find you are in the Jungle of Belize, filled with Mayan "
                "witchcraft and supernatural creatures.", 1)
    print_pause('Rumor has it that an evil sprit is still roaming the '
                'mountains.', 1.5)
    print_pause("In front of you is a Mayan Temple.", 1)
    print_pause("Beside the temple there is a roaring river.", 1)
    print_pause("In your hand you hold a hatchet, though it's a bit blunt."
                "\n", 2)
    options(weapon, enemy)


def valid_input(instructions, options):
    while True:
        option = input(instructions).lower()
        if option in options:
            return option
        print_pause(f"Sorry, {option} is an invalid input. Try again!\n", 1.5)


def first_choice(weapon, enemy):
    start = valid_input("(Please enter the numbers 1 or 2.)\n", ['1', '2'])

    if start == '1':
        knock_on_door(weapon, enemy)
    elif start == '2':
        drink_water(weapon, enemy)


def second_choice(weapon, enemy):
    sec_step = valid_input("(Please enter the numbers 1 or 2.)\n", ['1', '2'])

    if sec_step == '1':
        pierce_heart(weapon, enemy)
    elif sec_step == '2':
        run_away(weapon, enemy)


def final_choice(weapon, enemy):
    play_again = valid_input("Would you like to play again? (y/n)\n", ['y', 'n'])

    if play_again == 'y':
        print_pause("Fantastic! Let's take you back...\n", 2)
        enemies = ['Death Spirit', 'Duende', 'Zipacná', 'Xibalba',
                    'Buluc Chabtan']
        enemy = random.choice(enemies)
        weapon = "Hatchet"

        intro(weapon, enemy)
    elif play_again == 'n':
        bye()
        exit(0)


def options(weapon, enemy):
    print_pause("Enter 1 to knock on the door of the Mayan Temple.", 1)
    print_pause("Enter 2 to drink some water from the river.", 1)
    first_choice(weapon, enemy)


def knock_on_door(weapon, enemy):
    print_pause("You walk towards the weird door at the top of the Temple.", 1)
    print_pause(f"You are about to reach the door when a grotesque looking "
                f"{enemy} opens the door.", 2)
    print_pause("Holy Molly! This is the evil spirit incarnate!", 1.5)
    print_pause(f"The ugly {enemy} attacks you. You are quite frightened "
                "about this!", 1)
    print_pause("What should you do?", 1)
    print_pause(f"1. Use the {weapon} to pierce his heart.", 1)
    print_pause("2. RUN AWAY!", 1)
    second_choice(weapon, enemy)


def drink_water(weapon, enemy):
    if weapon == "Magical Sword":
        print_pause("You have been here before. You already found the Magical "
                    "sword. You drink some water.", 1)
    else:
        print_pause("You walk towards the river bank. ", 1.5)
        print_pause("As you bend down to drink, you see something glistening "
                    "in the water. You have found a magical sword!", 1.5)
        print_pause("You rid yourself of your hatchet and take the sword.", 2)
        weapon = "Magical Sword"

    print_pause("You head back to the jungle.\n", 2)
    options(weapon, enemy)


def run_away(weapon, enemy):
    print_pause("You run back to where you started in the Jungle of "
                "Belize!", 2)
    print_pause(f"Luckily the {enemy} didn't follow you.\n", 1)
    options(weapon, enemy)


def pierce_heart(weapon, enemy):
    if weapon == "Magical Sword":
        print_pause(f"As the {enemy} makes a move at you, you take the "
                    f"{weapon} and pierce his heart.", 2)
        print_pause("The body collapses and the spirit "
                    "is thrown down into the underworld.", 1.5)
        print_pause("You have rid the Mayan Temple of the evil spirit!", 1)
        print_pause("You have won!", 1)
    elif weapon == "Hatchet":
        print_pause(f"You do your best to aim at {enemy}'s heart.", 2)
        print_pause("The human form of it is too swift and he evades your "
                    "strike.", 1.5)
        print_pause("He possesses your body and steals your soul!", 1)
        print_pause("You have been defeated! :(", 1.5)

    final_choice(weapon, enemy)


def bye():
    print_pause("Thanks for playing! See you next time. :)", 1)
    end = time.time()
    print("The game ran for: {}".format(end-start), "seconds.")


enemies = ['Death Spirit', 'Duende', 'Zipacná', 'Xibalba', 'Buluc Chabtan']
enemy = random.choice(enemies)
weapon = "Hatchet"
intro(weapon, enemy)
