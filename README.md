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

The game() was defined to have 3 variables inside. One contains a list of 'evil' spirits from the Mayan superstitions in Central America. Using the choice method found in random, it helps to randomly select an evil spirit to start the game each time the function game is called. The weapon is also passed into intro, as that is part of the 'randomness' of the game. 

```Python
def game():
    enemies = ['Death Spirit', 'Duende', 'Zipacná', 'Xibalba', 'Buluc Chabtan']
    enemy = random.choice(enemies)
    weapon = "Hatchet"
    intro(weapon, enemy)
```


<br>

## 3. if else usage

<br>

## 4. print and 'f' prints

<br>

## 5. while loop usage with implicit joining for list provided

<br>

## 6. Choices affect path of game

<br>

## 7. Refactoring of code

<br>

## 8. pycodestyle checks done

![pycheck.png](https://github.com/codeandwine/AdventureGame/blob/main/pycheck.png)
<br>

## 9. Running from start to finish without crashing
