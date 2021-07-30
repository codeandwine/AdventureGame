# Adventure Game
# Introduction 

Adventure Game is a simple project that tests the skills below being used. This short game basically provides some output, the user chooses an option, and different events happen, depending on the user's choice. 
<br>
## 1. Using time.time and time.sleep methods

"time" was imported to be able to calculate the time for which the game is run.

```Python
import time
start = time.time()
.
.
.
end = time.time()
```
It is also used to control the pauses between the printing of each message by calling on the sleep method.

```Python
def print_pause(message, seconds):
    print(message)
    time.sleep(seconds)
```


<br>

## 2. Using random.choice method

The game() was defined to have 3 variables inside. One contains a list of 'evil' spirits from the Mayan superstitions in Central America. Using the choice method found in random, it helps to randomly select an evil spirit as an enemy to start the game each time the function game is called. The weapon and enemy are passed into intro, as that is part of the 'randomness' of the game. 

```Python
def game():
    enemies = ['Death Spirit', 'Duende', 'Zipacná', 'Xibalba', 'Buluc Chabtan']
    enemy = random.choice(enemies)
    weapon = "Hatchet"
    intro(weapon, enemy)
```


<br>

## 3. An example from all the if elses used

In this example, you can see that if you've visited this function before, it will print something different than if you haven't. Notice also the change of weapon when visiting this function for the first time.

```Python
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
    ...
```


<br>

## 4. print and 'f' prints

Sample code showing printing strings of text and fprints of strings that include variables enclosed in {}

```Python
def pierce_heart(weapon, enemy):
    if weapon == "Magical Sword":
        print_pause(f"As the {enemy} makes a move at you, you take the "
                    f"{weapon} and pierce his heart.", 2)
        print_pause("The body collapses and the spirit "
                    "is thrown down into the underworld.", 1.5)
    ...
```
<br>

## 5. while loop usage with implicit joining for list provided

The while loops is used here to handle faulty inputs by user. 

The variable options is in charge to implicitly join all options provided when passing a list to that variable. This is to allow the change in amount or type of options that want to be given/used in other functions. As it is noted, the function first_choice passes the list containing 1 and 2 as options of inputs to be accepted.

```Python
def valid_input(instructions, options):
    while True:
        option = input(instructions).lower()
        if option in options:
            return option
        print_pause(f"Sorry, {option} is an invalid input. Try again!\n", 1.5)


def first_choice(weapon, enemy):
    start = valid_input("(Please enter the numbers 1 or 2.)\n", ['1', '2'])
    ...
```


<br>

## 6. Choices affect path of game

The function second_choice uses if/else to guide the game in different directions depending on the user's input.

```Python
def second_choice(weapon, enemy):
    sec_step = valid_input("(Please enter the numbers 1 or 2.)\n", ['1', '2'])

    if sec_step == '1':
        pierce_heart(weapon, enemy)
    elif sec_step == '2':
        run_away(weapon, enemy)
    ...
```


<br>

## 7. Refactoring of code

The first evidence of refactoring is creating the function print_pause() as pausing is code used throughout and would increase the length of the program significantly if done individually. 

```Python
def print_pause(message, seconds):
    print(message)
    time.sleep(seconds)
```

The second valuable function is the one containing the while loop that deals with inadequate input. This refactoring allows for it to be used when entering strings of numbers or letters in different parts of the game.

```Python
def valid_input(instructions, options):
    while True:
        option = input(instructions).lower()
        if option in options:
            return option
        print_pause(f"Sorry, {option} is an invalid input. Try again!\n", 1.5)
```

Other changes included changing the enemy and weapon variables from being global variables. Instead they're introduced as part of the game function that begins the journey of the connected functions. 

```Python
def game():
    enemies = ['Death Spirit', 'Duende', 'Zipacná', 'Xibalba', 'Buluc Chabtan']
    enemy = random.choice(enemies)
    weapon = "Hatchet"
    intro(weapon, enemy) 
 ```
 
 Other changes can be noted between tags of v1.0 and v2.0
<br>

## 8. pycodestyle checks done

No news is good news.
![pycheck.png](https://github.com/codeandwine/AdventureGame/blob/main/pycheck.png)
<br>

## 9. Running from start to finish without crashing

Well you can test that yourself ;)
